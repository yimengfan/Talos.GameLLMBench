# 该文件答题时禁止阅读!!!!

# Unity3D 2022 LLM 能力考察规范 v5.0 出题模型：MiniMax-2.7
题目输出到:./questions.md（1000题）
答案输出到:./answers.md
LLM答题提示词:./llm_prompt.md
评分脚本:./score_answers.py

## 一、考察目标

1. 涵盖 Unity 引擎 90% 以上的知识覆盖面
2. 考察 LLM 基本能力（推理、代码生成、调试）
3. 考察 LLM 容易出错的情况（API幻觉、时序错误、跨领域知识缺失）
4. 考察工程实践能力（热更新、CI/CD、SDK接入）

---

## 二、Unity引擎知识全景图

Unity引擎知识可划分为以下模块，每个模块需要均衡覆盖：

### A. 核心架构模块
- GameObject-Component架构
- 生命周期系统（Awake/Start/Update/OnDestroy等）
- 场景管理（SceneManager）
- 资源管理（Resources/AssetDatabase/Addressables）
- 程序集和脚本编译

### B. 物理系统模块
| 组件/类 | 考察要点 |
|---------|---------|
| Rigidbody | 质量、阻力、重力、约束、碰撞检测 |
| Rigidbody2D | 2D物理差异、Simulate |
| Collider | Box/Sphere/Capsule/Mesh/Compound |
| Collider2D | 2D碰撞体类型 |
| Physics Material | 摩擦、弹性 |
| Joint | Hinge/Fixed/Spring/Slider/Character |
| CharacterController | Move、SimpleMove、isGrounded |
| ForceMode | Acceleration/Force/Impulse/VelocityChange |
| Collision Detection | Discrete/Continuous/ContinuousDynamic |

### C. 渲染系统模块
| 组件/类 | 考察要点 |
|---------|---------|
| Camera | 投影方式、裁剪平面、渲染路径、TargetTexture |
| Light | Directional/Point/Spot、Mode、阴影 |
| Renderer | Materials、shadowCastingMode、receiveShadows |
| MeshFilter/MeshRenderer | 网格、材质 |
| SkinnedMeshRenderer | 蒙皮网格、Bones |
| SpriteRenderer | Sprite、SortingLayer、Mask |
| LineRenderer | 线条渲染 |
| TrailRenderer | 拖尾效果 |
| Material | Shader、Properties、SetFloat/SetColor等 |
| RenderTexture | 渲染纹理 |
| Lightmap | 光照贴图烘焙 |

### D. UI系统基础模块
| 组件/类 | 考察要点 |
|---------|---------|
| Canvas | RenderMode、Scaler、GraphicRaycaster |
| CanvasScaler | UI缩放模式、ReferencePixelsPerUnit |
| EventSystem | InputModules、Raycast |
| GraphicRaycaster | BlockingObjects、blockingMask |
| Image | FillMethod、Sprite、RaycastTarget |
| RawImage | Texture、UVRect |
| Text | Font、Alignment、RichText |
| Button/ Toggle/ Slider/ Scrollbar | 交互组件、事件 |
| ScrollRect | MovementType、viewport、content |
| LayoutGroup | Vertical/Horizontal/Grid |
| ContentSizeFitter | Fit方法 |

### E. 动画系统模块
| 组件/类 | 考察要点 |
|---------|---------|
| Animation | 动画剪辑、播放模式 |
| Animator | Controller、Parameters、States |
| AnimatorController | Layers、StateMachine、Transitions |
| AnimationCurve | 关键帧、插值 |
| AnimationClip | 曲线、事件 |
| Avatar/AvatarMask | 动画重定向 |

### F. 音频系统模块
| 组件/类 | 考察要点 |
|---------|---------|
| AudioSource | Clip、Play/PlayOneShot、3D属性 |
| AudioListener | Volume、gameObject mute |
| AudioMixer | Groups、Expose |
| AudioClip | 加载方式、压缩 |
| AudioChorusFilter等 | 音效滤镜 |

### G. 寻路系统模块
| 组件/类 | 考察要点 |
|---------|---------|
| NavMeshAgent | destination、path、speed、angularSpeed |
| NavMesh | 烘焙、area |
| NavMeshObstacle | carving、shape |
| OffMeshLink | 链接、激活 |
| NavMeshSurface | 运行时烘焙 |

