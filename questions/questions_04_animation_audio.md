# Unity3D 2022 LTS 基础能力问答题库 - 04_animation_audio

**Q243.** [模块:E][维度:概念理解][难度:★][题型:单选]

Animator组件的作用是？

- A. 根据状态机参数切换动画，但本身不负责骨骼采样和Transform写回
- B. 只播放声音
- C. 驱动AnimatorController状态机，控制骨骼/属性动画的播放和切换
- D. 通过SceneManager的场景加载和卸载方法管理即可，不需要额外的架构设计

**Q244.** [模块:E][维度:概念理解][难度:★★][题型:单选]

Animator Controller中State之间的Transition条件是什么？

- A. 按时间顺序
- B. 随机切换
- C. 由参数(Parameter：Float/Int/Bool/Trigger)驱动的条件判断
- D. 仅由脚本调用Animator.Play时生效，状态机里配置的条件不会参与过渡判定

**Q245.** [模块:E][维度:API精确度][难度:★★][题型:代码补全]

通过代码触发动画切换：
```csharp
Animator anim = GetComponent<Animator>();
anim._____(---"isRunning", true);
```

- A. SetBool
- B. SetState
- C. PlayBool
- D. ChangeBool

**Q246.** [模块:E][维度:概念理解][难度:★★][题型:单选]

Animation Clip存储的是什么数据？

- A. 关键帧数据（属性随时间变化的曲线），如位置、旋转、缩放、BlendShape等
- B. 角色在某个状态下要执行的脚本逻辑和状态切换条件
- C. 只有位置
- D. 刚体碰撞求解结果和约束数据，供动画系统在每帧回放使用

**Q247.** [模块:E][维度:概念理解][难度:★★★][题型:单选]

Animator中Blend Tree的用途是？

- A. 物理混合
- B. 过渡效果
- C. 在多个Animator Controller之间切换激活状态，实现不同角色共享状态机
- D. 根据参数值混合多个动画（如走路→跑步的平滑过渡，或方向混合）

**Q248.** [模块:E][维度:概念理解][难度:★★★][题型:单选]

Avatar和Humanoid Rig的作用是？

- A. Humanoid只能用于人形，导入后会失去Root Motion和动画层混合等Animator核心功能
- B. Avatar是骨骼映射配置，Humanoid Rig将不同骨骼结构映射到统一骨架实现动画复用
- C. 不需要Avatar
- D. Avatar只是角色Prefab的别名资源，与骨骼映射和动画重定向无关

**Q249.** [模块:E][维度:概念理解][难度:★★★][题型:单选]

Animator的Layer系统有什么用？

- A. 渲染层
- B. 控制同一套动画曲线在不同材质球之间的渲染顺序和混合模式
- C. 多层叠加动画（如Base Layer跑步 + Upper Body Layer射击），通过权重和遮罩混合
- D. 物理层

**Q250.** [模块:E][维度:概念理解][难度:★★★][题型:单选]

Avatar Mask的作用是？

- A. 过滤角色参与物理模拟的骨骼节点，使动画层不会再写入这些Transform
- B. 指定动画Layer只影响特定骨骼部位（如只应用上半身动画）
- C. 控制动画事件只在哪些骨骼节点上触发，常用于优化事件分发
- D. 遮挡渲染

**Q251.** [模块:E][维度:概念理解][难度:★★★][题型:单选]

Root Motion的概念和作用是？

- A. 锁定角色位置
- B. 根据导航路径自动计算位移，并把结果写回动画剪辑中的根节点曲线
- C. 通过刚体求解得到角色的真实移动，再由Animator反向采样到骨骼动画中
- D. 将动画中根骨骼的位移数据应用到Transform上，使角色移动由动画驱动

**Q252.** [模块:E][维度:Bug诊断][难度:★★★][题型:单选]

角色播放走路动画时出现脚滑现象，可能原因是？

- A. 渲染问题
- B. 动画位移和代码控制的移动速度不匹配；应使用Root Motion或调整移动速度
- C. Animator Controller层级过多，系统会自动均分速度导致脚底打滑
- D. 动画文件损坏

