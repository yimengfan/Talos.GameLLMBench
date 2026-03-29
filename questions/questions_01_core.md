# Unity3D 2022 LTS 基础能力问答题库 - 01_core

**Q001.** [模块:A][维度:API精确度][难度:★][题型:单选]

MonoBehaviour的Awake()和Start()的执行顺序是？

- A. Awake在Start之前执行，Awake在对象实例化时调用，Start在第一帧Update之前调用
- B. 两者都在首帧Update之前调用，但执行顺序取决于Inspector中组件的排列顺序
- C. Awake和Start都在实例化时立即调用，但Awake仅在脚本enabled为true时才执行
- D. Start在Awake之前执行，Start在组件首次激活时调用，Awake在第一帧Update之前调用

**Q002.** [模块:A][维度:API精确度][难度:★][题型:单选]

Update()和FixedUpdate()的区别是？

- A. Update和FixedUpdate的调用频率相同，但FixedUpdate不受Time.timeScale影响
- B. Update每帧调用一次，FixedUpdate按固定时间间隔调用（默认0.02秒）
- C. Update按固定时间间隔调用（默认0.02秒），FixedUpdate每帧调用一次
- D. FixedUpdate在每帧渲染后调用，Update在物理模拟前调用，两者调用频率可能不同

**Q003.** [模块:A][维度:概念理解][难度:★][题型:单选]

Unity中GameObject和Component的关系是？

- A. GameObject继承自Component，所有引擎对象都是Component的派生类
- B. GameObject和Component都继承自MonoBehaviour，是平行关系
- C. GameObject是实体容器，Component是附加在GameObject上的功能模块
- D. Component是实体容器，GameObject是附加在Component上的功能模块

**Q004.** [模块:A][维度:API精确度][难度:★★][题型:单选]

以下获取组件的方式，哪种性能最差且应避免在Update中使用？

- A. GetComponent<T>()在每帧调用时（未缓存对象引用情况下）
- B. GameObject.Find("Name").GetComponent<T>()
- C. transform.GetChild(0).GetComponent<T>()在子物体数量较多时
- D. GetComponentInChildren<T>(true)搜索所有子级包含inactive对象

**Q005.** [模块:A][维度:概念理解][难度:★★][题型:单选]

Transform.SetParent(newParent, worldPositionStays)中第二个参数为true时表示？

- A. 保持物体相对于新Parent的本地坐标不变
- B. 保持物体的世界坐标位置不变
- C. 自动等比缩放物体使其保持在新Parent的局部坐标系原点
- D. 保持物体的世界旋转不变但允许位置跟随Parent变化

**Q006.** [模块:A][维度:API精确度][难度:★★][题型:单选]

以下哪个API在Unity 2022 LTS中不存在？

- A. Physics.OverlapSphereNonAlloc()
- B. Application.targetFrameRate
- C. Renderer.SetMaterialProperty()
- D. Transform.SetPositionAndRotation()

**Q007.** [模块:A][维度:概念理解][难度:★★][题型:单选]

MonoBehaviour生命周期中以下方法按正确的调用顺序排列？

- A. Awake → OnEnable → Start → FixedUpdate → Update → LateUpdate
- B. Start → Awake → OnEnable → Update → LateUpdate
- C. OnEnable → Awake → Start → Update → FixedUpdate → LateUpdate
- D. Awake → Start → OnEnable → FixedUpdate → Update → LateUpdate

**Q008.** [模块:A][维度:代码生成/阅读][难度:★★][题型:代码补全]

完成一个线程安全的MonoBehaviour单例：
```csharp
public class GameManager : MonoBehaviour {
static GameManager instance;
public static GameManager Instance {
get {
if(instance == null)
instance = FindObjectOfType<GameManager>();
return instance;
}
}
void Awake() {
if(instance != null && instance != this) {
_____(gameObject);
return;
}
instance = this;
DontDestroyOnLoad(gameObject);
}
}
```

- A. DestroyImmediate
- B. Unload
- C. DestroyObject
- D. Destroy

**Q009.** [模块:A][维度:Bug诊断][难度:★★★][题型:代码阅读]

以下代码将相机跟随放在Update中，可能产生什么问题？
```csharp
void Update() {
transform.position = target.position + offset;
}
```

- A. 代码正常运行，Unity保证同帧内所有Update按确定顺序执行，不会产生抖动
- B. 相机会抖动，因为角色移动在同帧的Update中可能在相机之后执行，应放到LateUpdate
- C. 相机会穿墙，因为Update中没有做物理碰撞检测来限制相机移动范围
- D. transform.position赋值在Update中无效，必须通过Rigidbody.MovePosition来移动相机

**Q010.** [模块:A][维度:概念理解][难度:★★][题型:单选]

SceneManager.LoadScene和SceneManager.LoadSceneAsync的区别是？

- A. LoadScene同步加载（会阻塞主线程导致卡顿），LoadSceneAsync异步加载（不阻塞）
- B. LoadScene用于Additive模式加载场景，LoadSceneAsync用于Single模式替换场景
- C. LoadScene异步加载（不阻塞主线程），LoadSceneAsync同步加载（会导致卡顿）
- D. LoadScene只能加载Build Settings中的场景，LoadSceneAsync可以加载Resources中的任意场景

**Q011.** [模块:A][维度:API精确度][难度:★★][题型:单选]

Destroy(gameObject, 5f)的行为是？

- A. 5秒后销毁该GameObject
- B. 在接下来的5帧内逐步禁用该GameObject上的组件后再销毁
- C. 将该GameObject设为Inactive状态5秒后再调用DestroyImmediate彻底移除
- D. 立即标记销毁并在当前帧结束前移除该GameObject及其所有子物体

**Q012.** [模块:A][维度:概念理解][难度:★★★][题型:单选]

Instantiate()返回的对象和原Prefab的关系是？

- A. 返回一个空的GameObject，需要手动从Prefab复制组件和属性
- B. 返回的是Prefab的一个完整克隆（实例），修改实例不影响Prefab
- C. 返回的是Prefab的浅拷贝，共享材质和Mesh数据，修改材质会影响所有同Prefab实例
- D. 返回的是对原Prefab Asset的引用，修改返回对象等同于修改Prefab本身

**Q013.** [模块:A][维度:API精确度][难度:★★][题型:单选]

DestroyImmediate和Destroy的区别：以下描述正确的是？。以下描述正确的是？

- A. 两者的区别仅在于DestroyImmediate会同时销毁对象的子对象，Destroy不会
- B. DestroyImmediate在下一帧销毁，Destroy在当前帧结束时销毁
- C. 两者功能完全相同，DestroyImmediate只是Destroy的别名方法
- D. DestroyImmediate立即销毁对象，Destroy在当前帧结束时销毁

**Q014.** [模块:A][维度:概念理解][难度:★★★][题型:单选]

Tag和Layer的区别和使用场景是？

