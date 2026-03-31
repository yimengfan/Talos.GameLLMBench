# 该文件答题时禁止阅读!!!!

# Unity3D 2022 LLM 能力考察规范 v6.0
4. 题目输出到: `./questions/` 目录下，分为 10 个文件，如 `questions_01_core.md` 到 `questions_10_advanced.md`。
5. 答案密钥输出到: `./answer_key/` 目录下，对应 10 个文件。
6. LLM答题提示词: `./llm_prompt.md`
7. 评分脚本: `./run_score.sh` (一键聚合评分)

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

### 7.1 答案密钥文件

每道题的正确答案通过独立答案密钥文件记录，评分时只读取 `./answer_key/` 目录下对应分片文件。

**答案密钥文件示例：**

```
**Q001.** A
**Q002.** B
**Q003.** C
**Q004.** D
```

- 题库文件与答案文件按相同分片命名组织
- 评分专用答案密钥禁止暴露给被测LLM
- 题目改动后必须同步更新对应答案密钥

### 7.2 LLM答题输出格式

LLM在答题时需严格按以下格式输出，不含任何解释文字：
```
Q001. A
Q002. B
Q003. D
Q004. C
```

标准提示词模板见 `llm_prompt.md`。

### 7.3 评分脚本使用

```bash
python3 score_answers.py --answer answer_key.md --llm llm_answer.txt --detail
```

评分维度：
- **按模块**：30个知识模块各自的正确率
- **按能力维度**：概念理解、API精确度、代码生成/阅读、Bug诊断、性能优化、架构设计
- **按难度等级**：★ ~ ★★★★★
- **按题型**：单选、判断、代码补全、代码生成、代码阅读、场景设计

---

## 八、高质量出题与反 AI 废话规范（核心红线）

为确保题库能够真正考察 LLM 的专家级能力，必须彻底杜绝“机器生成感”和“凑数选项”。出题质量是整个 Benchmark 的生命线。

### 8.1 干扰项设计原则（专家级迷惑性）

1. **技术合理性**：干扰项必须是与题目领域相关的、**看似合理**的技术概念。它们应该是初中级开发者真实容易犯的错误、过时的技术方案、或者在其他语境下正确但在此场景下错误的方案。
2. **长度与颗粒度均衡**：所有选项（A/B/C/D）的代码量或文字长度必须大致相当（差距控制在 ±20% 以内）。绝不能出现“正确答案详尽无比（三行字），错误答案短小空洞（两三个字）”的泄题现象。
3. **正确位置随机**：正确答案的位置应在A/B/C/D间均匀分布。
4. **工业界真实痛点**：选项和题干应尽量结合真实的商业项目场景（如：海量怪物同屏、内存泄漏排查、GC 尖峰、IL2CPP 代码裁剪、Shader 变体爆炸、AssetBundle 循环依赖等）。

### 8.2 绝对禁止的 AI 废话套路与出题红线

在大量 AI 自动生成的题目中，经常会出现用于“凑字数”的万能废话。**在生成和审核题目时，必须像代码审查一样严格扫除以下红线特征**：

| 严禁使用的 AI 废话模式 | 典型高频“毒词”示例（见到即视为不合格） | 正确的替代方案（如何写专家级干扰项） |
|---------|------|---------|
| **题干直接泄题（最致命）** | "Rigidbody设置IsKinematic为true后，该物体不再受物理引擎控制。请问..." | 题干必须是疑问句。例如："当Rigidbody的IsKinematic为true时，以下描述正确的是？" |
| **万金油式否定废话** | "这是一种非官方的Hack手段"、"该步骤不是必需的"、"该技术方案没有明显优势"、"在小型项目中反而增加复杂度" | 描述一个具体但错误的技术后果。如："这会导致该组件的 Awake 方法被跳过执行" |
| **推卸给版本或底层的废话** | "该问题与Unity版本相关，建议查阅Release Notes"、"引擎在底层已自动处理相关逻辑，无需额外配置"、"相关功能仅在旧版支持，最新版已移除" | 描述具体的底层机制错误。如："底层管线会强制将其归入 Opaque 渲染队列，导致半透明失效" |
| **乱用性能术语凑数** | "因为涉及跨线程同步和额外的内存拷贝开销"、"这种处理方式会引发严重的内存碎片问题"（在完全不相关的题目中滥用） | 只有在真实涉及多线程或GC的题目中才能使用这些词汇，且必须符合逻辑。 |
| **绝对化/敷衍表述** | "完全相同"、"不会有任何问题"、"不需要"、"看情况"、"全部默认" | 补充完整的技术条件。如："仅在开启了 GPU Instancing 时两者表现相同，否则会打断合批" |
| **生造凑数选项** | 题目问 ForceMode，选项生造了 "Linear"、"Smooth" | 干扰项必须是真实存在的同领域 API 或概念（如混用 `VelocityChange` 和 `Impulse`） |

### 8.3 良好与糟糕的选项对比示例

**示例：MonoBehaviour生命周期顺序**

❌ **糟糕的 AI 生成式选项（长度不均，充斥废话）**：
- A. Start 在 Awake 之前执行，Start 在组件首次激活时调用。
- B. 这是一种非官方的Hack手段，极易导致不同平台间的兼容性问题。（*典型AI废话*）
- C. Awake在Start之前执行，Awake在对象实例化时调用，Start在第一帧Update之前调用。（*正确答案，且明显最长*）
- D. 引擎底层会自动处理，不需要关心。（*典型AI废话*）

✅ **高质量的专家级选项（长度均衡，技术性强，极具迷惑性）**：
- A. `Start` 在 `Awake` 之前执行。`Start` 是在对象被 `Instantiate` 实例化的瞬间立即同步调用的，而 `Awake` 会推迟到该对象第一次参与物理计算前才调用。
- B. 两者都在首帧 `Update` 之前调用，但它们的执行顺序并不固定，完全取决于 Inspector 面板中脚本挂载的先后顺序以及 `Script Execution Order` 的配置。
- C. `Awake` 在 `Start` 之前执行。`Awake` 在对象实例化或场景加载完毕时触发，而 `Start` 则会在该脚本实例的第一个 `Update` 执行之前的同一帧内被调用。
- D. `Awake` 和 `Start` 都在实例化时立即执行。但如果预制体实例化时传入了 `inactive` 状态，则 `Awake` 会执行，而 `Start` 会被无限期挂起直到手动 `SetActive(true)`。

---

## 九、一句话总结

测 LLM 引擎开发能力 = 用统一极简脚手架 + 固定 prompt + 确定性验证（编译/测试/pass-fail），重点挖 **API幻觉、时序错误、资源管理、组件配置、工程实践** 五个高频致命缺陷，考察范围覆盖 **基础组件、渲染管线、热更新、CI/CD、Gameplay、战斗开发** 全链路知识。