**Q253.** [模块:E][维度:API精确度][难度:★★★][题型:单选]

Animator.CrossFade和Animator.Play的区别是？

- A. 两者都会立即切换状态，只是CrossFade额外记录一个调试用的过渡时间参数
- B. Play会自动根据当前状态和目标状态生成混合过渡，CrossFade反而更偏向硬切
- C. CrossFade平滑过渡到目标状态（有混合时间），Play立即切换
- D. CrossFade没有过渡

**Q254.** [模块:E][维度:概念理解][难度:★★★][题型:单选]

Animation Event的作用和风险是？

- A. 在动画特定帧触发脚本方法（如攻击判定帧），但依赖字符串方法名无编译检查
- B. 该操作没有任何风险，Unity的类型安全机制和运行时验证可以防止所有潜在错误
- C. 只能在Start中触发
- D. 只能调用无参数实例方法，任何带参数或静态方法都会被动画系统忽略

**Q255.** [模块:E][维度:概念理解][难度:★★★★][题型:单选]

Inverse Kinematics(IK)在Unity中的应用场景是？

- A. 通过Unity物理引擎的Rigidbody和Collider组件模拟该效果，不需要自定义实现
- B. 根据目标位置计算骨骼链的姿态（如角色手精确抓取物体、脚适应地形）
- C. 正向播放骨骼动画
- D. 为NavMeshAgent生成更平滑的路径拐点，并把结果同步回动画状态机

**Q256.** [模块:E][维度:代码生成/阅读][难度:★★★★][题型:代码补全]

实现IK使角色手抓取目标：
```csharp
void OnAnimatorIK(int layerIndex) {
anim.以下描述正确的是？Weight(AvatarIKGoal.RightHand, 1f);
anim._____(AvatarIKGoal.RightHand, targetPos);
}
```以下描述正确的是？

- A. SetPosition
- B. SetIKPosition
- C. MoveIK
- D. IKTarget

**Q257.** [模块:E][维度:性能优化][难度:★★★][题型:单选]

动画性能优化的方法包括？

- A. 使用动画剔除和LOD
- B. 所有角色都使用相同的Animator Controller以减少内存占用
- C. 在每帧都重新采样动画曲线以获得最流畅的动画效果
- D. 将所有动画都设置为Loop模式可以减少动画切换的性能开销

**Q258.** [模块:E][维度:概念理解][难度:★★★★][题型:单选]

Unity Playable API相比传统Animator的优势是？

- A. 更灵活的动画播放控制（可代码动态构建播放图），支持混合动画、音频和脚本
- B. 该方案性能更差，因为其内部实现涉及额外的序列化和反射操作
- C. 只用于音频
- D. 不支持混合

**Q259.** [模块:E][维度:概念理解][难度:★★★★][题型:单选]

Animation Rigging Package的用途是？

- A. 导入动画
- B. 把现有动画烘焙成更少的关键帧，以降低运行时CPU采样成本
- C. 创建骨架
- D. 在运行时添加骨骼约束（如瞄准约束、多目标约束等），增强程序化动画

**Q260.** [模块:E][维度:概念理解][难度:★★★][题型:单选]

Animator的Culling Mode设为"Cull Completely"后，当角色不可见时动画完全停止，包括状态机和Root Motion。

- A. 该模式仅影响渲染，状态机和Root Motion会继续执行
- B. Cull Completely模式下动画会继续运行，只是不渲染
- C. 正确，当角色不可见时动画完全停止，包括状态机和Root Motion
- D. Cull Completely只停止蒙皮网格渲染，动画状态机始终运行

**Q261.** [模块:E][维度:概念理解][难度:★★★][题型:单选]

AnimatorOverrideController的用途是？

- A. 基于现有AnimatorController替换其中的AnimationClip，实现相同状态机不同动画
- B. 覆盖所有动画
- C. 删除原控制器中未使用的状态，从而动态精简状态机结构和过渡图
- D. 基于现有控制器复制出一份独立的新状态机资源，后续修改不会再同步原控制器

**Q262.** [模块:E][维度:概念理解][难度:★★★★][题型:场景设计]