- A. Tag用于标识分类（如"Player","Enemy"），Layer用于物理碰撞过滤和Camera渲染过滤
- B. Layer用于标识对象类型，最多支持8个自定义Layer；Tag仅用于Sorting Layer渲染排序
- C. Tag和Layer都可用于物理碰撞过滤，区别在于Tag是字符串标识而Layer是基于位掩码的整数
- D. Tag用于物理碰撞过滤和Camera Culling Mask过滤，Layer用于标识分类（如"Player","Enemy"）

**Q015.** [模块:A][维度:代码生成/阅读][难度:★★★][题型:代码补全]

完成一个等待3秒后执行操作的协程：
```csharp
IEnumerator DelayedAction() {
yield return new _____(3f);
DoSomething();
}
```

- A. WaitForSecondsRealtime
- B. WaitForFixedUpdate
- C. WaitUntil
- D. WaitForSeconds

**Q016.** [模块:A][维度:概念理解][难度:★★★][题型:单选]

以下哪些可以作为协程中yield return的参数？

- A. WaitForEndOfFrame只能在OnGUI中有效，在协程中会被忽略
- B. 协程中只能使用WaitForSeconds，其他参数需要用Task替代
- C. null（等待下一帧）
- D. yield return null会导致协程立即终止，不能用于等待下一帧

**Q017.** [模块:A][维度:Bug诊断][难度:★★★][题型:代码阅读]

以下代码在运行时报NullReferenceException，可能原因是什么？
```csharp
void Start() {
var rb = GetComponent<Rigidbody>();
rb.AddForce(Vector3.up * 10);
}
```

- A. Start方法在Rigidbody组件初始化之前执行，物理组件尚未就绪
- B. Vector3.up * 10超出了AddForce允许的力值范围限制，触发异常
- C. 该GameObject上没有Rigidbody组件，GetComponent返回null
- D. AddForce的参数类型不匹配，应传入ForceMode枚举而不是Vector3

**Q018.** [模块:A][维度:概念理解][难度:★★★][题型:单选]

OnEnable()和OnDisable()的调用时机是？

- A. OnEnable仅在Awake之后调用一次，OnDisable仅在OnDestroy之前调用一次
- B. OnEnable在SetActive(true)之后的下一帧调用，OnDisable在SetActive(false)的下一帧调用
- C. OnEnable在每帧Update之前检查脚本状态后调用，OnDisable在LateUpdate之后调用
- D. OnEnable在脚本启用时调用，OnDisable在脚本禁用或物体销毁前调用

**Q019.** [模块:A][维度:性能优化][难度:★★★][题型:单选]

为什么应该避免在Update中使用FindObjectOfType？

- A. 它只能查找继承自MonoBehaviour的组件，无法查找原生Component如Transform
- B. 它每次调用都要遍历所有活动对象，性能开销大
- C. 它返回的对象类型不安全，多线程环境下可能产生InvalidCastException
- D. 它已在Unity 2022中被标记为Obsolete，编译时会产生警告导致CI构建失败

**Q020.** [模块:A][维度:概念理解][难度:★★★][题型:单选]

如何控制两个MonoBehaviour脚本的执行顺序？

- A. 在Edit → Preferences中设置全局脚本优先级，或通过[ExecuteAlways]属性控制
- B. 通过在脚本中重写ExecutionPriority属性来设置执行优先级，值越大越先执行
- C. 在Project Settings → Script Execution Order中设置，或使用[DefaultExecutionOrder]属性
- D. 在Hierarchy窗口中调整GameObject的排列顺序来控制其上脚本的执行顺序

**Q021.** [模块:A][维度:API精确度][难度:★★★][题型:单选]

Application.streamingAssetsPath和Application.persistentDataPath的区别是？

- A. streamingAssetsPath是可读写的持久化目录，persistentDataPath是只读的打包资源目录
- B. streamingAssetsPath是只读的资源目录（打包时包含），persistentDataPath是可读写的持久化目录
- C. streamingAssetsPath和persistentDataPath都指向Application.dataPath的子目录，区别在于压缩方式
- D. streamingAssetsPath在所有平台上都可读写，persistentDataPath只在PC/Mac平台可用

**Q022.** [模块:A][维度:代码生成/阅读][难度:★★★][题型:代码生成]

以下代码使用SendMessage，有什么缺点？
```csharp
gameObject.SendMessage("OnDamage", 10f);
```

- A. SendMessage会广播到场景中所有激活的GameObject，产生大量不必要的方法查找开销
- B. SendMessage仅支持无参方法调用，传递10f参数会导致运行时ArgumentException
- C. 使用字符串标识方法名，无编译时检查，性能差，推荐使用接口或事件系统
- D. SendMessage性能优于直接方法调用，但无法传递值类型参数（仅支持引用类型）

**Q023.** [模块:A][维度:概念理解][难度:★★★][题型:单选]

Static Batching和Dynamic Batching的区别是？

- A. Static Batching在运行时动态合并网格，Dynamic Batching在构建时预合并网格以提高效率
- B. Static Batching处理不透明物体的合批渲染，Dynamic Batching处理半透明物体的合批渲染
- C. Static Batching针对静止不动的物体（需标记Static），Dynamic Batching针对小面数的移动物体（自动合批）
- D. Static Batching针对小面数移动物体（自动合批），Dynamic Batching针对静止物体（需标记Static）

**Q024.** [模块:A][维度:性能优化][难度:★★★★][题型:单选]

在Update中使用字符串拼接 string s = "HP:" + health; 的问题是？

- A. 每帧产生GC分配（string是引用类型，拼接创建新对象），应使用StringBuilder或TextMeshPro.SetText
- B. string拼接仅在IL2CPP构建中才会产生GC问题，Mono后端下编译器会自动优化为栈分配
- C. string拼接在Update中与StringBuilder性能一致，JIT编译器会自动优化为StringBuilder操作
- D. health为数值类型不能与string直接拼接，需要显式调用Convert.ToString()否则编译错误

**Q025.** [模块:A][维度:概念理解][难度:★★★★][题型:单选]

UnityEvent和C# event的区别是？

- A. UnityEvent可在Inspector中编辑绑定，C# event只能代码绑定；UnityEvent有序列化开销
- B. UnityEvent和C# event都支持Inspector编辑绑定，但C# event额外支持多线程安全调用
- C. C# event可以在Inspector中编辑绑定且性能更优，UnityEvent仅支持代码中动态绑定
- D. UnityEvent在IL2CPP构建时会被自动转换为C# delegate，运行时行为完全一致

**Q026.** [模块:A][维度:概念理解][难度:★★★★][题型:单选]

Unity中Managed Memory和Native Memory的区别是？