### H. 网络系统模块
| 组件/类 | 考察要点 |
|---------|---------|
| NetworkManager | 客户端/服务器管理 |
| NetworkIdentity | localPlayerAuthority |
| NetworkBehaviour | SyncVar、ClientRpc |
| NetworkTransform | syncMode、compressRotation |

### I. 粒子系统模块
| 组件/类 | 考察要点 |
|---------|---------|
| ParticleSystem | Emission、Shape、VelocityOverLifetime |
| ParticleSystem.MainModule | duration、looping、emission |
| ParticleSystem.EmissionModule | rate、bursts |
| ParticleSystem.ShapeModule | shape、radius |
| ParticleSystemRenderer | renderMode、material |

### J. 其他常用组件
| 组件/类 | 考察要点 |
|---------|---------|
| Terrain | Heightmap、Trees、Detail |
| WindZone | 风力影响 |
| LODGroup | LOD配置 |
| OcclusionArea/AreaCulling | 遮挡剔除区域 |
| ConstantForce | 力矩 |
| JointMotor | 关节电机 |
| JointSpring | 关节弹簧 |
| ConfigurableJoint | 6DOF约束 |

### K. 2D系统模块
| 组件/类 | 考察要点 |
|---------|---------|
| Rigidbody2D | BodyType |
| Collider2D | 各种2D碰撞体 |
| CompositeCollider2D | 复合碰撞 |
| PhysicsMaterial2D | 2D物理材质 |
| Effector2D | AreaEffector/PlatformEffector等 |
| Joint2D | Hinge/Spring/Distance/Slider |
| Camera2D | Zoom、FramingComposing |

### L. 编辑器扩展模块
| 类/特性 | 考察要点 |
|---------|---------|
| EditorWindow | 创建编辑器窗口、OnEnable/OnDisable、GetWindow |
| CustomEditor | 自定义Inspector、Hasifier、绘制时机 |
| PropertyDrawer | 自定义属性绘制、GetPropertyHeight、OnGUI |
| Serialization | SerializeField、SerializeReference、序列化行为 |
| Attribute | Header/Range/Tooltip/HideInInspector/RequireComponent |
| MenuItem | 菜单扩展、快捷键、优先级 |
| ContextMenu | 组件上下文菜单、GameObject菜单 |
| Gizmos | 场景图标绘制、DrawIcon/DrawLine/DrawWireSphere |
| Handles | 编辑器手柄、PositionHandle/FreeMoveHandle/RotationHandle |
| Selection | 选中对象、activeTransform、activeGameObject |
| AssetDatabase | 资源操作、LoadAssetAtPath/SaveAsset/Refresh |
| PrefabUtility | 预制体操作、InstantiatePrefab/SaveAsPrefabAsset |
| Undo | 撤销系统、RecordObject/RegisterCompleteObject |
| EditorGUI/EditorGUILayout | GUI控件、LabelField/IntField/Slider |
| SceneView | 场景视图、FocusSceneView/AddSceneViewCorn |
| AssetModificationProcessor | 资源修改回调、IsAssetDirty/OnWillSaveAssets |
| AssetImporter | 资源导入器、GetAtPath/ChangeExtension |
| ModelImporter | 模型导入、骨骼/动画/材质配置 |
| TextureImporter | 纹理导入、压缩格式/Mipmap/ReadWrite |
| EditorBuildSettings | 构建配置、AddObjectToBuild/GetSceneObject |
| EditorUtility | 编辑器工具、DisplayDialog/SetDirty |
| EditorApplication | 编辑器状态、isPlaying/Update/Exit |
| PropertyModification | 属性修改回调、OnPropertyModified |
| BuildPlayerWindow | 构建窗口、自定义构建选项 |

### M. 资源系统模块
| 类/方法 | 考察要点 |
|---------|---------|
| Resources.Load | 同步加载 |
| AssetBundle | 打包、加载、依赖 |
| Addressables | 异步加载、标签 |
| AsyncOperation | 异步操作 |
| SceneManager | 场景加载/切换 |
| Object.Instantiate | 对象实例化 |
| Object.Destroy | 对象销毁 |
| Object.DontDestroyOnLoad | 持久化 |

### N. 输入系统模块
| 类/方法 | 考察要点 |
|---------|---------|
| Input.GetAxis/GetButton | 轴/按钮输入 |
| Input.GetKey/GetMouseButton | 键盘/鼠标 |
| Touch | 触摸输入 |
| InputField | 输入框 |
| EventSystem | 事件处理 |

