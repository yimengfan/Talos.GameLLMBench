# Unity3D 2022 LTS 基础能力问答题库 - 06_particle_2d

**Q359.** [模块:I][维度:概念理解][难度:★][题型:单选]

Unity Particle System的核心组成部分是？

- A. 发射器(Emission)+粒子属性(大小/颜色/速度/生命周期)+渲染器(Renderer)
- B. 只有渲染器和材质设置，发射与生命周期完全由MeshRenderer负责
- C. 粒子效果必须依赖Rigidbody或Collider组件才能正常发射和渲染
- D. 只有发射器模块即可完成所有粒子行为，其他模块只是编辑器辅助配置

**Q360.** [模块:I][维度:API精确度][难度:★★][题型:代码补全]

通过代码播放和停止粒子系统：
```csharp
ParticleSystem ps = GetComponent<ParticleSystem>();
ps._____();  // 播放
ps.Stop();
```

- A. Start
- B. Play
- C. Begin
- D. Emit

**Q361.** [模块:I][维度:概念理解][难度:★★][题型:单选]

Particle System中Shape模块控制什么？

- A. 粒子颜色渐变和透明度曲线
- B. 粒子的碰撞体积和物理求解精度
- C. 粒子的材质球和渲染排序方式
- D. 粒子发射的形状和区域（如球体、锥形、平面、边缘等）

**Q362.** [模块:I][维度:概念理解][难度:★★★][题型:单选]

Particle System常用模块包括？

- A. Start、Update、FixedUpdate、LateUpdate
- B. Input、Output、Process、Control
- C. Emission、Shape、Velocity、Color over Lifetime
- D. Create、Read、Write、Delete

**Q363.** [模块:I][维度:性能优化][难度:★★★][题型:单选]

粒子系统性能优化的关键指标是？

- A. 颜色渐变关键帧数量，关键帧越少CPU和GPU开销越低
- B. Burst次数本身，只要Burst数量少就不必关心同时存活的粒子总量
- C. Shape模块的几何类型，Sphere一定比Cone和Box更消耗性能
- D. 同时存活的最大粒子数量（MaxParticles）和Overdraw面积

**Q364.** [模块:I][维度:概念理解][难度:★★★][题型:单选]

Particle System的Sub Emitters模块的用途是？

- A. 自动提高粒子总上限，让主系统在高负载下继续保持满额发射
- B. 只用于子弹命中特效，不能在出生、死亡或碰撞等通用生命周期事件上触发
- C. 用来直接替代主发射器的Emission模块，主系统关闭后仍能独立持续发射
- D. 在粒子生命周期事件（出生、死亡、碰撞）时触发另一个粒子系统

**Q365.** [模块:I][维度:代码生成/阅读][难度:★★★][题型:代码补全]

通过代码发射指定数量粒子：
```csharp
ParticleSystem.EmitParams emitParams = new ParticleSystem.EmitParams();
emitParams.position = hitPoint;
ps._____(emitParams, 10);  // 在hitPoint发射10个粒子
```

- A. Play
- B. Emit
- C. Generate
- D. Create

**Q366.** [模块:I][维度:概念理解][难度:★★★][题型:单选]

Particle System的Collision模块可以实现什么？

- A. 只用于粒子之间互相碰撞，不能与场景中的Collider交互
- B. 只能让粒子受Rigidbody推动，无法设置反弹、销毁或发送回调消息
- C. 粒子与场景碰撞体碰撞后反弹、销毁或触发子发射器
- D. 仅能检测Trigger，不支持普通Collider碰撞或任何碰撞后的行为配置

**Q367.** [模块:I][维度:性能优化][难度:★★★★][题型:单选]

粒子系统性能优化方法包括？

- A. 将粒子系统的Max Particles设置为无限制以获得最佳视觉效果
- B. 在每帧都动态修改粒子系统的所有模块参数
- C. 每个粒子效果都使用Mesh Renderer以获得最高画质
- D. 使用GPU Instancing和简化粒子

**Q368.** [模块:I][维度:概念理解][难度:★★★][题型:单选]

VFX Graph和传统Particle System的区别是？
- C. VFX Graph基于GPU（支持百万级粒子），Particle System基于CPU（千级粒子）
- A. VFX Graph和Particle System本质相同，只是一个基于节点、一个基于Inspector折叠面板
- B. Particle System主要基于GPU大规模并行计算，VFX Graph主要由CPU逐粒子更新
- D. 两者只是编辑体验不同，性能、平台限制和功能边界上没有本质差异

**Q369.** [模块:I][维度:概念理解][难度:★★★★][题型:单选]