- A. Managed是Unity引擎C++层管理的内存（包含纹理和Mesh），Native是C# GC管理的脚本内存
- B. Managed和Native都由GC管理，区别在于Managed使用Incremental GC，Native使用Mark-and-Sweep GC
- C. Managed内存用于存储纹理和Mesh数据由开发者手动释放，Native内存用于C#对象由GC自动管理
- D. Managed是C# GC管理的堆内存，Native是Unity引擎C++层管理的内存（纹理、Mesh等）

**Q027.** [模块:A][维度:概念理解][难度:★★★★][题型:单选]

Unity编辑器中关闭Domain Reload以加速进入Play Mode后需要注意什么？

- A. ScriptableObject的数据会被清除，需要通过EditorPrefs在退出Play Mode时手动保存
- B. 静态变量不会在进入Play Mode时重置，需手动初始化或使用[RuntimeInitializeOnLoadMethod]
- C. MonoBehaviour实例会在进入Play Mode时自动调用Reset方法重置所有序列化字段
- D. 协程的执行状态不会被保留，所有运行中的协程在进入Play Mode时需要手动重新启动

**Q028.** [模块:A][维度:Bug诊断][难度:★★★★][题型:代码阅读]

以下两个脚本在同一GameObject上，有什么执行顺序问题？
```csharp
// ScriptA: void Awake() { data = LoadData(); }
// ScriptB: void Awake() { Process(FindObjectOfType<ScriptA>().data); }
```

- A. 同一GameObject上的脚本Awake始终按组件添加顺序执行，问题在于LoadData是异步操作
- B. LoadData()在Awake中调用会阻塞主线程导致死锁，应该在Start中使用async调用
- C. FindObjectOfType在Awake中调用会返回null，该API仅在Start及之后的生命周期中可用
- D. 两个脚本的Awake执行顺序不确定，ScriptB可能在ScriptA之前执行导致data为null

**Q029.** [模块:A][维度:概念理解][难度:★★★][题型:单选]

Assembly Definition(.asmdef)文件的作用是？

- A. 将C#代码编译为本地汇编指令（类似Burst Compiler），提升运行时性能
- B. 定义平台特定的编译指令和宏定义，控制不同平台的条件编译分支
- C. 配置项目的程序集签名和版本号，用于NuGet包的发布和依赖管理
- D. 将代码分成独立程序集，加速增量编译（只重编变化的程序集）

**Q030.** [模块:A][维度:概念理解][难度:★★★][题型:单选]

Unity Package Manager(UPM)的作用是？

- A. 管理项目的构建配置和输出平台，包括Android/iOS/WebGL的打包选项
- B. 管理Unity场景中的资源引用和依赖关系，自动检测并解决场景间的引用冲突
- C. 管理Unity官方包和第三方包的安装、更新和版本控制
- D. 管理Unity编辑器插件的安装和激活，支持编辑器扩展的热加载和卸载

**Q031.** [模块:A][维度:概念理解][难度:★★★★][题型:场景设计]

设计一个Unity游戏的合理启动流程顺序是？

- A. 框架初始化→配置加载→资源预热→登录/更新检查→进入主界面
- B. 登录验证→全量资源加载→配置解析→主界面渲染→框架异步初始化
- C. 主界面立即渲染→异步框架初始化→按需配置加载→延迟登录→资源流式加载
- D. 资源预热→框架初始化→主界面渲染→后台异步配置加载→延迟登录验证

**Q032.** [模块:A][维度:架构设计][难度:★★★★][题型:场景设计]

大型Unity项目推荐的代码架构层次是？

- A. 表现层(UI/特效)→业务层(具体功能)→服务层(业务通用)→框架层(底层通用)
- B. 按Unity概念划分：MonoBehaviour层→ScriptableObject层→纯C#层→Editor层
- C. 框架层(底层通用)→服务层(业务通用)→业务层(具体功能)→表现层(UI/特效)
- D. 按功能类型平铺：Manager层(所有管理器)→Util层(工具类)→Data层(数据类)→UI层(界面)

**Q033.** [模块:A][维度:概念理解][难度:★★★★][题型:单选]

Unity中协程、async/await和Thread的区别是？

- A. 三者都在主线程执行，区别在于yield/await/Join的语法差异和回调调度时机不同
- B. 协程在独立的Unity协程线程执行且可以安全访问Unity API，async在主线程执行，Thread在后台线程
- C. 协程和async在主线程执行（不能CPU密集计算），Thread是真正多线程（但不能直接访问Unity API）
- D. async/await在Unity中默认创建新线程执行，协程本质上基于线程池的Task实现

**Q034.** [模块:A][维度:概念理解][难度:★★★★][题型:单选]

Unity 2022 LTS的新特性/改进包括？

- A. 原生支持Vulkan 1.3和DirectX 12 Ultimate
- B. 全新的物理引擎替代PhysX，性能提升200%
- C. 内置AI行为树系统和视觉脚本编辑器
- D. 改进的UI Toolkit

**Q035.** [模块:A][维度:概念理解][难度:★★★][题型:单选]

在Unity中可以手动调用System.GC.Collect()。推荐在加载界面等不敏感时机调用以减少游玩时的GC Spike。

- A. 该方法仅适用于Mono运行时，在IL2CPP下调用会直接崩溃
- B. 可以手动调用，推荐在加载界面等不敏感时机调用以减少游玩时的GC Spike
- C. 仅在游戏启动时由Unity自动调用，开发者不应手动调用会导致内存泄漏
- D. 手动调用无效，Unity使用自己的内存管理系统而非.NET GC

**Q036.** [模块:A][维度:概念理解][难度:★★★][题型:单选]

Prefab Variant的用途是？

- A. 将多个不同的Prefab合并为一个组合Prefab，共享所有组件和属性设置
- B. 基于Base Prefab创建变体，继承Base的修改但可覆盖部分属性
- C. 将Prefab导出为独立的Asset文件，解除与Base Prefab所有关联以降低耦合
- D. 创建Prefab的轻量级引用（不拷贝数据），运行时动态加载Base Prefab并应用差异补丁

**Q037.** [模块:A][维度:概念理解][难度:★★★★][题型:单选]

Scriptable Build Pipeline(SBP)的作用是？

- A. 管理场景构建列表和构建编号，自动生成Player Build配置
- B. 替代Unity默认的C#编译器（Roslyn），支持更高版本的C#语法特性和更快编译速度
- C. 提供可编程的AssetBundle构建管线，支持自定义构建流程和缓存
- D. 控制渲染管线的构建过程，优化Shader编译时间和变体收集覆盖率

**Q038.** [模块:A][维度:概念理解][难度:★★★★][题型:单选]

Unity的Incremental GC(增量垃圾回收)的好处是？

- A. 完全消除GC暂停，改为引用计数方式管理所有托管内存的分配和释放
- B. 将GC工作分散到多帧执行，减少单帧GC卡顿
- C. 在独立的后台GC线程执行垃圾回收工作，对主线程渲染和逻辑无任何影响
- D. 增加可用堆内存上限至4GB，减少GC触发频率但不改变单次GC的耗时