### O. 数学和工具模块
| 类/方法 | 考察要点 |
|---------|---------|
| Vector3/Vector2 | 向量运算 |
| Quaternion | 四元数、旋转 |
| Matrix4x4 | 矩阵变换 |
| Mathf | 数学函数 |
| Color/Random | 颜色、随机 |
| Time | 时间控制 |
| Debug | 日志调试 |

### P. 渲染管线模块
| 组件/类 | 考察要点 |
|---------|---------|
| Built-in Render Pipeline | 传统渲染管线 |
| URP | Universal Render Pipeline、轻量级 |
| HDRP | High Definition Render Pipeline、高清 |
| ShaderGraph | 可视化Shader编辑 |
| VFX Graph | 视觉特效图 |
| Render Pipeline Asset | 管线配置 |
| Forward Rendering | 前向渲染 |
| Deferred Rendering | 延迟渲染 |
| CommandBuffer | 命令缓冲 |
| Core RP | 核心渲染管线 |

### Q. 游戏热更新模块
| 技术 | 考察要点 |
|------|---------|
| MonoCLR | IL2CPP/Mono运行时 |
| Lua (xLua/Slua) | Lua热更新机制 |
| C# 热更新 | 游戏逻辑热更新 |
| HybridCLR | 原生C#热更新 |
| AssetBundle热更新 | 资源热更新 |
| 版本管理 | 热更新策略 |
| 增量更新 | 差分更新机制 |

### R. AssetBundle打包加载模块
| 操作 | 考察要点 |
|------|---------|
| BuildPipeline.BuildAssetBundles | AB打包 |
| AssetBundle.LoadFromFile | 本地加载 |
| AssetBundle.LoadFromMemory | 内存加载 |
| AssetBundle.LoadAsset | 同步加载资源 |
| AssetBundle.LoadAssetAsync | 异步加载资源 |
| AssetBundleManifest | 依赖关系 |
| AssetBundle.Unload | 卸载策略 |
| 加密AB | 安全加载 |
| 压缩格式 | LZMA/LZ4压缩 |
| 依赖打包 | 共享依赖 |

### S. SDK接入模块
| SDK类型 | 考察要点 |
|---------|---------|
| 统计分析 | 埋点SDK |
| 广告SDK | 插屏/横幅/激励视频 |
| 推送SDK | 本地/远程推送 |
| 登录SDK | 平台账号 |
| 支付SDK | 内购/三方支付 |
| 分享SDK | 社交分享 |
| 崩溃SDK | 异常收集 |
| 性能SDK | 帧率/内存监控 |
| 推送集成 | iOS/Android差异 |

### T. CI/CD模块
| 技术 | 考察要点 |
|------|---------|
| Unity Build | 命令行构建 |
| Unity Cloud Build | 云构建 |
| Jenkins | 自动化构建 |
| GitHub Actions | CI工作流 |
| Gradle/Xcode | 平台构建 |
| Asset Bundle构建 | 资源打包 |
| 自动化测试 | 编辑器测试 |
| 版本号管理 | 自动递增 |
| 构建产物 | APK/IPA/PC |

### U. UI系统开发模块
| 架构 | 考察要点 |
|------|---------|
| MVC/MVVM | UI架构模式 |
| UIBase | UI基类 |
| Panel管理 | 界面层级 |
| TSD/Flow | 界面状态机 |
| 动画过渡 | Panel切换动画 |
| 数据绑定 | ViewModel绑定 |
| 事件中心 | UI事件分发 |
| 动效系统 | DOTween/Animation |

### V. Gameplay开发模块
| 系统 | 考察要点 |
|------|---------|
| Entity-Component | ECS架构 |
| 技能系统 | 技能配置/释放 |
| Buff/Debuff | 状态系统 |
| 物品系统 | 背包/装备 |
| 任务系统 | 任务配置/触发 |
| 商店系统 | 商品/交易 |
| 存档系统 | 数据持久化 |
| 事件系统 | GameEvent |
| 刷新机制 | Tick系统 |