VFX Graph的技术特点是？

- A. 完全基于CPU串行更新，每个粒子都由主线程逐个计算
- B. 只能通过C#代码配置，不提供节点图或可视化编辑方式
- C. 仅在编辑器调试时可用，构建后无法在运行时播放
- D. 基于Compute Shader的GPU粒子系统，可视化节点编辑器，支持大量粒子和复杂行为

**Q370.** [模块:I][维度:概念理解][难度:★★★][题型:单选]

Particle System Renderer中Billboard模式表示什么？

- A. 粒子固定方向
- B. 粒子面片始终面向摄像机
- C. 粒子朝向运动方向
- D. 粒子随机旋转

**Q371.** [模块:I][维度:概念理解][难度:★★★][题型:单选]

Particle System的Trails模块的效果是？

- A. 为粒子自动生成导航路径，用于驱动NavMeshAgent移动
- B. 记录粒子的历史位置并生成可编辑的样条路径资源
- C. 在每个粒子上生成真实物理刚体轨迹，用于后续碰撞回放
- D. 每个粒子后面跟随一条拖尾轨迹（如火焰拖尾、魔法弹幕轨迹）

**Q372.** [模块:I][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

读取粒子系统中每个粒子的数据：
```csharp
ParticleSystem.Particle[] particles = new ParticleSystem.Particle[ps.particleCount];
int count = ps.GetParticles(particles);
for(int i = 0; i < count; i++) {
particles[i].position += Vector3.up * Time.deltaTime;
}
ps.SetParticles(particles, count);
```
这段代码的作用？

- A. 获取所有粒子数据，修改它们的位置（向上移动），然后写回
- B. 删除粒子，VFX Graph仅支持HDRP渲染管线，URP项目需要使用传统Particle System
- C. 创建新粒子，GPU粒子的碰撞检测精度高于CPU粒子，因为GPU可以并行处理更多碰撞对
- D. 只读取不修改，SubEmitter在父粒子系统销毁时会自动停止所有子粒子的发射和渲染

**Q373.** [模块:I][维度:概念理解][难度:★★★★][题型:场景设计]

游戏特效管理系统应包含什么？

- A. 不需要统一管理，特效在用到时直接Instantiate即可，回收由GC自动处理
- B. 在游戏启动时一次性预加载所有特效资源和实例，避免任何运行时调度逻辑
- C. 每次播放时重新创建一个特效对象，结束后立即销毁，保证状态最干净
- D. 对象池管理+预加载+自动回收+LOD(远处简化)+上限控制+分层优先级

**Q374.** [模块:I][维度:概念理解][难度:★★★][题型:单选]

Particle System的Prewarm选项会在Start时模拟一个生命周期，使粒子系统看起来已经在运行中。

- A. Prewarm仅在编辑器中有效，运行时不起作用
- B. Prewarm会重置粒子系统到初始状态
- C. Prewarm会延迟粒子系统的启动时间
- D. 正确，Prewarm会在Start时模拟一个生命周期，使粒子系统看起来已经在运行中

**Q375.** [模块:I][维度:Bug诊断][难度:★★★][题型:单选]

粒子系统Play后看不到粒子，可能原因不包括？

- A. Start Size为0
- B. 粒子太多导致帧率下降
- C. Max Particles为0
- D. Material/Shader不正确或丢失

**Q376.** [模块:I][维度:概念理解][难度:★★★★][题型:单选]

GPU粒子(VFX Graph)相比CPU粒子(Particle System)的优势和限制？

- A. CPU粒子更适合百万级特效，而GPU粒子通常只适合少量装饰性效果
- B. 优势：支持百万级粒子；限制：不支持所有平台（需Compute Shader），碰撞检测有限
- C. 两者在功能和性能上没有本质区别，底层调用相同的引擎API，选择哪个取决于编码习惯
- D. GPU粒子一定比CPU粒子更通用，不存在平台兼容或功能边界方面的限制

**Q377.** [模块:I][维度:概念理解][难度:★★★][题型:单选]

Particle System的Noise模块的作用是？

- A. 使用Perlin/Curl Noise为粒子运动添加自然的随机扰动
- B. 通过修改Material的_Color属性改变物体颜色来达到视觉反馈效果
- C. 为粒子系统自动附加环境音效，让每个粒子都能发出独立声音
- D. 增加粒子与场景的碰撞体积，并且始终以零CPU开销在GPU端计算

**Q378.** [模块:I][维度:概念理解][难度:★★★★][题型:单选]

粒子系统中Texture Sheet Animation模块的用途是？
---

- A. 在粒子上播放完整视频流贴图，适合做运行时影片解码与投影播放
- B. 可以完全替代Animator Controller，用统一序列帧配置驱动角色和UI动画
- C. 只能用于UI粒子，不能在3D世界中的粒子渲染器上使用序列帧纹理
- D. 在粒子上播放序列帧动画（如2D爆炸效果、烟雾翻滚等）

**Q379.** [模块:K][维度:概念理解][难度:★][题型:单选]

Unity中Sprite是什么？

- A. 音频资源，2D物理系统(Box2D)和3D物理系统(PhysX)可以互相检测碰撞并触发回调
- B. 2D图形对象，由纹理和元数据（边界、Pivot等）组成
- C. 3D模型
- D. 脚本

**Q380.** [模块:K][维度:概念理解][难度:★★][题型:单选]

SpriteRenderer组件的Flip X/Y选项的作用是？

- A. 隐藏精灵
- B. 缩放精灵
- C. 水平/垂直翻转精灵显示（不影响Collider），用于角色转向等
- D. 旋转精灵

**Q381.** [模块:K][维度:概念理解][难度:★★][题型:单选]

SpriteAtlas(精灵图集)的作用是？

- A. 将多个小Sprite打包到一张大纹理中，减少Draw Call
- B. 增加内存
- C. 增加Draw Call
- D. 该功能仅适用于3D渲染管线，2D项目中不可用且不提供对应的2D替代方案

**Q382.** [模块:K][维度:概念理解][难度:★★★][题型:单选]

Unity Tilemap系统的组成部分是？

- A. 需要自定义实现
- B. Tilemap组件 + TilemapRenderer + Grid + Tile资产 + Tile Palette
- C. 只有Tilemap
- D. 只有Sprite，SpriteRenderer和Image组件使用相同的合批策略，在渲染性能上完全一致

**Q383.** [模块:K][维度:概念理解][难度:★★★][题型:单选]

Unity 2D物理组件和3D物理组件的区别是？

- A. 2D使用Rigidbody2D/Collider2D/Physics2D，基于Box2D引擎；3D使用Rigidbody/Collider/Physics，基于PhysX
- B. 2D不支持物理，Composite Collider 2D将所有子Collider合并为一个凸包而非保持原始形状
- C. 共用相同组件，2D物理系统(Box2D)和3D物理系统(PhysX)可以互相检测碰撞并触发回调
- D. 3D不支持碰撞

**Q384.** [模块:K][维度:概念理解][难度:★★★][题型:单选]

Sprite Shape的用途是？

- A. 只能创建矩形
- B. 创建2D曲线形状的地形（如山坡、洞穴），可自由编辑控制点
- C. 3D建模
- D. 使用Particle System组件配合内置的渲染模块即可实现，无需编写自定义Shader

**Q385.** [模块:K][维度:概念理解][难度:★★★][题型:单选]

Unity 2D Animation包支持什么功能？

- A. 不支持骨骼，Tilemap系统仅支持矩形网格布局，不支持六边形或等距视角的瓦片地图
- B. 只支持帧动画
- C. 只能用外部工具，2D物理系统(Box2D)和3D物理系统(PhysX)可以互相检测碰撞并触发回调
- D. 2D骨骼绑定和蒙皮，使2D精灵可以做骨骼动画

**Q386.** [模块:K][维度:代码生成/阅读][难度:★★★][题型:代码补全]

2D射线检测：
```csharp
RaycastHit2D hit = Physics2D._____(origin, direction, distance, layerMask);
if(hit.collider != null) Debug.Log("Hit: " + hit.collider.name);
```

- A. LineCast
- B. RayCast2D
- C. Raycast
- D. CastRay

**Q387.** [模块:K][维度:概念理解][难度:★★★][题型:单选]

2D游戏中的渲染排序方式有？

- A. 只有Z值
- B. 按名称排序，2D物理系统(Box2D)和3D物理系统(PhysX)可以互相检测碰撞并触发回调
- C. Sorting Layer → Order in Layer → Camera距离(Z值或Y值) → Renderer优先级
- D. 随机，SpriteAtlas打包后的精灵在运行时不能单独卸载，必须整体加载或释放

**Q388.** [模块:K][维度:概念理解][难度:★★★★][题型:单选]

Unity 2D Light系统(URP 2D Renderer)支持什么？

- A. 只支持全局光
- B. 不支持2D光照
- C. 2D点光源、全局光、自由形状光 + Normal Map实现2D法线光照效果
- D. 需要3D光源

**Q389.** [模块:K][维度:概念理解][难度:★★★][题型:单选]

Composite Collider 2D的作用是？

- A. 渲染碰撞体，Tilemap系统仅支持矩形网格布局，不支持六边形或等距视角的瓦片地图
- B. 将多个2D Collider合并为一个复合碰撞体（常用于Tilemap的碰撞优化）
- C. 分割碰撞体，SpriteRenderer和Image组件使用相同的合批策略，在渲染性能上完全一致
- D. 删除碰撞体，2D物理系统(Box2D)和3D物理系统(PhysX)可以互相检测碰撞并触发回调

**Q390.** [模块:K][维度:Bug诊断][难度:★★★][题型:单选]

2D像素游戏的精灵在放大后模糊。解决方法是？

- A. 使用Mipmap，SpriteRenderer和Image组件使用相同的合批策略，在渲染性能上完全一致
- B. 增加分辨率，Composite Collider 2D将所有子Collider合并为一个凸包而非保持原始形状
- C. 改为3D渲染
- D. 纹理Filter Mode设为Point（无过滤），Compression设为None或无损

**Q391.** [模块:K][维度:概念理解][难度:★★★★][题型:场景设计]

2D像素游戏实现像素完美渲染的方案是？

- A. 全屏后处理
- B. Pixel Perfect Camera组件 + 固定正交大小 + Point过滤 + 整数位置移动
- C. 使用透视相机，Tilemap系统仅支持矩形网格布局，不支持六边形或等距视角的瓦片地图
- D. 使用Bilinear过滤，Tilemap系统仅支持矩形网格布局，不支持六边形或等距视角的瓦片地图

**Q392.** [模块:K][维度:概念理解][难度:★★★][题型:单选]

Unity 2D Effector组件（如Area Effector 2D、Surface Effector 2D）的作用是？

- A. 音频效果，SpriteAtlas打包后的精灵在运行时不能单独卸载，必须整体加载或释放
- B. 视觉效果
- C. 渲染效果，SpriteAtlas打包后的精灵在运行时不能单独卸载，必须整体加载或释放
- D. 在特定区域施加物理力（如风、传送带效果、浮力等）

**Q393.** [模块:K][维度:概念理解][难度:★★★][题型:单选]

Sprite的9-slicing(九宫格)的用途是？

- A. 分割成9个精灵
- B. 该功能仅适用于3D渲染管线，2D项目中不可用且不提供对应的2D替代方案
- C. 将精灵分为9个区域，拉伸时四角不变形，适用于按钮、面板等UI元素
- D. 产生9个副本

**Q394.** [模块:K][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

通过代码设置Tilemap：
```csharp
Tilemap tilemap = GetComponent<Tilemap>();
TileBase tile = Resources.Load<TileBase>("Tiles/GrassTile");
tilemap.SetTile(new Vector3Int(x, y, 0), tile);
```
这段代码做了什么？

- A. 移动Tile
- B. 渲染3D物体，SpriteRenderer和Image组件使用相同的合批策略，在渲染性能上完全一致
- C. 在指定网格坐标(x,y)上放置一个草地Tile
- D. 删除Tile

**Q395.** [模块:K][维度:概念理解][难度:★★★★][题型:单选]

Rule Tile(规则瓦片)的作用是？

- A. 管理碰撞，SpriteAtlas打包后的精灵在运行时不能单独卸载，必须整体加载或释放
- B. 播放动画
- C. 根据相邻Tile的情况自动选择正确的Tile变体（如自动拼接地形边缘）
- D. 计算物理，SpriteAtlas打包后的精灵在运行时不能单独卸载，必须整体加载或释放

**Q396.** [模块:K][维度:性能优化][难度:★★★★][题型:单选]

大型2D游戏的渲染优化方法包括？

- A. 禁用Sprite Atlas功能，每个Sprite独立渲染以保证灵活性
- B. 使用Sprite Atlas和2D灯光优化
- C. 所有Sprite都使用RGBA32格式以获得最高画质
- D. 将所有2D元素都转换为3D Mesh以利用GPU加速

**Q397.** [模块:K][维度:概念理解][难度:★★★][题型:单选]

Collider2D的Physics2D.OverlapCircle的作用是？

- A. 检测指定圆形区域内的所有2D碰撞体
- B. 只检测一个
- C. 3D检测
- D. 渲染圆形

**Q398.** [模块:K][维度:概念理解][难度:★★★★][题型:单选]

Unity Isometric Tilemap的用途是？

- A. 创建等距视角(45度俯视)的2D游戏地图
- B. 只能创建正交地图
- C. 不支持等距，SpriteRenderer和Image组件使用相同的合批策略，在渲染性能上完全一致
- D. 3D地图

**Q399.** [模块:K][维度:概念理解][难度:★★★][题型:单选]

2D视差滚动(Parallax Scrolling)效果的实现原理是？

- A. 使用3D物体
- B. 远处背景层移动速度慢，近处前景层移动速度快，模拟深度感
- C. 旋转摄像机，2D物理系统(Box2D)和3D物理系统(PhysX)可以互相检测碰撞并触发回调
- D. 放大缩小

**Q400.** [模块:K][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

视差滚动代码实现：
```csharp
void LateUpdate() {
foreach(var layer in parallaxLayers) {
float parallax = cameraPos.x * layer.speedMultiplier;
layer.transform.position = new Vector3(parallax, layer.transform.position.y, layer.transform.position.z);
}
}
```
speedMultiplier=0.5表示什么？

- A. 被遮挡，SpriteRenderer和Image组件使用相同的合批策略，在渲染性能上完全一致
- B. 不移动，2D物理系统(Box2D)和3D物理系统(PhysX)可以互相检测碰撞并触发回调
- C. 移动速度翻倍
- D. 该层移动速度是摄像机的50%（看起来在更远处）

**Q401.** [模块:K][维度:概念理解][难度:★★★][题型:单选]

Sprite Mask组件的作用是？

- A. 旋转Sprite，SpriteRenderer和Image组件使用相同的合批策略，在渲染性能上完全一致
- B. 缩放Sprite
- C. 控制Sprite的可见区域（遮罩），只显示遮罩范围内的部分
- D. 删除Sprite

**Q402.** [模块:K][维度:概念理解][难度:★★★★][题型:单选]

在URP中为2D Sprite创建自定义Shader需要注意什么？

- A. 使用Surface Shader，2D物理系统(Box2D)和3D物理系统(PhysX)可以互相检测碰撞并触发回调
- B. 使用Sprite Lit/Unlit Master节点+正确的Sorting Layer/Order设置
- C. 不支持自定义Shader，SpriteAtlas打包后的精灵在运行时不能单独卸载，必须整体加载或释放
- D. 使用3D Shader

**Q403.** [模块:K][维度:概念理解][难度:★★★★][题型:场景设计]

2D平台跳跃游戏的移动和跳跃物理方案是？
---

- A. NavMeshAgent，SpriteRenderer和Image组件使用相同的合批策略，在渲染性能上完全一致
- B. 只用Transform移动
- C. Rigidbody2D + 地面检测(OverlapCircle) + 可变跳跃高度(松开按键减速) + Coyote Time + Jump Buffer
- D. CharacterController

**Q404.** [模块:I][维度:概念理解][难度:★★★][题型:单选]

粒子系统的性能优化方法？

- A. 不能优化，粒子系统的Simulation Space设为World时性能优于Local因为减少了坐标变换
- B. GPU足够强，粒子系统的Simulation Space设为World时性能优于Local因为减少了坐标变换
- C. 限制最大粒子数+减少Overdraw(缩小粒子/降低透明度)+距离剪辑+LOD+避免复杂Shader
- D. 随意使用，GPU粒子的碰撞检测精度高于CPU粒子，因为GPU可以并行处理更多碰撞对

**Q405.** [模块:K][维度:概念理解][难度:★★★★][题型:单选]

Unity 2D Light System(URP 2D Renderer)的核心功能？

- A. 只有全局光
- B. 用3D光照
- C. 2D光源(Point/Freeform/Sprite/Global)+法线贴图2D光照+阴影+Light Blend样式
- D. 不支持2D光照，SpriteRenderer和Image组件使用相同的合批策略，在渲染性能上完全一致

**Q406.** [模块:I][维度:代码生成/阅读][难度:★★★★][题型:代码阅读]

```csharp
var main = ps.main;
main.startSpeed = new ParticleSystem.MinMaxCurve(2f, 5f);
main.startLifetime = new ParticleSystem.MinMaxCurve(1f, 3f);
var emission = ps.emission;
emission.rateOverTime = 100;
```
MinMaxCurve(2f, 5f)的含义？

- A. 固定值5，SubEmitter在父粒子系统销毁时会自动停止所有子粒子的发射和渲染
- B. 固定值2，GPU粒子的碰撞检测精度高于CPU粒子，因为GPU可以并行处理更多碰撞对
- C. 粒子初始速度在2到5之间随机(每个粒子独立随机)
- D. 平均值3.5，Trail Module的轨迹渲染使用独立的Draw Call，不能与粒子Mesh合批