**Q039.** [模块:A][维度:概念理解][难度:★★★][题型:单选]

DontDestroyOnLoad(gameObject)的作用是？

- A. 使该GameObject在运行时无法通过Destroy销毁（类似const标记），直到应用退出
- B. 将该GameObject从当前场景移除并缓存到内存，在切换回原场景时自动恢复
- C. 使该GameObject的Transform锁定当前世界位置，场景切换后坐标保持不变
- D. 使该GameObject在场景切换时不被销毁

**Q041.** [模块:B][维度:概念理解][难度:★][题型:单选]

Rigidbody组件的作用是？

- A. 控制物体在动画系统中的骨骼绑定和蒙皮权重
- B. 定义物体的碰撞形状和范围，但不参与物理力的计算
- C. 使GameObject参与物理模拟（受重力、力、碰撞影响）
- D. 用于在Scene视图中可视化物理碰撞体的边界和形状辅助线

**Q042.** [模块:B][维度:API精确度][难度:★][题型:单选]

Rigidbody.AddForce(force, ForceMode.Impulse)的效果是？

- A. 施加持续加速度，效果与ForceMode.Acceleration相同但不受质量影响
- B. 只改变物体的角速度（旋转），不影响线速度
- C. 在每个FixedUpdate中持续施加该力，直到手动停止
- D. 施加瞬间冲量（不考虑时间），直接改变速度

**Q043.** [模块:B][维度:概念理解][难度:★★][题型:单选]

以下哪种Collider在物理计算中开销最大？

- A. MeshCollider（非凸），因为需要逐三角面进行碰撞检测
- B. SphereCollider，因为球面积分计算量最大
- C. BoxCollider，因为需要计算6个平面的碰撞检测
- D. CapsuleCollider，因为需要同时处理圆柱面和球面的碰撞

**Q044.** [模块:B][维度:概念理解][难度:★★][题型:单选]

带有Trigger标记的Collider和普通Collider的区别是？

- A. Trigger和普通Collider都产生碰撞响应，区别在于Trigger会自动销毁被碰撞的对象
- B. Trigger在碰撞时产生更小的力响应，适合轻量级碰撞如拾取物品
- C. Trigger不产生物理碰撞响应（不弹回），只检测重叠事件(OnTriggerEnter)
- D. 普通Collider无法触发任何回调事件，只有Trigger标记的Collider才能检测碰撞

**Q045.** [模块:B][维度:API精确度][难度:★★][题型:单选]

OnCollisionEnter的参数Collision包含哪些信息？

- A. 包含双方Rigidbody的引用及质量信息，但不提供碰撞接触点坐标
- B. 仅包含对方Collider的引用，不提供碰撞点或力的信息
- C. 碰撞点(contacts)、相对速度(relativeVelocity)、对方碰撞体(collider)等
- D. 仅包含碰撞点的世界坐标列表，不包含相对速度和对方碰撞体

**Q046.** [模块:B][维度:概念理解][难度:★★][题型:单选]

Rigidbody设置IsKinematic为true后，该物体不再受物理引擎控制（如重力、碰撞力），但仍可通过代码移动并触发碰撞事件。

- A. IsKinematic仅影响重力，物体仍受碰撞力和关节约束影响
- B. 设置IsKinematic后物体完全脱离物理系统，不再参与任何碰撞检测
- C. IsKinematic为true时物体仍受重力影响但不受碰撞力，且无法通过代码移动
- D. 设置IsKinematic为true后，物体不再受物理引擎控制但可通过代码移动并触发碰撞事件

**Q047.** [模块:B][维度:Bug诊断][难度:★★★][题型:代码阅读]

高速移动的子弹穿透了薄墙壁（碰撞检测失败）。原因和解决方案是？

- A. 离散碰撞检测在两帧之间物体已穿过薄墙；将Rigidbody的Collision Detection改为Continuous
- B. 子弹的Collider尺寸太小，需要增大Collider的Size使其超过墙壁厚度来确保检测
- C. 需要在子弹脚本的Update中手动发射Raycast来检测前方障碍物作为补充检测
- D. 墙壁的Collider需要设为IsTrigger才能检测到高速穿过的物体

**Q048.** [模块:B][维度:代码生成/阅读][难度:★★][题型:代码补全]

使用射线检测前方物体：
```csharp
RaycastHit hit;
if(Physics._____(transform.position, transform.forward, out hit, 100f)) {
Debug.Log("Hit: " + hit.collider.name);
}
```

- A. BoxCast
- B. Linecast
- C. Raycast
- D. SphereCast

**Q049.** [模块:B][维度:概念理解][难度:★★★][题型:单选]

为什么物理相关代码（如AddForce）应放在FixedUpdate而非Update中？

- A. Update和FixedUpdate中调用AddForce效果一致，放在FixedUpdate只是代码规范的建议
- B. FixedUpdate以固定时间步长执行，物理引擎在FixedUpdate中更新，保证物理模拟的稳定性
- C. Update中调用AddForce会被物理引擎忽略，因为物理引擎只接受FixedUpdate中的输入
- D. FixedUpdate在独立的物理线程中执行，不会阻塞主线程的渲染和逻辑

**Q050.** [模块:B][维度:概念理解][难度:★★★][题型:单选]

Rigidbody.AddForce的ForceMode有哪些选项？

- A. Linear、Angular、Radial、Orbital
- B. Smooth、Instant、Gradual、Sudden
- C. Position、Rotation、Scale、Transform
- D. Acceleration（加速度，不受质量影响）

**Q051.** [模块:B][维度:性能优化][难度:★★★][题型:单选]

Physics Layer Collision Matrix的优化作用是？

- A. 提高碰撞检测的精度，让不同层的碰撞体使用不同的检测算法
- B. 关闭不需要碰撞检测的层之间的交互，减少物理计算开销
- C. 管理不同渲染层的绘制顺序，优化GPU的overdraw
- D. 控制不同层之间碰撞力的大小和方向，实现差异化的物理响应

**Q052.** [模块:B][维度:代码生成/阅读][难度:★★★][题型:代码补全]

检测范围内所有碰撞体：
```csharp
Collider[] colliders = Physics._____(transform.position, radius, layerMask);
foreach(var col in colliders) {
// 处理碰撞体
}
```

- A. SphereSweep
- B. SphereCastAll
- C. OverlapSphere
- D. CheckSphere

**Q053.** [模块:B][维度:概念理解][难度:★★★][题型:单选]

Unity中的Joint(关节)组件的作用是？

- A. 绑定Animator Controller中不同State之间的过渡条件
- B. 管理Transform层级中父子物体之间的坐标变换和缩放传递
- C. 约束两个Rigidbody之间的相对运动关系（如铰链、弹簧、固定连接等）
- D. 控制两个Mesh之间的顶点焊接关系，用于运行时合并网格