### W. 战斗开发模块
| 系统 | 考察要点 |
|------|---------|
| 属性系统 | 攻防血速 |
| 战斗公式 | 伤害计算 |
| 技能释放 | 引导/吟唱 |
| 碰撞检测 | 技能范围 |
| 锁定系统 | 目标锁定 |
| 伤害飘字 | 伤害数字 |
| 打击感 | 顿帧/震动 |
| AI行为 | 寻敌/追击 |
| 战斗AI | 决策树 |
| 战斗表现 | 特效/音效 |

---

## 三、LLM高频缺陷检测体系

### 缺陷 1：API 幻觉

**检测题目类型：**
- "以下哪个API不存在？" - 辨别编造API
- "以下API使用是否正确？" - 验证真实API
- "补全代码中空缺的API" - 考察真实API记忆

**高频幻觉举例：**
- Vector3.Mix() - 不存在，应该是Lerp
- Renderer.SetMaterialProperty() - 虚幻API
- Transform.Focus() - 不存在
- Vector3.AngleTo() - 不存在
- Rigidbody.AddForce() 误用ForceMode

### 缺陷 2：生命周期和时序错误

**检测题目类型：**
- 生命周期顺序题（限制每主题型不超过3题）
- 协程执行时机题
- 组件初始化顺序题

### 缺陷 3：跨领域知识缺失

**检测题目类型：**
- 数学应用题（向量、四元数、矩阵）
- 物理参数合理性题
- Shader数学正确性题

### 缺陷 4：资源管理错误

**检测题目类型：**
- Resources/AssetBundle/Addressables使用题
- 场景切换资源处理题
- 内存泄漏检测题

### 缺陷 5：组件配置错误

**检测题目类型：**
- Collider类型选择题
- Physics/Rigidbody参数配置题
- Light/Camera参数配置题
- 2D/3D组件混淆题

### 缺陷 6：工程实践错误

**检测题目类型：**
- 热更新流程错误
- AssetBundle依赖配置错误
- SDK初始化顺序错误
- CI/CD配置错误

---

## 四、题目分布规划（1000题）

### 题目数量分配表

| 模块 | 题数 | 题号区间 | 说明 |
|------|------|---------|------|
| A. 核心架构 | 40 | Q001-Q040 | GameObject/生命周期/脚本编译/Assembly |
| B. C#与脚本编程 | 45 | Q041-Q085 | C#基础/协程/异步/GC/泛型/LINQ |
| C. 物理系统 | 50 | Q086-Q135 | Rigidbody/Collider/Joint/CharacterController |
| D. 渲染基础 | 30 | Q136-Q165 | Camera/Light/Material/LOD/烘焙 |
| E. 动画系统 | 30 | Q166-Q195 | Animator/BlendTree/IK/动画事件 |
| F. 音频系统 | 20 | Q196-Q215 | AudioSource/Mixer/3D音效 |
| G. 导航寻路 | 25 | Q216-Q240 | NavMeshAgent/Obstacle/Surface |
| H. 网络系统 | 25 | Q241-Q265 | Netcode/Mirror/同步/RPC |
| I. 粒子系统 | 20 | Q266-Q285 | ParticleSystem模块/SubEmitter |
| J. ScriptableObject与通用组件 | 20 | Q286-Q305 | SO设计模式/Attribute/通用组件 |
| K. 2D系统 | 25 | Q306-Q330 | 2D物理/Tilemap/SpriteShape |
| L. 编辑器扩展 | 40 | Q331-Q370 | EditorWindow/CustomEditor/Gizmos/Importer |
| M. 资源管理 | 30 | Q371-Q400 | Resources/Addressables/AB基础 |
| N. 输入系统 | 30 | Q401-Q430 | 新Input System/Action/触摸 |
| O. 数学与几何 | 35 | Q431-Q465 | Vector/Quaternion/Matrix/贝塞尔 |
| P. 渲染管线进阶 | 35 | Q466-Q500 | URP/HDRP/后处理/CommandBuffer |
| Q. 热更新方案 | 25 | Q501-Q525 | HybridCLR/Lua/AB热更新 |
| R. AssetBundle进阶 | 20 | Q526-Q545 | 打包策略/依赖管理/加密 |
| S. SDK与平台适配 | 20 | Q546-Q565 | 第三方SDK/平台对接 |
| T. CI/CD与自动化 | 20 | Q566-Q585 | Jenkins/测试/构建流水线 |
| U. UI进阶 | 30 | Q586-Q615 | UI Toolkit/TMP/虚拟列表/适配 |
| V. 游戏逻辑系统 | 30 | Q616-Q645 | 状态机/行为树/事件/存档 |
| W. 战斗系统 | 25 | Q646-Q670 | 伤害公式/Hitbox/Buff/连击 |
| X. Timeline与Cinemachine | 20 | Q671-Q690 | 过场动画/虚拟摄像机 |
| Y. DOTS/ECS | 20 | Q691-Q710 | Entity/Component/System/Baker |
| Z. Job System与Burst | 20 | Q711-Q730 | NativeArray/并行Job/Burst编译 |
| AA. 性能分析与优化 | 30 | Q731-Q760 | Profiler/GC/Draw Call/内存 |
| AB. 序列化与数据管理 | 30 | Q761-Q790 | JSON/Protobuf/存档/配置表 |
| AC. 跨平台开发 | 30 | Q791-Q820 | IL2CPP/Android/iOS/WebGL |
| AD. Shader编程 | 30 | Q821-Q850 | HLSL/光照/后处理/ComputeShader |
| 综合题与高频考点 | 50 | Q851-Q900 | 各模块补充基础/判断题 |
| 附录：高难度综合题 | 100 | Q901-Q1000 | 架构设计/代码阅读/综合场景 |
| **总计** | **1000** | **Q001-Q1000** | **30+模块全覆盖** |