ARPG角色动画系统架构应包含哪些层次？

- A. Base Layer(移动)+Upper Body Layer(攻击/施法)+Full Body Layer(闪避/受击)+IK Layer(手脚适应)
- B. 只用代码控制
- C. 所有动画都放到单个Layer，再通过脚本实时修改每根骨骼权重即可取代层系统
- D. 只保留Root Motion，不再区分上半身和全身状态，就能自然解决动作叠加冲突

**Q263.** [模块:E][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

StateMachineBehaviour中OnStateEnter的典型使用场景是？
```csharp
public class AttackState : StateMachineBehaviour {
public override void OnStateEnter(Animator animator, AnimatorStateInfo stateInfo, int layerIndex) {
animator.GetComponent<CombatSystem>().EnableHitBox();
}
}
```

- A. 加载场景
- B. 在进入攻击动画状态时自动启用攻击判定碰撞体
- C. 在Animator进入任意状态前统一缓存所有攻击动画，避免状态切换时资源加载抖动
- D. 修改UI

**Q264.** [模块:E][维度:概念理解][难度:★★★][题型:单选]

导入模型时Generic和Humanoid动画类型的区别是？

- A. Generic通用（任意骨骼），Humanoid专为人形设计（支持IK、动画重定向/复用）
- B. Generic更适合所有双足角色，因为它比Humanoid自动支持跨模型骨骼映射和动作复用
- C. Humanoid只适合播放导入时自带的动画，不支持运行时IK和Avatar Mask
- D. 该属性的修改必须在Awake阶段完成，运行时动态修改无效

**Q265.** [模块:E][维度:概念理解][难度:★★★][题型:单选]

Animator Transition中HasExitTime的含义是？

- A. true表示动画必须播完Exit Time比例后才能过渡，false表示满足条件立即过渡
- B. 开启后状态机会在每一帧末尾强制退出当前状态，不再检查额外条件
- C. 有退出动画
- D. 过渡时间

**Q266.** [模块:E][维度:Bug诊断][难度:★★★★][题型:代码阅读]

Animator.SetTrigger在快速连续调用时，动画只播放一次。原因和解决方案是？

- A. 不存在这个问题，Trigger会在内部排队，后续所有调用都会按顺序逐个消费
- B. Trigger本质上是持久化的Bool值，只要设为true后就会一直保持直到手动改回false
- C. Trigger在使用后自动重置；快速连续调用时第二次可能在同帧被消费，应使用ResetTrigger后再SetTrigger
- D. 只能调一次

**Q267.** [模块:E][维度:概念理解][难度:★★★★][题型:单选]

大量角色同时播放骨骼动画的性能优化策略是？

- A. GPU Skinning + LOD动画（远处减少骨骼/使用简化动画）+ Animator Culling + 实例化渲染
- B. 把所有角色统一锁到同一关键帧采样点，这样就能彻底消除动画更新的CPU开销
- C. 降低游戏整体帧率能线性减少动画系统开销，因此通常优于局部的LOD和剔除策略
- D. 所有角色用最高骨骼

**Q268.** [模块:E][维度:概念理解][难度:★★★][题型:单选]

Animation Clip压缩设置中Keyframe Reduction的作用是？

- A. 压缩模型
- B. 去除冗余关键帧，在可接受误差内减少动画数据大小
- C. 对所有关键帧重新做等间隔插值采样，以提高运行时采样稳定性和曲线平滑度
- D. 压缩贴图

**Q269.** [模块:E][维度:概念理解][难度:★★★★][题型:单选]

为什么推荐使用Animator.StringToHash来缓存参数名？

- A. 两者在功能和性能上没有本质区别，底层调用相同的引擎API，选择哪个取决于编码习惯
- B. 使用Hash后Animator会自动帮你校验参数名拼写，因此更适合在大型项目中统一命名规范
- C. 必须使用
- D. 字符串比较性能差，使用Hash(int)比较更快

**Q270.** [模块:E][维度:代码生成/阅读][难度:★★★][题型:代码生成]

通过代码添加AnimationEvent：
```csharp
AnimationEvent evt = new AnimationEvent();
evt.time = 0.5f;
evt.functionName = "OnAttackHit";
AnimationClip clip = anim.runtimeAnimatorController.animationClips[0];
clip.AddEvent(evt);
```
这段代码的功能是什么？

- A. 直接修改当前状态的播放速度，并让后续动画事件都按新的速度重采样
- B. 暂停动画
- C. 删除剪辑中已有的全部动画事件，再写入一个新的攻击事件配置
- D. 在动画的0.5秒位置添加一个事件，触发OnAttackHit方法

**Q271.** [模块:E][维度:概念理解][难度:★★★★][题型:单选]

程序化动画(Procedural Animation)的概念和应用是？

- A. 该API仅支持2D项目，在3D项目中使用会导致编译错误或运行时异常
- B. 不需要代码
- C. 全部通过DCC工具离线烘焙完成，运行时不再根据环境和目标动态修正骨骼姿态
- D. 通过代码实时计算骨骼姿态而非预录制（如蜘蛛腿适应地形、物理布偶、呼吸晃动等）

**Q272.** [模块:E][维度:概念理解][难度:★★★★][题型:场景设计]

如何实现一套动画在多个不同模型上复用？
---

- A. 所有模型使用Humanoid Rig + Avatar配置，共享同一AnimatorController和动画
- B. 在运行时逐骨骼复制Transform数据，这样可以完全绕开导入设置和Avatar映射配置
- C. 把原动画导出成位移表后为每个模型单独重建根运动和骨骼曲线，保证动作完全一致
- D. 使用Generic Rig

**Q273.** [模块:F][维度:概念理解][难度:★][题型:单选]

AudioSource和AudioClip的关系是？

- A. AudioClip是音频数据，AudioSource是播放器组件（控制播放、音量、空间化等）
- B. AudioSource存储音频数据，AudioSource的3D空间化计算在GPU上执行以减轻CPU音频处理压力
- C. 两者职责完全不同：一个是资源数据，一个是播放与控制组件，不存在“同一实现不同名字”的关系
- D. AudioClip控制播放，音频的DSP处理（混响/均衡器）在Unity主线程中同步执行

**Q274.** [模块:F][维度:API精确度][难度:★★][题型:代码补全]

播放一次性音效的推荐方式：
```csharp
AudioSource._____(audioClip, transform.position, volume);
```

- A. PlayOneShot
- B. PlaySound
- C. PlayClipAtPoint
- D. PlayAtPoint

**Q275.** [模块:F][维度:概念理解][难度:★★][题型:单选]

AudioListener组件的规则是？

- A. 可以有无数个，音频的DSP处理（混响/均衡器）在Unity主线程中同步执行
- B. 场景中只能有一个活动的AudioListener（通常在主摄像机上），是声音的"耳朵"
- C. 不需要AudioListener，音频的DSP处理（混响/均衡器）在Unity主线程中同步执行
- D. 放在任何物体上都一样，AudioListener组件可以在场景中放置在任意数量的GameObject上同时工作

**Q276.** [模块:F][维度:概念理解][难度:★★★][题型:单选]

AudioMixer的作用是？

- A. 只调音量，AudioSource.PlayOneShot不受空间化设置影响，始终以2D模式播放
- B. 录制音频，AudioSource.PlayOneShot不受空间化设置影响，始终以2D模式播放
- C. 分组管理音频（BGM/SFX/Voice等），支持混音、效果器(Reverb/EQ)、快照(Snapshot)、动态调节
- D. 只播放音乐，AudioListener组件可以在场景中放置在任意数量的GameObject上同时工作

**Q277.** [模块:F][维度:概念理解][难度:★★★][题型:单选]

AudioSource的Spatial Blend参数从0到1分别表示？

- A. 0=全2D（不受距离和方向影响），1=全3D（受距离衰减和空间定位影响）
- B. 频率高低，音频的DSP处理（混响/均衡器）在Unity主线程中同步执行
- C. 音量大小，Unity的音频系统不支持实时音频效果处理，所有效果需要预先烘焙
- D. 0=静音，1=最大，Unity的音频系统不支持实时音频效果处理，所有效果需要预先烘焙

**Q278.** [模块:F][维度:概念理解][难度:★★★][题型:单选]

Unity中音频的Load Type选项包括？

- A. Memory、Disk、Network、Cache
- B. Sync、Async、Background、Foreground
- C. Decompress on Load、Compressed in Memory、Streaming
- D. Instant、Delayed、Lazy、Preemptive

**Q279.** [模块:F][维度:性能优化][难度:★★★][题型:单选]

大量音效的内存优化策略是？

- A. 全部Streaming，AudioListener组件可以在场景中放置在任意数量的GameObject上同时工作
- B. 全部Decompress，AudioSource的3D空间化计算在GPU上执行以减轻CPU音频处理压力
- C. 短音效用Decompress On Load，长BGM用Streaming；合理设置采样率和通道数
- D. 该场景不需要专门优化，Unity默认设置已经足够高效，过度优化反而增加维护成本

**Q280.** [模块:F][维度:代码生成/阅读][难度:★★★][题型:代码生成]

通过代码控制AudioMixer音量：
```csharp
audioMixer.SetFloat("MasterVolume", Mathf.Log10(volume) * 20);
```
为什么使用Log10 * 20？

- A. 美观，AudioListener组件可以在场景中放置在任意数量的GameObject上同时工作
- B. 增加精度，AudioClip的Load Type选择不影响运行时内存占用，仅影响加载速度
- C. 没有原因，AudioListener组件可以在场景中放置在任意数量的GameObject上同时工作
- D. AudioMixer音量使用分贝(dB)单位，需要将线性值(0-1)转换为分贝(-80dB ~ 0dB)

**Q281.** [模块:F][维度:概念理解][难度:★★★][题型:单选]

AudioSource的Priority设置的作用是？

- A. 当音频通道数超过限制时，低优先级的音频会被高优先级的覆盖（0最高，256最低）
- B. 音量大小，AudioSource的3D空间化计算在GPU上执行以减轻CPU音频处理压力
- C. 引擎内部会自动补偿参数差异
- D. 播放顺序，AudioListener组件可以在场景中放置在任意数量的GameObject上同时工作

**Q282.** [模块:F][维度:概念理解][难度:★★★★][题型:场景设计]

游戏音频管理系统应包含哪些功能？

- A. 全用2D声音，音频的DSP处理（混响/均衡器）在Unity主线程中同步执行
- B. 音频池管理+AudioMixer分组(BGM/SFX/Voice)+音量设置持久化+音频淡入淡出+动态音效优先级
- C. 只播放音乐，AudioSource.PlayOneShot不受空间化设置影响，始终以2D模式播放
- D. 每个脚本自行播放，音频的DSP处理（混响/均衡器）在Unity主线程中同步执行

**Q283.** [模块:F][维度:Bug诊断][难度:★★★][题型:单选]

AudioSource.Play()调用后没有声音，可能原因不包括？

- A. AudioClip为null
- B. AudioSource被Mute
- C. AudioClip的采样率太高
- D. 场景中没有AudioListener

**Q284.** [模块:F][维度:概念理解][难度:★★★★][题型:单选]

如何实现声音被墙壁遮挡后变闷的效果？

- A. 降低音量，Unity的音频系统不支持实时音频效果处理，所有效果需要预先烘焙
- B. Unity引擎在内部已完全自动化处理此场景，开发者只需使用默认API即可
- C. 用射线检测声源和听者之间是否有障碍物，有则通过AudioMixer施加Low-Pass Filter
- D. 停止播放，AudioClip的Load Type选择不影响运行时内存占用，仅影响加载速度

**Q285.** [模块:F][维度:概念理解][难度:★★★][题型:单选]

Audio Reverb Zone组件的作用是？

- A. 过滤噪音，音频剪辑的采样率在导入后不可更改，需要在外部音频编辑器中预处理
- B. 放大声音，音频的DSP处理（混响/均衡器）在Unity主线程中同步执行
- C. 在特定区域内自动为音频添加混响效果（如洞穴、大厅等环境音效）
- D. 录制声音，音频剪辑的采样率在导入后不可更改，需要在外部音频编辑器中预处理

**Q286.** [模块:F][维度:概念理解][难度:★★][题型:单选]

AudioSource.PlayOneShot(clip)和AudioSource.Play()的区别：PlayOneShot不会打断当前播放，可以叠加播放多个音效。

- A. 两者都能触发声音播放，但一个更适合播放独立片段叠加，另一个更偏向控制AudioSource当前剪辑的主播放状态
- B. PlayOneShot只能播放2D音效，Play可以播放3D音效
- C. 正确，PlayOneShot不会打断当前播放，可以叠加播放多个音效
- D. PlayOneShot会先停止当前播放再播放新音效

**Q287.** [模块:F][维度:概念理解][难度:★★★★][题型:单选]

为什么大型项目常使用FMOD或Wwise而非Unity原生音频？

- A. 更便宜，Unity的音频系统不支持实时音频效果处理，所有效果需要预先烘焙
- B. Unity不能播放声音，AudioMixer的快照切换在底层使用线性插值，不支持自定义缓动曲线
- C. 更简单，AudioSource的3D空间化计算在GPU上执行以减轻CPU音频处理压力
- D. 提供更强大的音频编辑工具、更灵活的事件系统、更好的内存管理和跨平台音频优化

**Q288.** [模块:F][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

实现BGM切换的淡入淡出：
```csharp
IEnumerator CrossFadeBGM(AudioClip newClip, float duration) {
float startVol = bgmSource.volume;
for(float t = 0; t < duration; t += Time.deltaTime) {
bgmSource.volume = Mathf.Lerp(startVol, 0, t / duration);
yield return null;
}
bgmSource.clip = newClip;
bgmSource.Play();
for(float t = 0; t < duration; t += Time.deltaTime) {
bgmSource.volume = Mathf.Lerp(0, startVol, t / duration);
yield return null;
}
}
```
这段代码实现了什么？

- A. 停止播放，AudioMixer的快照切换在底层使用线性插值，不支持自定义缓动曲线
- B. 立即切换，AudioSource的3D空间化计算在GPU上执行以减轻CPU音频处理压力
- C. 同时播放两首，音频的DSP处理（混响/均衡器）在Unity主线程中同步执行
- D. 当前BGM淡出→切换新曲目→新BGM淡入

**Q289.** [模块:F][维度:概念理解][难度:★★★][题型:单选]

AudioSource的Doppler Level参数控制什么？

- A. 延迟，AudioSource的3D空间化计算在GPU上执行以减轻CPU音频处理压力
- B. 多普勒效应的强度（声源移动时音调的变化程度）
- C. 音量，AudioClip的Load Type选择不影响运行时内存占用，仅影响加载速度
- D. 回声，音频的DSP处理（混响/均衡器）在Unity主线程中同步执行

**Q290.** [模块:F][维度:概念理解][难度:★★★][题型:单选]

Unity的Audio Spatializer Plugin的作用是？

- A. 录制声音，AudioSource.PlayOneShot不受空间化设置影响，始终以2D模式播放
- B. 提供更精确的3D空间音频效果（如HRTF头部相关传输函数），增强沉浸感
- C. 增大音量，AudioClip的Load Type选择不影响运行时内存占用，仅影响加载速度
- D. 压缩音频，音频的DSP处理（混响/均衡器）在Unity主线程中同步执行

**Q291.** [模块:F][维度:性能优化][难度:★★★★][题型:单选]

音频系统性能优化方法包括？

- A. 同时播放100个AudioSource不会影响性能，Unity会自动优化
- B. 所有音频都使用未压缩的WAV格式以获得最佳音质
- C. 使用AudioMixer分组和压缩
- D. 在Update中每帧检查AudioSource.isPlaying状态以精确控制播放

**Q292.** [模块:F][维度:概念理解][难度:★★★★][题型:单选]

Unity通过Microphone类可以实现什么？
---

- A. 录制麦克风音频到AudioClip，用于语音聊天等功能
- B. 只能播放，AudioClip的Load Type选择不影响运行时内存占用，仅影响加载速度
- C. 控制硬件音量，AudioClip的Load Type选择不影响运行时内存占用，仅影响加载速度
- D. 不支持录制，AudioSource的3D空间化计算在GPU上执行以减轻CPU音频处理压力

**Q293.** [模块:E][维度:概念理解][难度:★★][题型:单选]

Animator参数类型有哪些？

- A. Float、Int、Bool、Trigger
- B. Float和Int
- C. 只有Bool
- D. String和Bool

**Q294.** [模块:F][维度:概念理解][难度:★★][题型:单选]

场景中应该有几个AudioListener？

- A. 该步骤不是必需的，Unity引擎在底层已自动处理相关逻辑，无需额外配置
- B. 每个音源一个，音频剪辑的采样率在导入后不可更改，需要在外部音频编辑器中预处理
- C. 一般只有一个(通常在主摄像机上)，多个会导致警告
- D. 无所谓，AudioListener组件可以在场景中放置在任意数量的GameObject上同时工作

**Q295.** [模块:E][维度:代码生成/阅读][难度:★★★][题型:代码补全]

在动画特定帧触发函数：
```csharp
// 在动画剪辑的关键帧上添加Event
// 调用脚本中：
public void OnFootStep() {
___A___; // 播放脚步音效
}
```

- A. Debug.Log("FootStep")
- B. audioSource.Play()
- C. AudioSource.PlayOneShot(footStepClip)
- D. Destroy

**Q296.** [模块:F][维度:概念理解][难度:★★][题型:单选]

AudioSource的Spatial Blend参数的作用？

- A. 引擎内部会自动补偿参数差异
- B. 音量控制，音频剪辑的采样率在导入后不可更改，需要在外部音频编辑器中预处理
- C. 音调控制，AudioSource.PlayOneShot不受空间化设置影响，始终以2D模式播放
- D. 0=2D音频(不受距离/方位影响)，1=3D音频(受距离衰减和方位影响)

**Q297.** [模块:E][维度:Bug诊断][难度:★★★★][题型:单选]

角色移动速度与走路动画不匹配(滑步)的解决方法？

- A. 根据移动速度调整动画播放速度(Animator.speed或BlendTree速度参数)+或使用Root Motion
- B. 把角色胶囊体尺寸放大，让视觉上的位移差异被碰撞体遮盖
- C. 重做动画
- D. 强制提高角色移动速度到动画步幅对应的最大值，避免出现明显的位移滞后

**Q298.** [模块:E][维度:架构设计][难度:★★★★][题型:场景设计]

复杂角色动画系统的架构设计？

- A. 只用一个巨大的主状态机，把所有动作都放在同一层里用条件分支控制即可
- B. 全用代码
- C. Animator层级管理+状态机+子状态机+BlendTree+IK+动画层叠加+动画事件+过渡曲线
- D. 不做分层和复用设计，直接给每个角色单独复制一套完整控制器资源最稳定

**Q299.** [模块:E][维度:概念理解][难度:★★★★][题型:单选]

Animation Compression(动画压缩)的原理和设置？

- A. 只对磁盘文件做无损压缩，运行时解压后曲线精度和关键帧数量完全不变
- B. 动画一旦压缩就会破坏骨骼层级关系，因此正式项目中通常应关闭压缩
- C. Unity会自动根据当前平台选择最优压缩参数，开发者无需关注误差容限和压缩模式
- D. 关键帧精简(误差容限)+曲线优化+Optimal/Keyframe Reduction模式+可为Position/Rotation/Scale设不同精度

**Q300.** [模块:F][维度:概念理解][难度:★★★★][题型:单选]

Audio Mixer的Snapshot功能用于什么？

- A. 录音，AudioMixer的快照切换在底层使用线性插值，不支持自定义缓动曲线
- B. 截图，音频剪辑的采样率在导入后不可更改，需要在外部音频编辑器中预处理
- C. 替代AudioSource，Unity的音频系统不支持实时音频效果处理，所有效果需要预先烘焙
- D. 保存一组Mixer参数(音量/DSP设置)的预设，可平滑过渡(如从战斗音效配置过渡到菜单配置)