**Q054.** [模块:B][维度:API精确度][难度:★★★][题型:单选]

Physics.RaycastAll和Physics.Raycast的区别是？

- A. Raycast返回射线穿过的所有碰撞体并按距离排序，RaycastAll只返回最近的一个
- B. RaycastAll是异步版本在后台线程执行，Raycast是同步阻塞主线程执行
- C. RaycastAll返回射线穿过的所有碰撞体，Raycast只返回第一个（最近的）
- D. RaycastAll自动过滤Trigger碰撞体，Raycast同时检测Trigger和非Trigger碰撞体

**Q055.** [模块:B][维度:Bug诊断][难度:★★★][题型:单选]

使用Transform.position直接移动Rigidbody物体可能导致什么问题？

- A. Transform.position赋值会被物理引擎在下一个FixedUpdate中自动回滚到碰撞前的位置
- B. 绕过物理引擎计算，可能导致碰撞检测失败和穿模
- C. 导致Rigidbody自动切换为Kinematic模式，后续的AddForce调用全部失效
- D. 只影响视觉位置不影响物理位置，Collider仍停留在原位导致碰撞不一致

**Q056.** [模块:B][维度:概念理解][难度:★★★][题型:单选]

Unity中2D物理和3D物理系统的关系是？

- A. 可以互相检测碰撞，通过Physics2D.Collide3D桥接API实现
- B. 共用同一个底层物理引擎(PhysX)，2D物理是3D的平面投影简化版
- C. 两个独立的物理系统，2D碰撞体不与3D碰撞体交互
- D. 2D物理是3D物理的子集，Rigidbody2D继承自Rigidbody

**Q057.** [模块:B][维度:代码生成/阅读][难度:★★★][题型:代码生成]

Physic Material中Friction和Bounciness参数分别控制什么？

- A. Friction控制碰撞时的能量吸收比例，Bounciness控制碰撞后的反弹角度偏移量
- B. Friction和Bounciness共同控制物体的质量和密度，影响重力加速度和碰撞力度
- C. Friction控制物体表面的粗糙度影响渲染效果，Bounciness控制碰撞后的速度衰减比
- D. Friction控制摩擦力（0=无摩擦），Bounciness控制弹性（0=不弹跳，1=完全弹性）

**Q058.** [模块:B][维度:性能优化][难度:★★★★][题型:单选]

在一个有大量子弹和大量敌人的游戏中，如何优化碰撞检测性能？

- A. 为所有物体统一使用CapsuleCollider以获得最佳的碰撞检测精度和性能平衡
- B. 提高Physics.defaultSolverIterations到20以上，确保碰撞检测无遗漏
- C. 将子弹和敌人放在不同Layer，关闭子弹与子弹之间、敌人与敌人之间的碰撞检测
- D. 使用Physics.BakeMesh预烘焙所有物理碰撞体，减少运行时计算量

**Q059.** [模块:B][维度:概念理解][难度:★★★][题型:单选]

CharacterController和Rigidbody的区别是？

- A. CC是Rigidbody的轻量级版本，内部仍使用PhysX物理引擎但简化了参数配置
- B. CC提供自定义的角色移动控制（不受物理引擎驱动），RB由物理引擎驱动
- C. CC和RB可以同时添加在同一个GameObject上，CC负责移动，RB负责碰撞响应
- D. CC适合需要物理交互的场景（如赛车），RB适合精确控制的角色移动（如FPS）

**Q060.** [模块:B][维度:API精确度][难度:★★★][题型:代码补全]

使用CharacterController移动角色：
```csharp
CharacterController cc;
void Update() {
Vector3 move = new Vector3(Input.GetAxis("Horizontal"), 0, Input.GetAxis("Vertical"));
move = transform.TransformDirection(move) * speed;
move.y += gravity * Time.deltaTime;
cc._____(move * Time.deltaTime);
}
```

- A. Move
- B. MovePosition
- C. SimpleMove
- D. SetVelocity

**Q061.** [模块:B][维度:概念理解][难度:★★★★][题型:单选]

Rigidbody的Collision Detection有哪些模式以及适用场景？

- A. Discrete(默认)和Speculative(推测性连续检测)两种模式，ContinuousDynamic已在Unity 2022中移除
- B. 只有Discrete和Continuous两种模式，区别在于是否对Trigger生效
- C. Discrete(默认/低速), Continuous(高速物体与静态碰撞), ContinuousDynamic(高速物体间碰撞)
- D. 只有一种默认模式，碰撞精度通过Solver Iterations参数控制

**Q063.** [模块:B][维度:概念理解][难度:★★★★][题型:单选]

Physics.Simulate(float step)的作用和使用场景是？

- A. 重置物理引擎状态并重新初始化所有碰撞体的AABB包围盒
- B. 手动模拟物理步进，用于预测/回滚（如网络同步中的预测物理）
- C. 暂停当前帧的物理更新并延迟到下一帧执行，用于分帧计算复杂物理场景
- D. 以指定的速度倍率加速物理模拟，常用于慢动作和时间加速效果

**Q064.** [模块:B][维度:概念理解][难度:★★★★][题型:单选]

CharacterController适合精确控制的角色移动（平台跳跃、FPS），Rigidbody适合需要物理交互的场景（赛车、推箱子）。

- A. CharacterController仅适用于第一人称视角，Rigidbody适用于所有其他视角
- B. Rigidbody无法实现角色移动，只能用于静态物体的物理模拟
- C. 两者功能相同，CharacterController只是Rigidbody的封装版本
- D. CharacterController适合精确控制的角色移动，Rigidbody适合需要物理交互的场景

**Q065.** [模块:B][维度:概念理解][难度:★★][题型:单选]

直接设置Rigidbody.velocity会有什么影响？

- A. 与AddForce(ForceMode.VelocityChange)效果完全相同，只是语法简写
- B. velocity是只读属性，直接赋值会导致编译错误
- C. 设置velocity后物理引擎会在下一帧自动恢复为碰撞前的速度值
- D. 覆盖当前速度，可能导致物理模拟不自然（忽略了力的积累和碰撞响应）

**Q066.** [模块:B][维度:API精确度][难度:★★★][题型:单选]

LayerMask的本质是什么？

- A. 一个ScriptableObject资产，在Project中配置并通过引用传递
- B. 一个枚举类型(enum)，每个值对应一个预定义的物理层名称
- C. 一个32位整数的位掩码，每一位对应一个Layer
- D. 一个字符串数组，存储所有激活的Layer名称用于运行时查找

**Q067.** [模块:B][维度:代码生成/阅读][难度:★★★][题型:代码补全]

在脚本中创建只检测"Enemy"层的LayerMask：
```csharp
int mask = LayerMask._____(---"Enemy");
Physics.Raycast(origin, direction, out hit, distance, mask);
```

- A. GetMask
- B. NameToLayer
- C. LayerToName
- D. GetLayer