### 能力维度分布

| 维度 | 占比 | 说明 |
|------|------|------|
| API精确度 | 12% | 辨别真假API/参数正确性 |
| 概念理解 | 20% | 核心概念/原理/区别 |
| 代码生成/阅读 | 25% | 代码补全/生成/阅读理解 |
| Bug诊断 | 18% | 错误排查/异常分析 |
| 架构设计 | 15% | 系统设计/方案选型 |
| 性能优化 | 10% | 性能分析/优化方案 |

### 难度分布

| 难度 | 占比 | 说明 |
|------|------|------|
| ★ 入门 | 10% | 基础概念/API使用 |
| ★★ 初级 | 25% | 常用功能/基本原理 |
| ★★★ 中级 | 35% | 进阶用法/原理分析 |
| ★★★★ 高级 | 30% | 架构设计/深度优化/综合 |

### 题型分布

| 形式 | 数量 | 占比 |
|------|------|------|
| 单选题 | 600 | 60% |
| 判断题 | 50 | 5% |
| 代码补全题 | 80 | 8% |
| 代码生成题 | 100 | 10% |
| 代码阅读题 | 70 | 7% |
| 场景设计题 | 60 | 6% |
| 概念/配置题 | 40 | 4% |

---

## 五、组件知识详细考察点

### P. 渲染管线（20题）

**URP/HDRP（8题）：**
1. URP vs Built-in 差异
2. Forward/Deferred渲染选择
3. Renderer Feature 自定义
4. Volume 框架
5. HDRP vs URP 适用场景
6. Render Pipeline Asset 配置
7. 双目渲染/Stereo Rendering
8. 平台特定优化（移动/PC/主机）

**ShaderGraph（6题）：**
1. 节点基础（UV/颜色/数学）
2. 自定义节点
3. 关键字/变体
4. LOD Shader
5. 曲面细分
6. 粒子Shader

**后处理（6题）：**
1. Bloom/发光效果
2. Depth of Field/景深
3. Motion Blur/运动模糊
4. Color Grading/调色
5. Vignette/暗角
6. Post Processing Stack

### Q. 游戏热更新（15题）

**热更新机制（8题）：**
1. IL2CPP vs Mono 区别
2. Lua虚拟机选择(xLua/Slua)
3. C#反射机制热更新
4. HybridCLR原理
5. 热更新范围限制
6. 版本号管理
7. 回滚机制
8. 增量更新策略

**AssetBundle热更新（7题）：**
1. AB热更新流程
2. MD5比对版本
3. CDN下发策略
4. 本地缓存策略
5. 强更vs弱更
6. 资源加密
7. 加载优先级

### R. AssetBundle打包加载（20题）

**打包策略（8题）：**
1. 主动包 vs 被动包
2. 依赖打包原则
3. 共享包拆分
4. 变体策略
5. 压缩格式选择
6. 构建选项
7. 清单文件
8. 打包自动化