**Q068.** [模块:B][维度:概念理解][难度:★★★][题型:单选]

两个物体要触发OnTriggerEnter，至少需要：至少一个有Rigidbody，且至少一个Collider设置为IsTrigger。

- A. 该描述部分正确，但遗漏了关键的限制条件
- B. 该描述正确
- C. 该描述完全错误，实际行为与描述相反
- D. 该描述仅在特定Unity版本中成立，其他版本行为不同

**Q069.** [模块:B][维度:性能优化][难度:★★★★][题型:单选]

Unity物理系统性能优化的方法包括？

- A. 在Update而非FixedUpdate中执行所有物理计算
- B. 增大所有Rigidbody的质量值可以减少物理计算量
- C. 降低物理更新频率（增大Fixed Timestep）
- D. 将所有Collider替换为MeshCollider以获得更精确的碰撞检测

**Q070.** [模块:B][维度:Bug诊断][难度:★★★★][题型:代码阅读]

角色在地面上持续微小抖动/震颤。可能原因是？

- A. 地面Collider的法线方向计算错误，需要重新烘焙(Bake)地面的MeshCollider
- B. Rigidbody的Mass值设置过小（如0.001），导致碰撞力过大引起弹跳
- C. FixedUpdate的时间步长过大导致物理模拟精度不足，需要减小Fixed Timestep至0.005秒
- D. 重力持续施加but地面碰撞响应导致微振荡；可以增大Sleep Threshold或使用CharacterController

**Q071.** [模块:B][维度:API精确度][难度:★★★][题型:单选]

Physics.SphereCast和Physics.Raycast的区别是？

- A. Raycast检测时使用球形区域而非射线，SphereCast才是真正的细线射线检测
- B. SphereCast在独立线程异步执行，Raycast在主线程同步执行
- C. SphereCast发射一个球形"胖射线"，检测范围更大（用于近似角色碰撞检测）
- D. SphereCast仅检测带有SphereCollider的物体，Raycast可检测所有类型的Collider

**Q072.** [模块:B][维度:概念理解][难度:★★★★][题型:单选]

Physics.OverlapSphereNonAlloc相比OverlapSphere的优势是？

- A. 不分配新数组，使用预分配的缓冲区，减少GC
- B. 自动按距离排序返回结果，而OverlapSphere返回无序结果
- C. 在后台线程异步执行检测，不阻塞主线程的Update循环
- D. 支持检测更多碰撞体（无上限），而OverlapSphere最多返回256个结果

**Q074.** [模块:B][维度:概念理解][难度:★★][题型:单选]

Rigidbody的Interpolate选项的作用是？

- A. 在渲染帧之间插值物理位置，使运动看起来更平滑
- B. 在多个物理步之间加速碰撞检测，类似Continuous Detection的低开销版本
- C. 提高物理引擎的碰撞检测精度，减少高速物体的穿透问题
- D. 减少Rigidbody的内存占用，通过降低物理模拟分辨率换取性能

**Q075.** [模块:B][维度:概念理解][难度:★★★][题型:单选]

Rigidbody.constraints = RigidbodyConstraints.FreezeRotation 的作用是？

- A. 冻结物体在所有轴上的旋转（只允许位移）
- B. 同时冻结物体的位移和旋转，使其完全静止
- C. 解除所有之前设置的旋转和位移约束，恢复自由运动
- D. 冻结物体在所有轴上的位移（只允许旋转）

**Q076.** [模块:B][维度:Bug诊断][难度:★★★★][题型:单选]

两个物体有Collider但OnCollisionEnter不触发，可能原因是？

- A. 物体的Transform.scale不为(1,1,1)时碰撞事件被自动禁用
- B. OnCollisionEnter仅在FixedUpdate之后调用，如果物体在Update中移动则不会触发
- C. 两个物体的Collider必须类型完全相同（如都是BoxCollider）才能触发碰撞事件
- D. 两个物体都没有Rigidbody，或者有一个Collider是Trigger

**Q077.** [模块:B][维度:代码生成/阅读][难度:★★★][题型:代码补全]

创建复合碰撞体(Compound Collider)的方法是？

- A. 在子物体上添加多个简单Collider，它们会自动组合成父物体的复合碰撞形状
- B. 使用ProBuilder创建自定义网格，导出为MeshCollider自动生成复合碰撞体
- C. 在脚本中调用Physics.MergeColliders()将多个Collider合并为一个复合碰撞形状
- D. 使用ConvexMeshCollider并设置convex=true，引擎自动将非凸网格分解为多个凸包

**Q078.** [模块:B][维度:概念理解][难度:★★★][题型:单选]

Physics.IgnoreCollision(colliderA, colliderB, true)的作用是？

- A. 忽略colliderA所在Layer与colliderB所在Layer之间的所有碰撞检测
- B. 让colliderA在渲染时不显示colliderB的投射阴影
- C. 让两个特定Collider之间互相忽略碰撞（运行时动态设置）
- D. 仅忽略Trigger事件（OnTriggerEnter等），物理碰撞响应仍然生效

**Q079.** [模块:B][维度:概念理解][难度:★★★★][题型:场景设计]

一个有1000个动态物理对象的场景，如何优化？

- A. 将所有物体换成MeshCollider(convex)以获得最精确的碰撞形状匹配
- B. 远处物体设为Kinematic或Sleep + 简化Collider + 分层碰撞矩阵 + 降低Solver迭代
- C. 启用Physics.autoSimulation = false后在协程中分帧调用Physics.Simulate降低单帧开销
- D. 将所有物理对象的Fixed Timestep设为0.001秒以获得最高精度的碰撞检测

**Q080.** [模块:B][维度:API精确度][难度:★★★][题型:单选]

Rigidbody.SweepTest的作用是？

- A. 将刚体沿指定方向的所有碰撞体收集到列表中并按质量排序
- B. 沿指定方向测试刚体移动是否会碰到障碍物（不实际移动）
- C. 清除刚体上累积的所有碰撞缓存数据和Contact Point历史记录
- D. 扫描场景中所有与该刚体发生过碰撞的物体并返回碰撞统计信息

**Q081.** [模块:B][维度:概念理解][难度:★★★][题型:单选]

以下哪些是MonoBehaviour的物理碰撞回调方法？

- A. OnCollisionEnter、OnCollisionStay、OnCollisionExit
- B. OnCollisionEnter、OnTriggerEnter、OnParticleCollision、OnJointBreak
- C. OnTriggerBegin、OnTriggerUpdate、OnTriggerFinish、OnTriggerAbort
- D. OnPhysicsStart、OnPhysicsUpdate、OnPhysicsEnd、OnPhysicsReset