**加载机制（8题）：**
1. LoadFromFile vs LoadFromMemory
2. 同步vs异步加载
3. 依赖加载顺序
4. 引用计数管理
5. 场景AB加载
6. 资源卸载时机
7. 内存峰值控制
8. 错误处理

**依赖管理（4题）：**
1. Manifest依赖解析
2. 循环依赖处理
3. GPU显存在AB中的管理
4. Shader预编译

### S. SDK接入（15题）

**初始化流程（5题）：**
1. SDK初始化顺序
2. 模块解耦
3. 生命周期管理
4. 异常处理
5. 多平台适配

**典型SDK（10题）：**
1. 埋点设计
2. 广告填充逻辑
3. 推送注册
4. 平台账号SSO
5. IAP流程
6. 分享回调
7. 崩溃堆栈收集
8. 性能监控
9. 推送权限
10. SDK版本兼容

### T. CI/CD（12题）

**构建系统（6题）：**
1. Unity命令行构建
2. Gradle/Xcodebuild
3. 多平台构建
4. 构建缓存
5. 产物签名
6. 自动化测试

**流水线（6题）：**
1. Jenkins/GHA配置
2. 构建触发器
3. 版本号生成
4. 增量构建
5. 构建通知
6. 构建产物分发

### U. UI系统开发（15题）

**架构设计（6题）：**
1. MVC vs MVVM选择
2. UIBase类设计
3. Panel堆栈管理
4. 界面生命周期
5. 数据绑定实现
6. 事件总线设计

**动效开发（5题）：**
1. Tween动画
2. Panel过渡动画
3. 粒子特效集成
4. 骨骼动画UI
5. Shader UI特效

**适配优化（4题）：**
1. 多分辨率适配
2. 深色/浅色主题
3. UI批处理优化
4. 懒加载UI

### V. Gameplay开发（17题）

**核心系统（8题）：**
1. ECS vs传统OOP
2. 技能系统设计
3. Buff/Debuff机制
4. 物品/装备系统
5. 任务系统配置
6. 事件驱动设计
7. 配置表设计
8. 存档加密

**常用模式（5题）：**
1. 对象池应用
2. 状态机应用
3. 观察者模式
4. 命令模式
5. 享元模式

**工程实践（4题）：**
1. 代码结构
2. 命名规范
3. 配置表规范
4. 日志系统

### W. 战斗开发（15题）

**数值系统（5题）：**
1. 属性定义
2. 伤害公式
3. 暴击/穿透
4. 抗性减伤
5. 速度计算

**技能表现（5题）：**
1. 技能范围检测
2. 引导/吟唱
3. 子弹/投射物
4. 锁定目标
5. 伤害数字

**战斗AI（5题）：**
1. 寻敌逻辑
2. 仇恨系统
3. 技能CD
4. 走位策略
5. BOSS行为

### L. 编辑器扩展详细考察点（25题）

**EditorWindow（5题）：**
1. GetWindow<T>()创建窗口
2. OnEnable/OnDisable生命周期
3. titleContent/position设置
4. ShowNotification显示通知
5. wantsMouseMove/wantsMouseEnterLeaveWindow

**CustomEditor（5题）：**
1. [CustomEditor(typeof(T))]特性
2. Hasifier判断绘制
3. OnInspectorGUI重绘
4. serializedObject/serializedProperty
5. DrawDefaultInspector默认绘制

**PropertyDrawer（3题）：**
1. GetPropertyHeight获取高度
2. OnGUI绘制GUI
3. 适用于自定义类型/属性

**序列化系统（4题）：**
1. [SerializeField]序列化私有字段
2. [SerializeReference]引用类型多态序列化
3. OnBeforeSerialize/OnAfterSerialize
4. 循环引用处理

**MenuItem和ContextMenu（3题）：**
1. MenuItem菜单扩展、快捷键%/*/$
2. ContextMenu添加组件菜单
3. ContextMenuItem回调

**Gizmos和Handles（5题）：**
1. Gizmos.DrawIcon/Line/WireSphere
2. Handles.PositionHandle/FreeMoveHandle
3. Handles.RotationHandle/ScaleHandle
4. Handles.Button点击检测
5. Handles.Label标签绘制

**AssetDatabase（3题）：**
1. LoadAssetAtPath/LoadAllAssets
2. SaveAssets/Refresh
3. GetAssetPath/GetGUID

**SceneView和Editor工具（3题）：**
1. SceneView.OnSceneFunc自定义场景绘制
2. EditorUtility.DisplayPopupMenu
3. EditorUtility.SetDirty标记脏

**资源导入器（2题）：**
1. AssetImporter自定义导入器
2. OnPostprocessAsset资产导入后处理

---

## 六、验证方式

- **编译验证：** 代码生成题必须通过C#编译
- **行为测试：** 功能实现题需要通过行为验证
- **PASS/FAIL判定：** Bug修复题修复后测试必须通过
- **回归检测：** 修复不能破坏已有通过的测试
- **代码审查：** 生成的代码符合Unity最佳实践

---

## 七、答案输出与评分体系

### 7.1 标准答案格式（answers.md）

```
**Q001.** C　　`[考点名]`
**Q002.** C　　`[考点名]`
**Q003.** C　　`[考点名]`
```

- 单选题：C（所有正确答案统一为C）
- 判断题：C（正确）

### 7.2 选项置换规则

为确保所有题目答案统一为C选项，出题时需遵循以下规则：

1. **选项置换原则**：将正确答案所在的选项内容与C选项内容互换
2. **保持干扰项质量**：置换后的干扰项仍需符合迷惑性要求
3. **避免明显规律**：C选项内容应与其他选项长度、形式保持一致
4. **判断题特殊处理**：判断题中，C选项代表"正确"，错误选项置于A/B/D

### 7.3 LLM答题输出格式

LLM在答题时需严格按以下格式输出，不含任何解释文字：
```
Q001. C
Q002. C
Q003. C
```

标准提示词模板见 `Unity3d/llm_prompt.md`。

### 7.3 评分脚本使用

```bash
python3 Unity3d/score_answers.py --answer answers.md --llm llm_answer.txt --detail
```

评分维度：
- **按模块**：30个知识模块各自的正确率
- **按能力维度**：概念理解、API精确度、代码生成/阅读、Bug诊断、性能优化、架构设计
- **按难度等级**：★ ~ ★★★★★
- **按题型**：单选、判断、代码补全、代码生成、代码阅读、场景设计

---

## 八、选项设计规范（迷惑性要求）

### 8.1 干扰项设计原则

1. **技术相关性**：干扰项必须是与题目领域相关的技术概念，不能是无关词汇
2. **长度均衡**：所有选项长度应大致相当（±30%），避免正确答案明显长于其他选项
3. **正确位置随机**：正确答案的位置应在A/B/C/D间均匀分布
4. **常见误区**：干扰项应来自开发者常见的理解错误或相近概念混淆

### 8.2 禁止使用的干扰选项模式

以下模式过于明显，LLM和人类都能轻易排除：

| 禁止模式 | 示例 | 替代方案 |
|---------|------|---------|
| 否定式废话 | "不需要"、"不影响"、"没有区别" | 用具体但错误的技术描述 |
| 绝对化表述 | "完全相同"、"不会有任何问题" | 用有条件但不完全正确的表述 |
| 非技术选项 | "全部默认"、"用最新的"、"抄别人的" | 用具体但不适用的技术方案 |
| 极端简短 | 两三个字的选项 | 补充技术细节使长度接近正确答案 |
| 跨领域混淆 | 在物理题中放渲染概念 | 用同领域的相近但不正确的概念 |

### 8.3 良好干扰项示例

**示例：MonoBehaviour生命周期顺序**

❌ 差的选项设计：
- A. Awake在Start之前执行 ← 正确（明显最长最详细）
- B. 没有区别 ← 太明显
- C. 不影响 ← 太明显
- D. 看情况 ← 太明显

✅ 好的选项设计：
- A. Start在Awake之前执行，Start在组件首次激活时调用
- B. 两者都在首帧Update之前调用，执行顺序取决于Inspector中组件排列顺序
- C. Awake在Start之前执行，Awake在对象实例化时调用，Start在第一帧Update之前调用 ← 正确
- D. Awake和Start都在实例化时立即调用，但Awake仅在enabled为true时执行

---

## 九、一句话总结

测 LLM 引擎开发能力 = 用统一极简脚手架 + 固定 prompt + 确定性验证（编译/测试/pass-fail），重点挖 **API幻觉、时序错误、资源管理、组件配置、工程实践** 五个高频致命缺陷，考察范围覆盖 **基础组件、渲染管线、热更新、CI/CD、Gameplay、战斗开发** 全链路知识。