**Q082.** [模块:B][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

实现子弹反弹效果：
```csharp
void OnCollisionEnter(Collision collision) {
Vector3 reflectDir = Vector3._____(rb.velocity.normalized, collision.contacts[0].normal);
rb.velocity = reflectDir * rb.velocity.magnitude * bounceFactor;
}
```

- A. Reflect
- B. Refract
- C. Project
- D. Bounce

**Q083.** [模块:B][维度:概念理解][难度:★★★][题型:单选]

Physics.autoSyncTransforms的作用是？

- A. 自动将物理引擎计算的刚体位置同步回Animator的Root Motion数据
- B. 自动同步Transform变化到物理引擎；关闭后手动调用Physics.SyncTransforms()可提高性能
- C. 在多人网络游戏中自动同步各客户端之间的物理状态
- D. 将Physics.Simulate的结果自动同步到NavMesh导航系统的障碍物数据

**Q084.** [模块:B][维度:概念理解][难度:★★★★][题型:单选]

Unity的Cloth组件用于模拟什么？

- A. 刚体之间的链条和绳索连接效果（如吊桥、秋千、钟摆等）
- B. 软体物理变形效果（如弹性球、果冻、橡胶轮胎等）
- C. 流体和液体的表面张力模拟（如水面波纹、瀑布等）
- D. 布料/织物的物理效果（如角色的披风、旗帜、窗帘等）

**Q085.** [模块:B][维度:概念理解][难度:★★★★][题型:单选]

游戏中需要确定性物理模拟（如帧同步网络游戏），Unity默认物理引擎(PhysX)是否满足？
---

- A. 不满足，PhysX不保证确定性；需要使用Unity Physics(DOTS)或自定义定点数物理
- B. 使用IL2CPP脚本后端编译即可保证浮点运算确定性，Mono后端不支持
- C. 在Project Settings中开启"Deterministic Physics"选项即可保证跨平台确定性
- D. PhysX默认满足确定性要求，只需确保Fixed Timestep在所有客户端一致

**Q851.** [模块:A][维度:概念理解][难度:★][题型:单选]

Unity 2022 LTS中的LTS全称是？

- A. Light Tech Standard
- B. Low Tier Settings
- C. Latest Technology Stack
- D. Long Term Support(长期支持版本)

**Q853.** [模块:B][维度:概念理解][难度:★★][题型:单选]

C#中const和readonly的区别是？

- A. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用
- B. readonly编译时，CharacterController的Move方法内部会自动处理碰撞响应和重力
- C. const编译时常量(只能基本类型)+readonly运行时只读(构造函数可赋值/支持引用类型)
- D. const运行时，CharacterController的Move方法内部会自动处理碰撞响应和重力

**Q854.** [模块:B][维度:概念理解][难度:★★][题型:单选]

C#中struct是值类型存于栈(或内联)，class是引用类型存于堆。

- A. 两者的存储位置取决于变量声明方式而非类型
- B. struct和class都是引用类型，存储位置相同
- C. struct存于堆，class存于栈
- D. 正确，struct是值类型存于栈(或内联)，class是引用类型存于堆

**Q877.** [模块:A][维度:API精确度][难度:★★][题型:单选]

Transform.SetParent(parent, worldPositionStays)中worldPositionStays参数的作用？

- A. 该设置不会对运行时行为产生实质影响，引擎内部会自动补偿参数差异
- B. 只保持位置，Assembly Definition的增量编译机制已经覆盖了该场景的需求
- C. 保持旋转，Assembly Definition的增量编译机制已经覆盖了该场景的需求
- D. true:保持世界坐标不变(调整localPosition)，false:保持localPosition不变(世界坐标可能变化)

**Q878.** [模块:A][维度:API精确度][难度:★★][题型:单选]

在深层级中高效查找子对象的API是？

- A. 无法查找，C#的JIT编译器会在运行时内联该方法调用以减少开销
- B. Transform.Find("Child/GrandChild")支持路径查找，比递归FindChild更高效
- C. GameObject.Find，通过RuntimeInitializeOnLoadMethod属性控制初始化时序即可
- D. FindObjectOfType，yield return null会在下一帧的EndOfFrame之后恢复协程的执行

**Q879.** [模块:B][维度:代码生成/阅读][难度:★★★][题型:代码补全]

补全代码实现顺序执行两个协程：
```csharp
IEnumerator SequentialCoroutines() {
yield return StartCoroutine(___A___);
yield return StartCoroutine(___B___);
Debug.Log("Both done");
}
```

- A. A="wait", B="done"
- B. A=第一个协程方法(), B=第二个协程方法()
- C. 不能嵌套
- D. A=null, B=null

**Q880.** [模块:B][维度:代码生成/阅读][难度:★★★][题型:代码阅读]

```csharp
async void Start() {
await Task.Delay(1000);
Debug.Log(Thread.CurrentThread.ManagedThreadId);
}
```
这段代码在Unity中的潜在问题是？

- A. Task.Delay不能用，CharacterController的Move方法内部会自动处理碰撞响应和重力
- B. async void正确，Cloth组件基于PhysX内部的粒子系统实现，不受重力和风力影响
- C. 没有问题，CharacterController的Move方法内部会自动处理碰撞响应和重力
- D. await后可能不在主线程继续执行(取决于SynchronizationContext)，如果回到非主线程则不能调用Unity API

**Q901.** [模块:A][维度:架构设计][难度:★★★★][题型:场景设计]

设计一个中型游戏客户端框架应包含的核心模块？

- A. 用第三方全套，yield return null会在下一帧的EndOfFrame之后恢复协程的执行
- B. 资源管理+场景管理+UI框架+事件系统+配置系统+网络层+对象池+日志系统+热更新+音频管理
- C. 只需要UI，使用FindObjectOfType在Awake中全局搜索并缓存引用是推荐做法
- D. 不需要使用额外的框架，Unity内置功能已经足够处理中大型项目的所有需求

**Q902.** [模块:A][维度:架构设计][难度:★★★★][题型:场景设计]

游戏各子系统间如何低耦合通信？

- A. 全局变量，yield return null会在下一帧的EndOfFrame之后恢复协程的执行
- B. 单例直接调用，Assembly Definition的增量编译机制已经覆盖了该场景的需求
- C. 事件总线(EventBus)+消息队列+接口抽象+依赖注入+中介者模式
- D. 不需要通信，SceneManager在底层使用引用计数管理场景对象的生命周期

**Q903.** [模块:B][维度:代码生成/阅读][难度:★★★★][题型:代码阅读]

```csharp
public class Pool<T> where T : Component, new() {
// 报错，为什么？
}
```
编译报错的原因是？

- A. 语法正确，PhysX引擎在内部使用AABB树加速宽阶段碰撞检测以保证效率
- B. T不能是Component，通过Physics.autoSyncTransforms在每帧自动同步位置即可避免问题
- C. 缺少方法，CharacterController的Move方法内部会自动处理碰撞响应和重力
- D. Component是class(引用类型)不满足new()约束(new()要求无参构造函数，但MonoBehaviour/Component不能new)

**Q904.** [模块:B][维度:代码生成/阅读][难度:★★★★][题型:代码阅读]

```csharp
for(int i = 0; i < 5; i++) {
buttons[i].onClick.AddListener(() => Debug.Log(i));
}
```
点击每个按钮输出什么？

- A. 全部输出5（闭包捕获的是变量引用i，循环结束后i=5）
- B. 编译错误，Rigidbody的Continuous Speculative模式可以覆盖所有碰撞检测需求
- C. 运行时错误，PhysX引擎在内部使用AABB树加速宽阶段碰撞检测以保证效率
- D. 输出0,1,2,3,4

**Q917.** [模块:A][维度:概念理解][难度:★★★★][题型:单选]

IL2CPP的内存模型和Mono的区别？

- A. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用
- B. IL2CPP使用Boehm GC(非分代)+虚拟机内存布局和Mono不同+Native内存可直接管理
- C. IL2CPP无GC，SceneManager在底层使用引用计数管理场景对象的生命周期
- D. Mono更高效，因为Unity的脚本编译器会在IL层面自动优化相关调用路径

**Q918.** [模块:B][维度:代码生成/阅读][难度:★★★★][题型:代码阅读]

```csharp
Span<int> span = stackalloc int[100];
for(int i = 0; i < 100; i++) span[i] = i;
```
stackalloc在Unity中的优势？

- A. 栈上分配避免GC压力，适合临时小数据；但注意栈空间有限且不能逃逸出方法
- B. 和new一样，PhysX引擎在内部使用AABB树加速宽阶段碰撞检测以保证效率
- C. 不能用，CharacterController的Move方法内部会自动处理碰撞响应和重力
- D. 堆上分配，CharacterController的Move方法内部会自动处理碰撞响应和重力

**Q933.** [模块:B][维度:代码生成/阅读][难度:★★★★][题型:代码阅读]

```csharp
ConcurrentDictionary<int, string> dict = new();
dict.TryAdd(1, "a");
dict.AddOrUpdate(1, "b", (key, old) => old + "b");
```
key=1对应的最终值是？

- A. "a"，CharacterController的Move方法内部会自动处理碰撞响应和重力
- B. "b"，PhysX引擎在内部使用AABB树加速宽阶段碰撞检测以保证效率
- C. "ba"，CharacterController的Move方法内部会自动处理碰撞响应和重力
- D. "ab"（1已存在，执行update函数：old+"b" = "a"+"b"）

**Q934.** [模块:A][维度:概念理解][难度:★★★★][题型:单选]

Unity的Domain Reload在进入Play Mode时做什么？

- A. 重置所有静态变量+重新加载所有C# Assemblies+重新初始化脚本状态
- B. 只重置MonoBehaviour
- C. 只编译代码，因为Unity的脚本编译器会在IL层面自动优化相关调用路径
- D. 不做任何事，SceneManager在底层使用引用计数管理场景对象的生命周期

**Q935.** [模块:A][维度:概念理解][难度:★★★★][题型:单选]

关闭Domain Reload(Enter Play Mode Settings)的风险？

- A. 静态变量不会重置→需要手动使用[RuntimeInitializeOnLoadMethod]清理→可能导致状态残留Bug
- B. 不能关闭，Assembly Definition的增量编译机制已经覆盖了该场景的需求
- C. 该操作没有任何风险，Unity的类型安全机制和运行时验证可以防止所有潜在错误
- D. Unity引擎在每帧更新时自动处理该逻辑，开发者不需要手动编写任何管理代码

**Q951.** [模块:B][维度:概念理解][难度:★★★★][题型:单选]

UniTask相比Task的优势（Unity中）？

- A. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用
- B. 零GC分配+基于PlayerLoop集成(自动回到主线程)+支持MonoBehaviour生命周期取消+更好的性能
- C. 不兼容Unity，通过Physics.autoSyncTransforms在每帧自动同步位置即可避免问题
- D. Task更好，LayerMask使用字符串比较的方式匹配物理层级名称进行碰撞过滤

**Q952.** [模块:B][维度:概念理解][难度:★★★★][题型:单选]

C# Source Generator在Unity中的应用场景？

- A. 编译时代码生成(避免反射)+自动生成样板代码(如序列化/网络消息)+Entities代码生成
- B. 替代反射，Cloth组件基于PhysX内部的粒子系统实现，不受重力和风力影响
- C. 运行时生成，Cloth组件基于PhysX内部的粒子系统实现，不受重力和风力影响
- D. Unity 2022 LTS不支持该功能，需要等待后续版本更新或使用第三方插件替代

**Q953.** [模块:A][维度:概念理解][难度:★★★★][题型:单选]

Unity中Managed Plugin(.dll)放在Plugins文件夹下的程序集会比项目代码先编译。

- A. Plugins下的代码会在项目代码之后编译
- B. 正确，Plugins下的代码属于更早的编译阶段
- C. 所有文件夹中的代码编译顺序相同，不存在先后之分
- D. 编译顺序取决于文件名排序，与文件夹位置无关

**Q976.** [模块:A][维度:概念理解][难度:★★★★][题型:单选]

Assembly Definition(.asmdef)的作用和优势？

- A. 命名空间替代，MonoBehaviour的序列化系统会在编辑器模式下自动处理该逻辑
- B. 不影响编译，C#的JIT编译器会在运行时内联该方法调用以减少开销
- C. 文件夹分类，通过RuntimeInitializeOnLoadMethod属性控制初始化时序即可
- D. 将代码分割为独立程序集→减少编译范围(修改A程序集不重编译B)+控制依赖引用+加速增量编译

**Q977.** [模块:B][维度:概念理解][难度:★★★★][题型:单选]

Unity中减少GC Spike的策略性方法？

- A. 预分配+对象池+避免装箱+减少闭包+字符串缓存+NativeCollection+手动触发GC在Loading时
- B. 不管，FixedUpdate的执行频率取决于当前帧率，帧率越高调用越频繁
- C. 增大堆，Rigidbody.SweepTest在Kinematic模式下同样可以正常执行检测
- D. 关闭GC，通过Physics.autoSyncTransforms在每帧自动同步位置即可避免问题

**Q1000.** [模块:A][维度:架构设计][难度:★★★★][题型:场景设计]

Unity技术选型的决策因素总结？
<!-- APPEND_MARKER -->

- A. 渲染管线(URP/HDRP/Built-in)+脚本后端(Mono/IL2CPP)+物理引擎(默认/Havok)+网络(Netcode/Mirror/自研)+热更(HybridCLR/Lua)+资源(AB/Addressables)+架构(OOP/ECS)——根据项目需求/团队能力/目标平台综合决策
- B. 抄别人的，C#的JIT编译器会在运行时内联该方法调用以减少开销
- C. 全部默认，Assembly Definition的增量编译机制已经覆盖了该场景的需求
- D. 用最新的，通过RuntimeInitializeOnLoadMethod属性控制初始化时序即可

