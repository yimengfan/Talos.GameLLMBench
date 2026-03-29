# Unity3D 2022 LTS 基础能力问答题库（1000题）
# 涵盖30大知识模块 × 6大能力维度
# 版本: v5.0（迷惑选项增强版）
# 元数据格式: [模块:X][维度:Y][难度:Z][题型:W]

---

## 模块A：核心架构（40题）

**Q001.** [模块:A][维度:API精确度][难度:★][题型:单选]
[考点: MonoBehaviour生命周期]

MonoBehaviour的Awake()和Start()的执行顺序是？

- A. Awake在Start之前执行，Awake在对象实例化时调用，Start在第一帧Update之前调用
- B. 两者都在首帧Update之前调用，但执行顺序取决于Inspector中组件的排列顺序
- C. Awake和Start都在实例化时立即调用，但Awake仅在脚本enabled为true时才执行
- D. Start在Awake之前执行，Start在组件首次激活时调用，Awake在第一帧Update之前调用

**Q002.** [模块:A][维度:API精确度][难度:★][题型:单选]
[考点: Update与FixedUpdate]

Update()和FixedUpdate()的区别是？

- A. Update和FixedUpdate的调用频率相同，但FixedUpdate不受Time.timeScale影响
- B. Update每帧调用一次，FixedUpdate按固定时间间隔调用（默认0.02秒）
- C. Update按固定时间间隔调用（默认0.02秒），FixedUpdate每帧调用一次
- D. FixedUpdate在每帧渲染后调用，Update在物理模拟前调用，两者调用频率可能不同

**Q003.** [模块:A][维度:概念理解][难度:★][题型:单选]
[考点: GameObject与Component关系]

Unity中GameObject和Component的关系是？

- A. GameObject继承自Component，所有引擎对象都是Component的派生类
- B. GameObject和Component都继承自MonoBehaviour，是平行关系
- C. GameObject是实体容器，Component是附加在GameObject上的功能模块
- D. Component是实体容器，GameObject是附加在Component上的功能模块

**Q004.** [模块:A][维度:API精确度][难度:★★][题型:单选]
[考点: GetComponent性能]

以下获取组件的方式，哪种性能最差且应避免在Update中使用？

- A. GetComponent<T>()在每帧调用时（未缓存对象引用情况下）
- B. GameObject.Find("Name").GetComponent<T>()
- C. transform.GetChild(0).GetComponent<T>()在子物体数量较多时
- D. GetComponentInChildren<T>(true)搜索所有子级包含inactive对象

**Q005.** [模块:A][维度:概念理解][难度:★★][题型:单选]
[考点: Transform层级关系]

Transform.SetParent(newParent, worldPositionStays)中第二个参数为true时表示？

- A. 保持物体相对于新Parent的本地坐标不变
- B. 保持物体的世界坐标位置不变
- C. 自动等比缩放物体使其保持在新Parent的局部坐标系原点
- D. 保持物体的世界旋转不变但允许位置跟随Parent变化

**Q006.** [模块:A][维度:API精确度][难度:★★][题型:单选]
[考点: 不存在的API]

以下哪个API在Unity 2022 LTS中不存在？

- A. Physics.OverlapSphereNonAlloc()
- B. Application.targetFrameRate
- C. Renderer.SetMaterialProperty()
- D. Transform.SetPositionAndRotation()

**Q007.** [模块:A][维度:概念理解][难度:★★][题型:单选]
[考点: 对象生命周期]

MonoBehaviour生命周期中以下方法按正确的调用顺序排列？（多选正确的）

- A. Awake → OnEnable → Start → FixedUpdate → Update → LateUpdate
- B. Start → Awake → OnEnable → Update → LateUpdate
- C. OnEnable → Awake → Start → Update → FixedUpdate → LateUpdate
- D. Awake → Start → OnEnable → FixedUpdate → Update → LateUpdate

**Q008.** [模块:A][维度:代码生成/阅读][难度:★★][题型:代码补全]
[考点: 单例MonoBehaviour]

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
[考点: LateUpdate用途]

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
[考点: SceneManager加载场景]

SceneManager.LoadScene和SceneManager.LoadSceneAsync的区别是？

- A. LoadScene同步加载（会阻塞主线程导致卡顿），LoadSceneAsync异步加载（不阻塞）
- B. LoadScene用于Additive模式加载场景，LoadSceneAsync用于Single模式替换场景
- C. LoadScene异步加载（不阻塞主线程），LoadSceneAsync同步加载（会导致卡顿）
- D. LoadScene只能加载Build Settings中的场景，LoadSceneAsync可以加载Resources中的任意场景

**Q011.** [模块:A][维度:API精确度][难度:★★][题型:单选]
[考点: Destroy延迟]

Destroy(gameObject, 5f)的行为是？

- A. 5秒后销毁该GameObject
- B. 在接下来的5帧内逐步禁用该GameObject上的组件后再销毁
- C. 将该GameObject设为Inactive状态5秒后再调用DestroyImmediate彻底移除
- D. 立即标记销毁并在当前帧结束前移除该GameObject及其所有子物体

**Q012.** [模块:A][维度:概念理解][难度:★★★][题型:单选]
[考点: Prefab实例化]

Instantiate()返回的对象和原Prefab的关系是？

- A. 返回一个空的GameObject，需要手动从Prefab复制组件和属性
- B. 返回的是Prefab的一个完整克隆（实例），修改实例不影响Prefab
- C. 返回的是Prefab的浅拷贝，共享材质和Mesh数据，修改材质会影响所有同Prefab实例
- D. 返回的是对原Prefab Asset的引用，修改返回对象等同于修改Prefab本身

**Q013.** [模块:A][维度:API精确度][难度:★★][题型:单选]
[考点: DestroyImmediate]

DestroyImmediate和Destroy的区别：DestroyImmediate立即销毁对象，Destroy在当前帧结束时销毁。


- A. 两者的区别仅在于DestroyImmediate会同时销毁对象的子对象，Destroy不会
- B. DestroyImmediate在下一帧销毁，Destroy在当前帧结束时销毁
- C. 两者功能完全相同，DestroyImmediate只是Destroy的别名方法
- D. DestroyImmediate立即销毁对象，Destroy在当前帧结束时销毁

**Q014.** [模块:A][维度:概念理解][难度:★★★][题型:单选]
[考点: Tag与Layer]

Tag和Layer的区别和使用场景是？

- A. Tag用于标识分类（如"Player","Enemy"），Layer用于物理碰撞过滤和Camera渲染过滤
- B. Layer用于标识对象类型，最多支持8个自定义Layer；Tag仅用于Sorting Layer渲染排序
- C. Tag和Layer都可用于物理碰撞过滤，区别在于Tag是字符串标识而Layer是基于位掩码的整数
- D. Tag用于物理碰撞过滤和Camera Culling Mask过滤，Layer用于标识分类（如"Player","Enemy"）

**Q015.** [模块:A][维度:代码生成/阅读][难度:★★★][题型:代码补全]
[考点: 协程基本用法]

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
[考点: yield return类型]

以下哪些可以作为协程中yield return的参数？
- A. WaitForEndOfFrame只能在OnGUI中有效，在协程中会被忽略
- B. 协程中只能使用WaitForSeconds，其他参数需要用Task替代
- C. null（等待下一帧）
- D. yield return null会导致协程立即终止，不能用于等待下一帧

**Q017.** [模块:A][维度:Bug诊断][难度:★★★][题型:代码阅读]
[考点: 空引用诊断]

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
[考点: OnEnable/OnDisable]

OnEnable()和OnDisable()的调用时机是？

- A. OnEnable仅在Awake之后调用一次，OnDisable仅在OnDestroy之前调用一次
- B. OnEnable在SetActive(true)之后的下一帧调用，OnDisable在SetActive(false)的下一帧调用
- C. OnEnable在每帧Update之前检查脚本状态后调用，OnDisable在LateUpdate之后调用
- D. OnEnable在脚本启用时调用，OnDisable在脚本禁用或物体销毁前调用

**Q019.** [模块:A][维度:性能优化][难度:★★★][题型:单选]
[考点: FindObjectOfType代替方案]

为什么应该避免在Update中使用FindObjectOfType？

- A. 它只能查找继承自MonoBehaviour的组件，无法查找原生Component如Transform
- B. 它每次调用都要遍历所有活动对象，性能开销大
- C. 它返回的对象类型不安全，多线程环境下可能产生InvalidCastException
- D. 它已在Unity 2022中被标记为Obsolete，编译时会产生警告导致CI构建失败

**Q020.** [模块:A][维度:概念理解][难度:★★★][题型:单选]
[考点: ExecutionOrder脚本执行顺序]

如何控制两个MonoBehaviour脚本的执行顺序？

- A. 在Edit → Preferences中设置全局脚本优先级，或通过[ExecuteAlways]属性控制
- B. 通过在脚本中重写ExecutionPriority属性来设置执行优先级，值越大越先执行
- C. 在Project Settings → Script Execution Order中设置，或使用[DefaultExecutionOrder]属性
- D. 在Hierarchy窗口中调整GameObject的排列顺序来控制其上脚本的执行顺序

**Q021.** [模块:A][维度:API精确度][难度:★★★][题型:单选]
[考点: Application路径]

Application.streamingAssetsPath和Application.persistentDataPath的区别是？

- A. streamingAssetsPath是可读写的持久化目录，persistentDataPath是只读的打包资源目录
- B. streamingAssetsPath是只读的资源目录（打包时包含），persistentDataPath是可读写的持久化目录
- C. streamingAssetsPath和persistentDataPath都指向Application.dataPath的子目录，区别在于压缩方式
- D. streamingAssetsPath在所有平台上都可读写，persistentDataPath只在PC/Mac平台可用

**Q022.** [模块:A][维度:代码生成/阅读][难度:★★★][题型:代码生成]
[考点: 消息传递SendMessage]

以下代码使用SendMessage，有什么缺点？
```csharp
gameObject.SendMessage("OnDamage", 10f);
```

- A. SendMessage会广播到场景中所有激活的GameObject，产生大量不必要的方法查找开销
- B. SendMessage仅支持无参方法调用，传递10f参数会导致运行时ArgumentException
- C. 使用字符串标识方法名，无编译时检查，性能差，推荐使用接口或事件系统
- D. SendMessage性能优于直接方法调用，但无法传递值类型参数（仅支持引用类型）

**Q023.** [模块:A][维度:概念理解][难度:★★★][题型:单选]
[考点: Static Batching vs Dynamic Batching]

Static Batching和Dynamic Batching的区别是？

- A. Static Batching在运行时动态合并网格，Dynamic Batching在构建时预合并网格以提高效率
- B. Static Batching处理不透明物体的合批渲染，Dynamic Batching处理半透明物体的合批渲染
- C. Static Batching针对静止不动的物体（需标记Static），Dynamic Batching针对小面数的移动物体（自动合批）
- D. Static Batching针对小面数移动物体（自动合批），Dynamic Batching针对静止物体（需标记Static）

**Q024.** [模块:A][维度:性能优化][难度:★★★★][题型:单选]
[考点: 字符串拼接GC]

在Update中使用字符串拼接 string s = "HP:" + health; 的问题是？

- A. 每帧产生GC分配（string是引用类型，拼接创建新对象），应使用StringBuilder或TextMeshPro.SetText
- B. string拼接仅在IL2CPP构建中才会产生GC问题，Mono后端下编译器会自动优化为栈分配
- C. string拼接在Update中与StringBuilder性能一致，JIT编译器会自动优化为StringBuilder操作
- D. health为数值类型不能与string直接拼接，需要显式调用Convert.ToString()否则编译错误

**Q025.** [模块:A][维度:概念理解][难度:★★★★][题型:单选]
[考点: UnityEvent vs C# Event]

UnityEvent和C# event的区别是？

- A. UnityEvent可在Inspector中编辑绑定，C# event只能代码绑定；UnityEvent有序列化开销
- B. UnityEvent和C# event都支持Inspector编辑绑定，但C# event额外支持多线程安全调用
- C. C# event可以在Inspector中编辑绑定且性能更优，UnityEvent仅支持代码中动态绑定
- D. UnityEvent在IL2CPP构建时会被自动转换为C# delegate，运行时行为完全一致

**Q026.** [模块:A][维度:概念理解][难度:★★★★][题型:单选]
[考点: Managed vs Native Memory]

Unity中Managed Memory和Native Memory的区别是？

- A. Managed是Unity引擎C++层管理的内存（包含纹理和Mesh），Native是C# GC管理的脚本内存
- B. Managed和Native都由GC管理，区别在于Managed使用Incremental GC，Native使用Mark-and-Sweep GC
- C. Managed内存用于存储纹理和Mesh数据由开发者手动释放，Native内存用于C#对象由GC自动管理
- D. Managed是C# GC管理的堆内存，Native是Unity引擎C++层管理的内存（纹理、Mesh等）

**Q027.** [模块:A][维度:概念理解][难度:★★★★][题型:单选]
[考点: Domain Reload]

Unity编辑器中关闭Domain Reload以加速进入Play Mode后需要注意什么？

- A. ScriptableObject的数据会被清除，需要通过EditorPrefs在退出Play Mode时手动保存
- B. 静态变量不会在进入Play Mode时重置，需手动初始化或使用[RuntimeInitializeOnLoadMethod]
- C. MonoBehaviour实例会在进入Play Mode时自动调用Reset方法重置所有序列化字段
- D. 协程的执行状态不会被保留，所有运行中的协程在进入Play Mode时需要手动重新启动

**Q028.** [模块:A][维度:Bug诊断][难度:★★★★][题型:代码阅读]
[考点: ExecutionOrder执行顺序风险]

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
[考点: Assembly Definition文件]

Assembly Definition(.asmdef)文件的作用是？

- A. 将C#代码编译为本地汇编指令（类似Burst Compiler），提升运行时性能
- B. 定义平台特定的编译指令和宏定义，控制不同平台的条件编译分支
- C. 配置项目的程序集签名和版本号，用于NuGet包的发布和依赖管理
- D. 将代码分成独立程序集，加速增量编译（只重编变化的程序集）

**Q030.** [模块:A][维度:概念理解][难度:★★★][题型:单选]
[考点: Package Manager]

Unity Package Manager(UPM)的作用是？

- A. 管理项目的构建配置和输出平台，包括Android/iOS/WebGL的打包选项
- B. 管理Unity场景中的资源引用和依赖关系，自动检测并解决场景间的引用冲突
- C. 管理Unity官方包和第三方包的安装、更新和版本控制
- D. 管理Unity编辑器插件的安装和激活，支持编辑器扩展的热加载和卸载

**Q031.** [模块:A][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: 游戏启动流程设计]

设计一个Unity游戏的合理启动流程顺序是？

- A. 框架初始化→配置加载→资源预热→登录/更新检查→进入主界面
- B. 登录验证→全量资源加载→配置解析→主界面渲染→框架异步初始化
- C. 主界面立即渲染→异步框架初始化→按需配置加载→延迟登录→资源流式加载
- D. 资源预热→框架初始化→主界面渲染→后台异步配置加载→延迟登录验证

**Q032.** [模块:A][维度:架构设计][难度:★★★★][题型:场景设计]
[考点: 大型项目代码架构]

大型Unity项目推荐的代码架构层次是？

- A. 表现层(UI/特效)→业务层(具体功能)→服务层(业务通用)→框架层(底层通用)
- B. 按Unity概念划分：MonoBehaviour层→ScriptableObject层→纯C#层→Editor层
- C. 框架层(底层通用)→服务层(业务通用)→业务层(具体功能)→表现层(UI/特效)
- D. 按功能类型平铺：Manager层(所有管理器)→Util层(工具类)→Data层(数据类)→UI层(界面)

**Q033.** [模块:A][维度:概念理解][难度:★★★★][题型:单选]
[考点: 协程vs异步vs多线程]

Unity中协程、async/await和Thread的区别是？

- A. 三者都在主线程执行，区别在于yield/await/Join的语法差异和回调调度时机不同
- B. 协程在独立的Unity协程线程执行且可以安全访问Unity API，async在主线程执行，Thread在后台线程
- C. 协程和async在主线程执行（不能CPU密集计算），Thread是真正多线程（但不能直接访问Unity API）
- D. async/await在Unity中默认创建新线程执行，协程本质上基于线程池的Task实现

**Q034.** [模块:A][维度:概念理解][难度:★★★★][题型:单选]
[考点: Unity 2022 LTS特性]

Unity 2022 LTS的新特性/改进包括？
- A. 原生支持Vulkan 1.3和DirectX 12 Ultimate
- B. 全新的物理引擎替代PhysX，性能提升200%
- C. 内置AI行为树系统和视觉脚本编辑器
- D. 改进的UI Toolkit

**Q035.** [模块:A][维度:概念理解][难度:★★★][题型:单选]
[考点: GC.Collect使用]

在Unity中可以手动调用System.GC.Collect()。推荐在加载界面等不敏感时机调用以减少游玩时的GC Spike。


- A. 该方法仅适用于Mono运行时，在IL2CPP下调用会直接崩溃
- B. 可以手动调用，推荐在加载界面等不敏感时机调用以减少游玩时的GC Spike
- C. 仅在游戏启动时由Unity自动调用，开发者不应手动调用会导致内存泄漏
- D. 手动调用无效，Unity使用自己的内存管理系统而非.NET GC

**Q036.** [模块:A][维度:概念理解][难度:★★★][题型:单选]
[考点: Prefab Variant]

Prefab Variant的用途是？

- A. 将多个不同的Prefab合并为一个组合Prefab，共享所有组件和属性设置
- B. 基于Base Prefab创建变体，继承Base的修改但可覆盖部分属性
- C. 将Prefab导出为独立的Asset文件，解除与Base Prefab所有关联以降低耦合
- D. 创建Prefab的轻量级引用（不拷贝数据），运行时动态加载Base Prefab并应用差异补丁

**Q037.** [模块:A][维度:概念理解][难度:★★★★][题型:单选]
[考点: Scriptable Build Pipeline]

Scriptable Build Pipeline(SBP)的作用是？

- A. 管理场景构建列表和构建编号，自动生成Player Build配置
- B. 替代Unity默认的C#编译器（Roslyn），支持更高版本的C#语法特性和更快编译速度
- C. 提供可编程的AssetBundle构建管线，支持自定义构建流程和缓存
- D. 控制渲染管线的构建过程，优化Shader编译时间和变体收集覆盖率

**Q038.** [模块:A][维度:概念理解][难度:★★★★][题型:单选]
[考点: Incremental GC]

Unity的Incremental GC(增量垃圾回收)的好处是？

- A. 完全消除GC暂停，改为引用计数方式管理所有托管内存的分配和释放
- B. 将GC工作分散到多帧执行，减少单帧GC卡顿
- C. 在独立的后台GC线程执行垃圾回收工作，对主线程渲染和逻辑无任何影响
- D. 增加可用堆内存上限至4GB，减少GC触发频率但不改变单次GC的耗时

**Q039.** [模块:A][维度:概念理解][难度:★★★][题型:单选]
[考点: DontDestroyOnLoad]

DontDestroyOnLoad(gameObject)的作用是？

- A. 使该GameObject在运行时无法通过Destroy销毁（类似const标记），直到应用退出
- B. 将该GameObject从当前场景移除并缓存到内存，在切换回原场景时自动恢复
- C. 使该GameObject的Transform锁定当前世界位置，场景切换后坐标保持不变
- D. 使该GameObject在场景切换时不被销毁

**Q040.** [模块:A][维度:概念理解][难度:★★★★][题型:单选]
[考点: Unity调试技巧]

Unity开发中实用的调试技巧包括？
- A. 使用Debug.Error()代替Debug.LogError()可以获得更详细的堆栈信息
- B. 在Update中每帧调用Debug.Log可以监控变量实时变化且不影响性能
- C. 使用Conditional特性控制调试代码的编译
- D. 所有Log调用在发布版本中会自动移除，无需手动删除
---

## 模块B：物理系统（45题）

- A. Debug.DrawRay/DrawLine可视化射线
- B. [Header][Tooltip][Range]属性增强Inspector
- C. #if UNITY_EDITOR条件编译只在编辑器执行的调试代码
- D. Gizmos绘制辅助图形
**Q041.** [模块:B][维度:概念理解][难度:★][题型:单选]
[考点: Rigidbody基本概念]

Rigidbody组件的作用是？

- A. 控制物体在动画系统中的骨骼绑定和蒙皮权重
- B. 定义物体的碰撞形状和范围，但不参与物理力的计算
- C. 使GameObject参与物理模拟（受重力、力、碰撞影响）
- D. 用于在Scene视图中可视化物理碰撞体的边界和形状辅助线

**Q042.** [模块:B][维度:API精确度][难度:★][题型:单选]
[考点: AddForce方法]

Rigidbody.AddForce(force, ForceMode.Impulse)的效果是？

- A. 施加持续加速度，效果与ForceMode.Acceleration相同但不受质量影响
- B. 只改变物体的角速度（旋转），不影响线速度
- C. 在每个FixedUpdate中持续施加该力，直到手动停止
- D. 施加瞬间冲量（不考虑时间），直接改变速度

**Q043.** [模块:B][维度:概念理解][难度:★★][题型:单选]
[考点: Collider类型]

以下哪种Collider在物理计算中开销最大？

- A. MeshCollider（非凸），因为需要逐三角面进行碰撞检测
- B. SphereCollider，因为球面积分计算量最大
- C. BoxCollider，因为需要计算6个平面的碰撞检测
- D. CapsuleCollider，因为需要同时处理圆柱面和球面的碰撞

**Q044.** [模块:B][维度:概念理解][难度:★★][题型:单选]
[考点: Trigger vs Collision]

带有Trigger标记的Collider和普通Collider的区别是？

- A. Trigger和普通Collider都产生碰撞响应，区别在于Trigger会自动销毁被碰撞的对象
- B. Trigger在碰撞时产生更小的力响应，适合轻量级碰撞如拾取物品
- C. Trigger不产生物理碰撞响应（不弹回），只检测重叠事件(OnTriggerEnter)
- D. 普通Collider无法触发任何回调事件，只有Trigger标记的Collider才能检测碰撞

**Q045.** [模块:B][维度:API精确度][难度:★★][题型:单选]
[考点: OnCollisionEnter参数]

OnCollisionEnter的参数Collision包含哪些信息？

- A. 包含双方Rigidbody的引用及质量信息，但不提供碰撞接触点坐标
- B. 仅包含对方Collider的引用，不提供碰撞点或力的信息
- C. 碰撞点(contacts)、相对速度(relativeVelocity)、对方碰撞体(collider)等
- D. 仅包含碰撞点的世界坐标列表，不包含相对速度和对方碰撞体

**Q046.** [模块:B][维度:概念理解][难度:★★][题型:单选]
[考点: IsKinematic]

Rigidbody设置IsKinematic为true后，该物体不再受物理引擎控制（如重力、碰撞力），但仍可通过代码移动并触发碰撞事件。


- A. IsKinematic仅影响重力，物体仍受碰撞力和关节约束影响
- B. 设置IsKinematic后物体完全脱离物理系统，不再参与任何碰撞检测
- C. IsKinematic为true时物体仍受重力影响但不受碰撞力，且无法通过代码移动
- D. 设置IsKinematic为true后，物体不再受物理引擎控制但可通过代码移动并触发碰撞事件

**Q047.** [模块:B][维度:Bug诊断][难度:★★★][题型:代码阅读]
[考点: 物体穿透问题]

高速移动的子弹穿透了薄墙壁（碰撞检测失败）。原因和解决方案是？

- A. 离散碰撞检测在两帧之间物体已穿过薄墙；将Rigidbody的Collision Detection改为Continuous
- B. 子弹的Collider尺寸太小，需要增大Collider的Size使其超过墙壁厚度来确保检测
- C. 需要在子弹脚本的Update中手动发射Raycast来检测前方障碍物作为补充检测
- D. 墙壁的Collider需要设为IsTrigger才能检测到高速穿过的物体

**Q048.** [模块:B][维度:代码生成/阅读][难度:★★][题型:代码补全]
[考点: Raycast射线检测]

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
[考点: FixedUpdate物理更新]

为什么物理相关代码（如AddForce）应放在FixedUpdate而非Update中？

- A. Update和FixedUpdate中调用AddForce效果一致，放在FixedUpdate只是代码规范的建议
- B. FixedUpdate以固定时间步长执行，物理引擎在FixedUpdate中更新，保证物理模拟的稳定性
- C. Update中调用AddForce会被物理引擎忽略，因为物理引擎只接受FixedUpdate中的输入
- D. FixedUpdate在独立的物理线程中执行，不会阻塞主线程的渲染和逻辑

**Q050.** [模块:B][维度:概念理解][难度:★★★][题型:单选]
[考点: ForceMode类型]

Rigidbody.AddForce的ForceMode有哪些选项？
- A. Linear、Angular、Radial、Orbital
- B. Smooth、Instant、Gradual、Sudden
- C. Position、Rotation、Scale、Transform
- D. Acceleration（加速度，不受质量影响）

**Q051.** [模块:B][维度:性能优化][难度:★★★][题型:单选]
[考点: 物理层碰撞矩阵]

Physics Layer Collision Matrix的优化作用是？

- A. 提高碰撞检测的精度，让不同层的碰撞体使用不同的检测算法
- B. 关闭不需要碰撞检测的层之间的交互，减少物理计算开销
- C. 管理不同渲染层的绘制顺序，优化GPU的overdraw
- D. 控制不同层之间碰撞力的大小和方向，实现差异化的物理响应

**Q052.** [模块:B][维度:代码生成/阅读][难度:★★★][题型:代码补全]
[考点: OverlapSphere检测]

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
[考点: Joint物理关节]

Unity中的Joint(关节)组件的作用是？

- A. 绑定Animator Controller中不同State之间的过渡条件
- B. 管理Transform层级中父子物体之间的坐标变换和缩放传递
- C. 约束两个Rigidbody之间的相对运动关系（如铰链、弹簧、固定连接等）
- D. 控制两个Mesh之间的顶点焊接关系，用于运行时合并网格

**Q054.** [模块:B][维度:API精确度][难度:★★★][题型:单选]
[考点: Physics.RaycastAll]

Physics.RaycastAll和Physics.Raycast的区别是？

- A. Raycast返回射线穿过的所有碰撞体并按距离排序，RaycastAll只返回最近的一个
- B. RaycastAll是异步版本在后台线程执行，Raycast是同步阻塞主线程执行
- C. RaycastAll返回射线穿过的所有碰撞体，Raycast只返回第一个（最近的）
- D. RaycastAll自动过滤Trigger碰撞体，Raycast同时检测Trigger和非Trigger碰撞体

**Q055.** [模块:B][维度:Bug诊断][难度:★★★][题型:单选]
[考点: MovePosition vs Transform.position]

使用Transform.position直接移动Rigidbody物体可能导致什么问题？

- A. Transform.position赋值会被物理引擎在下一个FixedUpdate中自动回滚到碰撞前的位置
- B. 绕过物理引擎计算，可能导致碰撞检测失败和穿模
- C. 导致Rigidbody自动切换为Kinematic模式，后续的AddForce调用全部失效
- D. 只影响视觉位置不影响物理位置，Collider仍停留在原位导致碰撞不一致

**Q056.** [模块:B][维度:概念理解][难度:★★★][题型:单选]
[考点: 2D vs 3D物理]

Unity中2D物理和3D物理系统的关系是？

- A. 可以互相检测碰撞，通过Physics2D.Collide3D桥接API实现
- B. 共用同一个底层物理引擎(PhysX)，2D物理是3D的平面投影简化版
- C. 两个独立的物理系统，2D碰撞体不与3D碰撞体交互
- D. 2D物理是3D物理的子集，Rigidbody2D继承自Rigidbody

**Q057.** [模块:B][维度:代码生成/阅读][难度:★★★][题型:代码生成]
[考点: 物理材质]

Physic Material中Friction和Bounciness参数分别控制什么？

- A. Friction控制碰撞时的能量吸收比例，Bounciness控制碰撞后的反弹角度偏移量
- B. Friction和Bounciness共同控制物体的质量和密度，影响重力加速度和碰撞力度
- C. Friction控制物体表面的粗糙度影响渲染效果，Bounciness控制碰撞后的速度衰减比
- D. Friction控制摩擦力（0=无摩擦），Bounciness控制弹性（0=不弹跳，1=完全弹性）

**Q058.** [模块:B][维度:性能优化][难度:★★★★][题型:单选]
[考点: 物理分层优化]

在一个有大量子弹和大量敌人的游戏中，如何优化碰撞检测性能？

- A. 为所有物体统一使用CapsuleCollider以获得最佳的碰撞检测精度和性能平衡
- B. 提高Physics.defaultSolverIterations到20以上，确保碰撞检测无遗漏
- C. 将子弹和敌人放在不同Layer，关闭子弹与子弹之间、敌人与敌人之间的碰撞检测
- D. 使用Physics.BakeMesh预烘焙所有物理碰撞体，减少运行时计算量

**Q059.** [模块:B][维度:概念理解][难度:★★★][题型:单选]
[考点: CharacterController]

CharacterController和Rigidbody的区别是？

- A. CC是Rigidbody的轻量级版本，内部仍使用PhysX物理引擎但简化了参数配置
- B. CC提供自定义的角色移动控制（不受物理引擎驱动），RB由物理引擎驱动
- C. CC和RB可以同时添加在同一个GameObject上，CC负责移动，RB负责碰撞响应
- D. CC适合需要物理交互的场景（如赛车），RB适合精确控制的角色移动（如FPS）

**Q060.** [模块:B][维度:API精确度][难度:★★★][题型:代码补全]
[考点: CharacterController.Move]

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
[考点: Continuous碰撞检测模式]

Rigidbody的Collision Detection有哪些模式以及适用场景？

- A. Discrete(默认)和Speculative(推测性连续检测)两种模式，ContinuousDynamic已在Unity 2022中移除
- B. 只有Discrete和Continuous两种模式，区别在于是否对Trigger生效
- C. Discrete(默认/低速), Continuous(高速物体与静态碰撞), ContinuousDynamic(高速物体间碰撞)
- D. 只有一种默认模式，碰撞精度通过Solver Iterations参数控制

**Q062.** [模块:B][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 自定义重力]

实现自定义重力方向（球面重力）：
```csharp
void FixedUpdate() {
    Vector3 gravityDir = (planetCenter - transform.position).normalized;
    rb.AddForce(gravityDir * gravityForce);
    Quaternion targetRot = Quaternion.FromToRotation(transform.up, -gravityDir) * transform.rotation;
    transform.rotation = Quaternion._____(transform.rotation, targetRot, rotSpeed * Time.fixedDeltaTime);
}
```

- A. Lerp
- B. Slerp
- C. LookRotation
- D. RotateTowards

**Q063.** [模块:B][维度:概念理解][难度:★★★★][题型:单选]
[考点: Physics.Simulate]

Physics.Simulate(float step)的作用和使用场景是？

- A. 重置物理引擎状态并重新初始化所有碰撞体的AABB包围盒
- B. 手动模拟物理步进，用于预测/回滚（如网络同步中的预测物理）
- C. 暂停当前帧的物理更新并延迟到下一帧执行，用于分帧计算复杂物理场景
- D. 以指定的速度倍率加速物理模拟，常用于慢动作和时间加速效果

**Q064.** [模块:B][维度:概念理解][难度:★★★★][题型:单选]
[考点: CC vs RB选择]

CharacterController适合精确控制的角色移动（平台跳跃、FPS），Rigidbody适合需要物理交互的场景（赛车、推箱子）。


- A. CharacterController仅适用于第一人称视角，Rigidbody适用于所有其他视角
- B. Rigidbody无法实现角色移动，只能用于静态物体的物理模拟
- C. 两者功能相同，CharacterController只是Rigidbody的封装版本
- D. CharacterController适合精确控制的角色移动，Rigidbody适合需要物理交互的场景

**Q065.** [模块:B][维度:概念理解][难度:★★][题型:单选]
[考点: Rigidbody.velocity]

直接设置Rigidbody.velocity会有什么影响？

- A. 与AddForce(ForceMode.VelocityChange)效果完全相同，只是语法简写
- B. velocity是只读属性，直接赋值会导致编译错误
- C. 设置velocity后物理引擎会在下一帧自动恢复为碰撞前的速度值
- D. 覆盖当前速度，可能导致物理模拟不自然（忽略了力的积累和碰撞响应）

**Q066.** [模块:B][维度:API精确度][难度:★★★][题型:单选]
[考点: LayerMask位掩码]

LayerMask的本质是什么？

- A. 一个ScriptableObject资产，在Project中配置并通过引用传递
- B. 一个枚举类型(enum)，每个值对应一个预定义的物理层名称
- C. 一个32位整数的位掩码，每一位对应一个Layer
- D. 一个字符串数组，存储所有激活的Layer名称用于运行时查找

**Q067.** [模块:B][维度:代码生成/阅读][难度:★★★][题型:代码补全]
[考点: LayerMask使用]

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
[考点: Trigger条件]

两个物体要触发OnTriggerEnter，至少需要：至少一个有Rigidbody，且至少一个Collider设置为IsTrigger。


- A. 该描述部分正确，但遗漏了关键的限制条件
- B. 该描述正确
- C. 该描述完全错误，实际行为与描述相反
- D. 该描述仅在特定Unity版本中成立，其他版本行为不同

**Q069.** [模块:B][维度:性能优化][难度:★★★★][题型:单选]
[考点: 物理性能优化]

Unity物理系统性能优化的方法包括？
- A. 在Update而非FixedUpdate中执行所有物理计算
- B. 增大所有Rigidbody的质量值可以减少物理计算量
- C. 降低物理更新频率（增大Fixed Timestep）
- D. 将所有Collider替换为MeshCollider以获得更精确的碰撞检测

**Q070.** [模块:B][维度:Bug诊断][难度:★★★★][题型:代码阅读]
[考点: 物理振荡问题]

角色在地面上持续微小抖动/震颤。可能原因是？

- A. 地面Collider的法线方向计算错误，需要重新烘焙(Bake)地面的MeshCollider
- B. Rigidbody的Mass值设置过小（如0.001），导致碰撞力过大引起弹跳
- C. FixedUpdate的时间步长过大导致物理模拟精度不足，需要减小Fixed Timestep至0.005秒
- D. 重力持续施加but地面碰撞响应导致微振荡；可以增大Sleep Threshold或使用CharacterController

**Q071.** [模块:B][维度:API精确度][难度:★★★][题型:单选]
[考点: SphereCast]

Physics.SphereCast和Physics.Raycast的区别是？

- A. Raycast检测时使用球形区域而非射线，SphereCast才是真正的细线射线检测
- B. SphereCast在独立线程异步执行，Raycast在主线程同步执行
- C. SphereCast发射一个球形"胖射线"，检测范围更大（用于近似角色碰撞检测）
- D. SphereCast仅检测带有SphereCollider的物体，Raycast可检测所有类型的Collider

**Q072.** [模块:B][维度:概念理解][难度:★★★★][题型:单选]
[考点: Physics Query NonAlloc]

Physics.OverlapSphereNonAlloc相比OverlapSphere的优势是？

- A. 不分配新数组，使用预分配的缓冲区，减少GC
- B. 自动按距离排序返回结果，而OverlapSphere返回无序结果
- C. 在后台线程异步执行检测，不阻塞主线程的Update循环
- D. 支持检测更多碰撞体（无上限），而OverlapSphere最多返回256个结果

**Q073.** [模块:B][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 扇形范围检测]

检测前方扇形范围内的目标：
```csharp
bool IsInSector(Vector3 origin, Vector3 forward, Vector3 targetPos, float radius, float halfAngle) {
    Vector3 dir = (targetPos - origin);
    if(dir.magnitude > radius) return false;
    float angle = Vector3._____(forward, dir.normalized);
    return angle <= halfAngle;
}
```

- A. SignedAngle
- B. Distance
- C. Dot
- D. Angle

**Q074.** [模块:B][维度:概念理解][难度:★★][题型:单选]
[考点: Rigidbody插值]

Rigidbody的Interpolate选项的作用是？

- A. 在渲染帧之间插值物理位置，使运动看起来更平滑
- B. 在多个物理步之间加速碰撞检测，类似Continuous Detection的低开销版本
- C. 提高物理引擎的碰撞检测精度，减少高速物体的穿透问题
- D. 减少Rigidbody的内存占用，通过降低物理模拟分辨率换取性能

**Q075.** [模块:B][维度:概念理解][难度:★★★][题型:单选]
[考点: Rigidbody约束]

Rigidbody.constraints = RigidbodyConstraints.FreezeRotation 的作用是？

- A. 冻结物体在所有轴上的旋转（只允许位移）
- B. 同时冻结物体的位移和旋转，使其完全静止
- C. 解除所有之前设置的旋转和位移约束，恢复自由运动
- D. 冻结物体在所有轴上的位移（只允许旋转）

**Q076.** [模块:B][维度:Bug诊断][难度:★★★★][题型:单选]
[考点: 碰撞事件不触发]

两个物体有Collider但OnCollisionEnter不触发，可能原因是？

- A. 物体的Transform.scale不为(1,1,1)时碰撞事件被自动禁用
- B. OnCollisionEnter仅在FixedUpdate之后调用，如果物体在Update中移动则不会触发
- C. 两个物体的Collider必须类型完全相同（如都是BoxCollider）才能触发碰撞事件
- D. 两个物体都没有Rigidbody，或者有一个Collider是Trigger

**Q077.** [模块:B][维度:代码生成/阅读][难度:★★★][题型:代码补全]
[考点: CompoundCollider]

创建复合碰撞体(Compound Collider)的方法是？

- A. 在子物体上添加多个简单Collider，它们会自动组合成父物体的复合碰撞形状
- B. 使用ProBuilder创建自定义网格，导出为MeshCollider自动生成复合碰撞体
- C. 在脚本中调用Physics.MergeColliders()将多个Collider合并为一个复合碰撞形状
- D. 使用ConvexMeshCollider并设置convex=true，引擎自动将非凸网格分解为多个凸包

**Q078.** [模块:B][维度:概念理解][难度:★★★][题型:单选]
[考点: Physics.IgnoreCollision]

Physics.IgnoreCollision(colliderA, colliderB, true)的作用是？

- A. 忽略colliderA所在Layer与colliderB所在Layer之间的所有碰撞检测
- B. 让colliderA在渲染时不显示colliderB的投射阴影
- C. 让两个特定Collider之间互相忽略碰撞（运行时动态设置）
- D. 仅忽略Trigger事件（OnTriggerEnter等），物理碰撞响应仍然生效

**Q079.** [模块:B][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: 物理模拟优化方案]

一个有1000个动态物理对象的场景，如何优化？

- A. 将所有物体换成MeshCollider(convex)以获得最精确的碰撞形状匹配
- B. 远处物体设为Kinematic或Sleep + 简化Collider + 分层碰撞矩阵 + 降低Solver迭代
- C. 启用Physics.autoSimulation = false后在协程中分帧调用Physics.Simulate降低单帧开销
- D. 将所有物理对象的Fixed Timestep设为0.001秒以获得最高精度的碰撞检测

**Q080.** [模块:B][维度:API精确度][难度:★★★][题型:单选]
[考点: Rigidbody.SweepTest]

Rigidbody.SweepTest的作用是？

- A. 将刚体沿指定方向的所有碰撞体收集到列表中并按质量排序
- B. 沿指定方向测试刚体移动是否会碰到障碍物（不实际移动）
- C. 清除刚体上累积的所有碰撞缓存数据和Contact Point历史记录
- D. 扫描场景中所有与该刚体发生过碰撞的物体并返回碰撞统计信息

**Q081.** [模块:B][维度:概念理解][难度:★★★][题型:单选]
[考点: 碰撞回调方法]

以下哪些是MonoBehaviour的物理碰撞回调方法？
- A. OnCollisionEnter、OnCollisionStay、OnCollisionExit
- B. OnCollisionEnter、OnTriggerEnter、OnParticleCollision、OnJointBreak
- C. OnTriggerBegin、OnTriggerUpdate、OnTriggerFinish、OnTriggerAbort
- D. OnPhysicsStart、OnPhysicsUpdate、OnPhysicsEnd、OnPhysicsReset

**Q082.** [模块:B][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 反弹物理]

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
[考点: Physics.autoSyncTransforms]

Physics.autoSyncTransforms的作用是？

- A. 自动将物理引擎计算的刚体位置同步回Animator的Root Motion数据
- B. 自动同步Transform变化到物理引擎；关闭后手动调用Physics.SyncTransforms()可提高性能
- C. 在多人网络游戏中自动同步各客户端之间的物理状态
- D. 将Physics.Simulate的结果自动同步到NavMesh导航系统的障碍物数据

**Q084.** [模块:B][维度:概念理解][难度:★★★★][题型:单选]
[考点: 布料物理Cloth]

Unity的Cloth组件用于模拟什么？

- A. 刚体之间的链条和绳索连接效果（如吊桥、秋千、钟摆等）
- B. 软体物理变形效果（如弹性球、果冻、橡胶轮胎等）
- C. 流体和液体的表面张力模拟（如水面波纹、瀑布等）
- D. 布料/织物的物理效果（如角色的披风、旗帜、窗帘等）

**Q085.** [模块:B][维度:概念理解][难度:★★★★][题型:单选]
[考点: 确定性物理]

游戏中需要确定性物理模拟（如帧同步网络游戏），Unity默认物理引擎(PhysX)是否满足？

---

## 模块C：渲染系统（50题）

- A. 不满足，PhysX不保证确定性；需要使用Unity Physics(DOTS)或自定义定点数物理
- B. 使用IL2CPP脚本后端编译即可保证浮点运算确定性，Mono后端不支持
- C. 在Project Settings中开启"Deterministic Physics"选项即可保证跨平台确定性
- D. PhysX默认满足确定性要求，只需确保Fixed Timestep在所有客户端一致

**Q086.** [模块:C][维度:概念理解][难度:★][题型:单选]
[考点: Camera组件]

Camera组件的Clear Flags设置为Skybox表示什么？

- A. 将天空盒作为后处理效果叠加在场景渲染结果之上
- B. 摄像机先渲染天空盒作为背景，再渲染场景物体
- C. 使用上一帧的渲染结果作为背景，天空盒仅在第一帧渲染
- D. 仅在天空盒纹理加载完成后才开始渲染场景物体，否则显示Loading画面

**Q087.** [模块:C][维度:概念理解][难度:★][题型:单选]
[考点: Material与Shader关系]

Material和Shader的关系是？

- A. Shader是Material的一个实例，多个Shader可共享同一个Material
- B. Material和Shader是同一概念的不同称呼，在Inspector中的显示方式不同
- C. Material包含Shader的HLSL/GLSL源码，运行时编译为GPU指令
- D. Shader定义渲染算法，Material是Shader的一个实例（保存具体参数值如颜色、纹理）

**Q088.** [模块:C][维度:概念理解][难度:★★][题型:单选]
[考点: Draw Call概念]

什么是Draw Call？

- A. Unity编辑器中Scene视图每帧刷新的回调函数
- B. GPU内部每个像素的着色器计算过程
- C. CPU向GPU发送的一次渲染请求指令
- D. 内存管理系统中分配GPU显存的操作

**Q089.** [模块:C][维度:性能优化][难度:★★][题型:单选]
[考点: Draw Call优化]

减少Draw Call的常用方法不包括？

- A. 使用SpriteAtlas/TextureAtlas
- B. GPU Instancing
- C. 增加材质数量
- D. Static Batching

**Q090.** [模块:C][维度:概念理解][难度:★★][题型:单选]
[考点: LOD系统]

LOD(Level of Detail)系统的作用是？

- A. 按GPU占用率自动控制物体的渲染开关，优先渲染距离最近的物体
- B. 根据物体与摄像机的距离切换不同精度的模型，远处使用低精度模型减少渲染开销
- C. 管理纹理Mipmap级别，控制不同距离下的纹理分辨率选择策略
- D. 根据当前帧率动态调整所有物体的网格面数，低帧率时自动简化Mesh

**Q091.** [模块:C][维度:概念理解][难度:★★][题型:单选]
[考点: Occlusion Culling]

Occlusion Culling(遮挡剔除)的作用是：在渲染前剔除被其他物体完全遮挡的物体，不送入GPU渲染。


- A. 在渲染前剔除被其他物体完全遮挡的物体，不送入GPU渲染
- B. 仅剔除超出摄像机视锥体范围的物体，不处理遮挡关系
- C. 动态调整物体的LOD级别，远处物体使用低精度模型减少渲染
- D. 根据物体材质透明度决定是否渲染，半透明物体不参与剔除

**Q092.** [模块:C][维度:概念理解][难度:★★★][题型:单选]
[考点: 渲染管线选择]

Unity支持的三种渲染管线分别是？

- A. 2D Render Pipeline、3D Render Pipeline、Compute Pipeline
- B. Forward Rendering、Deferred Rendering、Hybrid Rendering
- C. Built-in Render Pipeline、URP(Universal)、HDRP(High Definition)
- D. Mobile Pipeline、Desktop Pipeline、VR Pipeline

**Q093.** [模块:C][维度:概念理解][难度:★★★][题型:单选]
[考点: Forward vs Deferred]

Forward Rendering和Deferred Rendering的主要区别是？

- A. Forward渲染到Framebuffer，Deferred渲染到RenderTexture，两者输出格式不同
- B. Forward对每个物体逐光源计算光照，Deferred先渲染G-Buffer再统一计算光照
- C. Forward仅支持方向光，Deferred支持所有光源类型
- D. Forward每次渲染整个场景然后逐光源叠加，Deferred每个光源单独渲染一遍完整场景

**Q094.** [模块:C][维度:性能优化][难度:★★★][题型:单选]
[考点: 纹理优化]

纹理性能优化的方法包括？
- A. 将所有纹理尺寸调整为2的幂次方以外的值可以避免Mipmap生成
- B. 禁用Mipmap可以减少50%的内存占用且不影响渲染质量
- C. 所有纹理都使用RGBA32格式以保证最高画质
- D. 使用纹理压缩格式（如ASTC、ETC2）

**Q095.** [模块:C][维度:概念理解][难度:★★★][题型:单选]
[考点: SRP Batcher]

SRP Batcher的工作原理是？

- A. 将多个不同Mesh的渲染命令合并为一个Draw Call提交给GPU
- B. 缓存Material属性，减少CPU向GPU上传数据的次数（减少SetPass Call）
- C. 将GPU渲染命令序列化到CommandBuffer中批量提交，减少CPU-GPU通信次数
- D. 压缩Shader变体数量，减少运行时Shader编译和切换开销

**Q096.** [模块:C][维度:API精确度][难度:★★★][题型:单选]
[考点: Camera.cullingMask]

Camera.cullingMask的作用是？

- A. 设置摄像机的视野角度大小(FOV)，限制可见区域
- B. 控制后处理效果的应用范围，指定哪些Layer不做后处理
- C. 通过LayerMask控制相机只渲染特定Layer上的物体
- D. 控制相机的远近裁剪面距离，超出范围的物体不渲染

**Q097.** [模块:C][维度:概念理解][难度:★★★][题型:单选]
[考点: 光照贴图Lightmap]

烘焙Lightmap的优势和限制是？

- A. 优势：静态光照零运行时开销。限制：只适用于静态物体，不能反映动态变化
- B. 优势：无需预计算即可获得全局光照效果。限制：文件体积大增加安装包大小
- C. 优势：支持所有物体包括动态物体的全局光照。限制：增加运行时GPU计算开销
- D. 优势：实时更新光照支持昼夜变化。限制：需要高端GPU才能使用

**Q098.** [模块:C][维度:代码生成/阅读][难度:★★★][题型:代码补全]
[考点: Material属性设置]

通过代码修改Material颜色：
```csharp
GetComponent<Renderer>().material._____(---"_Color", Color.red);
```

- A. SetColor
- B. SetValue
- C. SetVector4
- D. SetProperty

**Q099.** [模块:C][维度:Bug诊断][难度:★★★][题型:单选]
[考点: Material实例化内存泄漏]

通过renderer.material访问Material会发生什么？

- A. 返回sharedMaterial的只读副本，任何Set操作都会抛出InvalidOperationException
- B. 仅在Editor中创建实例，Build后直接返回sharedMaterial引用以节省内存
- C. Unity自动创建该Material的实例副本，如不注意会导致内存泄漏；应使用sharedMaterial（只读）或手动管理实例
- D. 直接返回项目中Material Asset的引用，修改renderer.material等同于修改Asset文件

**Q100.** [模块:C][维度:概念理解][难度:★★★][题型:单选]
[考点: Frustum Culling]

Camera的Frustum Culling(视锥体剔除)的原理是？

- A. 与Occlusion Culling算法相同，都使用预烘焙的可见性数据
- B. 通过深度测试剔除被前方物体遮挡的像素片段
- C. 剔除面积小于屏幕1%的物体以减少小物件渲染开销
- D. 物体的包围盒不在摄像机视锥体内时，不提交渲染

**Q101.** [模块:C][维度:性能优化][难度:★★★][题型:单选]
[考点: GPU Instancing]

GPU Instancing的作用和要求是？

- A. 一次Draw Call渲染多个相同Mesh+Material的对象；要求Shader支持Instancing
- B. 将多个不同Mesh合并为一个DrawCall渲染，不要求Shader做特殊支持
- C. 仅适用于标记为Static的物体，动态物体不支持GPU Instancing
- D. 在GPU上实例化运行时生成的程序化Mesh，不需要预定义模型数据

**Q102.** [模块:C][维度:概念理解][难度:★★★][题型:单选]
[考点: RenderTexture]

RenderTexture的用途包括？

- A. 作为纹理压缩的中间格式，在ASTC/ETC2格式转换时使用
- B. 仅用于UI的Image组件显示静态图片，不支持实时渲染内容
- C. 存储顶点和索引缓冲区数据，供ComputeShader读写使用
- D. 将摄像机渲染结果输出到纹理中（如小地图、镜面反射、后处理等）

**Q103.** [模块:C][维度:概念理解][难度:★★★★][题型:单选]
[考点: Shader变体Variant]

Shader Variant过多会导致什么问题？

- A. 仅影响编辑器中的Shader编译速度，不影响运行时性能和包体大小
- B. GPU渲染速度下降，因为每个变体都需要占用独立的GPU寄存器
- C. 提高运行时性能，因为更多变体意味着更精确的渲染路径选择
- D. 编译时间长、运行时内存占用大、构建包体增大

**Q104.** [模块:C][维度:概念理解][难度:★★★★][题型:单选]
[考点: Light Probe]

Light Probe(光照探针)的作用是？

- A. 实时追踪光源方向变化，动态更新所有物体的阴影方向
- B. 记录场景中每个物体的阴影遮挡信息，用于实时阴影渲染
- C. 存储高分辨率环境光照纹理，替代HDRI Skybox用于Image Based Lighting
- D. 在场景中采样烘焙光照信息，为动态物体提供间接光照近似

**Q105.** [模块:C][维度:概念理解][难度:★★★★][题型:单选]
[考点: Reflection Probe]

Reflection Probe(反射探针)的工作方式是？

- A. 在探针位置渲染周围环境为Cubemap，用于反射环境的近似
- B. 将平面镜反射投影到表面UV空间，仅支持平面反射效果
- C. 实时渲染6个方向的高分辨率深度图，通过视差校正实现精确反射
- D. 使用屏幕空间光线追踪(SSR)计算精确反射，Probe仅提供追踪起点

**Q106.** [模块:C][维度:概念理解][难度:★★★★][题型:单选]
[考点: 全局光照GI]

Unity支持的全局光照(GI)方案包括？
- A. Forward GI、Deferred GI、ForwardPlus GI、TileBased GI
- B. Raytraced GI、PathTraced GI、PhotonMapped GI、Radiosity GI
- C. Enlighten（已弃用）、Lightmaps（烘焙）
- D. Realtime GI、Baked GI、Dynamic GI、Static GI

**Q107.** [模块:C][维度:概念理解][难度:★★★★][题型:单选]
[考点: 动态分辨率]

Unity的Dynamic Resolution(动态分辨率)的工作原理是？

- A. 仅在编辑器Profiler中模拟不同分辨率的性能表现，不影响实际构建
- B. 仅降低UI元素的渲染分辨率不影响3D场景，因为UI对清晰度要求低
- C. 固定以50%分辨率渲染所有场景，然后通过超采样上采样到目标分辨率
- D. 根据GPU负载动态降低渲染分辨率以维持帧率，在性能和画质间自动平衡

**Q108.** [模块:C][维度:概念理解][难度:★★★★][题型:单选]
[考点: Cascade Shadow]

级联阴影贴图(Cascaded Shadow Maps)的原理是？

- A. 将阴影贴图按时间级联更新，每帧只更新一段区域，多帧累积完整阴影
- B. 使用一张超大分辨率阴影贴图覆盖整个场景，不做分段处理
- C. 每个产生阴影的物体使用独立的阴影贴图，按物体优先级分配分辨率
- D. 将视锥体分段，每段使用不同分辨率的阴影贴图，近处精度高远处精度低

**Q109.** [模块:C][维度:概念理解][难度:★★★★][题型:单选]
[考点: SSAO]

屏幕空间环境光遮蔽(SSAO)的原理是？

- A. 在屏幕空间根据深度和法线信息估算每个像素被周围几何体遮蔽的程度，增加接触阴影
- B. 通过实时光线追踪计算每个表面点接收的环境光比例
- C. 基于全局光照的光子映射算法计算环境光遮蔽，需要预烘焙数据
- D. 使用预计算的AO贴图纹理存储遮蔽信息，运行时直接采样叠加

**Q110.** [模块:C][维度:概念理解][难度:★★★★][题型:单选]
[考点: Texture Streaming]

Texture Streaming(纹理流式加载)的工作原理是？

- A. 将纹理数据存储在StreamingAssets目录，通过文件流按需读取像素数据
- B. 在场景加载时将所有纹理预加载到GPU显存中以避免运行时加载卡顿
- C. 根据摄像机距离动态加载不同Mipmap级别的纹理，减少内存占用
- D. 仅加载最高分辨率Mipmap并在GPU上实时生成低级别Mipmap

**Q111.** [模块:C][维度:性能优化][难度:★★★★][题型:单选]
[考点: 移动端渲染优化]

移动端渲染优化措施包括？
- A. 在Fragment Shader中进行复杂的光照计算和阴影采样
- B. 将所有对象的Draw Call合并为一个以减少渲染开销
- C. 使用高精度的Float纹理替代压缩纹理以提高画质
- D. 使用简化版Shader和LOD系统

**Q112.** [模块:C][维度:概念理解][难度:★★★][题型:单选]
[考点: 半透明渲染排序]

半透明物体的渲染顺序是？

- A. 与不透明物体使用相同的深度测试渲染顺序，不做特殊排序
- B. 按Material排序渲染以最大化合批效率，不考虑物体前后关系
- C. 从前往后排序渲染（离摄像机近的先画），写入深度缓冲后裁剪后方重叠部分
- D. 从后往前排序渲染（离摄像机远的先画），不写入深度缓冲

**Q113.** [模块:C][维度:代码生成/阅读][难度:★★★][题型:代码补全]
[考点: Camera渲染到RT]

将摄像机渲染结果用作小地图纹理：
```csharp
Camera miniMapCam;
RenderTexture rt;
void Start() {
    rt = new RenderTexture(256, 256, 16);
    miniMapCam._____ = rt;
    miniMapImage.texture = rt;
}
```

- A. outputTexture
- B. mainTexture
- C. targetTexture
- D. renderTexture

**Q114.** [模块:C][维度:概念理解][难度:★★★★][题型:单选]
[考点: SetPass Call]

SetPass Call和Draw Call的区别是什么？

- A. SetPass Call和Draw Call是同一操作的不同阶段名称，本质上没有区别
- B. Draw Call是CPU侧的渲染指令提交，SetPass Call是GPU侧的渲染管线状态配置
- C. SetPass Call是切换Shader Pass或材质状态的调用，Draw Call是提交渲染命令；SetPass Call对性能影响更大
- D. SetPass Call发生在每帧开始时初始化渲染状态，Draw Call发生在每个物体渲染时

**Q115.** [模块:C][维度:概念理解][难度:★★★][题型:单选]
[考点: Projector vs Decal]

Unity URP中Decal Renderer Feature的作用是？

- A. 将聚光灯(Spot Light)的光照范围投射为指定形状的Cookie纹理
- B. 在物体表面投射贴花效果（如弹孔、血迹等）
- C. 投影远处物体的阴影贴图到近处地面增强阴影视觉效果
- D. 将摄像机视角的渲染结果投射到指定表面实现屏幕录制效果

**Q116.** [模块:C][维度:概念理解][难度:★★★][题型:单选]
[考点: Mipmap作用]

纹理Mipmap的作用是？

- A. 预计算不同分辨率的纹理版本，远处使用低分辨率避免摩尔纹并提高采样效率
- B. 压缩纹理数据减少文件大小，运行时解压还原为原始分辨率
- C. 将多个小纹理打包到一张大图集中以减少Draw Call
- D. 使纹理在所有距离上都保持最高清晰度，自动增强远处物体的纹理细节

**Q117.** [模块:C][维度:性能优化][难度:★★★★][题型:单选]
[考点: Overdraw]

什么是Overdraw以及如何减少？

- A. CPU和GPU之间数据传输超过带宽限制；减少方法：降低纹理分辨率和顶点数量
- B. 同一像素被多次绘制；减少方法：合理排序、裁剪不可见UI、减少粒子/半透明面积
- C. 内存碎片化导致的GC频繁触发；减少方法：使用对象池和预分配缓冲区
- D. 网络数据包重复传输造成的带宽浪费；减少方法：启用UDP协议和数据压缩

**Q118.** [模块:C][维度:概念理解][难度:★★★★][题型:单选]
[考点: HDR渲染]

HDR(High Dynamic Range)渲染的好处是？

- A. 仅用于VR/AR渲染中的双目立体视觉效果，普通游戏不需要
- B. 减少GPU显存占用，HDR格式比LDR格式每像素占用更少字节
- C. 提高渲染帧率，因为HDR格式纹理的GPU采样速度更快
- D. 允许像素值超过0-1范围，保留高亮度信息，支持Bloom、色调映射等效果

**Q119.** [模块:C][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: CommandBuffer自定义渲染]

通过CommandBuffer添加自定义渲染指令：
```csharp
CommandBuffer cmd = new CommandBuffer();
cmd.name = "MyCustomPass";
cmd.DrawMesh(mesh, matrix, material);
Camera.main.AddCommandBuffer(CameraEvent.AfterForwardOpaque, cmd);
```
这段代码的效果是？

- A. 仅在Scene视图中绘制调试用辅助网格，在Game视图和Build中不生效
- B. 将指定Mesh的渲染命令插入到后处理阶段之后执行，覆盖后处理效果
- C. 替换Camera.main的整个渲染管线为自定义管线，只渲染指定Mesh
- D. 在前向不透明渲染之后插入一个自定义渲染指令，绘制指定Mesh

**Q120.** [模块:C][维度:概念理解][难度:★★★][题型:单选]
[考点: Linear vs Gamma色彩空间]

Linear和Gamma色彩空间的区别是？

- A. Linear空间仅适用于2D项目，3D项目应使用Gamma空间以获得更好的法线计算
- B. Linear物理正确（推荐），光照计算在线性空间中进行更准确；Gamma是遗留方式
- C. Gamma空间在光照计算上更加准确，Linear是为了兼容老旧硬件的简化方案
- D. Linear和Gamma仅影响编辑器中的颜色显示，不影响最终构建的渲染结果

**Q121.** [模块:C][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: 大型开放世界渲染策略]

大型开放世界场景的渲染优化策略应包括？

- A. 减少场景中的物体数量到1000个以内，多余物体使用粒子系统模拟
- B. LOD系统+Occlusion Culling+场景流式加载+Shader LOD+纹理Streaming+远景Impostor
- C. 将所有资源在启动时一次性加载到内存中以避免运行时加载卡顿
- D. 仅使用低分辨率纹理和简化模型，牺牲画质确保稳定帧率

**Q122.** [模块:C][维度:概念理解][难度:★★★][题型:单选]
[考点: 天空盒Skybox]

Unity中Skybox可以通过什么方式设置？

- A. Lighting Settings中设置全局Skybox，或Camera组件单独设置
- B. 仅能通过代码RenderSettings.skybox动态设置，不支持在编辑器中可视化配置
- C. 只能在Camera的Clear Flags为Depth Only时才能显示Skybox
- D. 只能使用6张独立纹理组成Cubemap，不支持Procedural或HDRI全景Skybox

**Q123.** [模块:C][维度:性能优化][难度:★★★★][题型:单选]
[考点: Shader优化]

Shader性能优化的方法包括？
- A. 在Fragment Shader中进行大量循环计算和复杂光照
- B. 将所有计算都放在Vertex Shader中执行以减少GPU负载
- C. 减少分支语句和复杂数学运算
- D. 使用discard/clip指令可以提升移动端Shader性能

**Q124.** [模块:C][维度:概念理解][难度:★★★][题型:单选]
[考点: Mesh Renderer设置]

MeshRenderer组件中Cast Shadows和Receive Shadows选项的作用是？

- A. Cast Shadows控制是否接收阴影，Receive Shadows控制是否投射阴影（名称与功能相反）
- B. 两个选项共同控制阴影的分辨率级别，Off/On/Two Sided/Shadows Only对应不同精度
- C. Cast Shadows控制该物体是否产生阴影，Receive Shadows控制是否接收其他物体的阴影
- D. Cast Shadows仅在Built-in管线中生效，URP/HDRP中阴影由Volume组件统一控制

**Q125.** [模块:C][维度:Bug诊断][难度:★★★★][题型:单选]
[考点: Shader粉色物体]

场景中某个物体显示为粉色（品红色）。原因是什么？

- A. 纹理文件损坏或格式不支持，Unity将缺失纹理的像素填充为品红色
- B. 该物体的Layer未包含在Camera的Culling Mask中但仍被强制渲染
- C. 物体的法线方向全部反转，导致光照计算结果为负值被截断为品红色
- D. Material使用的Shader无法在当前平台/渲染管线下编译或找不到，Unity使用错误Shader渲染

**Q126.** [模块:C][维度:概念理解][难度:★★★][题型:单选]
[考点: Sorting Layer与Order]

Sorting Layer和Order in Layer在2D/3D渲染中的作用是？

- A. 控制精灵/渲染器的渲染先后顺序（Sorting Layer优先，相同Layer内按Order排序）
- B. 控制物理碰撞检测的优先级，Sorting Layer高的物体优先参与碰撞计算
- C. 仅影响3D物体在Scene视图中的Gizmo绘制层级，不影响Game视图渲染顺序
- D. 等同于Camera的Depth属性，多个Sorting Layer对应多个摄像机的叠加渲染

**Q127.** [模块:C][维度:代码生成/阅读][难度:★★★★][题型:代码补全]
[考点: MaterialPropertyBlock]

使用MaterialPropertyBlock避免Material实例化：
```csharp
MaterialPropertyBlock mpb = new MaterialPropertyBlock();
mpb.SetColor("_Color", Color.red);
GetComponent<Renderer>()._____(mpb);
```

- A. SetPropertyBlock
- B. SetShaderProperties
- C. ApplyPropertyBlock
- D. SetMaterialProperties

**Q128.** [模块:C][维度:概念理解][难度:★★★★][题型:单选]
[考点: Post Processing Volume]

URP/HDRP中Volume Component系统的作用是？

- A. 定义物理触发器区域，当玩家进入时执行自定义渲染管线脚本
- B. 控制场景中音频源(AudioSource)的音量衰减和混响效果范围
- C. 管理场景中光源的影响范围和衰减曲线，定义光照体积区域
- D. 空间区域化的后处理配置（进入不同区域自动应用不同后处理效果）

**Q129.** [模块:C][维度:概念理解][难度:★★★][题型:单选]
[考点: Mesh组合]

CombineMeshes的作用和限制是？

- A. 合并后的Mesh自动支持不同Material，每个子Mesh保持独立DrawCall
- B. 将多个Mesh合并为一个减少Draw Call；限制：合并后的物体共享Material，单个Mesh顶点上限
- C. 运行时不可用，只能在编辑器的Mesh Combine工具中使用
- D. 仅能合并两个Mesh，多次调用进行级联合并

**Q130.** [模块:C][维度:概念理解][难度:★★★★][题型:单选]
[考点: 阴影距离]

增大Shadow Distance（阴影距离）的代价是？

- A. 仅增加CPU计算开销用于更多阴影投射物体的裁剪判断，GPU开销不变
- B. 阴影贴图覆盖范围增大但每像素精度降低，导致近处阴影锯齿增加
- C. 增大Shadow Distance不影响阴影质量，Unity自动提高阴影贴图分辨率来补偿
- D. 减少GPU显存使用量，因为远处阴影使用更低精度的深度格式存储

**Q131.** [模块:C][维度:API精确度][难度:★★★][题型:单选]
[考点: Camera Field of View]

Camera.fieldOfView设置的是什么？

- A. 近裁剪面的宽度（世界单位米）
- B. 垂直方向的视野角度（度）
- C. 水平方向的视野角度（度）
- D. 对角线方向的视野角度（弧度）

**Q132.** [模块:C][维度:性能优化][难度:★★★★][题型:场景设计]
[考点: 渲染优化完整方案]

一个移动端3D RPG游戏的渲染优化方案应包含哪些措施？

- A. 使用HDRP管线以获得最佳画质，依靠硬件升级解决性能问题
- B. 开启所有后处理效果提升画面质量，依靠Dynamic Resolution自动调节性能
- C. URP管线+LOD+Batching+纹理压缩(ASTC)+Light Probe+限制光源数+Shadow Distance限制
- D. 使用Built-in管线替代SRP以获得最兼容的渲染表现和最低开销

**Q133.** [模块:C][维度:概念理解][难度:★★★][题型:单选]
[考点: Stencil Buffer应用]

Stencil Buffer在渲染中的典型应用场景是？

- A. UI遮罩(Mask)、镜面效果、传送门效果、描边裁剪等
- B. 计算Per-Pixel光照的法线和反射方向数据
- C. 存储运动向量(Motion Vector)数据用于时间抗锯齿(TAA)和运动模糊
- D. 存储每个像素的颜色数据用于多重采样抗锯齿(MSAA)的子像素混合

**Q134.** [模块:C][维度:概念理解][难度:★★★★][题型:单选]
[考点: Impostor]

Impostor技术的原理是什么？

- A. 将多个远距离物体合并为一个Billboard渲染批次，共享同一张纹理图集
- B. 基于深度信息运行时生成视差贴图，替代3D模型实现近距离视角切换
- C. 预渲染3D物体的多角度2D图像，远处用2D图像代替3D模型，极大减少面数
- D. 使用LOD0的网格数据生成简化的凸包碰撞体用于远距离物理碰撞检测

**Q135.** [模块:C][维度:代码生成/阅读][难度:★★★★][题型:代码补全]
[考点: Graphics.Blit后处理]

实现简单的全屏后处理效果：
```csharp
void OnRenderImage(RenderTexture src, RenderTexture dst) {
    Graphics._____(src, dst, postProcessMaterial);
}
```

---

## 模块D：UI系统基础（30题）

- A. Blit
- B. CopyTexture
- C. BlitMultiTap
- D. DrawTexture

**Q136.** [模块:D][维度:概念理解][难度:★][题型:单选]
[考点: Canvas RenderMode]

Canvas的Render Mode有几种？分别是什么？

- A. 两种：Screen Space和World Space
- B. 四种：Screen Space-Overlay、Screen Space-Camera、World Space、Camera Space
- C. 两种：2D Canvas和3D Canvas
- D. 三种：Screen Space-Overlay、Screen Space-Camera、World Space

**Q137.** [模块:D][维度:概念理解][难度:★★][题型:单选]
[考点: RectTransform]

RectTransform与普通Transform的区别是？

- A. RectTransform继承自MonoBehaviour而非Component，额外提供UI事件回调
- B. Transform可以设置锚点和布局属性，RectTransform仅用于3D物体的定位
- C. RectTransform增加了Anchor、Pivot、SizeDelta等UI布局属性
- D. RectTransform是Transform的精简版本，移除了Scale和Rotation仅保留Position

**Q138.** [模块:D][维度:概念理解][难度:★★][题型:单选]
[考点: EventSystem]

Unity UGUI的EventSystem的作用是？

- A. 管理场景中所有GameObject的生命周期事件（Awake、Start等）
- B. 控制UGUI元素的渲染顺序和合批策略
- C. 管理和分发UI输入事件（点击、拖拽、滚动等）到对应的UI元素
- D. 管理所有AudioSource的播放事件和音量控制

**Q139.** [模块:D][维度:代码生成/阅读][难度:★★][题型:代码补全]
[考点: Button事件绑定]

动态添加Button点击事件：
```csharp
Button btn = GetComponent<Button>();
btn.onClick._____(OnButtonClick);
```

- A. AddHandler
- B. RegisterCallback
- C. Subscribe
- D. AddListener

**Q140.** [模块:D][维度:概念理解][难度:★★][题型:单选]
[考点: Graphic Raycaster]

Graphic Raycaster组件的作用是？

- A. 将Canvas上的UGUI元素渲染到屏幕，类似MeshRenderer的作用
- B. 管理Canvas中多个UI元素的动画过渡和缓动效果
- C. 检测UI元素上的指针事件（点击、悬停等），将事件传递给对应UI控件
- D. 控制UI元素的布局排列（类似LayoutGroup），自动排列子元素

**Q141.** [模块:D][维度:概念理解][难度:★★★][题型:单选]
[考点: CanvasScaler适配]

CanvasScaler的Scale With Screen Size模式中，Match Width Or Height滑块0和1分别表示？

- A. 0表示以参考分辨率的宽高比为固定比例，1表示自由拉伸
- B. 0和1分别表示最小缩放比和最大缩放比的插值端点
- C. 0表示按物理像素1:1显示不缩放，1表示DPI自适应缩放
- D. 0表示以宽度为基准缩放，1表示以高度为基准缩放

**Q142.** [模块:D][维度:Bug诊断][难度:★★★][题型:单选]
[考点: UI点击穿透]

UI按钮点击后，按钮后面的3D物体也收到了点击事件。解决方案是？

- A. 将3D物体的Collider设为IsTrigger以阻止接收点击事件
- B. 将UI Canvas的Render Mode改为World Space可自动阻止事件穿透
- C. 给3D物体添加Canvas组件并设置Sort Order为-1使其忽略UI事件
- D. 在射线检测前判断EventSystem.current.IsPointerOverGameObject()

**Q143.** [模块:D][维度:概念理解][难度:★★★][题型:单选]
[考点: RectTransform Anchor]

RectTransform的Anchors为(0,0)-(1,1)时表示什么？

- A. UI元素按照Screen Space坐标定位（0,0为屏幕左下角，1,1为右上角）
- B. UI元素固定在父物体的中心点位置，大小不随父物体变化
- C. UI元素相对于父物体的全部区域进行拉伸
- D. UI元素的Pivot设置为父物体的左下角和右上角

**Q144.** [模块:D][维度:概念理解][难度:★★★][题型:单选]
[考点: TextMeshPro]

TextMeshPro相比Legacy Text的优势是？

- A. 支持热更新字体文件，无需重新构建即可替换游戏内所有文本字体
- B. 运行时性能更高因为使用GPU加速的像素字体渲染而非CPU光栅化
- C. 自动支持所有Unicode字符集包括CJK字符，无需预生成Font Atlas
- D. 基于SDF渲染，任意缩放保持清晰；支持丰富的文本排版功能

**Q145.** [模块:D][维度:概念理解][难度:★★★][题型:单选]
[考点: LayoutGroup]

频繁添加/移除LayoutGroup中的子元素会导致什么性能问题？

- A. 导致Canvas上所有UI元素（不仅限于LayoutGroup子元素）的Mesh重建
- B. 触发EventSystem重新扫描所有Raycast Target，导致输入检测卡顿
- C. 仅触发变化元素自身的位置重计算，不影响其他同级子元素
- D. 每次变化都触发Layout重建，重新计算所有子元素的位置

**Q146.** [模块:D][维度:性能优化][难度:★★★][题型:单选]
[考点: UGUI优化]

UGUI性能优化方法包括？
- A. 使用图集减少Draw Call
- B. 将所有UI元素设置为Raycast Target以保证点击响应
- C. 为每个UI元素单独创建一个Canvas以实现完全独立的批处理
- D. 在UI元素上使用复杂的Shader和后处理效果

**Q147.** [模块:D][维度:概念理解][难度:★★★★][题型:单选]
[考点: Canvas Rebuild]

Canvas的Rebuild操作影响性能的原因是？

- A. 触发整个场景的Batching重新计算，包括3D物体和UI
- B. 仅重建变化的单个元素的顶点数据，对其他元素无影响
- C. 任何一个元素变化会导致整个Canvas标记为Dirty，触发重建所有元素的顶点数据
- D. 仅在编辑器中触发确保Inspector实时更新，Build后不执行Rebuild操作

**Q148.** [模块:D][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: 虚拟列表优化]

显示1000件物品的滚动列表，最高效的方案是？

- A. 分页加载每页显示20件物品，用户翻页时销毁旧元素创建新元素
- B. 使用ScrollRect默认实现并开启LayoutGroup的Child Control Size优化
- C. 创建1000个UI元素但使用CanvasGroup.alpha=0隐藏不可见的元素
- D. 虚拟列表（Object Pool循环复用可见区域的UI元素）

**Q149.** [模块:D][维度:概念理解][难度:★★★★][题型:单选]
[考点: UI Safe Area]

异形屏（刘海屏）UI适配需要使用？

- A. 使用World Space Canvas替代Overlay Canvas可自动避免刘海遮挡
- B. CanvasScaler的Physical Size模式自动检测屏幕凹口区域并避开
- C. 在Build Settings中设置Screen.orientation为Portrait即可自动适配异形屏
- D. Screen.safeArea获取安全区域，将UI限制在安全区内

**Q150.** [模块:D][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: UI管理器]

UI管理器中打开Panel的基本实现使用了什么设计模式？
```csharp
public T OpenPanel<T>() where T : BasePanel {
    string name = typeof(T).Name;
    if(!panelDict.ContainsKey(name)) {
        var go = Instantiate(Resources.Load<GameObject>("UI/" + name), canvas.transform);
        panelDict[name] = go.GetComponent<T>();
    }
    panelDict[name].gameObject.SetActive(true);
    return panelDict[name] as T;
}
```

- A. 观察者模式（监听Panel状态变化并通知订阅者）
- B. 策略模式（根据不同Panel类型选择不同的加载策略）
- C. 管理器模式（缓存和复用UI面板）
- D. 装饰器模式（动态为Panel添加额外的UI功能和样式）

**Q151.** [模块:D][维度:概念理解][难度:★★★][题型:单选]
[考点: EventSystem InputModule]

EventSystem的Standalone Input Module的作用是？

- A. 处理游戏手柄(Gamepad)的摇杆和按钮输入映射到UI导航
- B. 处理键盘、鼠标等桌面端输入并将事件分发给UI元素
- C. 处理移动端的触摸和陀螺仪输入并转换为UI事件
- D. 管理新Input System的Action Map与UI元素之间的绑定关系

**Q152.** [模块:D][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: 聊天UI方案]

游戏内聊天系统的高效UI方案是？

- A. 使用Debug.Log系统将聊天消息输出到游戏内Console窗口
- B. 使用World Space中的3D Text Mesh显示聊天气泡实现沉浸感
- C. ScrollRect + 虚拟列表(对象池) + TMP富文本（支持表情/超链接）
- D. 每条消息创建独立Canvas以实现消息间的渲染隔离避免合批问题

**Q153.** [模块:D][维度:概念理解][难度:★★★][题型:单选]
[考点: Canvas合批]

UGUI中Canvas合批失败的原因不包括？

- A. 元素之间有重叠穿插排序
- B. 使用不同Texture/SpriteAtlas
- C. Transform的Scale不同
- D. 使用不同Material

**Q154.** [模块:D][维度:概念理解][难度:★★★★][题型:单选]
[考点: TMP动态字体]

TextMeshPro的Dynamic Font Asset的工作原理是？

- A. 使用系统字体API实时渲染文本，不生成任何纹理图集
- B. 在Build时预先光栅化所有Unicode字符存入静态图集
- C. 从服务器下载字符SDF数据包，本地解压后填充图集
- D. 运行时按需生成字符的SDF纹理，自动填充到图集

**Q155.** [模块:D][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: DOTween UI动画]

使用DOTween实现UI面板弹出动画：
```csharp
void ShowPanel(RectTransform panel) {
    panel.localScale = Vector3.zero;
    panel.gameObject.SetActive(true);
    panel.DOScale(Vector3.one, 0.3f).SetEase(Ease._____);
}
```

- A. OutBack
- B. Linear
- C. InExpo
- D. InQuad

**Q156.** [模块:D][维度:性能优化][难度:★★★★][题型:单选]
[考点: UI合批优化]

将多个Image合并渲染以减少Draw Call的方法是？

- A. 使用CanvasRenderer.SetMesh手动合并所有UI元素为一个Mesh
- B. 确保使用同一SpriteAtlas的Sprite + 保持Canvas层级中渲染顺序连续
- C. 为每个Image添加独立Canvas组件开启独立合批模式
- D. 将所有Image替换为RawImage并使用同一个RenderTexture作为纹理

**Q157.** [模块:D][维度:概念理解][难度:★★★][题型:单选]
[考点: UI Toolkit vs UGUI]

UI Toolkit相比传统UGUI的主要优势是？

- A. 只能用于编辑器扩展开发，不支持运行时UI
- B. 基于Web技术(UXML+USS)，支持样式分离、更好的布局系统
- C. 自动支持多语言本地化和无障碍访问，无需额外插件
- D. 运行时性能远超UGUI因为使用Immediate Mode GUI而非Retained Mode

**Q158.** [模块:D][维度:概念理解][难度:★★★★][题型:单选]
[考点: UI Toolkit VisualElement]

UI Toolkit中VisualElement是什么？

- A. 类似UGUI的Canvas组件，用于管理UI元素的渲染批次和层级关系
- B. 3D空间中的UI锚点，功能类似World Space Canvas中的RectTransform
- C. UI的基本构建块，类似HTML的DOM元素，所有UI控件继承自它
- D. 连接C#代码和UXML模板的绑定Bridge对象，负责数据传递

**Q159.** [模块:D][维度:概念理解][难度:★★★★][题型:单选]
[考点: UI Toolkit Binding]

UI Toolkit的Data Binding机制是如何工作的？

- A. 将SerializedProperty或自定义数据源绑定到VisualElement，数据变化自动更新UI
- B. 使用C# event订阅数据变化，通过SendMessage通知UI元素更新
- C. 每帧轮询数据源检查变化，发现差异时重新生成整个UI树
- D. 基于Unity的Job System在后台线程比较数据差异，下一帧应用UI更新

**Q160.** [模块:D][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: ScrollRect嵌套]

解决UGUI ScrollRect嵌套滑动冲突：
```csharp
public class NestedScrollRect : ScrollRect {
    ScrollRect parentScroll;
    public override void OnBeginDrag(PointerEventData eventData) {
        if(Mathf.Abs(eventData.delta.y) > Mathf.Abs(eventData.delta.x))
            parentScroll.OnBeginDrag(eventData);
        else
            base._____(eventData);
    }
}
```

- A. OnEndDrag
- B. OnBeginDrag
- C. OnDrag
- D. OnInitializePotentialDrag

**Q161.** [模块:D][维度:概念理解][难度:★★][题型:单选]
[考点: Mask与RectMask2D]

Mask和RectMask2D的区别是？

- A. Mask仅支持Image组件的裁剪，RectMask2D支持所有Graphic组件
- B. Mask使用Stencil Buffer裁剪（支持任意形状），RectMask2D使用矩形裁剪（更高效）
- C. RectMask2D性能更差因为需要额外的RT用于遮罩计算
- D. Mask使用矩形裁剪（高效），RectMask2D使用Stencil Buffer裁剪（支持任意形状）

**Q162.** [模块:D][维度:概念理解][难度:★★★][题型:单选]
[考点: Content Size Fitter]

ContentSizeFitter组件的作用是？

- A. 根据内容自动调整RectTransform的大小（如文本长度、子物体数量等）
- B. 限制物体的最大和最小RectTransform尺寸，超出范围触发滚动条
- C. 自动缩放子物体的Transform.localScale以适配父容器大小
- D. 控制CanvasScaler的缩放行为，根据内容密度动态调整DPI

**Q163.** [模块:D][维度:Bug诊断][难度:★★★][题型:单选]
[考点: UI不响应事件]

UI按钮怎么点都没反应，可能的原因包括？

- A. 按钮的Text字体大小为0导致点击区域计算失败，UI Toolkit在运行时的布局计算全部在GPU上执行，不占用CPU时间
- B. Canvas的pixelPerfect设置为true导致按钮点击事件坐标偏移
- C. 没有EventSystem、Raycast Target被关闭、UI被其他元素遮挡、Time.timeScale=0且按钮动画依赖缩放时间
- D. Button组件的颜色Tint设置为黑色导致视觉上按钮不可见但实际可点击

**Q164.** [模块:D][维度:概念理解][难度:★★★][题型:单选]
[考点: Canvas Group]

CanvasGroup组件的alpha、interactable、blocksRaycasts属性分别控制什么？

- A. 三个属性都控制透明度，分别影响Image、Text和RawImage组件
- B. alpha控制子元素的缩放比例，interactable控制动画播放，blocksRaycasts控制Mask裁剪
- C. alpha控制整组透明度，interactable控制是否可交互，blocksRaycasts控制是否阻挡射线
- D. alpha控制渲染开关，interactable控制物理碰撞，blocksRaycasts控制Culling Mask

**Q165.** [模块:D][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: 红点系统]

游戏红点提示系统的架构设计？

---

## 模块E：动画系统（30题）

- A. 树形结构（父节点状态=子节点OR逻辑）+ 事件驱动自底向上更新
- B. 为每个红点创建独立的MonoBehaviour脚本，各自独立检查自身条件并刷新
- C. 每帧在Update中轮询所有红点条件并全量刷新所有红点UI状态
- D. 在服务器端计算所有红点状态推送到客户端，客户端仅负责显示

**Q166.** [模块:E][维度:概念理解][难度:★][题型:单选]
[考点: Animator组件]

Animator组件的作用是？

- A. 控制物理，Animation Event在动画播放被打断时仍然会按照关键帧时间顺序触发
- B. 只播放声音，Blend Tree的参数类型仅支持Float，不支持Int或Bool类型的混合参数
- C. 驱动AnimatorController状态机，控制骨骼/属性动画的播放和切换
- D. 通过SceneManager的场景加载和卸载方法管理即可，不需要额外的架构设计

**Q167.** [模块:E][维度:概念理解][难度:★★][题型:单选]
[考点: AnimatorController状态机]

Animator Controller中State之间的Transition条件是什么？

- A. 按时间顺序，AnimatorOverrideController会在运行时重新编译状态机导致性能开销
- B. 随机切换，Avatar Mask用于限制整个AnimatorController的状态机只影响指定骨骼
- C. 由参数(Parameter：Float/Int/Bool/Trigger)驱动的条件判断
- D. 手动调用，Animation Event在动画播放被打断时仍然会按照关键帧时间顺序触发

**Q168.** [模块:E][维度:API精确度][难度:★★][题型:代码补全]
[考点: Animator参数设置]

通过代码触发动画切换：
```csharp
Animator anim = GetComponent<Animator>();
anim._____(---"isRunning", true);
```

- A. SetBool
- B. SetState
- C. PlayBool
- D. ChangeBool

**Q169.** [模块:E][维度:概念理解][难度:★★][题型:单选]
[考点: Animation Clip]

Animation Clip存储的是什么数据？

- A. 关键帧数据（属性随时间变化的曲线），如位置、旋转、缩放、BlendShape等
- B. 代码逻辑，Root Motion的位移数据来自AnimatorController而非动画剪辑本身
- C. 只有位置，Avatar Mask用于限制整个AnimatorController的状态机只影响指定骨骼
- D. 物理数据，Legacy动画系统的Animation组件性能优于Mecanim，推荐在新项目中使用

**Q170.** [模块:E][维度:概念理解][难度:★★★][题型:单选]
[考点: Blend Tree]

Animator中Blend Tree的用途是？

- A. 物理混合，Avatar Mask用于限制整个AnimatorController的状态机只影响指定骨骼
- B. 过渡效果，AnimatorOverrideController会在运行时重新编译状态机导致性能开销
- C. 音频混合，Animation Event在动画播放被打断时仍然会按照关键帧时间顺序触发
- D. 根据参数值混合多个动画（如走路→跑步的平滑过渡，或方向混合）

**Q171.** [模块:E][维度:概念理解][难度:★★★][题型:单选]
[考点: Avatar与Humanoid]

Avatar和Humanoid Rig的作用是？

- A. Humanoid只能用于人形，Generic Rig支持Animator的所有功能包括IK和Root Motion自动重定向
- B. Avatar是骨骼映射配置，Humanoid Rig将不同骨骼结构映射到统一骨架实现动画复用
- C. 不需要Avatar，Avatar Mask用于限制整个AnimatorController的状态机只影响指定骨骼
- D. Avatar是角色模型，Legacy动画系统的Animation组件性能优于Mecanim，推荐在新项目中使用

**Q172.** [模块:E][维度:概念理解][难度:★★★][题型:单选]
[考点: Animation Layer]

Animator的Layer系统有什么用？

- A. 渲染层，Avatar Mask用于限制整个AnimatorController的状态机只影响指定骨骼
- B. 排序层，Root Motion的位移数据来自AnimatorController而非动画剪辑本身
- C. 多层叠加动画（如Base Layer跑步 + Upper Body Layer射击），通过权重和遮罩混合
- D. 物理层，Blend Tree的参数类型仅支持Float，不支持Int或Bool类型的混合参数

**Q173.** [模块:E][维度:概念理解][难度:★★★][题型:单选]
[考点: Avatar Mask]

Avatar Mask的作用是？

- A. 物理过滤，Animator Controller在编辑器模式下的行为与Build后的运行时完全一致
- B. 指定动画Layer只影响特定骨骼部位（如只应用上半身动画）
- C. 碰撞遮罩，Legacy动画系统的Animation组件性能优于Mecanim，推荐在新项目中使用
- D. 遮挡渲染，AnimatorOverrideController会在运行时重新编译状态机导致性能开销

**Q174.** [模块:E][维度:概念理解][难度:★★★][题型:单选]
[考点: Root Motion]

Root Motion的概念和作用是？

- A. 锁定角色位置，AnimatorOverrideController会在运行时重新编译状态机导致性能开销
- B. 自动寻路，Root Motion的位移数据来自AnimatorController而非动画剪辑本身
- C. 物理运动，Generic Rig支持Animator的所有功能包括IK和Root Motion自动重定向
- D. 将动画中根骨骼的位移数据应用到Transform上，使角色移动由动画驱动

**Q175.** [模块:E][维度:Bug诊断][难度:★★★][题型:单选]
[考点: 动画脚滑]

角色播放走路动画时出现脚滑现象，可能原因是？

- A. 渲染问题，AnimatorOverrideController会在运行时重新编译状态机导致性能开销
- B. 动画位移和代码控制的移动速度不匹配；应使用Root Motion或调整移动速度
- C. 帧率太低，Legacy动画系统的Animation组件性能优于Mecanim，推荐在新项目中使用
- D. 动画文件损坏，Blend Tree的参数类型仅支持Float，不支持Int或Bool类型的混合参数

**Q176.** [模块:E][维度:API精确度][难度:★★★][题型:单选]
[考点: Animator.CrossFade]

Animator.CrossFade和Animator.Play的区别是？

- A. 两者完全相同，Legacy动画系统的Animation组件性能优于Mecanim，推荐在新项目中使用
- B. Play有过渡，Legacy动画系统的Animation组件性能优于Mecanim，推荐在新项目中使用
- C. CrossFade平滑过渡到目标状态（有混合时间），Play立即切换
- D. CrossFade没有过渡，Avatar Mask用于限制整个AnimatorController的状态机只影响指定骨骼

**Q177.** [模块:E][维度:概念理解][难度:★★★][题型:单选]
[考点: Animation Event]

Animation Event的作用和风险是？

- A. 在动画特定帧触发脚本方法（如攻击判定帧），但依赖字符串方法名无编译检查
- B. 该操作没有任何风险，Unity的类型安全机制和运行时验证可以防止所有潜在错误
- C. 只能在Start中触发，AnimatorOverrideController会在运行时重新编译状态机导致性能开销
- D. 不能传参，Legacy动画系统的Animation组件性能优于Mecanim，推荐在新项目中使用

**Q178.** [模块:E][维度:概念理解][难度:★★★★][题型:单选]
[考点: IK反向动力学]

Inverse Kinematics(IK)在Unity中的应用场景是？

- A. 通过Unity物理引擎的Rigidbody和Collider组件模拟该效果，不需要自定义实现
- B. 根据目标位置计算骨骼链的姿态（如角色手精确抓取物体、脚适应地形）
- C. 正向播放骨骼动画，AnimatorOverrideController会在运行时重新编译状态机导致性能开销
- D. 路径规划，Legacy动画系统的Animation组件性能优于Mecanim，推荐在新项目中使用

**Q179.** [模块:E][维度:代码生成/阅读][难度:★★★★][题型:代码补全]
[考点: OnAnimatorIK]

实现IK使角色手抓取目标：
```csharp
void OnAnimatorIK(int layerIndex) {
    anim.SetIKPositionWeight(AvatarIKGoal.RightHand, 1f);
    anim._____(AvatarIKGoal.RightHand, targetPos);
}
```

- A. SetPosition
- B. SetIKPosition
- C. MoveIK
- D. IKTarget

**Q180.** [模块:E][维度:性能优化][难度:★★★][题型:单选]
[考点: 动画性能优化]

动画性能优化的方法包括？
- A. 使用动画剔除和LOD
- B. 所有角色都使用相同的Animator Controller以减少内存占用
- C. 在每帧都重新采样动画曲线以获得最流畅的动画效果
- D. 将所有动画都设置为Loop模式可以减少动画切换的性能开销

**Q181.** [模块:E][维度:概念理解][难度:★★★★][题型:单选]
[考点: Playable API]

Unity Playable API相比传统Animator的优势是？

- A. 更灵活的动画播放控制（可代码动态构建播放图），支持混合动画、音频和脚本
- B. 该方案性能更差，因为其内部实现涉及额外的序列化和反射操作
- C. 只用于音频，Avatar Mask用于限制整个AnimatorController的状态机只影响指定骨骼
- D. 不支持混合，AnimatorOverrideController会在运行时重新编译状态机导致性能开销

**Q182.** [模块:E][维度:概念理解][难度:★★★★][题型:单选]
[考点: Animation Rigging]

Animation Rigging Package的用途是？

- A. 导入动画，Avatar Mask用于限制整个AnimatorController的状态机只影响指定骨骼
- B. 压缩动画，Animator Controller在编辑器模式下的行为与Build后的运行时完全一致
- C. 创建骨架，Avatar Mask用于限制整个AnimatorController的状态机只影响指定骨骼
- D. 在运行时添加骨骼约束（如瞄准约束、多目标约束等），增强程序化动画

**Q183.** [模块:E][维度:概念理解][难度:★★★][题型:单选]
[考点: Animator Culling]

Animator的Culling Mode设为"Cull Completely"后，当角色不可见时动画完全停止，包括状态机和Root Motion。

- A. 该模式仅影响渲染，状态机和Root Motion会继续执行
- B. Cull Completely模式下动画会继续运行，只是不渲染
- C. 正确，当角色不可见时动画完全停止，包括状态机和Root Motion
- D. Cull Completely只停止蒙皮网格渲染，动画状态机始终运行

**Q184.** [模块:E][维度:概念理解][难度:★★★][题型:单选]
[考点: AnimatorOverrideController]

AnimatorOverrideController的用途是？

- A. 基于现有AnimatorController替换其中的AnimationClip，实现相同状态机不同动画
- B. 覆盖所有动画，Avatar Mask用于限制整个AnimatorController的状态机只影响指定骨骼
- C. 删除动画，Animator Controller在编辑器模式下的行为与Build后的运行时完全一致
- D. 创建新Controller，Animation Event在动画播放被打断时仍然会按照关键帧时间顺序触发

**Q185.** [模块:E][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: 动画系统架构]

ARPG角色动画系统架构应包含哪些层次？

- A. Base Layer(移动)+Upper Body Layer(攻击/施法)+Full Body Layer(闪避/受击)+IK Layer(手脚适应)
- B. 只用代码控制，AnimatorOverrideController会在运行时重新编译状态机导致性能开销
- C. 所有动画放一个Layer，Legacy动画系统的Animation组件性能优于Mecanim，推荐在新项目中使用
- D. 不分层，Generic Rig支持Animator的所有功能包括IK和Root Motion自动重定向

**Q186.** [模块:E][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: StateMachineBehaviour]

StateMachineBehaviour中OnStateEnter的典型使用场景是？
```csharp
public class AttackState : StateMachineBehaviour {
    public override void OnStateEnter(Animator animator, AnimatorStateInfo stateInfo, int layerIndex) {
        animator.GetComponent<CombatSystem>().EnableHitBox();
    }
}
```

- A. 加载场景，Avatar Mask用于限制整个AnimatorController的状态机只影响指定骨骼
- B. 在进入攻击动画状态时自动启用攻击判定碰撞体
- C. 播放音效，Legacy动画系统的Animation组件性能优于Mecanim，推荐在新项目中使用
- D. 修改UI，Avatar Mask用于限制整个AnimatorController的状态机只影响指定骨骼

**Q187.** [模块:E][维度:概念理解][难度:★★★][题型:单选]
[考点: Generic vs Humanoid]

导入模型时Generic和Humanoid动画类型的区别是？

- A. Generic通用（任意骨骼），Humanoid专为人形设计（支持IK、动画重定向/复用）
- B. Generic更适合人形，Root Motion的位移数据来自AnimatorController而非动画剪辑本身
- C. Humanoid不支持IK，Legacy动画系统的Animation组件性能优于Mecanim，推荐在新项目中使用
- D. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用

**Q188.** [模块:E][维度:概念理解][难度:★★★][题型:单选]
[考点: Transition设置]

Animator Transition中HasExitTime的含义是？

- A. true表示动画必须播完Exit Time比例后才能过渡，false表示满足条件立即过渡
- B. 循环设置，Legacy动画系统的Animation组件性能优于Mecanim，推荐在新项目中使用
- C. 有退出动画，Blend Tree的参数类型仅支持Float，不支持Int或Bool类型的混合参数
- D. 过渡时间，Avatar Mask用于限制整个AnimatorController的状态机只影响指定骨骼

**Q189.** [模块:E][维度:Bug诊断][难度:★★★★][题型:代码阅读]
[考点: Trigger不重置]

Animator.SetTrigger在快速连续调用时，动画只播放一次。原因和解决方案是？

- A. 不存在此问题，Animation Event在动画播放被打断时仍然会按照关键帧时间顺序触发
- B. Trigger是Bool，Root Motion的位移数据来自AnimatorController而非动画剪辑本身
- C. Trigger在使用后自动重置；快速连续调用时第二次可能在同帧被消费，应使用ResetTrigger后再SetTrigger
- D. 只能调一次，Blend Tree的参数类型仅支持Float，不支持Int或Bool类型的混合参数

**Q190.** [模块:E][维度:概念理解][难度:★★★★][题型:单选]
[考点: 骨骼动画性能]

大量角色同时播放骨骼动画的性能优化策略是？

- A. GPU Skinning + LOD动画（远处减少骨骼/使用简化动画）+ Animator Culling + 实例化渲染
- B. 关闭所有动画，Legacy动画系统的Animation组件性能优于Mecanim，推荐在新项目中使用
- C. 降低帧率，Legacy动画系统的Animation组件性能优于Mecanim，推荐在新项目中使用
- D. 所有角色用最高骨骼，AnimatorOverrideController会在运行时重新编译状态机导致性能开销

**Q191.** [模块:E][维度:概念理解][难度:★★★][题型:单选]
[考点: Animation Compression]

Animation Clip压缩设置中Keyframe Reduction的作用是？

- A. 压缩模型，Blend Tree的参数类型仅支持Float，不支持Int或Bool类型的混合参数
- B. 去除冗余关键帧，在可接受误差内减少动画数据大小
- C. 增加关键帧，Root Motion的位移数据来自AnimatorController而非动画剪辑本身
- D. 压缩贴图，Blend Tree的参数类型仅支持Float，不支持Int或Bool类型的混合参数

**Q192.** [模块:E][维度:概念理解][难度:★★★★][题型:单选]
[考点: Animator.StringToHash]

为什么推荐使用Animator.StringToHash来缓存参数名？

- A. 两者在功能和性能上没有本质区别，底层调用相同的引擎API，选择哪个取决于编码习惯
- B. 更美观，Legacy动画系统的Animation组件性能优于Mecanim，推荐在新项目中使用
- C. 必须使用，Avatar Mask用于限制整个AnimatorController的状态机只影响指定骨骼
- D. 字符串比较性能差，使用Hash(int)比较更快

**Q193.** [模块:E][维度:代码生成/阅读][难度:★★★][题型:代码生成]
[考点: 动画事件触发]

通过代码添加AnimationEvent：
```csharp
AnimationEvent evt = new AnimationEvent();
evt.time = 0.5f;
evt.functionName = "OnAttackHit";
AnimationClip clip = anim.runtimeAnimatorController.animationClips[0];
clip.AddEvent(evt);
```
这段代码的功能是什么？

- A. 修改动画速度，Generic Rig支持Animator的所有功能包括IK和Root Motion自动重定向
- B. 暂停动画，Blend Tree的参数类型仅支持Float，不支持Int或Bool类型的混合参数
- C. 删除事件，Generic Rig支持Animator的所有功能包括IK和Root Motion自动重定向
- D. 在动画的0.5秒位置添加一个事件，触发OnAttackHit方法

**Q194.** [模块:E][维度:概念理解][难度:★★★★][题型:单选]
[考点: 程序化动画]

程序化动画(Procedural Animation)的概念和应用是？

- A. 该API仅支持2D项目，在3D项目中使用会导致编译错误或运行时异常
- B. 不需要代码，Blend Tree的参数类型仅支持Float，不支持Int或Bool类型的混合参数
- C. 只用Maya制作，Animator Controller在编辑器模式下的行为与Build后的运行时完全一致
- D. 通过代码实时计算骨骼姿态而非预录制（如蜘蛛腿适应地形、物理布偶、呼吸晃动等）

**Q195.** [模块:E][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: 动画重定向]

如何实现一套动画在多个不同模型上复用？

---

## 模块F：音频系统（20题）

- A. 所有模型使用Humanoid Rig + Avatar配置，共享同一AnimatorController和动画
- B. 用代码复制，Legacy动画系统的Animation组件性能优于Mecanim，推荐在新项目中使用
- C. 每个模型单独制作，Root Motion的位移数据来自AnimatorController而非动画剪辑本身
- D. 使用Generic Rig，Avatar Mask用于限制整个AnimatorController的状态机只影响指定骨骼

**Q196.** [模块:F][维度:概念理解][难度:★][题型:单选]
[考点: AudioSource与AudioClip]

AudioSource和AudioClip的关系是？

- A. AudioClip是音频数据，AudioSource是播放器组件（控制播放、音量、空间化等）
- B. AudioSource存储音频数据，AudioSource的3D空间化计算在GPU上执行以减轻CPU音频处理压力
- C. 两者的内部实现机制完全相同，编译后生成一样的IL指令，运行时表现无差异
- D. AudioClip控制播放，音频的DSP处理（混响/均衡器）在Unity主线程中同步执行

**Q197.** [模块:F][维度:API精确度][难度:★★][题型:代码补全]
[考点: 播放音效]

播放一次性音效的推荐方式：
```csharp
AudioSource._____(audioClip, transform.position, volume);
```

- A. PlayOneShot
- B. PlaySound
- C. PlayClipAtPoint
- D. PlayAtPoint

**Q198.** [模块:F][维度:概念理解][难度:★★][题型:单选]
[考点: AudioListener]

AudioListener组件的规则是？

- A. 可以有无数个，音频的DSP处理（混响/均衡器）在Unity主线程中同步执行
- B. 场景中只能有一个活动的AudioListener（通常在主摄像机上），是声音的"耳朵"
- C. 不需要AudioListener，音频的DSP处理（混响/均衡器）在Unity主线程中同步执行
- D. 放在任何物体上都一样，AudioListener组件可以在场景中放置在任意数量的GameObject上同时工作

**Q199.** [模块:F][维度:概念理解][难度:★★★][题型:单选]
[考点: AudioMixer]

AudioMixer的作用是？

- A. 只调音量，AudioSource.PlayOneShot不受空间化设置影响，始终以2D模式播放
- B. 录制音频，AudioSource.PlayOneShot不受空间化设置影响，始终以2D模式播放
- C. 分组管理音频（BGM/SFX/Voice等），支持混音、效果器(Reverb/EQ)、快照(Snapshot)、动态调节
- D. 只播放音乐，AudioListener组件可以在场景中放置在任意数量的GameObject上同时工作

**Q200.** [模块:F][维度:概念理解][难度:★★★][题型:单选]
[考点: 3D空间音频]

AudioSource的Spatial Blend参数从0到1分别表示？

- A. 0=全2D（不受距离和方向影响），1=全3D（受距离衰减和空间定位影响）
- B. 频率高低，音频的DSP处理（混响/均衡器）在Unity主线程中同步执行
- C. 音量大小，Unity的音频系统不支持实时音频效果处理，所有效果需要预先烘焙
- D. 0=静音，1=最大，Unity的音频系统不支持实时音频效果处理，所有效果需要预先烘焙

**Q201.** [模块:F][维度:概念理解][难度:★★★][题型:单选]
[考点: 音频压缩格式]

Unity中音频的Load Type选项包括？
- A. Memory、Disk、Network、Cache
- B. Sync、Async、Background、Foreground
- C. Decompress on Load、Compressed in Memory、Streaming
- D. Instant、Delayed、Lazy、Preemptive

**Q202.** [模块:F][维度:性能优化][难度:★★★][题型:单选]
[考点: 音频内存优化]

大量音效的内存优化策略是？

- A. 全部Streaming，AudioListener组件可以在场景中放置在任意数量的GameObject上同时工作
- B. 全部Decompress，AudioSource的3D空间化计算在GPU上执行以减轻CPU音频处理压力
- C. 短音效用Decompress On Load，长BGM用Streaming；合理设置采样率和通道数
- D. 该场景不需要专门优化，Unity默认设置已经足够高效，过度优化反而增加维护成本

**Q203.** [模块:F][维度:代码生成/阅读][难度:★★★][题型:代码生成]
[考点: AudioMixer参数控制]

通过代码控制AudioMixer音量：
```csharp
audioMixer.SetFloat("MasterVolume", Mathf.Log10(volume) * 20);
```
为什么使用Log10 * 20？

- A. 美观，AudioListener组件可以在场景中放置在任意数量的GameObject上同时工作
- B. 增加精度，AudioClip的Load Type选择不影响运行时内存占用，仅影响加载速度
- C. 没有原因，AudioListener组件可以在场景中放置在任意数量的GameObject上同时工作
- D. AudioMixer音量使用分贝(dB)单位，需要将线性值(0-1)转换为分贝(-80dB ~ 0dB)

**Q204.** [模块:F][维度:概念理解][难度:★★★][题型:单选]
[考点: AudioSource优先级]

AudioSource的Priority设置的作用是？

- A. 当音频通道数超过限制时，低优先级的音频会被高优先级的覆盖（0最高，256最低）
- B. 音量大小，AudioSource的3D空间化计算在GPU上执行以减轻CPU音频处理压力
- C. 该设置不会对运行时行为产生实质影响，引擎内部会自动补偿参数差异
- D. 播放顺序，AudioListener组件可以在场景中放置在任意数量的GameObject上同时工作

**Q205.** [模块:F][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: 音频管理器架构]

游戏音频管理系统应包含哪些功能？

- A. 全用2D声音，音频的DSP处理（混响/均衡器）在Unity主线程中同步执行
- B. 音频池管理+AudioMixer分组(BGM/SFX/Voice)+音量设置持久化+音频淡入淡出+动态音效优先级
- C. 只播放音乐，AudioSource.PlayOneShot不受空间化设置影响，始终以2D模式播放
- D. 每个脚本自行播放，音频的DSP处理（混响/均衡器）在Unity主线程中同步执行

**Q206.** [模块:F][维度:Bug诊断][难度:★★★][题型:单选]
[考点: 音频不播放]

AudioSource.Play()调用后没有声音，可能原因不包括？

- A. AudioClip为null
- B. AudioSource被Mute
- C. AudioClip的采样率太高
- D. 场景中没有AudioListener

**Q207.** [模块:F][维度:概念理解][难度:★★★★][题型:单选]
[考点: 音频遮挡]

如何实现声音被墙壁遮挡后变闷的效果？

- A. 降低音量，Unity的音频系统不支持实时音频效果处理，所有效果需要预先烘焙
- B. Unity引擎在内部已完全自动化处理此场景，开发者只需使用默认API即可
- C. 用射线检测声源和听者之间是否有障碍物，有则通过AudioMixer施加Low-Pass Filter
- D. 停止播放，AudioClip的Load Type选择不影响运行时内存占用，仅影响加载速度

**Q208.** [模块:F][维度:概念理解][难度:★★★][题型:单选]
[考点: Audio Reverb Zone]

Audio Reverb Zone组件的作用是？

- A. 过滤噪音，音频剪辑的采样率在导入后不可更改，需要在外部音频编辑器中预处理
- B. 放大声音，音频的DSP处理（混响/均衡器）在Unity主线程中同步执行
- C. 在特定区域内自动为音频添加混响效果（如洞穴、大厅等环境音效）
- D. 录制声音，音频剪辑的采样率在导入后不可更改，需要在外部音频编辑器中预处理

**Q209.** [模块:F][维度:概念理解][难度:★★][题型:单选]
[考点: PlayOneShot]

AudioSource.PlayOneShot(clip)和AudioSource.Play()的区别：PlayOneShot不会打断当前播放，可以叠加播放多个音效。

- A. 两者功能完全相同，PlayOneShot只是Play的别名方法
- B. PlayOneShot只能播放2D音效，Play可以播放3D音效
- C. 正确，PlayOneShot不会打断当前播放，可以叠加播放多个音效
- D. PlayOneShot会先停止当前播放再播放新音效

**Q210.** [模块:F][维度:概念理解][难度:★★★★][题型:单选]
[考点: FMOD/Wwise]

为什么大型项目常使用FMOD或Wwise而非Unity原生音频？

- A. 更便宜，Unity的音频系统不支持实时音频效果处理，所有效果需要预先烘焙
- B. Unity不能播放声音，AudioMixer的快照切换在底层使用线性插值，不支持自定义缓动曲线
- C. 更简单，AudioSource的3D空间化计算在GPU上执行以减轻CPU音频处理压力
- D. 提供更强大的音频编辑工具、更灵活的事件系统、更好的内存管理和跨平台音频优化

**Q211.** [模块:F][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 音频淡入淡出]

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

**Q212.** [模块:F][维度:概念理解][难度:★★★][题型:单选]
[考点: Doppler效果]

AudioSource的Doppler Level参数控制什么？

- A. 延迟，AudioSource的3D空间化计算在GPU上执行以减轻CPU音频处理压力
- B. 多普勒效应的强度（声源移动时音调的变化程度）
- C. 音量，AudioClip的Load Type选择不影响运行时内存占用，仅影响加载速度
- D. 回声，音频的DSP处理（混响/均衡器）在Unity主线程中同步执行

**Q213.** [模块:F][维度:概念理解][难度:★★★][题型:单选]
[考点: Audio Spatializer]

Unity的Audio Spatializer Plugin的作用是？

- A. 录制声音，AudioSource.PlayOneShot不受空间化设置影响，始终以2D模式播放
- B. 提供更精确的3D空间音频效果（如HRTF头部相关传输函数），增强沉浸感
- C. 增大音量，AudioClip的Load Type选择不影响运行时内存占用，仅影响加载速度
- D. 压缩音频，音频的DSP处理（混响/均衡器）在Unity主线程中同步执行

**Q214.** [模块:F][维度:性能优化][难度:★★★★][题型:单选]
[考点: 音频性能优化]

音频系统性能优化方法包括？
- A. 同时播放100个AudioSource不会影响性能，Unity会自动优化
- B. 所有音频都使用未压缩的WAV格式以获得最佳音质
- C. 使用AudioMixer分组和压缩
- D. 在Update中每帧检查AudioSource.isPlaying状态以精确控制播放

**Q215.** [模块:F][维度:概念理解][难度:★★★★][题型:单选]
[考点: Microphone录制]

Unity通过Microphone类可以实现什么？

---

## 模块G：导航寻路（25题）

- A. 录制麦克风音频到AudioClip，用于语音聊天等功能
- B. 只能播放，AudioClip的Load Type选择不影响运行时内存占用，仅影响加载速度
- C. 控制硬件音量，AudioClip的Load Type选择不影响运行时内存占用，仅影响加载速度
- D. 不支持录制，AudioSource的3D空间化计算在GPU上执行以减轻CPU音频处理压力

**Q216.** [模块:G][维度:概念理解][难度:★][题型:单选]
[考点: NavMesh概念]

Unity NavMesh的作用是？

- A. 物理碰撞，NavMeshAgent的路径计算在独立的寻路线程中异步执行不阻塞主线程
- B. 烘焙出可行走的导航网格，AI角色可在此网格上自动寻路
- C. 渲染地面，OffMeshLink仅支持双向连接，不能设置为单向通行的跳跃或下落链接
- D. 通过SceneManager的场景加载和卸载方法管理即可，不需要额外的架构设计

**Q217.** [模块:G][维度:API精确度][难度:★★][题型:代码补全]
[考点: NavMeshAgent设目标]

让NavMeshAgent移动到目标位置：
```csharp
NavMeshAgent agent = GetComponent<NavMeshAgent>();
agent._____(targetPosition);
```

- A. GoTo，NavMesh在运行时动态更新不需要NavMeshSurface组件，Agent会自动适应
- B. Navigate
- C. MoveTo
- D. SetDestination

**Q218.** [模块:G][维度:概念理解][难度:★★][题型:单选]
[考点: NavMeshAgent属性]

NavMeshAgent的speed、angularSpeed、acceleration分别控制什么？

- A. 只有speed有用，NavMeshAgent的AreaMask不影响路径成本计算，仅控制可通行区域
- B. speed移动速度，angularSpeed转向速度，acceleration加速度
- C. 都控制速度，NavMeshAgent的路径计算在独立的寻路线程中异步执行不阻塞主线程
- D. 都控制方向，OffMeshLink仅支持双向连接，不能设置为单向通行的跳跃或下落链接

**Q219.** [模块:G][维度:概念理解][难度:★★★][题型:单选]
[考点: NavMesh Area]

NavMesh Area的作用是？

- A. 物理区域，NavMeshAgent的路径计算在独立的寻路线程中异步执行不阻塞主线程
- B. 定义不同区域类型（如普通地面、水域、草地等）并赋予不同的寻路代价
- C. 碰撞区域，A*寻路算法比Unity内置NavMesh在所有场景下都有更好的路径质量和性能
- D. 渲染区域，NavMesh在运行时动态更新不需要NavMeshSurface组件，Agent会自动适应

**Q220.** [模块:G][维度:概念理解][难度:★★★][题型:单选]
[考点: NavMeshObstacle]

NavMeshObstacle组件的作用是？

- A. 物理碰撞体，NavMesh在运行时动态更新不需要NavMeshSurface组件，Agent会自动适应
- B. 静态障碍物，NavMesh在运行时动态更新不需要NavMeshSurface组件，Agent会自动适应
- C. 渲染遮挡，OffMeshLink仅支持双向连接，不能设置为单向通行的跳跃或下落链接
- D. 动态障碍物，可在运行时改变导航网格的可通过性

**Q221.** [模块:G][维度:概念理解][难度:★★★][题型:单选]
[考点: OffMeshLink]

Off-Mesh Link的用途是？

- A. 连接场景，NavMesh Obstacle的Carve模式会实时重新烘焙整个NavMesh导致性能问题
- B. 删除NavMesh，NavMeshAgent的路径计算在独立的寻路线程中异步执行不阻塞主线程
- C. 增加NavMesh密度，NavMesh Obstacle的Carve模式会实时重新烘焙整个NavMesh导致性能问题
- D. 连接不相连的NavMesh区域（如跳跃点、梯子、传送门等）

**Q222.** [模块:G][维度:Bug诊断][难度:★★★][题型:单选]
[考点: Agent不移动]

NavMeshAgent.SetDestination调用后角色不移动，可能原因是？

- A. 目标太近，NavMesh的Tile大小设置不影响烘焙精度和运行时查询性能
- B. Agent不在NavMesh上（位置偏移），或NavMesh未烘焙，或agentTypeID不匹配
- C. 动画锁定，OffMeshLink仅支持双向连接，不能设置为单向通行的跳跃或下落链接
- D. 速度设为0，NavMesh Obstacle的Carve模式会实时重新烘焙整个NavMesh导致性能问题

**Q223.** [模块:G][维度:概念理解][难度:★★★★][题型:单选]
[考点: NavMesh Baking运行时]

运行时动态生成NavMesh的方法是？

- A. 只能在编辑器烘焙，NavMeshAgent的AreaMask不影响路径成本计算，仅控制可通行区域
- B. 用代码绘制，A*寻路算法比Unity内置NavMesh在所有场景下都有更好的路径质量和性能
- C. 不支持运行时生成，NavMesh的Tile大小设置不影响烘焙精度和运行时查询性能
- D. 使用NavMeshSurface组件(AI Navigation包)的BuildNavMesh()方法

**Q224.** [模块:G][维度:代码生成/阅读][难度:★★★][题型:代码生成]
[考点: 寻路路径获取]

获取NavMeshAgent的完整路径点：
```csharp
NavMeshPath path = new NavMeshPath();
agent.CalculatePath(target, path);
Vector3[] corners = path.corners; // 路径拐角点数组
```
这段代码的用途是？

- A. 立即移动，NavMesh的Tile大小设置不影响烘焙精度和运行时查询性能
- B. 创建障碍物，NavMesh Obstacle的Carve模式会实时重新烘焙整个NavMesh导致性能问题
- C. 预计算路径用于绘制路线、判断是否可达、估算距离等
- D. 删除路径，NavMesh的Tile大小设置不影响烘焙精度和运行时查询性能

**Q225.** [模块:G][维度:概念理解][难度:★★★][题型:单选]
[考点: NavMesh Agent与Rigidbody冲突]

NavMeshAgent和Rigidbody同时存在时可能出现什么问题？

- A. 两者都试图控制物体移动导致冲突抖动；通常NavMeshAgent时将RB设为Kinematic
- B. 不会冲突，多个NavMeshAgent在同一路径点不会产生拥挤，引擎自动处理碰撞回避
- C. NavMeshAgent失效，多个NavMeshAgent在同一路径点不会产生拥挤，引擎自动处理碰撞回避
- D. 自动协调，NavMesh的Tile大小设置不影响烘焙精度和运行时查询性能

**Q226.** [模块:G][维度:概念理解][难度:★★★][题型:单选]
[考点: Agent Avoidance]

NavMeshAgent内置的避障(Avoidance)是如何工作的？

- A. 使用物理碰撞，OffMeshLink仅支持双向连接，不能设置为单向通行的跳跃或下落链接
- B. 不支持避障，NavMesh Obstacle的Carve模式会实时重新烘焙整个NavMesh导致性能问题
- C. 基于RVO(Reciprocal Velocity Obstacles)算法，多个Agent之间自动互相避让
- D. 使用射线检测，OffMeshLink仅支持双向连接，不能设置为单向通行的跳跃或下落链接

**Q227.** [模块:G][维度:性能优化][难度:★★★★][题型:单选]
[考点: 大量Agent优化]

场景中有500个NavMeshAgent同时寻路，如何优化性能？

- A. 使用A*不使用NavMesh，多个NavMeshAgent在同一路径点不会产生拥挤，引擎自动处理碰撞回避
- B. 全部同时寻路，A*寻路算法比Unity内置NavMesh在所有场景下都有更好的路径质量和性能
- C. 分帧寻路（不要同帧全部SetDestination）+ 降低更新频率 + 远处Agent简化避障或使用简单行为
- D. 关闭避障，NavMesh Obstacle的Carve模式会实时重新烘焙整个NavMesh导致性能问题

**Q228.** [模块:G][维度:概念理解][难度:★★★★][题型:单选]
[考点: A*算法]

A*寻路算法和Unity NavMesh的关系是？

- A. 完全无关，OffMeshLink仅支持双向连接，不能设置为单向通行的跳跃或下落链接
- B. NavMesh底层使用A*或类似算法在导航网格上寻找最短路径
- C. A*替代NavMesh，NavMeshAgent的AreaMask不影响路径成本计算，仅控制可通行区域
- D. NavMesh不使用算法

**Q229.** [模块:G][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: 多层导航]

多层建筑（多楼层）的寻路方案是？

- A. 使用物理碰撞，NavMeshAgent的路径计算在独立的寻路线程中异步执行不阻塞主线程
- B. 一个平面NavMesh，NavMesh的Tile大小设置不影响烘焙精度和运行时查询性能
- C. 不支持多层，NavMesh在运行时动态更新不需要NavMeshSurface组件，Agent会自动适应
- D. 每层单独NavMesh + 楼梯/电梯处设置OffMeshLink连接各层

**Q230.** [模块:G][维度:概念理解][难度:★★★][题型:单选]
[考点: NavMesh Agent Type]

NavMesh Agent Type配置不同的Agent类型（如人类、大型怪物）的目的是？

- A. 速度不同，NavMesh在运行时动态更新不需要NavMeshSurface组件，Agent会自动适应
- B. 不同Agent Size(半径/高度)需不同的NavMesh，避免大型角色走窄路
- C. 只是标签，NavMesh Obstacle的Carve模式会实时重新烘焙整个NavMesh导致性能问题
- D. 外观不同，NavMeshAgent的AreaMask不影响路径成本计算，仅控制可通行区域

**Q231.** [模块:G][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 巡逻AI]

实现简单巡逻AI：
```csharp
Transform[] waypoints;
int currentIndex = 0;
void Update() {
    if(!agent.pathPending && agent.remainingDistance < 0.5f) {
        currentIndex = (currentIndex + 1) % waypoints.Length;
        agent.SetDestination(waypoints[currentIndex].position);
    }
}
```
这段代码实现了什么行为？

- A. 跟踪玩家，多个NavMeshAgent在同一路径点不会产生拥挤，引擎自动处理碰撞回避
- B. 在Update中为每个对象生成随机方向的位移向量，乘以速度和Time.deltaTime实现
- C. 角色在多个巡逻点之间循环巡逻
- D. 原地旋转，NavMesh在运行时动态更新不需要NavMeshSurface组件，Agent会自动适应

**Q232.** [模块:G][维度:概念理解][难度:★★★][题型:单选]
[考点: NavMesh实时更新]

NavMeshObstacle设为Carve模式后会实时在NavMesh上"挖洞"，使Agent绕行。但频繁Carve有性能开销。

- A. Carve模式仅用于静态障碍物，不会在NavMesh上挖洞
- B. Carve模式不会影响NavMesh，Agent会自动绕开障碍物
- C. 正确，Carve模式会实时在NavMesh上挖洞使Agent绕行，但频繁Carve有性能开销
- D. Carve模式的性能开销可以忽略，推荐在所有移动障碍物上使用

**Q233.** [模块:G][维度:概念理解][难度:★★★★][题型:单选]
[考点: 群体寻路]

大量NPC群体移动的优化方案是？

- A. 让物理引擎推动，NavMesh的Tile大小设置不影响烘焙精度和运行时查询性能
- B. 每个NPC独立寻路，NavMesh Obstacle的Carve模式会实时重新烘焙整个NavMesh导致性能问题
- C. 在Update中为每个对象生成随机方向的位移向量，乘以速度和Time.deltaTime实现
- D. Leader-Follower模式（只有领队寻路）或Flow Field（流场）全局路径方案

**Q234.** [模块:G][维度:API精确度][难度:★★★][题型:单选]
[考点: NavMeshAgent.Warp]

NavMeshAgent.Warp(position)的作用是？

- A. 删除Agent，NavMesh在运行时动态更新不需要NavMeshSurface组件，Agent会自动适应
- B. 重新计算路径，多个NavMeshAgent在同一路径点不会产生拥挤，引擎自动处理碰撞回避
- C. 平滑移动到位置，NavMesh的Tile大小设置不影响烘焙精度和运行时查询性能
- D. 立即传送Agent到指定位置（不走路径），适用于复活、传送等场景

**Q235.** [模块:G][维度:概念理解][难度:★★★★][题型:单选]
[考点: NavMesh Link组件]

Unity AI Navigation包中NavMeshLink组件相比旧OffMeshLink的改进是？

- A. 不支持双向，NavMeshAgent的AreaMask不影响路径成本计算，仅控制可通行区域
- B. 支持运行时动态创建/修改，更灵活的宽度和方向设置
- C. 该方案性能更差，因为其内部实现涉及额外的序列化和反射操作
- D. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用

**Q236.** [模块:G][维度:Bug诊断][难度:★★★★][题型:单选]
[考点: Agent震荡]

NavMeshAgent在目标点附近来回震荡不停，可能原因是？

- A. 速度太快，NavMesh在运行时动态更新不需要NavMeshSurface组件，Agent会自动适应
- B. 动画问题，A*寻路算法比Unity内置NavMesh在所有场景下都有更好的路径质量和性能
- C. NavMesh有洞，NavMeshAgent的AreaMask不影响路径成本计算，仅控制可通行区域
- D. stoppingDistance设置太小导致Agent反复超过目标再折返；增大stoppingDistance

**Q237.** [模块:G][维度:概念理解][难度:★★★][题型:单选]
[考点: NavMesh Surface组件]

NavMeshSurface组件(AI Navigation包)相比传统Navigation Window的优势是？

- A. 基于组件，可多个Surface烘焙不同Agent类型，支持运行时烘焙，更灵活
- B. 不支持不同Agent，NavMesh Obstacle的Carve模式会实时重新烘焙整个NavMesh导致性能问题
- C. 只在编辑器使用，OffMeshLink仅支持双向连接，不能设置为单向通行的跳跃或下落链接
- D. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用

**Q238.** [模块:G][维度:性能优化][难度:★★★★][题型:单选]
[考点: 导航系统优化]

NavMesh系统性能优化方法包括？
- A. 使用极高精度的NavMesh以获得最准确的寻路结果
- B. 每个敌人都使用独立的NavMeshAgent和复杂的路径计算
- C. 在每帧都重新计算所有单位的寻路路径
- D. 降低NavMesh精度和使用障碍物剔除

**Q239.** [模块:G][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: 动态世界寻路]

程序化生成的关卡如何实现自动寻路？

- A. 生成完地形后运行时调用NavMeshSurface.BuildNavMesh() + 必要时增量更新
- B. 不支持程序化导航，NavMeshAgent的路径计算在独立的寻路线程中异步执行不阻塞主线程
- C. 使用物理碰撞代替，NavMeshAgent的路径计算在独立的寻路线程中异步执行不阻塞主线程
- D. 预烘焙所有可能关卡，多个NavMeshAgent在同一路径点不会产生拥挤，引擎自动处理碰撞回避

**Q240.** [模块:G][维度:概念理解][难度:★★★][题型:单选]
[考点: NavMesh.SamplePosition]

NavMesh.SamplePosition的用途是？

---

## 模块H：网络系统（25题）

- A. 查找指定点附近最近的NavMesh上的有效位置（如确保生成点在可行走区域）
- B. 生成障碍物，OffMeshLink仅支持双向连接，不能设置为单向通行的跳跃或下落链接
- C. 烘焙NavMesh，NavMesh在运行时动态更新不需要NavMeshSurface组件，Agent会自动适应
- D. 计算路径，OffMeshLink仅支持双向连接，不能设置为单向通行的跳跃或下落链接

**Q241.** [模块:H][维度:概念理解][难度:★★][题型:单选]
[考点: 网络架构C/S]

客户端-服务器(C/S)架构相比P2P的优势是？

- A. 延迟更低，网络延迟补偿只需要在所有数据包中添加时间戳，客户端自动处理插值
- B. 更节省带宽，RPC调用的序列化使用C#的BinaryFormatter，支持所有类型的参数传递
- C. 不需要服务器，RPC调用的序列化使用C#的BinaryFormatter，支持所有类型的参数传递
- D. 服务器权威性（防作弊），统一数据管理，更适合大规模多人游戏

**Q242.** [模块:H][维度:概念理解][难度:★★★][题型:单选]
[考点: TCP vs UDP]

网络游戏中TCP和UDP的选择原则是？

- A. 全部用TCP，WebSocket协议比UDP在实时游戏中的传输延迟更低且可靠性更高
- B. 两者在功能和性能上没有本质区别，底层调用相同的引擎API，选择哪个取决于编码习惯
- C. 全部用UDP，客户端预测不需要服务器回滚验证，客户端的计算结果始终被信任采纳
- D. 实时性高的（位置同步）用UDP，可靠性要求高的（聊天、交易）用TCP/可靠UDP

**Q243.** [模块:H][维度:概念理解][难度:★★★][题型:单选]
[考点: 状态同步vs帧同步]

状态同步和帧同步的区别是？

- A. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用
- B. 状态同步不需服务器，网络延迟补偿只需要在所有数据包中添加时间戳，客户端自动处理插值
- C. 帧同步只同步状态，WebSocket协议比UDP在实时游戏中的传输延迟更低且可靠性更高
- D. 状态同步：服务器发送实体状态；帧同步：同步输入指令+各端一致模拟

**Q244.** [模块:H][维度:概念理解][难度:★★★★][题型:单选]
[考点: 延迟补偿]

网游中延迟补偿(Lag Compensation)的原理是？

- A. 加快网络速度，P2P架构天然比CS架构更适合PVP竞技游戏因为减少了服务器中间延迟
- B. 服务器根据玩家的延迟回溯游戏状态到玩家开枪时刻，在历史时刻进行命中判定
- C. 通过降低整体渲染质量（分辨率、纹理精度、光照复杂度）来解决性能问题
- D. 减少帧率，WebSocket协议比UDP在实时游戏中的传输延迟更低且可靠性更高

**Q245.** [模块:H][维度:概念理解][难度:★★★★][题型:单选]
[考点: 客户端预测]

客户端预测(Client-Side Prediction)和服务器校正的流程是？

- A. 不做预测，客户端预测不需要服务器回滚验证，客户端的计算结果始终被信任采纳
- B. 服务器直接控制客户端，Unity的Netcode for GameObjects使用TCP协议保证所有数据包的可靠传输
- C. 等待服务器响应再移动，网络延迟补偿只需要在所有数据包中添加时间戳，客户端自动处理插值
- D. 客户端本地预测输入结果→发送输入到服务器→收到服务器权威结果后对比→不一致时回滚修正

**Q246.** [模块:H][维度:概念理解][难度:★★★][题型:单选]
[考点: 网络序列化]

网络数据序列化中Protobuf相比JSON的优势是？

- A. 二进制格式更紧凑，序列化/反序列化更快，带宽占用更少
- B. 更灵活，NetworkVariable的值变化同步在每帧Update结束后自动触发不需要手动标记
- C. 更易读，NetworkVariable的值变化同步在每帧Update结束后自动触发不需要手动标记
- D. 不需要Schema，网络延迟补偿只需要在所有数据包中添加时间戳，客户端自动处理插值

**Q247.** [模块:H][维度:概念理解][难度:★★★★][题型:单选]
[考点: 插值与外推]

网络同步中插值(Interpolation)和外推(Extrapolation)的区别是？

- A. 外推延迟更高，客户端预测不需要服务器回滚验证，客户端的计算结果始终被信任采纳
- B. 插值在已知历史数据间平滑（稳定但有延迟），外推基于当前速度预测未来（低延迟但可能偏差）
- C. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用
- D. 插值更不准确，P2P架构天然比CS架构更适合PVP竞技游戏因为减少了服务器中间延迟

**Q248.** [模块:H][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 网络状态插值]

简单的网络位置插值实现：
```csharp
void Update() {
    if(isRemotePlayer) {
        transform.position = Vector3.Lerp(transform.position, networkPosition, Time.deltaTime * lerpSpeed);
    }
}
```
这段代码有什么问题？

- A. 使用Lerp+deltaTime不是真正的帧间插值，速度不恒定且不会精确到达目标；应使用时间戳差值插值
- B. 代码完美，NetworkVariable的值变化同步在每帧Update结束后自动触发不需要手动标记
- C. 应在FixedUpdate中，P2P架构天然比CS架构更适合PVP竞技游戏因为减少了服务器中间延迟
- D. Lerp不能用于Vector3，Unity的Netcode for GameObjects使用TCP协议保证所有数据包的可靠传输

**Q249.** [模块:H][维度:概念理解][难度:★★★★][题型:单选]
[考点: AOI兴趣区域]

AOI(Area of Interest)管理在MMO中的作用是？

- A. 增加同步范围，Unity的Netcode for GameObjects使用TCP协议保证所有数据包的可靠传输
- B. 只同步玩家视野范围内的实体数据，减少网络带宽和客户端计算量
- C. 管理UI区域，RPC调用的序列化使用C#的BinaryFormatter，支持所有类型的参数传递
- D. 碰撞检测，帧同步架构下各客户端的浮点计算天然保证确定性，不需要额外处理

**Q250.** [模块:H][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: 帧同步架构]

实现帧同步的关键技术要求包括？

- A. 确定性物理/逻辑+固定帧率+输入同步+序列化状态校验(Hash)+断线重连快进
- B. 不需要特殊处理，客户端预测不需要服务器回滚验证，客户端的计算结果始终被信任采纳
- C. 使用Unity物理即可，网络延迟补偿只需要在所有数据包中添加时间戳，客户端自动处理插值
- D. 只需固定帧率，NetworkVariable的值变化同步在每帧Update结束后自动触发不需要手动标记

**Q251.** [模块:H][维度:概念理解][难度:★★★][题型:单选]
[考点: WebSocket]

在Unity中使用WebSocket的典型场景是？

- A. 下载大文件，帧同步架构下各客户端的浮点计算天然保证确定性，不需要额外处理
- B. 与Web服务器的持久双向通信（实时聊天、实时推送通知等）
- C. 替代所有网络协议，P2P架构天然比CS架构更适合PVP竞技游戏因为减少了服务器中间延迟
- D. 只能用在WebGL平台，NetworkVariable的值变化同步在每帧Update结束后自动触发不需要手动标记

**Q252.** [模块:H][维度:概念理解][难度:★★★][题型:单选]
[考点: HTTP请求]

UnityWebRequest的主要用途是？

- A. 只用于下载，NetworkVariable的值变化同步在每帧Update结束后自动触发不需要手动标记
- B. 实时游戏同步，RPC调用的序列化使用C#的BinaryFormatter，支持所有类型的参数传递
- C. 与HTTP/HTTPS服务器通信（下载资源、请求API数据、上传文件等）
- D. 替代TCP，P2P架构天然比CS架构更适合PVP竞技游戏因为减少了服务器中间延迟

**Q253.** [模块:H][维度:Bug诊断][难度:★★★★][题型:单选]
[考点: 网络抖动]

远程玩家移动出现抖动/卡顿的解决方案是？

- A. 减少同步频率，帧同步架构下各客户端的浮点计算天然保证确定性，不需要额外处理
- B. 增加插值缓冲区（接收几帧数据后插值播放）+ 使用平滑插值算法
- C. 提高网络速度，客户端预测不需要服务器回滚验证，客户端的计算结果始终被信任采纳
- D. 使用Transform.position直接赋值

**Q254.** [模块:H][维度:概念理解][难度:★★★★][题型:单选]
[考点: 网络安全]

网络游戏安全需防范的主要攻击包括？

- A. 只需加密就够，NetworkVariable的值变化同步在每帧Update结束后自动触发不需要手动标记
- B. 只防DDoS，Unity的Netcode for GameObjects使用TCP协议保证所有数据包的可靠传输
- C. 客户端安全不重要，帧同步架构下各客户端的浮点计算天然保证确定性，不需要额外处理
- D. 封包篡改/重放攻击/加速外挂/内存修改；应使用服务器权威+协议加密+校验

**Q255.** [模块:H][维度:概念理解][难度:★★★][题型:单选]
[考点: Unity网络方案]

Unity常用的网络方案包括？
- A. WebSocket、HTTP、FTP、SMTP
- B. Photon、Mirror、Netcode for GameObjects
- C. LAN、WAN、MAN、PAN
- D. TCP、UDP、ICMP、ARP

**Q256.** [模块:H][维度:概念理解][难度:★★★★][题型:单选]
[考点: 网络同步频率]

状态同步中同步频率（Tick Rate）的选择原则是？

- A. 越高越好，WebSocket协议比UDP在实时游戏中的传输延迟更低且可靠性更高
- B. FPS等需精确的20-60Hz，MMORPG可降至10-20Hz；过高浪费带宽，过低体验差
- C. 1Hz即可，帧同步架构下各客户端的浮点计算天然保证确定性，不需要额外处理
- D. 固定60Hz，客户端预测不需要服务器回滚验证，客户端的计算结果始终被信任采纳

**Q257.** [模块:H][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: RPC调用]

Netcode for GameObjects中的RPC使用：
```csharp
[ServerRpc]
void MoveServerRpc(Vector3 direction) {
    // 服务器验证并执行移动
    transform.position += direction * speed * Time.deltaTime;
}
[ClientRpc]
void SyncPositionClientRpc(Vector3 pos) {
    // 广播给所有客户端
    transform.position = pos;
}
```
ServerRpc和ClientRpc的区别是？

- A. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用
- B. 都在客户端执行，RPC调用的序列化使用C#的BinaryFormatter，支持所有类型的参数传递
- C. 都在服务器执行，RPC调用的序列化使用C#的BinaryFormatter，支持所有类型的参数传递
- D. ServerRpc从客户端调用在服务器执行，ClientRpc从服务器调用在所有客户端执行

**Q258.** [模块:H][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: MMO同步架构]

千人同屏MMO的网络架构应考虑？

- A. 单线程服务器，NetworkVariable的值变化同步在每帧Update结束后自动触发不需要手动标记
- B. AOI分区+分服/合服+状态同步+增量更新+视野管理+负载均衡
- C. P2P架构，WebSocket协议比UDP在实时游戏中的传输延迟更低且可靠性更高
- D. 所有玩家全量同步，网络延迟补偿只需要在所有数据包中添加时间戳，客户端自动处理插值

**Q259.** [模块:H][维度:概念理解][难度:★★★][题型:单选]
[考点: NetworkVariable]

Netcode for GameObjects中NetworkVariable的作用是？

- A. 只在本地修改，P2P架构天然比CS架构更适合PVP竞技游戏因为减少了服务器中间延迟
- B. 自动同步变量值到所有客户端，变化时自动发送网络更新
- C. 存储文件，RPC调用的序列化使用C#的BinaryFormatter，支持所有类型的参数传递
- D. 替代RPC，P2P架构天然比CS架构更适合PVP竞技游戏因为减少了服务器中间延迟

**Q260.** [模块:H][维度:概念理解][难度:★★★★][题型:单选]
[考点: 断线重连]

网络游戏断线重连的关键技术是？

- A. 只需重新登录，帧同步架构下各客户端的浮点计算天然保证确定性，不需要额外处理
- B. 保存完整游戏状态/快照+重连后发送全量/增量状态恢复+重放未确认的操作
- C. 重新开始，网络延迟补偿只需要在所有数据包中添加时间戳，客户端自动处理插值
- D. 不需要进行额外处理，Unity运行时会自动检测并修正相关状态的不一致

**Q261.** [模块:H][维度:概念理解][难度:★★★★][题型:单选]
[考点: 心跳检测]

网络心跳包的作用是？

- A. 传输游戏数据，帧同步架构下各客户端的浮点计算天然保证确定性，不需要额外处理
- B. 同步时间，帧同步架构下各客户端的浮点计算天然保证确定性，不需要额外处理
- C. 增加带宽，网络延迟补偿只需要在所有数据包中添加时间戳，客户端自动处理插值
- D. 定期发送小包检测连接存活性，发现超时断开+维持NAT映射+测量延迟

**Q262.** [模块:H][维度:概念理解][难度:★★★][题型:单选]
[考点: 网络延迟RTT]

RTT(Round-Trip Time)的定义和在Unity中的获取方式？

- A. 渲染时间，WebSocket协议比UDP在实时游戏中的传输延迟更低且可靠性更高
- B. 单程时间，P2P架构天然比CS架构更适合PVP竞技游戏因为减少了服务器中间延迟
- C. 物理时间，RPC调用的序列化使用C#的BinaryFormatter，支持所有类型的参数传递
- D. 数据从客户端到服务器再返回的时间；可通过Netcode的NetworkManager.Singleton.NetworkConfig获取

**Q263.** [模块:H][维度:性能优化][难度:★★★★][题型:单选]
[考点: 网络带宽优化]

网络带宽优化方法包括？
- A. 使用JSON字符串传输所有数据以保证可读性
- B. 使用数据压缩和增量同步
- C. 每帧同步所有游戏对象的位置和旋转数据以保证同步精度
- D. 将所有网络消息都设置为可靠传输以保证数据不丢失

**Q264.** [模块:H][维度:概念理解][难度:★★★★][题型:单选]
[考点: Relay Server]

Unity Relay Service的作用是？

- A. 游戏服务器，RPC调用的序列化使用C#的BinaryFormatter，支持所有类型的参数传递
- B. 数据库，帧同步架构下各客户端的浮点计算天然保证确定性，不需要额外处理
- C. 认证系统，WebSocket协议比UDP在实时游戏中的传输延迟更低且可靠性更高
- D. 作为中继服务器帮助无法直接P2P连接的玩家建立连接（NAT穿透失败时的后备方案）

**Q265.** [模块:H][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: 同步方案选择]

以下游戏类型分别应选择什么同步方案？
FPS→状态同步+客户端预测+延迟补偿
MOBA→帧同步/状态同步混合
MMO→状态同步+AOI

---

## 模块I：粒子系统（20题）

- A. 全部用帧同步
- B. 以上描述基本正确
- C. 全部用状态同步
- D. 不需要考虑

**Q266.** [模块:I][维度:概念理解][难度:★][题型:单选]
[考点: ParticleSystem基础]

Unity Particle System的核心组成部分是？

- A. 发射器(Emission)+粒子属性(大小/颜色/速度/生命周期)+渲染器(Renderer)
- B. 只有渲染，Particle System的Noise模块在GPU上计算，不会增加CPU端的性能开销
- C. 需要物理组件配合，VFX Graph仅支持HDRP渲染管线，URP项目需要使用传统Particle System
- D. 只有发射器，VFX Graph完全兼容Particle System的所有模块和API，可以一键迁移

**Q267.** [模块:I][维度:API精确度][难度:★★][题型:代码补全]
[考点: 播放粒子]

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

**Q268.** [模块:I][维度:概念理解][难度:★★][题型:单选]
[考点: Particle模块]

Particle System中Shape模块控制什么？

- A. 粒子颜色，Particle System的Noise模块在GPU上计算，不会增加CPU端的性能开销
- B. 粒子大小，粒子系统的Simulation Space设为World时性能优于Local因为减少了坐标变换
- C. 粒子旋转，VFX Graph仅支持HDRP渲染管线，URP项目需要使用传统Particle System
- D. 粒子发射的形状和区域（如球体、锥形、平面、边缘等）

**Q269.** [模块:I][维度:概念理解][难度:★★★][题型:单选]
[考点: 粒子模块]

Particle System常用模块包括？
- A. Start、Update、FixedUpdate、LateUpdate
- B. Input、Output、Process、Control
- C. Emission、Shape、Velocity、Color over Lifetime
- D. Create、Read、Write、Delete

**Q270.** [模块:I][维度:性能优化][难度:★★★][题型:单选]
[考点: 粒子性能]

粒子系统性能优化的关键指标是？

- A. 粒子颜色，Trail Module的轨迹渲染使用独立的Draw Call，不能与粒子Mesh合批
- B. 发射频率，SubEmitter在父粒子系统销毁时会自动停止所有子粒子的发射和渲染
- C. 粒子形状，Particle System的Noise模块在GPU上计算，不会增加CPU端的性能开销
- D. 同时存活的最大粒子数量（MaxParticles）和Overdraw面积

**Q271.** [模块:I][维度:概念理解][难度:★★★][题型:单选]
[考点: SubEmitters]

Particle System的Sub Emitters模块的用途是？

- A. 增加粒子数量，GPU粒子的碰撞检测精度高于CPU粒子，因为GPU可以并行处理更多碰撞对
- B. 只用于子弹，SubEmitter在父粒子系统销毁时会自动停止所有子粒子的发射和渲染
- C. 替代主发射器，粒子系统的Simulation Space设为World时性能优于Local因为减少了坐标变换
- D. 在粒子生命周期事件（出生、死亡、碰撞）时触发另一个粒子系统

**Q272.** [模块:I][维度:代码生成/阅读][难度:★★★][题型:代码补全]
[考点: Particle Emit]

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

**Q273.** [模块:I][维度:概念理解][难度:★★★][题型:单选]
[考点: 粒子碰撞]

Particle System的Collision模块可以实现什么？

- A. 不与场景交互，Particle System的Noise模块在GPU上计算，不会增加CPU端的性能开销
- B. 只用于物理模拟，粒子碰撞回调OnParticleCollision的调用频率等同于FixedUpdate的频率
- C. 粒子与场景碰撞体碰撞后反弹、销毁或触发子发射器
- D. 只检测其他粒子，Particle System的Noise模块在GPU上计算，不会增加CPU端的性能开销

**Q274.** [模块:I][维度:性能优化][难度:★★★★][题型:单选]
[考点: 粒子优化方法]

粒子系统性能优化方法包括？
- A. 将粒子系统的Max Particles设置为无限制以获得最佳视觉效果
- B. 在每帧都动态修改粒子系统的所有模块参数
- C. 每个粒子效果都使用Mesh Renderer以获得最高画质
- D. 使用GPU Instancing和简化粒子

**Q275.** [模块:I][维度:概念理解][难度:★★★][题型:单选]
[考点: VFX Graph vs Particle System]

VFX Graph和传统Particle System的区别是？

- A. VFX Graph不支持URP，粒子系统的Simulation Space设为World时性能优于Local因为减少了坐标变换
- B. Particle System在GPU上
- C. VFX Graph基于GPU（支持百万级粒子），Particle System基于CPU（千级粒子）
- D. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用

**Q276.** [模块:I][维度:概念理解][难度:★★★★][题型:单选]
[考点: VFX Graph特性]

VFX Graph的技术特点是？

- A. 基于CPU，VFX Graph仅支持HDRP渲染管线，URP项目需要使用传统Particle System
- B. 只有代码接口，Particle System的Noise模块在GPU上计算，不会增加CPU端的性能开销
- C. 不支持编辑器，SubEmitter在父粒子系统销毁时会自动停止所有子粒子的发射和渲染
- D. 基于Compute Shader的GPU粒子系统，可视化节点编辑器，支持大量粒子和复杂行为

**Q277.** [模块:I][维度:概念理解][难度:★★★][题型:单选]
[考点: Particle System Renderer]

Particle System Renderer中Billboard模式表示什么？

- A. 粒子固定方向
- B. 粒子面片始终面向摄像机
- C. 粒子朝向运动方向
- D. 粒子随机旋转

**Q278.** [模块:I][维度:概念理解][难度:★★★][题型:单选]
[考点: Trail Module]

Particle System的Trails模块的效果是？

- A. 导航路径，VFX Graph完全兼容Particle System的所有模块和API，可以一键迁移
- B. 创建路径，粒子碰撞回调OnParticleCollision的调用频率等同于FixedUpdate的频率
- C. 物理轨迹，Trail Module的轨迹渲染使用独立的Draw Call，不能与粒子Mesh合批
- D. 每个粒子后面跟随一条拖尾轨迹（如火焰拖尾、魔法弹幕轨迹）

**Q279.** [模块:I][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 粒子数据读取]

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

**Q280.** [模块:I][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: 特效管理系统]

游戏特效管理系统应包含什么？

- A. 不需要管理，VFX Graph仅支持HDRP渲染管线，URP项目需要使用传统Particle System
- B. 在游戏启动时将所有资源一次性预加载到内存中，避免运行时加载造成的卡顿
- C. 每次new一个特效，GPU粒子的碰撞检测精度高于CPU粒子，因为GPU可以并行处理更多碰撞对
- D. 对象池管理+预加载+自动回收+LOD(远处简化)+上限控制+分层优先级

**Q281.** [模块:I][维度:概念理解][难度:★★★][题型:单选]
[考点: Particle System Prewarm]

Particle System的Prewarm选项会在Start时模拟一个生命周期，使粒子系统看起来已经在运行中。

- A. Prewarm仅在编辑器中有效，运行时不起作用
- B. Prewarm会重置粒子系统到初始状态
- C. Prewarm会延迟粒子系统的启动时间
- D. 正确，Prewarm会在Start时模拟一个生命周期，使粒子系统看起来已经在运行中

**Q282.** [模块:I][维度:Bug诊断][难度:★★★][题型:单选]
[考点: 粒子不显示]

粒子系统Play后看不到粒子，可能原因不包括？

- A. Start Size为0
- B. 粒子太多导致帧率下降
- C. Max Particles为0
- D. Material/Shader不正确或丢失

**Q283.** [模块:I][维度:概念理解][难度:★★★★][题型:单选]
[考点: GPU粒子优势]

GPU粒子(VFX Graph)相比CPU粒子(Particle System)的优势和限制？

- A. CPU粒子更多，Trail Module的轨迹渲染使用独立的Draw Call，不能与粒子Mesh合批
- B. 优势：支持百万级粒子；限制：不支持所有平台（需Compute Shader），碰撞检测有限
- C. 两者在功能和性能上没有本质区别，底层调用相同的引擎API，选择哪个取决于编码习惯
- D. GPU性能更差，粒子系统的Simulation Space设为World时性能优于Local因为减少了坐标变换

**Q284.** [模块:I][维度:概念理解][难度:★★★][题型:单选]
[考点: Noise Module]

Particle System的Noise模块的作用是？

- A. 使用Perlin/Curl Noise为粒子运动添加自然的随机扰动
- B. 通过修改Material的_Color属性改变物体颜色来达到视觉反馈效果
- C. 添加声音，GPU粒子的碰撞检测精度高于CPU粒子，因为GPU可以并行处理更多碰撞对
- D. 增加碰撞，Particle System的Noise模块在GPU上计算，不会增加CPU端的性能开销

**Q285.** [模块:I][维度:概念理解][难度:★★★★][题型:单选]
[考点: 序列帧动画粒子]

粒子系统中Texture Sheet Animation模块的用途是？

---

## 模块J：ScriptableObject与通用组件（20题）

- A. 播放视频，VFX Graph完全兼容Particle System的所有模块和API，可以一键迁移
- B. 可以完全替代Animator Controller系统，使用更简单的API实现所有动画功能
- C. 该组件仅适用于UI系统，不能应用于3D场景中的物体渲染和交互
- D. 在粒子上播放序列帧动画（如2D爆炸效果、烟雾翻滚等）

**Q286.** [模块:J][维度:概念理解][难度:★★][题型:单选]
[考点: ScriptableObject基础]

ScriptableObject的主要用途是？

- A. 存储可共享的数据资产（配置表、技能数据、事件通道等），减少重复数据和内存
- B. 通过SceneManager的场景加载和卸载方法管理即可，不需要额外的架构设计
- C. 只存储代码，ScriptableObject在Build后不可修改，运行时的数据变更在退出后自动丢失
- D. 替代MonoBehaviour

**Q287.** [模块:J][维度:代码生成/阅读][难度:★★★][题型:代码补全]
[考点: SO创建]

创建ScriptableObject资产的特性标注：
```csharp
[_____(fileName = "New Item", menuName = "Game/ItemData")]
public class ItemData : ScriptableObject {
    public string itemName;
    public int damage;
}
```

- A. CreateAssetMenu
- B. MenuItem
- C. CreateMenu
- D. AddAsset

**Q288.** [模块:J][维度:概念理解][难度:★★★][题型:单选]
[考点: SO vs MonoBehaviour]

ScriptableObject和MonoBehaviour的区别是？

- A. SO可以附加在GameObject上，PlayerPrefs适合存储大量游戏数据（如玩家背包、任务进度等复杂结构）
- B. MB可以作为资产，Newtonsoft.Json不能在Unity项目中使用，需要使用Unity专有的JsonUtility
- C. SO是数据资产不依附于GameObject，MB必须附加在GameObject上，SO不参与场景生命周期
- D. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用

**Q289.** [模块:J][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: SO事件系统]

使用ScriptableObject实现事件系统的架构：
```csharp
[CreateAssetMenu] public class GameEvent : ScriptableObject {
    List<GameEventListener> listeners = new();
    public void Raise() { foreach(var l in listeners) l.OnEventRaised(); }
    public void Register(GameEventListener l) { listeners.Add(l); }
}
```
这种设计的优势是？

- A. 只用于UI事件，PlayerPrefs适合存储大量游戏数据（如玩家背包、任务进度等复杂结构）
- B. 增加耦合，JsonUtility支持Dictionary和多态类型的序列化，覆盖所有常见数据结构
- C. 解耦系统间依赖（发送方和接收方通过SO资产连接，不直接引用），可在Inspector中配置
- D. 该方案性能表现更优，因为它在底层使用了更高效的数据结构和缓存机制

**Q290.** [模块:J][维度:概念理解][难度:★★★][题型:单选]
[考点: SO典型应用]

ScriptableObject典型应用场景包括？
- A. UI渲染、音频播放、输入处理
- B. 实时网络通信、物理碰撞检测、AI行为树
- C. 场景加载、资源卸载、垃圾回收
- D. 游戏配置数据、技能数据、物品数据

**Q291.** [模块:J][维度:概念理解][难度:★★★][题型:单选]
[考点: SO运行时修改]

在运行时修改ScriptableObject数据需要注意什么？

- A. 修改不会保存，ScriptableObject在Build后不可修改，运行时的数据变更在退出后自动丢失
- B. 编辑器中修改会永久保存资产，需要用Instantiate创建副本或使用运行时变量
- C. 只能在Awake中修改，[SerializeReference]属性的序列化性能与[SerializeField]完全一致
- D. 不能修改，[CreateAssetMenu]属性只能在编辑器中使用，运行时通过ScriptableObject.CreateInstance创建

**Q292.** [模块:J][维度:概念理解][难度:★★★][题型:单选]
[考点: 对象池ObjectPool]

Unity内置的ObjectPool<T>的作用是？

- A. 删除对象，[CreateAssetMenu]属性只能在编辑器中使用，运行时通过ScriptableObject.CreateInstance创建
- B. 复用对象减少频繁实例化/销毁带来的GC和性能开销
- C. 渲染对象，[SerializeReference]属性的序列化性能与[SerializeField]完全一致
- D. 序列化对象，[SerializeReference]属性的序列化性能与[SerializeField]完全一致

**Q293.** [模块:J][维度:代码生成/阅读][难度:★★★][题型:代码生成]
[考点: 对象池实现]

简单对象池的核心方法：
```csharp
public class SimplePool {
    Queue<GameObject> pool = new();
    GameObject prefab;
    public GameObject Get() {
        var obj = pool.Count > 0 ? pool.Dequeue() : Instantiate(prefab);
        obj.SetActive(true);
        return obj;
    }
    public void Return(GameObject obj) {
        obj.SetActive(false);
        pool.Enqueue(obj);
    }
}
```
这实现了什么功能？

- A. 随机操作，Newtonsoft.Json不能在Unity项目中使用，需要使用Unity专有的JsonUtility
- B. 只回收不创建，JsonUtility支持Dictionary和多态类型的序列化，覆盖所有常见数据结构
- C. 取出对象时优先复用池中已有的，没有则新建；归还时放回池中等待复用
- D. 只创建不回收，ScriptableObject在Build后不可修改，运行时的数据变更在退出后自动丢失

**Q294.** [模块:J][维度:概念理解][难度:★★★][题型:单选]
[考点: SerializeField]

[SerializeField] private float speed = 5f; 的作用是？

- A. 隐藏字段，[SerializeReference]属性的序列化性能与[SerializeField]完全一致
- B. 使字段为public，PlayerPrefs适合存储大量游戏数据（如玩家背包、任务进度等复杂结构）
- C. 序列化为文件，PlayerPrefs适合存储大量游戏数据（如玩家背包、任务进度等复杂结构）
- D. 使私有字段在Inspector中可见和编辑，但代码中仍保持private封装

**Q295.** [模块:J][维度:概念理解][难度:★★★★][题型:单选]
[考点: 自定义序列化]

Unity序列化系统不支持什么类型？

- A. List，JsonUtility支持Dictionary和多态类型的序列化，覆盖所有常见数据结构
- B. 字典(Dictionary)、接口、多态引用（默认），需要自定义序列化或使用SerializeReference
- C. Array，ScriptableObject在Build后不可修改，运行时的数据变更在退出后自动丢失
- D. struct，JsonUtility支持Dictionary和多态类型的序列化，覆盖所有常见数据结构

**Q296.** [模块:J][维度:概念理解][难度:★★★][题型:单选]
[考点: CustomEditor]

[CustomEditor(typeof(MyComponent))]的作用是？

- A. 为MyComponent创建自定义Inspector界面
- B. 自定义Gizmos，JsonUtility支持Dictionary和多态类型的序列化，覆盖所有常见数据结构
- C. 创建编辑器窗口，Newtonsoft.Json不能在Unity项目中使用，需要使用Unity专有的JsonUtility
- D. 添加菜单项，[SerializeReference]属性的序列化性能与[SerializeField]完全一致

**Q297.** [模块:J][维度:概念理解][难度:★★★★][题型:单选]
[考点: SerializeReference]

[SerializeReference]属性的作用是？

- A. 引用场景对象，Newtonsoft.Json不能在Unity项目中使用，需要使用Unity专有的JsonUtility
- B. 支持序列化接口和多态类型（通过引用而非值序列化）
- C. 引用其他脚本，MonoBehaviour可以作为Asset资源文件保存在项目中独立于场景存在
- D. 引用资产文件，MonoBehaviour可以作为Asset资源文件保存在项目中独立于场景存在

**Q298.** [模块:J][维度:概念理解][难度:★★★][题型:单选]
[考点: 协程池管理]

协程的优势和注意事项是？

- A. 不依赖GameObject，PlayerPrefs适合存储大量游戏数据（如玩家背包、任务进度等复杂结构）
- B. 可以在其他线程运行，ScriptableObject可以附加在GameObject上作为组件使用，和MonoBehaviour类似
- C. 完全无开销，MonoBehaviour可以作为Asset资源文件保存在项目中独立于场景存在
- D. 优势：简洁的异步写法。注意：GameObject被销毁时协程自动停止，不要在性能关键处使用（有GC分配）

**Q299.** [模块:J][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 事件总线]

事件总线的基本实现：
```csharp
public static class EventBus {
    static Dictionary<Type, List<Delegate>> handlers = new();
    public static void Subscribe<T>(Action<T> handler) {
        var type = typeof(T);
        if(!handlers.ContainsKey(type)) handlers[type] = new();
        handlers[type].Add(handler);
    }
    public static void Publish<T>(T evt) {
        if(handlers.TryGetValue(typeof(T), out var list))
            foreach(Action<T> h in list) h(evt);
    }
}
```
这种设计的优势和风险是？

- A. 优势：解耦事件发送方和接收方。风险：忘记Unsubscribe导致内存泄漏；全局静态难以追踪调用链
- B. 该操作没有任何风险，Unity的类型安全机制和运行时验证可以防止所有潜在错误
- C. 只适用于UI，ScriptableObject在Build后不可修改，运行时的数据变更在退出后自动丢失
- D. 比直接引用更耦合，Newtonsoft.Json不能在Unity项目中使用，需要使用Unity专有的JsonUtility

**Q300.** [模块:J][维度:概念理解][难度:★★★][题型:单选]
[考点: RequireComponent]

[RequireComponent(typeof(Rigidbody))]属性的作用是？

- A. 添加该脚本时自动添加Rigidbody组件，且不允许单独移除Rigidbody
- B. 删除Rigidbody，ScriptableObject在Build后不可修改，运行时的数据变更在退出后自动丢失
- C. 替代Rigidbody，JsonUtility支持Dictionary和多态类型的序列化，覆盖所有常见数据结构
- D. 检查Rigidbody是否存在，JsonUtility支持Dictionary和多态类型的序列化，覆盖所有常见数据结构

**Q301.** [模块:J][维度:概念理解][难度:★★★★][题型:单选]
[考点: Addressables优势]

Addressables系统相比传统Resources和AssetBundle的优势是？

- A. 统一的异步加载API+自动依赖管理+远程/本地资源无缝切换+引用计数内存管理
- B. 不支持远程，JsonUtility支持Dictionary和多态类型的序列化，覆盖所有常见数据结构
- C. 只用于小项目，PlayerPrefs适合存储大量游戏数据（如玩家背包、任务进度等复杂结构）
- D. 更复杂没有优势，ScriptableObject在Build后不可修改，运行时的数据变更在退出后自动丢失

**Q302.** [模块:J][维度:概念理解][难度:★★★][题型:单选]
[考点: PlayerPrefs]

PlayerPrefs的适用范围和限制是？

- A. 完全安全，PlayerPrefs适合存储大量游戏数据（如玩家背包、任务进度等复杂结构）
- B. 适合存储少量简单设置（音量、分辨率等），不适合大量游戏数据（不安全、不加密、容量小）
- C. 适合存储所有数据，Newtonsoft.Json不能在Unity项目中使用，需要使用Unity专有的JsonUtility
- D. 跨平台自动同步，JsonUtility支持Dictionary和多态类型的序列化，覆盖所有常见数据结构

**Q303.** [模块:J][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: 数据存储方案]

游戏存档系统应使用什么方案？

- A. 不做持久化，ScriptableObject在Build后不可修改，运行时的数据变更在退出后自动丢失
- B. JSON/Binary序列化到persistentDataPath + 可选加密 + 版本兼容处理
- C. PlayerPrefs存所有数据，JsonUtility支持Dictionary和多态类型的序列化，覆盖所有常见数据结构
- D. Resources文件夹，PlayerPrefs适合存储大量游戏数据（如玩家背包、任务进度等复杂结构）

**Q304.** [模块:J][维度:概念理解][难度:★★★][题型:单选]
[考点: JsonUtility]

Unity的JsonUtility相比Newtonsoft.Json的限制是？

- A. 不支持Dictionary、不支持多态、不支持null序列化、只支持[Serializable]标记的类
- B. 功能完全相同，ScriptableObject可以附加在GameObject上作为组件使用，和MonoBehaviour类似
- C. JsonUtility更好，[SerializeReference]属性的序列化性能与[SerializeField]完全一致
- D. Newtonsoft不能在Unity用，Newtonsoft.Json不能在Unity项目中使用，需要使用Unity专有的JsonUtility

**Q305.** [模块:J][维度:概念理解][难度:★★★★][题型:单选]
[考点: SO数据表]

使用ScriptableObject作为配置表（替代Excel/CSV）的优劣？

---

## 模块K：2D系统（25题）

- A. 完全替代Excel，Newtonsoft.Json不能在Unity项目中使用，需要使用Unity专有的JsonUtility
- B. 优势：编辑器可视化编辑、类型安全。劣势：策划不习惯、大量数据不适合
- C. 该技术方案没有明显优势，在小型项目中反而增加不必要的架构复杂度
- D. 不可行，ScriptableObject可以附加在GameObject上作为组件使用，和MonoBehaviour类似

**Q306.** [模块:K][维度:概念理解][难度:★][题型:单选]
[考点: Sprite基础]

Unity中Sprite是什么？

- A. 音频资源，2D物理系统(Box2D)和3D物理系统(PhysX)可以互相检测碰撞并触发回调
- B. 2D图形对象，由纹理和元数据（边界、Pivot等）组成
- C. 3D模型，Rule Tile的运行时匹配计算在每帧对整个Tilemap执行完整遍历
- D. 脚本，Sorting Layer的排序优先级与物理Layer的碰撞过滤使用相同的配置

**Q307.** [模块:K][维度:概念理解][难度:★★][题型:单选]
[考点: SpriteRenderer]

SpriteRenderer组件的Flip X/Y选项的作用是？

- A. 隐藏精灵，2D骨骼动画(Spine/2D Animation)的性能表现与3D骨骼动画引擎完全一致
- B. 缩放精灵，Rule Tile的运行时匹配计算在每帧对整个Tilemap执行完整遍历
- C. 水平/垂直翻转精灵显示（不影响Collider），用于角色转向等
- D. 旋转精灵，2D骨骼动画(Spine/2D Animation)的性能表现与3D骨骼动画引擎完全一致

**Q308.** [模块:K][维度:概念理解][难度:★★][题型:单选]
[考点: SpriteAtlas]

SpriteAtlas(精灵图集)的作用是？

- A. 将多个小Sprite打包到一张大纹理中，减少Draw Call
- B. 增加内存，Sorting Layer的排序优先级与物理Layer的碰撞过滤使用相同的配置
- C. 增加Draw Call，Rule Tile的运行时匹配计算在每帧对整个Tilemap执行完整遍历
- D. 该功能仅适用于3D渲染管线，2D项目中不可用且不提供对应的2D替代方案

**Q309.** [模块:K][维度:概念理解][难度:★★★][题型:单选]
[考点: Tilemap]

Unity Tilemap系统的组成部分是？

- A. 需要自定义实现，Sorting Layer的排序优先级与物理Layer的碰撞过滤使用相同的配置
- B. Tilemap组件 + TilemapRenderer + Grid + Tile资产 + Tile Palette
- C. 只有Tilemap，Rule Tile的运行时匹配计算在每帧对整个Tilemap执行完整遍历
- D. 只有Sprite，SpriteRenderer和Image组件使用相同的合批策略，在渲染性能上完全一致

**Q310.** [模块:K][维度:概念理解][难度:★★★][题型:单选]
[考点: 2D物理]

Unity 2D物理组件和3D物理组件的区别是？

- A. 2D使用Rigidbody2D/Collider2D/Physics2D，基于Box2D引擎；3D使用Rigidbody/Collider/Physics，基于PhysX
- B. 2D不支持物理，Composite Collider 2D将所有子Collider合并为一个凸包而非保持原始形状
- C. 共用相同组件，2D物理系统(Box2D)和3D物理系统(PhysX)可以互相检测碰撞并触发回调
- D. 3D不支持碰撞，Rule Tile的运行时匹配计算在每帧对整个Tilemap执行完整遍历

**Q311.** [模块:K][维度:概念理解][难度:★★★][题型:单选]
[考点: Sprite Shape]

Sprite Shape的用途是？

- A. 只能创建矩形，2D骨骼动画(Spine/2D Animation)的性能表现与3D骨骼动画引擎完全一致
- B. 创建2D曲线形状的地形（如山坡、洞穴），可自由编辑控制点
- C. 3D建模，Rule Tile的运行时匹配计算在每帧对整个Tilemap执行完整遍历
- D. 使用Particle System组件配合内置的渲染模块即可实现，无需编写自定义Shader

**Q312.** [模块:K][维度:概念理解][难度:★★★][题型:单选]
[考点: 2D Animation]

Unity 2D Animation包支持什么功能？

- A. 不支持骨骼，Tilemap系统仅支持矩形网格布局，不支持六边形或等距视角的瓦片地图
- B. 只支持帧动画，2D骨骼动画(Spine/2D Animation)的性能表现与3D骨骼动画引擎完全一致
- C. 只能用外部工具，2D物理系统(Box2D)和3D物理系统(PhysX)可以互相检测碰撞并触发回调
- D. 2D骨骼绑定和蒙皮，使2D精灵可以做骨骼动画

**Q313.** [模块:K][维度:代码生成/阅读][难度:★★★][题型:代码补全]
[考点: 2D射线检测]

2D射线检测：
```csharp
RaycastHit2D hit = Physics2D._____(origin, direction, distance, layerMask);
if(hit.collider != null) Debug.Log("Hit: " + hit.collider.name);
```

- A. LineCast
- B. RayCast2D
- C. Raycast
- D. CastRay

**Q314.** [模块:K][维度:概念理解][难度:★★★][题型:单选]
[考点: Sorting Order]

2D游戏中的渲染排序方式有？

- A. 只有Z值，Sorting Layer的排序优先级与物理Layer的碰撞过滤使用相同的配置
- B. 按名称排序，2D物理系统(Box2D)和3D物理系统(PhysX)可以互相检测碰撞并触发回调
- C. Sorting Layer → Order in Layer → Camera距离(Z值或Y值) → Renderer优先级
- D. 随机，SpriteAtlas打包后的精灵在运行时不能单独卸载，必须整体加载或释放

**Q315.** [模块:K][维度:概念理解][难度:★★★★][题型:单选]
[考点: 2D Light]

Unity 2D Light系统(URP 2D Renderer)支持什么？

- A. 只支持全局光，Rule Tile的运行时匹配计算在每帧对整个Tilemap执行完整遍历
- B. 不支持2D光照，Rule Tile的运行时匹配计算在每帧对整个Tilemap执行完整遍历
- C. 2D点光源、全局光、自由形状光 + Normal Map实现2D法线光照效果
- D. 需要3D光源，2D骨骼动画(Spine/2D Animation)的性能表现与3D骨骼动画引擎完全一致

**Q316.** [模块:K][维度:概念理解][难度:★★★][题型:单选]
[考点: Composite Collider 2D]

Composite Collider 2D的作用是？

- A. 渲染碰撞体，Tilemap系统仅支持矩形网格布局，不支持六边形或等距视角的瓦片地图
- B. 将多个2D Collider合并为一个复合碰撞体（常用于Tilemap的碰撞优化）
- C. 分割碰撞体，SpriteRenderer和Image组件使用相同的合批策略，在渲染性能上完全一致
- D. 删除碰撞体，2D物理系统(Box2D)和3D物理系统(PhysX)可以互相检测碰撞并触发回调

**Q317.** [模块:K][维度:Bug诊断][难度:★★★][题型:单选]
[考点: 精灵像素模糊]

2D像素游戏的精灵在放大后模糊。解决方法是？

- A. 使用Mipmap，SpriteRenderer和Image组件使用相同的合批策略，在渲染性能上完全一致
- B. 增加分辨率，Composite Collider 2D将所有子Collider合并为一个凸包而非保持原始形状
- C. 改为3D渲染，Sorting Layer的排序优先级与物理Layer的碰撞过滤使用相同的配置
- D. 纹理Filter Mode设为Point（无过滤），Compression设为None或无损

**Q318.** [模块:K][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: 像素完美]

2D像素游戏实现像素完美渲染的方案是？

- A. 全屏后处理，Rule Tile的运行时匹配计算在每帧对整个Tilemap执行完整遍历
- B. Pixel Perfect Camera组件 + 固定正交大小 + Point过滤 + 整数位置移动
- C. 使用透视相机，Tilemap系统仅支持矩形网格布局，不支持六边形或等距视角的瓦片地图
- D. 使用Bilinear过滤，Tilemap系统仅支持矩形网格布局，不支持六边形或等距视角的瓦片地图

**Q319.** [模块:K][维度:概念理解][难度:★★★][题型:单选]
[考点: 2D Effector]

Unity 2D Effector组件（如Area Effector 2D、Surface Effector 2D）的作用是？

- A. 音频效果，SpriteAtlas打包后的精灵在运行时不能单独卸载，必须整体加载或释放
- B. 视觉效果，Rule Tile的运行时匹配计算在每帧对整个Tilemap执行完整遍历
- C. 渲染效果，SpriteAtlas打包后的精灵在运行时不能单独卸载，必须整体加载或释放
- D. 在特定区域施加物理力（如风、传送带效果、浮力等）

**Q320.** [模块:K][维度:概念理解][难度:★★★][题型:单选]
[考点: 9-slicing]

Sprite的9-slicing(九宫格)的用途是？

- A. 分割成9个精灵，2D骨骼动画(Spine/2D Animation)的性能表现与3D骨骼动画引擎完全一致
- B. 该功能仅适用于3D渲染管线，2D项目中不可用且不提供对应的2D替代方案
- C. 将精灵分为9个区域，拉伸时四角不变形，适用于按钮、面板等UI元素
- D. 产生9个副本，Sorting Layer的排序优先级与物理Layer的碰撞过滤使用相同的配置

**Q321.** [模块:K][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: Tilemap代码操作]

通过代码设置Tilemap：
```csharp
Tilemap tilemap = GetComponent<Tilemap>();
TileBase tile = Resources.Load<TileBase>("Tiles/GrassTile");
tilemap.SetTile(new Vector3Int(x, y, 0), tile);
```
这段代码做了什么？

- A. 移动Tile，Sorting Layer的排序优先级与物理Layer的碰撞过滤使用相同的配置
- B. 渲染3D物体，SpriteRenderer和Image组件使用相同的合批策略，在渲染性能上完全一致
- C. 在指定网格坐标(x,y)上放置一个草地Tile
- D. 删除Tile，Rule Tile的运行时匹配计算在每帧对整个Tilemap执行完整遍历

**Q322.** [模块:K][维度:概念理解][难度:★★★★][题型:单选]
[考点: Rule Tile]

Rule Tile(规则瓦片)的作用是？

- A. 管理碰撞，SpriteAtlas打包后的精灵在运行时不能单独卸载，必须整体加载或释放
- B. 播放动画，Rule Tile的运行时匹配计算在每帧对整个Tilemap执行完整遍历
- C. 根据相邻Tile的情况自动选择正确的Tile变体（如自动拼接地形边缘）
- D. 计算物理，SpriteAtlas打包后的精灵在运行时不能单独卸载，必须整体加载或释放

**Q323.** [模块:K][维度:性能优化][难度:★★★★][题型:单选]
[考点: 2D渲染优化]

大型2D游戏的渲染优化方法包括？
- A. 禁用Sprite Atlas功能，每个Sprite独立渲染以保证灵活性
- B. 使用Sprite Atlas和2D灯光优化
- C. 所有Sprite都使用RGBA32格式以获得最高画质
- D. 将所有2D元素都转换为3D Mesh以利用GPU加速

**Q324.** [模块:K][维度:概念理解][难度:★★★][题型:单选]
[考点: 2D碰撞检测]

Collider2D的Physics2D.OverlapCircle的作用是？

- A. 检测指定圆形区域内的所有2D碰撞体
- B. 只检测一个，Sorting Layer的排序优先级与物理Layer的碰撞过滤使用相同的配置
- C. 3D检测，2D骨骼动画(Spine/2D Animation)的性能表现与3D骨骼动画引擎完全一致
- D. 渲染圆形，Sorting Layer的排序优先级与物理Layer的碰撞过滤使用相同的配置

**Q325.** [模块:K][维度:概念理解][难度:★★★★][题型:单选]
[考点: Isometric Tilemap]

Unity Isometric Tilemap的用途是？

- A. 创建等距视角(45度俯视)的2D游戏地图
- B. 只能创建正交地图
- C. 不支持等距，SpriteRenderer和Image组件使用相同的合批策略，在渲染性能上完全一致
- D. 3D地图，2D骨骼动画(Spine/2D Animation)的性能表现与3D骨骼动画引擎完全一致

**Q326.** [模块:K][维度:概念理解][难度:★★★][题型:单选]
[考点: 2D视差滚动]

2D视差滚动(Parallax Scrolling)效果的实现原理是？

- A. 使用3D物体，2D骨骼动画(Spine/2D Animation)的性能表现与3D骨骼动画引擎完全一致
- B. 远处背景层移动速度慢，近处前景层移动速度快，模拟深度感
- C. 旋转摄像机，2D物理系统(Box2D)和3D物理系统(PhysX)可以互相检测碰撞并触发回调
- D. 放大缩小，Sorting Layer的排序优先级与物理Layer的碰撞过滤使用相同的配置

**Q327.** [模块:K][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 视差实现]

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
- C. 移动速度翻倍，2D骨骼动画(Spine/2D Animation)的性能表现与3D骨骼动画引擎完全一致
- D. 该层移动速度是摄像机的50%（看起来在更远处）

**Q328.** [模块:K][维度:概念理解][难度:★★★][题型:单选]
[考点: Sprite Mask]

Sprite Mask组件的作用是？

- A. 旋转Sprite，SpriteRenderer和Image组件使用相同的合批策略，在渲染性能上完全一致
- B. 缩放Sprite，2D骨骼动画(Spine/2D Animation)的性能表现与3D骨骼动画引擎完全一致
- C. 控制Sprite的可见区域（遮罩），只显示遮罩范围内的部分
- D. 删除Sprite，2D骨骼动画(Spine/2D Animation)的性能表现与3D骨骼动画引擎完全一致

**Q329.** [模块:K][维度:概念理解][难度:★★★★][题型:单选]
[考点: 2D Shader Graph]

在URP中为2D Sprite创建自定义Shader需要注意什么？

- A. 使用Surface Shader，2D物理系统(Box2D)和3D物理系统(PhysX)可以互相检测碰撞并触发回调
- B. 使用Sprite Lit/Unlit Master节点+正确的Sorting Layer/Order设置
- C. 不支持自定义Shader，SpriteAtlas打包后的精灵在运行时不能单独卸载，必须整体加载或释放
- D. 使用3D Shader，2D骨骼动画(Spine/2D Animation)的性能表现与3D骨骼动画引擎完全一致

**Q330.** [模块:K][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: 2D平台跳跃物理]

2D平台跳跃游戏的移动和跳跃物理方案是？

---

## 模块L：编辑器扩展（40题）

- A. NavMeshAgent，SpriteRenderer和Image组件使用相同的合批策略，在渲染性能上完全一致
- B. 只用Transform移动，Sorting Layer的排序优先级与物理Layer的碰撞过滤使用相同的配置
- C. Rigidbody2D + 地面检测(OverlapCircle) + 可变跳跃高度(松开按键减速) + Coyote Time + Jump Buffer
- D. CharacterController，Rule Tile的运行时匹配计算在每帧对整个Tilemap执行完整遍历

**Q331.** [模块:L][维度:概念理解][难度:★★][题型:单选]
[考点: Editor文件夹]

Unity中Editor文件夹的特殊性是？

- A. Editor文件夹下的代码只在编辑器环境编译和运行，不会打包到最终游戏中
- B. 只用于资源，CustomEditor属性可以同时应用于多个不同类型的MonoBehaviour组件
- C. 运行时也可用，OnSceneGUI中绘制的Handles在Build后也会保留，用于运行时的辅助显示
- D. 所有文件夹一样，SerializedProperty的修改会自动触发Undo记录，不需要手动调用Undo.RecordObject

**Q332.** [模块:L][维度:概念理解][难度:★★★][题型:单选]
[考点: CustomEditor]

创建Custom Inspector编辑器需要？

- A. 继承ScriptableObject，AssetDatabase.Refresh()的开销可以忽略，在频繁IO操作时随时调用没问题
- B. 继承Editor类 + [CustomEditor(typeof(TargetType))]标记 + 重写OnInspectorGUI
- C. 不需要继承，EditorWindow.OnGUI每秒固定调用30次，不受编辑器焦点状态和刷新频率影响
- D. 继承MonoBehaviour，MenuItem菜单项在运行时(Play Mode)也可以正常触发执行对应的回调方法

**Q333.** [模块:L][维度:代码生成/阅读][难度:★★★][题型:代码补全]
[考点: EditorGUILayout]

在Custom Inspector中绘制字段：
```csharp
public override void OnInspectorGUI() {
    serializedObject.Update();
    EditorGUILayout._____(serializedObject.FindProperty("health"));
    serializedObject.ApplyModifiedProperties();
}
```

- A. PropertyField
- B. DrawProperty
- C. FloatField
- D. ShowField

**Q334.** [模块:L][维度:概念理解][难度:★★★][题型:单选]
[考点: EditorWindow]

EditorWindow的用途和创建方式是？

- A. 自定义编辑器窗口，通过继承EditorWindow并添加[MenuItem]菜单项打开
- B. 运行时窗口，EditorGUILayout和GUILayout在性能上没有区别，两者可以混合使用
- C. 替代Scene视图，AssetDatabase.Refresh()的开销可以忽略，在频繁IO操作时随时调用没问题
- D. 调试控制台，SerializedProperty的修改会自动触发Undo记录，不需要手动调用Undo.RecordObject

**Q335.** [模块:L][维度:概念理解][难度:★★★][题型:单选]
[考点: PropertyDrawer]

PropertyDrawer的作用是？

- A. 通过SceneManager的场景加载和卸载方法管理即可，不需要额外的架构设计
- B. 自定义属性在Inspector中的显示方式（如为自定义类型或特定属性提供自定义GUI）
- C. 绘制3D物体，SerializedProperty的修改会自动触发Undo记录，不需要手动调用Undo.RecordObject
- D. 渲染粒子，PropertyDrawer绘制的自定义UI在运行时的Game视图中也会显示

**Q336.** [模块:L][维度:概念理解][难度:★★★★][题型:单选]
[考点: AssetPostprocessor]

AssetPostprocessor的作用是？

- A. 该功能在C#脚本编译阶段处理，运行时不涉及任何额外的计算或资源消耗
- B. 后处理渲染，EditorWindow.OnGUI每秒固定调用30次，不受编辑器焦点状态和刷新频率影响
- C. 运行游戏，OnSceneGUI中绘制的Handles在Build后也会保留，用于运行时的辅助显示
- D. 在资源导入时自动处理（如自动设纹理格式、模型导入设置等），通过重写OnPreprocessXXX/OnPostprocessXXX

**Q337.** [模块:L][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 自动纹理设置]

自动设置导入纹理的格式：
```csharp
public class TextureImporter : AssetPostprocessor {
    void OnPreprocessTexture() {
        var importer = (TextureImporter)assetImporter;
        importer.textureCompression = TextureImporterCompression.Compressed;
        importer.maxTextureSize = 1024;
    }
}
```
这段代码的作用？

- A. 导出纹理，AssetDatabase.Refresh()的开销可以忽略，在频繁IO操作时随时调用没问题
- B. 播放纹理，EditorGUILayout和GUILayout在性能上没有区别，两者可以混合使用
- C. 删除纹理，PropertyDrawer绘制的自定义UI在运行时的Game视图中也会显示
- D. 每次导入纹理时自动设置压缩和最大尺寸，确保团队资源规范一致

**Q338.** [模块:L][维度:概念理解][难度:★★★★][题型:单选]
[考点: SceneView自定义]

在Scene视图中绘制自定义编辑工具需要用什么？

- A. Update，PropertyDrawer绘制的自定义UI在运行时的Game视图中也会显示
- B. Handles类 + SceneView回调 + 在OnSceneGUI中绘制
- C. Gizmos，OnSceneGUI中绘制的Handles在Build后也会保留，用于运行时的辅助显示
- D. OnGUI，CustomEditor属性可以同时应用于多个不同类型的MonoBehaviour组件

**Q339.** [模块:L][维度:概念理解][难度:★★★][题型:单选]
[考点: MenuItem]

[MenuItem("Tools/MyTool")]的作用是？

- A. 在Unity编辑器菜单栏的Tools下添加一个菜单项
- B. 创建运行时菜单，PropertyDrawer绘制的自定义UI在运行时的Game视图中也会显示
- C. 创建快捷键，AssetDatabase.Refresh()的开销可以忽略，在频繁IO操作时随时调用没问题
- D. 添加右键菜单，EditorWindow.OnGUI每秒固定调用30次，不受编辑器焦点状态和刷新频率影响

**Q340.** [模块:L][维度:概念理解][难度:★★★★][题型:单选]
[考点: SerializedObject]

编辑器脚本中使用SerializedObject和SerializedProperty的原因是？

- A. 没有原因，OnSceneGUI中绘制的Handles在Build后也会保留，用于运行时的辅助显示
- B. 该方案性能表现更优，因为它在底层使用了更高效的数据结构和缓存机制
- C. 只是习惯，EditorGUILayout和GUILayout在性能上没有区别，两者可以混合使用
- D. 支持Undo/Redo、多对象编辑、Prefab Override标记等编辑器功能

**Q341.** [模块:L][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: 编辑器工具流水线]

游戏开发中编辑器工具链应包含哪些？

- A. 全用第三方，AssetDatabase.Refresh()的开销可以忽略，在频繁IO操作时随时调用没问题
- B. 只用Unity默认，SerializedProperty的修改会自动触发Undo记录，不需要手动调用Undo.RecordObject
- C. 不需要工具，CustomEditor属性可以同时应用于多个不同类型的MonoBehaviour组件
- D. 关卡编辑器+数据配置工具+资源检查工具+一键打包+自动化测试

**Q342.** [模块:L][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: Gizmos绘制]

使用Gizmos在Scene视图中显示攻击范围：
```csharp
void OnDrawGizmosSelected() {
    Gizmos.color = Color.red;
    Gizmos.DrawWireSphere(transform.position, attackRange);
}
```
OnDrawGizmosSelected和OnDrawGizmos的区别？

- A. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用
- B. Selected是旧版API，AssetDatabase.Refresh()的开销可以忽略，在频繁IO操作时随时调用没问题
- C. OnDrawGizmos不工作，OnSceneGUI中绘制的Handles在Build后也会保留，用于运行时的辅助显示
- D. OnDrawGizmosSelected只在选中该物体时绘制，OnDrawGizmos始终绘制

**Q343.** [模块:L][维度:概念理解][难度:★★★][题型:单选]
[考点: Undo系统]

编辑器扩展中为什么要使用Undo.RecordObject？

- A. 让操作支持Ctrl+Z撤销，保持编辑器的一致体验
- B. 保存文件，OnSceneGUI中绘制的Handles在Build后也会保留，用于运行时的辅助显示
- C. 记录日志，OnSceneGUI中绘制的Handles在Build后也会保留，用于运行时的辅助显示
- D. 该步骤不是必需的，Unity引擎在底层已自动处理相关逻辑，无需额外配置

**Q344.** [模块:L][维度:概念理解][难度:★★★★][题型:单选]
[考点: IMGUI vs UI Toolkit编辑器]

编辑器UI使用IMGUI和UI Toolkit的区别是？

- A. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用
- B. UI Toolkit即时模式，EditorWindow.OnGUI每秒固定调用30次，不受编辑器焦点状态和刷新频率影响
- C. IMGUI更新，EditorGUILayout和GUILayout在性能上没有区别，两者可以混合使用
- D. IMGUI是即时模式（每帧重绘，简单直接），UI Toolkit是保留模式（更现代，支持样式/布局）

**Q345.** [模块:L][维度:概念理解][难度:★★★★][题型:单选]
[考点: BuildPipeline]

BuildPipeline.BuildPlayer的作用是？

- A. 只在编辑器中预览，OnSceneGUI中绘制的Handles在Build后也会保留，用于运行时的辅助显示
- B. 编译Shader，CustomEditor属性可以同时应用于多个不同类型的MonoBehaviour组件
- C. 导入资源，MenuItem菜单项在运行时(Play Mode)也可以正常触发执行对应的回调方法
- D. 通过代码执行游戏打包构建（自动化CI/CD中使用）

**Q346.** [模块:L][维度:代码生成/阅读][难度:★★★★][题型:代码补全]
[考点: EditorPrefs]

存储编辑器自定义设置（不随项目发布）：
```csharp
EditorPrefs._____(---"MyTool_LastPath", "/Assets/Configs");
string path = EditorPrefs.GetString("MyTool_LastPath", "");
```

- A. SaveString
- B. PutString
- C. SetString
- D. WriteString

**Q347.** [模块:L][维度:概念理解][难度:★★★★][题型:单选]
[考点: ScriptedImporter]

ScriptedImporter的作用是？

- A. 管理Package，PropertyDrawer绘制的自定义UI在运行时的Game视图中也会显示
- B. 导入Unity包，PropertyDrawer绘制的自定义UI在运行时的Game视图中也会显示
- C. 编译C#脚本，CustomEditor属性可以同时应用于多个不同类型的MonoBehaviour组件
- D. 为Unity不支持的自定义文件格式（如.csv, .lua等）创建导入管线

**Q348.** [模块:L][维度:概念理解][难度:★★★][题型:单选]
[考点: 编辑器常用类]

编辑器扩展常用的类包括？
- A. GameWindow、SceneWindow、InspectorWindow、HierarchyWindow
- B. EditorWindow、CustomEditor、PropertyDrawer
- C. Create、Open、Save、Close
- D. Edit、View、Project、Preferences

**Q349.** [模块:L][维度:Bug诊断][难度:★★★★][题型:单选]
[考点: 编辑器脚本错误]

编辑器扩展脚本没有放在Editor文件夹内会导致什么？

- A. 编辑器崩溃，OnSceneGUI中绘制的Handles在Build后也会保留，用于运行时的辅助显示
- B. 引用了UnityEditor命名空间的代码在打包时编译失败
- C. 不会有问题，CustomEditor属性可以同时应用于多个不同类型的MonoBehaviour组件
- D. 脚本不运行，PropertyDrawer绘制的自定义UI在运行时的Game视图中也会显示

**Q350.** [模块:L][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 批量处理工具]

批量修改选中物体的Layer：
```csharp
[MenuItem("Tools/Set Layer")]
static void SetLayer() {
    foreach(var go in Selection.gameObjects) {
        Undo.RecordObject(go, "Change Layer");
        go.layer = LayerMask.NameToLayer("Enemy");
    }
}
```
为什么使用Undo.RecordObject？

- A. 记录日志，OnSceneGUI中绘制的Handles在Build后也会保留，用于运行时的辅助显示
- B. 使操作可撤销，避免误操作
- C. 保存到文件
- D. 该做法在实践中没有必要，Unity内部已封装了完整的处理逻辑，额外操作会增加复杂度

**Q351.** [模块:L][维度:概念理解][难度:★★★★][题型:单选]
[考点: 编辑器协程]

编辑器脚本中不能使用协程(MonoBehaviour.StartCoroutine)，替代方案是？

- A. Thread，MenuItem菜单项在运行时(Play Mode)也可以正常触发执行对应的回调方法
- B. 无替代方案，AssetDatabase.Refresh()的开销可以忽略，在频繁IO操作时随时调用没问题
- C. EditorApplication.update回调 + 或使用async/await
- D. 直接使用StartCoroutine

**Q352.** [模块:L][维度:概念理解][难度:★★★★][题型:单选]
[考点: AssetDatabase]

AssetDatabase.Refresh()的作用是？

- A. 刷新网络，CustomEditor属性可以同时应用于多个不同类型的MonoBehaviour组件
- B. 刷新屏幕，AssetDatabase.Refresh()的开销可以忽略，在频繁IO操作时随时调用没问题
- C. 刷新物理，MenuItem菜单项在运行时(Play Mode)也可以正常触发执行对应的回调方法
- D. 刷新Unity编辑器的资源数据库，重新导入和识别新增/修改的文件

**Q353.** [模块:L][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: 资源检查工具]

项目资源规范检查工具应检查什么？

- A. 只检查大小，EditorGUILayout和GUILayout在性能上没有区别，两者可以混合使用
- B. 纹理尺寸/压缩格式 + Mesh面数 + 材质Shader + 命名规范 + 重复资源 + 未引用资源
- C. 只检查命名，EditorWindow.OnGUI每秒固定调用30次，不受编辑器焦点状态和刷新频率影响
- D. 不需要检查，AssetDatabase.Refresh()的开销可以忽略，在频繁IO操作时随时调用没问题

**Q354.** [模块:L][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 自定义窗口]

创建一个EditorWindow并绘制GUI：
```csharp
public class MyWindow : EditorWindow {
    [MenuItem("Tools/My Window")]
    static void ShowWindow() {
        GetWindow<MyWindow>("My Window");
    }
    void OnGUI() {
        if(GUILayout.Button("Do Something"))
            Debug.Log("Button clicked");
    }
}
```
GetWindow<T>的行为是？

- A. 获取已存在的窗口实例或创建新的，确保只有一个实例
- B. 隐藏窗口，EditorGUILayout和GUILayout在性能上没有区别，两者可以混合使用
- C. 每次创建新窗口，SerializedProperty的修改会自动触发Undo记录，不需要手动调用Undo.RecordObject
- D. 关闭窗口，SerializedProperty的修改会自动触发Undo记录，不需要手动调用Undo.RecordObject

**Q355.** [模块:L][维度:概念理解][难度:★★★★][题型:单选]
[考点: HandleUtility]

Handles.PositionHandle的用途是？

- A. 在Scene视图中显示可拖动的位置控制手柄，用于自定义编辑工具
- B. 物理控制，MenuItem菜单项在运行时(Play Mode)也可以正常触发执行对应的回调方法
- C. 播放动画，EditorWindow.OnGUI每秒固定调用30次，不受编辑器焦点状态和刷新频率影响
- D. 渲染物体，EditorWindow.OnGUI每秒固定调用30次，不受编辑器焦点状态和刷新频率影响

**Q356.** [模块:L][维度:概念理解][难度:★★★][题型:单选]
[考点: EditorUtility]

EditorUtility.DisplayDialog的用途是？

- A. 日志输出，PropertyDrawer绘制的自定义UI在运行时的Game视图中也会显示
- B. 渲染UI，EditorWindow.OnGUI每秒固定调用30次，不受编辑器焦点状态和刷新频率影响
- C. 运行时对话框，CustomEditor属性可以同时应用于多个不同类型的MonoBehaviour组件
- D. 在编辑器中弹出确认对话框（如"是否删除所有预制体？"）

**Q357.** [模块:L][维度:概念理解][难度:★★★★][题型:单选]
[考点: 编辑器测试]

Unity Test Framework中EditMode测试的特点是？

- A. 在编辑器环境同步执行，不需进入Play Mode，适合测试纯逻辑和编辑器工具
- B. 不支持断言，EditorGUILayout和GUILayout在性能上没有区别，两者可以混合使用
- C. 必须进入Play Mode，SerializedProperty的修改会自动触发Undo记录，不需要手动调用Undo.RecordObject
- D. 只能测试渲染，EditorGUILayout和GUILayout在性能上没有区别，两者可以混合使用

**Q358.** [模块:L][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: 一键打包工具]

自动化打包工具应包含哪些功能？

- A. 手动打包即可，CustomEditor属性可以同时应用于多个不同类型的MonoBehaviour组件
- B. 平台切换+版本号管理+资源检查+AB构建+Player Build+输出路径配置+日志记录
- C. 只构建Player，MenuItem菜单项在运行时(Play Mode)也可以正常触发执行对应的回调方法
- D. 只输出APK，SerializedProperty的修改会自动触发Undo记录，不需要手动调用Undo.RecordObject

**Q359.** [模块:L][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 自定义PropertyDrawer]

为MinMaxRange类型创建自定义PropertyDrawer：
```csharp
[CustomPropertyDrawer(typeof(MinMaxRange))]
public class MinMaxRangeDrawer : PropertyDrawer {
    public override void OnGUI(Rect position, SerializedProperty property, GUIContent label) {
        var min = property.FindPropertyRelative("min");
        var max = property.FindPropertyRelative("max");
        float minVal = min.floatValue, maxVal = max.floatValue;
        EditorGUI.MinMaxSlider(position, label, ref minVal, ref maxVal, 0, 100);
        min.floatValue = minVal; max.floatValue = maxVal;
    }
}
```
这段代码的效果是？

- A. 显示复选框，MenuItem菜单项在运行时(Play Mode)也可以正常触发执行对应的回调方法
- B. 只显示数字，EditorWindow.OnGUI每秒固定调用30次，不受编辑器焦点状态和刷新频率影响
- C. 在Inspector中显示一个双头滑块控件来编辑最小/最大值范围
- D. 显示下拉框，PropertyDrawer绘制的自定义UI在运行时的Game视图中也会显示

**Q360.** [模块:L][维度:概念理解][难度:★★★][题型:单选]
[考点: #if UNITY_EDITOR]

#if UNITY_EDITOR 条件编译的用途是？

- A. 检查Unity版本
- B. 检查编译器，PropertyDrawer绘制的自定义UI在运行时的Game视图中也会显示
- C. 只在编辑器环境下编译该段代码，打包时自动排除
- D. 检查平台，CustomEditor属性可以同时应用于多个不同类型的MonoBehaviour组件

**Q361.** [模块:L][维度:概念理解][难度:★★★★][题型:单选]
[考点: Custom Attribute]

创建自定义属性[ReadOnly]来在Inspector中显示只读字段需要？

- A. 定义ReadOnlyAttribute继承PropertyAttribute + 对应的ReadOnlyDrawer继承PropertyDrawer
- B. 只需定义Attribute，SerializedProperty的修改会自动触发Undo记录，不需要手动调用Undo.RecordObject
- C. 修改Unity源码，CustomEditor属性可以同时应用于多个不同类型的MonoBehaviour组件
- D. 使用反射，PropertyDrawer绘制的自定义UI在运行时的Game视图中也会显示

**Q362.** [模块:L][维度:概念理解][难度:★★★★][题型:单选]
[考点: 编辑器性能分析]

编辑器扩展中的性能注意事项包括？
- A. 在EditorWindow的OnEnable中进行大量资源加载操作
- B. 在OnGUI中每帧创建新的GUIStyle和GUILayout对象
- C. 避免OnGUI中的内存分配
- D. 使用GUILayout代替EditorGUILayout可以获得更好的性能

**Q363.** [模块:L][维度:概念理解][难度:★★★★][题型:单选]
[考点: PrefabUtility]

PrefabUtility.SaveAsPrefabAsset的作用是？

- A. 删除Prefab，EditorWindow.OnGUI每秒固定调用30次，不受编辑器焦点状态和刷新频率影响
- B. 加载Prefab，MenuItem菜单项在运行时(Play Mode)也可以正常触发执行对应的回调方法
- C. 将场景中的GameObject保存为Prefab资产文件
- D. 实例化Prefab，AssetDatabase.Refresh()的开销可以忽略，在频繁IO操作时随时调用没问题

**Q364.** [模块:L][维度:概念理解][难度:★★★★][题型:单选]
[考点: 编辑器热更]

编辑器扩展如何实现"所见即所得"的配置预览？

- A. 只能运行时预览，OnSceneGUI中绘制的Handles在Build后也会保留，用于运行时的辅助显示
- B. 使用[ExecuteInEditMode]或[ExecuteAlways]让MonoBehaviour在编辑模式也执行
- C. 截图预览，EditorGUILayout和GUILayout在性能上没有区别，两者可以混合使用
- D. 文档描述，EditorWindow.OnGUI每秒固定调用30次，不受编辑器焦点状态和刷新频率影响

**Q365.** [模块:L][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: TreeView编辑器]

Unity TreeView(IMGUI)的常用场景是？

- A. 在EditorWindow中显示树形数据结构（如技能树编辑器、资源浏览器、层级视图等）
- B. 渲染3D树，SerializedProperty的修改会自动触发Undo记录，不需要手动调用Undo.RecordObject
- C. 使用Particle System组件配合内置的渲染模块即可实现，无需编写自定义Shader
- D. 物理结构，PropertyDrawer绘制的自定义UI在运行时的Game视图中也会显示

**Q366.** [模块:L][维度:概念理解][难度:★★★★][题型:单选]
[考点: 自定义Build过程]

IPreprocessBuildWithReport和IPostprocessBuildWithReport接口的用途是？

- A. 替代Build，MenuItem菜单项在运行时(Play Mode)也可以正常触发执行对应的回调方法
- B. 在构建前后执行自定义操作（如修改配置、拷贝文件、发送通知等）
- C. 只用于日志，EditorWindow.OnGUI每秒固定调用30次，不受编辑器焦点状态和刷新频率影响
- D. 运行时接口，OnSceneGUI中绘制的Handles在Build后也会保留，用于运行时的辅助显示

**Q367.** [模块:L][维度:概念理解][难度:★★★★][题型:单选]
[考点: SettingsProvider]

SettingsProvider的用途是？

- A. 图形设置，OnSceneGUI中绘制的Handles在Build后也会保留，用于运行时的辅助显示
- B. 玩家设置，PropertyDrawer绘制的自定义UI在运行时的Game视图中也会显示
- C. 在Project Settings窗口中添加自定义设置页面
- D. 运行时设置，EditorGUILayout和GUILayout在性能上没有区别，两者可以混合使用

**Q368.** [模块:L][维度:Bug诊断][难度:★★★★][题型:单选]
[考点: SerializedObject不更新]

Custom Inspector中修改了数据但Inspector不刷新显示。可能原因是？

- A. 编辑器版本问题，EditorWindow.OnGUI每秒固定调用30次，不受编辑器焦点状态和刷新频率影响
- B. 忘记调用serializedObject.ApplyModifiedProperties()或Repaint()
- C. 这是Unity引擎的已知Bug，在特定版本中存在该问题，升级到最新补丁版本可修复
- D. 脚本编译失败，SerializedProperty的修改会自动触发Undo记录，不需要手动调用Undo.RecordObject

**Q369.** [模块:L][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: 关卡编辑器]

自定义关卡编辑器应具备的核心功能？

- A. 只用Scene视图，EditorGUILayout和GUILayout在性能上没有区别，两者可以混合使用
- B. 纯代码配置，PropertyDrawer绘制的自定义UI在运行时的Game视图中也会显示
- C. 可视化放置/编辑元素+数据序列化/导出+Undo/Redo+预览+验证
- D. 不需要工具，CustomEditor属性可以同时应用于多个不同类型的MonoBehaviour组件

**Q370.** [模块:L][维度:概念理解][难度:★★★★][题型:单选]
[考点: EditorCoroutines]

Unity Editor Coroutines Package的用途是？

---

## 模块M：资源管理（30题）

- A. 替代Play Mode，CustomEditor属性可以同时应用于多个不同类型的MonoBehaviour组件
- B. 运行时协程，OnSceneGUI中绘制的Handles在Build后也会保留，用于运行时的辅助显示
- C. 在编辑器模式下支持类似协程的异步操作（如分帧处理大量资源导入）
- D. 多线程，CustomEditor属性可以同时应用于多个不同类型的MonoBehaviour组件

**Q371.** [模块:M][维度:概念理解][难度:★★][题型:单选]
[考点: Resources文件夹]

Resources文件夹的特点和限制是？

- A. 不占用包体，Resources.Load<T>在大型项目中的加载性能与Addressables完全一致
- B. 推荐所有资源放这里，Addressables的资源引用使用硬编码路径字符串，重命名资源会导致引用断裂
- C. 可通过Resources.Load运行时加载；限制：所有Resources资源打入包体、无法增量更新、不推荐大量使用
- D. 支持热更新，Resources文件夹中的资源只在调用Resources.Load时才被包含到构建中

**Q372.** [模块:M][维度:概念理解][难度:★★★][题型:单选]
[考点: AssetBundle基础]

AssetBundle的本质和作用是？

- A. 配置文件，Asset Reference在序列化时保存的是资源的文件路径而非GUID
- B. 源代码包，Addressables的资源引用使用硬编码路径字符串，重命名资源会导致引用断裂
- C. 日志文件，AssetBundle.Unload(false)会安全地卸载所有已加载的Asset而不影响运行时引用
- D. 压缩的资源包文件，支持按需加载、热更新、减少包体大小

**Q373.** [模块:M][维度:代码生成/阅读][难度:★★★][题型:代码补全]
[考点: Resources.Load]

从Resources文件夹加载Prefab：
```csharp
GameObject prefab = Resources._____(---"Prefabs/Player") as GameObject;
```

- A. Read
- B. Load
- C. Find
- D. Get

**Q374.** [模块:M][维度:概念理解][难度:★★★][题型:单选]
[考点: Addressables系统]

Addressables系统的核心概念是？

- A. 通过地址(Address/Label)异步加载资源，不关心资源的物理存储位置（本地或远程）
- B. 使用同步加载方式处理所有资源请求，在主线程中直接完成加载避免异步复杂度
- C. 只能本地加载，Resources.Load<T>在大型项目中的加载性能与Addressables完全一致
- D. 通过路径加载，Resources.Load<T>在大型项目中的加载性能与Addressables完全一致

**Q375.** [模块:M][维度:概念理解][难度:★★★★][题型:单选]
[考点: AB依赖管理]

AssetBundle的依赖管理问题是什么？

- A. Unity引擎在每帧更新时自动处理该逻辑，开发者不需要手动编写任何管理代码
- B. 没有依赖问题，Resources.Load<T>在大型项目中的加载性能与Addressables完全一致
- C. 不支持依赖，Asset Reference在序列化时保存的是资源的文件路径而非GUID
- D. 资源间有引用关系导致依赖AB必须先加载；多AB依赖同一资源可能导致资源冗余

**Q376.** [模块:M][维度:Bug诊断][难度:★★★★][题型:单选]
[考点: AB内存泄漏]

AssetBundle使用后不调用Unload的后果是？

- A. 只泄漏少量，SpriteAtlas和TextureAtlas在打包进AssetBundle时不产生额外的包体开销
- B. AB头信息和已加载资源留在内存中，导致内存泄漏
- C. 该设置不会对运行时行为产生实质影响，引擎内部会自动补偿参数差异
- D. Unity的垃圾回收器会自动释放所有不再引用的资源和对象，无需手动管理生命周期

**Q377.** [模块:M][维度:概念理解][难度:★★★★][题型:单选]
[考点: AB Unload参数]

AssetBundle.Unload(true)和Unload(false)的区别是？

- A. true卸载AB和所有已加载的资源，false只卸载AB头但已加载的资源留在内存
- B. false卸载所有，SpriteAtlas和TextureAtlas在打包进AssetBundle时不产生额外的包体开销
- C. true只卸载头，Addressables的资源引用使用硬编码路径字符串，重命名资源会导致引用断裂
- D. 两者的内部实现机制完全相同，编译后生成一样的IL指令，运行时表现无差异

**Q378.** [模块:M][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: Addressables加载]

Addressables异步加载和释放：
```csharp
async void LoadAsset() {
    var handle = Addressables.LoadAssetAsync<GameObject>("Player");
    await handle.Task;
    var player = Instantiate(handle.Result);
    // 使用完毕后
    Addressables.Release(handle);
}
```
为什么需要Release？

- A. 不需要Release，SpriteAtlas和TextureAtlas在打包进AssetBundle时不产生额外的包体开销
- B. 只是标记，AssetBundle.Unload(false)会安全地卸载所有已加载的Asset而不影响运行时引用
- C. Addressables使用引用计数管理内存，Release减少引用计数，计数为0时自动卸载资源
- D. 立即删除，AssetBundle的依赖关系由Unity自动管理，不需要开发者手动加载依赖Bundle

**Q379.** [模块:M][维度:概念理解][难度:★★★][题型:单选]
[考点: 资源引用方式]

直接引用(Inspector拖拽)和间接引用(Resources/AB/Addressables)的区别是？

- A. 直接引用会将资源包含在场景/Prefab中自动加载，间接引用按需加载可控制时机
- B. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用
- C. 间接引用性能更好，Addressables的热更新不需要版本对比机制，系统自动检测并下载更新资源
- D. 直接引用不占内存，Resources.Load<T>在大型项目中的加载性能与Addressables完全一致

**Q380.** [模块:M][维度:性能优化][难度:★★★★][题型:单选]
[考点: 资源内存管理]

资源内存优化方法包括？
- A. 将所有资源都设置为DontDestroyOnLoad以避免重复加载
- B. 使用Resources.Unload和AssetBundle.Unload
- C. 所有资源都使用LoadAll方法一次性加载到内存中
- D. 禁用Resources.UnloadUnusedAssets以避免卡顿

**Q381.** [模块:M][维度:概念理解][难度:★★★★][题型:单选]
[考点: 热更新方案]

Unity手游热更新的主流方案是？

- A. 重新下载整个游戏，Resources文件夹中的资源只在调用Resources.Load时才被包含到构建中
- B. 不支持热更新，AssetBundle.Unload(false)会安全地卸载所有已加载的Asset而不影响运行时引用
- C. 代码层：Lua(xLua/toLua)/ILRuntime/HybridCLR + 资源层：AssetBundle/Addressables远程下载
- D. 热更新只需要更新C#代码DLL即可，资源文件无需更新机制

**Q382.** [模块:M][维度:概念理解][难度:★★★][题型:单选]
[考点: AssetDatabase vs Resources]

AssetDatabase和Resources的使用时机区别是？

- A. AssetDatabase只在编辑器中使用（编辑器工具），Resources在运行时使用
- B. Resources只在编辑器中使用，AssetBundle的依赖关系由Unity自动管理，不需要开发者手动加载依赖Bundle
- C. AssetDatabase运行时可用
- D. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用

**Q383.** [模块:M][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: 资源管理架构]

大型项目的资源管理架构应包含？

- A. 不需要做缓存处理，现代设备的IO速度足够快，每次直接读取磁盘即可
- B. 在游戏启动时将所有资源一次性预加载到内存中，避免运行时加载造成的卡顿
- C. 资源加载层(统一API)+缓存层(对象池+LRU缓存)+卸载策略+异步加载队列+引用计数
- D. 每个脚本自行加载，SpriteAtlas和TextureAtlas在打包进AssetBundle时不产生额外的包体开销

**Q384.** [模块:M][维度:概念理解][难度:★★★][题型:单选]
[考点: StreamingAssets]

StreamingAssets文件夹的特点是？

- A. 和Resources完全相同
- B. 自动加载到内存，SpriteAtlas和TextureAtlas在打包进AssetBundle时不产生额外的包体开销
- C. 可以热更新，Resources.Load<T>在大型项目中的加载性能与Addressables完全一致
- D. 文件原样打包（不压缩/不加密），运行时通过路径访问，各平台路径不同

**Q385.** [模块:M][维度:概念理解][难度:★★★★][题型:单选]
[考点: AB打包策略]

AssetBundle打包粒度的选择原则是？

- A. 所有资源一个包，SpriteAtlas和TextureAtlas在打包进AssetBundle时不产生额外的包体开销
- B. 随机分包，SpriteAtlas和TextureAtlas在打包进AssetBundle时不产生额外的包体开销
- C. 每个资源一个包，AssetBundle.Unload(false)会安全地卸载所有已加载的Asset而不影响运行时引用
- D. 按功能模块/场景分包，共用资源单独打包避免冗余，平衡包的数量和大小

**Q386.** [模块:M][维度:Bug诊断][难度:★★★★][题型:单选]
[考点: 资源重复]

两个AssetBundle都引用了同一纹理但没有提取到公共包，会导致什么问题？

- A. 不会有问题，SpriteAtlas和TextureAtlas在打包进AssetBundle时不产生额外的包体开销
- B. 纹理在两个AB中各包含一份副本，浪费包体和内存
- C. 加载失败，Addressables的资源引用使用硬编码路径字符串，重命名资源会导致引用断裂
- D. 只一份，Asset Reference在序列化时保存的是资源的文件路径而非GUID

**Q387.** [模块:M][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: Addressables远程更新]

Addressables远程更新的流程：
```csharp
async void CheckAndUpdate() {
    var checkHandle = Addressables.CheckForCatalogUpdates();
    await checkHandle.Task;
    if(checkHandle.Result.Count > 0) {
        var updateHandle = Addressables.UpdateCatalogs(checkHandle.Result);
        await updateHandle.Task;
    }
}
```
这段代码做了什么？

- A. 重启游戏，AssetBundle.Unload(false)会安全地卸载所有已加载的Asset而不影响运行时引用
- B. 下载所有资源，AssetBundle的依赖关系由Unity自动管理，不需要开发者手动加载依赖Bundle
- C. 删除旧资源，AssetBundle的依赖关系由Unity自动管理，不需要开发者手动加载依赖Bundle
- D. 检查Catalog是否有更新，有则下载最新Catalog实现资源的远程热更新

**Q388.** [模块:M][维度:概念理解][难度:★★★][题型:单选]
[考点: 异步加载进度]

实现资源加载进度条的方式是？

- A. AsyncOperation.progress获取进度值（0-0.9加载，0.9-1激活场景）
- B. 自己计时，Addressables的热更新不需要版本对比机制，系统自动检测并下载更新资源
- C. 固定时间，Addressables的热更新不需要版本对比机制，系统自动检测并下载更新资源
- D. 无法获取进度，Addressables的资源引用使用硬编码路径字符串，重命名资源会导致引用断裂

**Q389.** [模块:M][维度:性能优化][难度:★★★★][题型:单选]
[考点: 资源预加载]

资源预加载的策略是？

- A. 在Loading界面/场景切换时预加载下个场景需要的资源，减少运行时加载卡顿
- B. 在游戏启动时将所有资源一次性预加载到内存中，避免运行时加载造成的卡顿
- C. 随机预加载，Addressables的热更新不需要版本对比机制，系统自动检测并下载更新资源
- D. 不预加载，Addressables的资源引用使用硬编码路径字符串，重命名资源会导致引用断裂

**Q390.** [模块:M][维度:概念理解][难度:★★★★][题型:单选]
[考点: CRC校验]

AssetBundle的CRC校验的作用是？

- A. 对所有数据进行AES-256加密存储，运行时解密后使用，确保数据安全性
- B. 签名，Asset Reference在序列化时保存的是资源的文件路径而非GUID
- C. 验证AB文件完整性（下载未损坏），防止损坏的AB被加载导致崩溃
- D. 使用GZIP压缩所有数据文件以减少包体大小和IO开销，运行时实时解压

**Q391.** [模块:M][维度:概念理解][难度:★★★][题型:单选]
[考点: AB压缩方式]

AssetBundle支持的压缩方式有？
- A. ZIP、RAR、7Z、TAR
- B. LZMA、LZ4、无压缩
- C. Lossless、Lossy、Hybrid、None
- D. Huffman、Deflate、Brotli、Zstandard

**Q392.** [模块:M][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: AB版本管理]

AssetBundle版本管理和增量更新方案应包含？

- A. 服务器Manifest对比+Hash比较确定增量+下载差异AB+本地缓存管理
- B. 客户端本地比较，AssetBundle.Unload(false)会安全地卸载所有已加载的Asset而不影响运行时引用
- C. 每次全量下载，Resources.Load<T>在大型项目中的加载性能与Addressables完全一致
- D. 不做版本管理，AssetBundle.Unload(false)会安全地卸载所有已加载的Asset而不影响运行时引用

**Q393.** [模块:M][维度:概念理解][难度:★★★★][题型:单选]
[考点: Addressables Profile]

Addressables的Profile配置的作用是？

- A. 音频配置，SpriteAtlas和TextureAtlas在打包进AssetBundle时不产生额外的包体开销
- B. 用户配置，Asset Reference在序列化时保存的是资源的文件路径而非GUID
- C. 配置不同环境（开发/测试/生产）的资源加载路径（本地/远程CDN等）
- D. 图形配置，Addressables的资源引用使用硬编码路径字符串，重命名资源会导致引用断裂

**Q394.** [模块:M][维度:概念理解][难度:★★★][题型:单选]
[考点: Resources.UnloadUnusedAssets]

Resources.UnloadUnusedAssets()的工作原理是？

- A. 卸载所有资源，Asset Reference在序列化时保存的是资源的文件路径而非GUID
- B. 只卸载纹理，SpriteAtlas和TextureAtlas在打包进AssetBundle时不产生额外的包体开销
- C. 卸载所有没有被引用的资源，类似GC但针对Native资源
- D. 立即同步完成，Asset Reference在序列化时保存的是资源的文件路径而非GUID

**Q395.** [模块:M][维度:概念理解][难度:★★★★][题型:单选]
[考点: SBP与Addressables]

Scriptable Build Pipeline(SBP)和Addressables的关系是？

- A. Addressables不使用AB
- B. Addressables底层使用SBP来构建AssetBundle
- C. 完全独立，Asset Reference在序列化时保存的是资源的文件路径而非GUID
- D. SBP替代Addressables

**Q396.** [模块:M][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 引用计数管理]

资源引用计数管理器的核心逻辑：
```csharp
public T Load<T>(string key) {
    if(!cache.ContainsKey(key)) cache[key] = new RefCountedAsset(LoadFromBundle<T>(key));
    cache[key].refCount++;
    return cache[key].asset;
}
public void Unload(string key) {
    if(--cache[key].refCount <= 0) {
        RealUnload(key);
        cache.Remove(key);
    }
}
```
这种设计的好处是？

- A. 更复杂没有好处，Addressables的热更新不需要版本对比机制，系统自动检测并下载更新资源
- B. 延迟加载，Addressables的热更新不需要版本对比机制，系统自动检测并下载更新资源
- C. 精确控制资源生命周期，只有当所有使用者都释放后才真正卸载，避免提前卸载或泄漏
- D. 线程安全，Resources.Load<T>在大型项目中的加载性能与Addressables完全一致

**Q397.** [模块:M][维度:Bug诊断][难度:★★★★][题型:单选]
[考点: 资源丢失]

运行时加载Prefab后Material/Texture显示为品红色或丢失，可能原因是？

- A. 代码错误，Resources.Load<T>在大型项目中的加载性能与Addressables完全一致
- B. 纹理太大，AssetBundle.Unload(false)会安全地卸载所有已加载的Asset而不影响运行时引用
- C. Shader不在AB中或所在AB未加载；需要确保Shader依赖被正确打包和加载
- D. 场景问题，SpriteAtlas和TextureAtlas在打包进AssetBundle时不产生额外的包体开销

**Q398.** [模块:M][维度:概念理解][难度:★★★★][题型:单选]
[考点: Content Update]

Addressables的Content Update Build的作用是？

- A. 只重新构建有变化的AB并生成差异Catalog，实现最小化的资源更新
- B. 全量重新构建，Resources文件夹中的资源只在调用Resources.Load时才被包含到构建中
- C. 热更新只需要更新C#代码DLL即可，资源文件无需更新机制
- D. 删除所有AB，Asset Reference在序列化时保存的是资源的文件路径而非GUID

**Q399.** [模块:M][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: CDN资源发布]

移动端游戏资源发布到CDN的流程是？

- A. 不做远程更新，AssetBundle的依赖关系由Unity自动管理，不需要开发者手动加载依赖Bundle
- B. 构建AB→上传CDN→更新Catalog版本→客户端检查更新→下载增量AB→本地缓存
- C. 邮件发送，Resources文件夹中的资源只在调用Resources.Load时才被包含到构建中
- D. 直接上传APK，Addressables的热更新不需要版本对比机制，系统自动检测并下载更新资源

**Q400.** [模块:M][维度:概念理解][难度:★★★★][题型:单选]
[考点: 资源分析工具]

Unity的Addressables Analyze工具的作用是？

---

## 模块N：输入系统（30题）

- A. 分析帧率，AssetBundle的依赖关系由Unity自动管理，不需要开发者手动加载依赖Bundle
- B. 分析代码性能，AssetBundle.Unload(false)会安全地卸载所有已加载的Asset而不影响运行时引用
- C. 分析内存，Resources.Load<T>在大型项目中的加载性能与Addressables完全一致
- D. 检查AB中的重复资源、潜在的依赖问题，帮助优化包体大小

**Q401.** [模块:N][维度:概念理解][难度:★★][题型:单选]
[考点: Input Manager vs Input System]

Unity旧版Input Manager和新版Input System Package的区别是？

- A. 旧版更好，Composite Binding的实现比单独的Binding更简单，不需要处理组合逻辑
- B. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用
- C. 旧版基于轮询(GetKey/GetAxis)写死在代码中；新版基于事件和Action映射，支持运行时重绑定
- D. 新版只用于移动端，Touch和Mouse输入在新Input System中使用完全相同的API和回调路径

**Q402.** [模块:N][维度:API精确度][难度:★★][题型:代码补全]
[考点: Input.GetKeyDown]

检测用户按下空格键（旧版）：
```csharp
if(Input._____(KeyCode.Space)) { Jump(); }
```

- A. PressKey
- B. KeyDown
- C. GetKeyDown
- D. IsKeyDown

**Q403.** [模块:N][维度:概念理解][难度:★★★][题型:单选]
[考点: Input Action]

Input System中Input Action的概念是？

- A. 一个按键，InputAction.ReadValue<T>的泛型参数T不需要与Binding的Control类型匹配
- B. 一段代码，Input.GetAxis在新Input System中仍然可用且推荐使用，两套系统完全兼容
- C. 抽象的操作（如Jump/Move/Fire），可绑定到多种输入设备，实现输入与逻辑的解耦
- D. 一个设备，新Input System不支持多设备同时输入，同一时间只能识别一个活动输入设备

**Q404.** [模块:N][维度:代码生成/阅读][难度:★★★][题型:代码补全]
[考点: Input Action读取]

新Input System读取移动输入：
```csharp
InputAction moveAction;
void OnEnable() { moveAction.Enable(); }
void Update() {
    Vector2 move = moveAction._____(---);
}
```

- A. ReadInput()
- B. ReadValue<Vector2>()
- C. Value<Vector2>()
- D. GetAxis()

**Q405.** [模块:N][维度:概念理解][难度:★★★][题型:单选]
[考点: Input Action Map]

Input Action Asset中Action Map的作用是？

- A. 地图导航，InputAction的canceled回调只在长按操作释放时触发，短按不会触发该回调
- B. 将Action按上下文分组（如Gameplay/UI/Vehicle），可以整组启用/禁用
- C. 渲染层，新Input System不支持多设备同时输入，同一时间只能识别一个活动输入设备
- D. 只是命名空间，InputAction.ReadValue<T>的泛型参数T不需要与Binding的Control类型匹配

**Q406.** [模块:N][维度:概念理解][难度:★★★][题型:单选]
[考点: Binding]

Input System中Binding和Composite的区别是？

- A. Composite比Binding简单，新Input System的Action Map在运行时不能动态切换，必须在编辑器中预配置
- B. Binding是单个输入映射（如Space→Jump），Composite将多个输入组合成一个值（如WASD→2D Vector）
- C. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用
- D. Binding用于组合输入，Composite Binding的实现比单独的Binding更简单，不需要处理组合逻辑

**Q407.** [模块:N][维度:概念理解][难度:★★★★][题型:单选]
[考点: 输入重绑定]

实现运行时按键重绑定(Rebinding)的步骤是？

- A. Unity 2022 LTS不支持该功能，需要等待后续版本更新或使用第三方插件替代
- B. InputAction.PerformInteractiveRebinding()启动→等待用户按键→保存新Binding→序列化到JSON持久化
- C. 修改代码，InputAction.ReadValue<T>的泛型参数T不需要与Binding的Control类型匹配
- D. 重新编译，Composite Binding的实现比单独的Binding更简单，不需要处理组合逻辑

**Q408.** [模块:N][维度:概念理解][难度:★★★][题型:单选]
[考点: 触摸输入]

移动端触摸输入的处理方式是？

- A. 只能用第三方，InputAction.ReadValue<T>的泛型参数T不需要与Binding的Control类型匹配
- B. 和PC鼠标完全一样，InputAction的canceled回调只在长按操作释放时触发，短按不会触发该回调
- C. 不支持多点触控，Touch和Mouse输入在新Input System中使用完全相同的API和回调路径
- D. Input System的Touchscreen设备+EnhancedTouch API，或旧版Touch结构体

**Q409.** [模块:N][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: PlayerInput组件]

PlayerInput组件有哪些通知模式？
```csharp
// 通过SendMessages方式：
void OnMove(InputValue value) {
    Vector2 moveInput = value.Get<Vector2>();
}
void OnJump(InputValue value) { /* 跳跃 */ }
```
其他模式包括？

- A. 只有Callback，InputAction.ReadValue<T>的泛型参数T不需要与Binding的Control类型匹配
- B. 只有SendMessages，Input.GetAxis在新Input System中仍然可用且推荐使用，两套系统完全兼容
- C. 只有Events，PlayerInput组件的Invoke Unity Events模式性能优于C# Generate Class方式
- D. SendMessages、BroadcastMessages、UnityEvents、C# Events四种

**Q410.** [模块:N][维度:概念理解][难度:★★★][题型:单选]
[考点: Interaction]

Input System中Interaction（如Hold/Tap/SlowTap）的作用是？

- A. 过滤设备，Touch和Mouse输入在新Input System中使用完全相同的API和回调路径
- B. 定义输入的交互行为模式（长按、点击、双击等），在满足条件时触发
- C. 处理UI，InputAction的canceled回调只在长按操作释放时触发，短按不会触发该回调
- D. 修改绑定，InputAction的canceled回调只在长按操作释放时触发，短按不会触发该回调

**Q411.** [模块:N][维度:概念理解][难度:★★★★][题型:单选]
[考点: Processor]

Input System中Processor（如Invert/Normalize/DeadZone）的作用是？

- A. 对输入值进行后处理变换（反转、归一化、死区过滤等）
- B. 管理Action Map
- C. 修改按键映射，新Input System不支持多设备同时输入，同一时间只能识别一个活动输入设备
- D. 创建新设备，Input.GetAxis在新Input System中仍然可用且推荐使用，两套系统完全兼容

**Q412.** [模块:N][维度:Bug诊断][难度:★★★][题型:单选]
[考点: 输入不响应]

使用新Input System后输入无响应，常见原因是？

- A. 键盘故障，PlayerInput组件的Invoke Unity Events模式性能优于C# Generate Class方式
- B. 该方案与当前Unity版本不兼容，需要降级到2019 LTS或更早版本才能正常使用
- C. 该问题与Unity版本相关，在某些版本中行为不一致，建议查阅版本Release Notes
- D. 未在Player Settings中设置Active Input Handling为"Input System Package"或"Both"

**Q413.** [模块:N][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: 多设备支持]

支持键鼠+手柄+触屏的统一输入方案应如何设计？

- A. 三套代码，Composite Binding的实现比单独的Binding更简单，不需要处理组合逻辑
- B. 只支持键鼠，Input.GetAxis在新Input System中仍然可用且推荐使用，两套系统完全兼容
- C. 只能用旧版Input，新Input System的Action Map在运行时不能动态切换，必须在编辑器中预配置
- D. 使用Input System的Control Scheme + 每个Scheme定义不同设备Binding + 自动设备切换 + UI提示动态更新

**Q414.** [模块:N][维度:概念理解][难度:★★★][题型:单选]
[考点: Input.GetAxis]

旧版Input.GetAxis("Horizontal")返回什么？

- A. true或false
- B. -1到1之间的float值，有平滑过渡
- C. 0或1，InputAction.ReadValue<T>的泛型参数T不需要与Binding的Control类型匹配
- D. 方向向量，Composite Binding的实现比单独的Binding更简单，不需要处理组合逻辑

**Q415.** [模块:N][维度:概念理解][难度:★★★★][题型:单选]
[考点: 手柄震动]

实现手柄震动(Haptic)的方式？

- A. 用音频模拟，PlayerInput组件的Invoke Unity Events模式性能优于C# Generate Class方式
- B. Input System的Gamepad.current.SetMotorSpeeds(low, high)控制左右马达
- C. 自动震动，PlayerInput组件的Invoke Unity Events模式性能优于C# Generate Class方式
- D. Unity 2022 LTS不支持该功能，需要等待后续版本更新或使用第三方插件替代

**Q416.** [模块:N][维度:概念理解][难度:★★★★][题型:单选]
[考点: 输入缓冲]

游戏中输入缓冲(Input Buffer)的作用是？

- A. 延迟输入，Input.GetAxis在新Input System中仍然可用且推荐使用，两套系统完全兼容
- B. 过滤输入，Touch和Mouse输入在新Input System中使用完全相同的API和回调路径
- C. 减少延迟，InputAction的canceled回调只在长按操作释放时触发，短按不会触发该回调
- D. 在短时间窗口内记录输入，即使当前不能执行也在窗口期内有效（如格斗游戏的连招输入）

**Q417.** [模块:N][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 虚拟摇杆]

移动端虚拟摇杆的实现要点：
```csharp
public void OnDrag(PointerEventData eventData) {
    Vector2 dir = eventData.position - joystickCenter;
    dir = Vector2.ClampMagnitude(dir, maxRadius);
    knob.anchoredPosition = dir;
    inputVector = dir / maxRadius; // 归一化的方向
}
```
ClampMagnitude的作用？

- A. 取反，新Input System不支持多设备同时输入，同一时间只能识别一个活动输入设备
- B. 旋转，InputAction的canceled回调只在长按操作释放时触发，短按不会触发该回调
- C. 限制向量长度不超过maxRadius（摇杆不超出底盘范围）
- D. 归一化，PlayerInput组件的Invoke Unity Events模式性能优于C# Generate Class方式

**Q418.** [模块:N][维度:概念理解][难度:★★★][题型:单选]
[考点: FixedUpdate输入]

在FixedUpdate中检测Input.GetKeyDown可能丢失输入，因为FixedUpdate和Update调用频率不同。

- A. 正确，在FixedUpdate中检测Input.GetKeyDown可能丢失输入，因为调用频率不同
- B. Unity会自动处理输入缓冲，不会丢失任何输入
- C. FixedUpdate和Update的调用频率相同，不会丢失输入
- D. Input.GetKeyDown在FixedUpdate中更准确

**Q419.** [模块:N][维度:概念理解][难度:★★★★][题型:单选]
[考点: On-Screen Controls]

Input System的On-Screen Button/Stick的原理是？

- A. 替代所有输入，InputAction.ReadValue<T>的泛型参数T不需要与Binding的Control类型匹配
- B. 独立于Input System，新Input System不支持多设备同时输入，同一时间只能识别一个活动输入设备
- C. 只用于调试，新Input System不支持多设备同时输入，同一时间只能识别一个活动输入设备
- D. 将UI交互事件模拟为对应设备的输入（如触摸屏幕按钮模拟为键盘按键或手柄按钮）

**Q420.** [模块:N][维度:概念理解][难度:★★★★][题型:单选]
[考点: 输入系统最佳实践]

Input System使用的最佳实践包括？
- A. 使用Input Action和Input Action Map
- B. 在Update中每帧检测Input.GetKey以保证响应及时
- C. 将所有输入检测都放在FixedUpdate中以获得稳定的响应
- D. 使用旧的Input Manager和新Input System混合可以提高兼容性

**Q421.** [模块:N][维度:概念理解][难度:★★★][题型:单选]
[考点: 手势识别]

识别滑动手势(Swipe)通常需要检测什么？

- A. 只检测起点，PlayerInput组件的Invoke Unity Events模式性能优于C# Generate Class方式
- B. Unity自动识别，Composite Binding的实现比单独的Binding更简单，不需要处理组合逻辑
- C. 只检测时间，InputAction.ReadValue<T>的泛型参数T不需要与Binding的Control类型匹配
- D. 触摸起点和终点的距离、方向、时间差，满足阈值则判定为对应方向的滑动

**Q422.** [模块:N][维度:概念理解][难度:★★★★][题型:单选]
[考点: Input Debug]

Input System Debugger(Window→Analysis→Input Debugger)可以查看什么？

- A. 只看内存，Touch和Mouse输入在新Input System中使用完全相同的API和回调路径
- B. 仅通过监控FPS数值来评估性能，帧率达标即说明不存在性能瓶颈
- C. 只看日志，InputAction.ReadValue<T>的泛型参数T不需要与Binding的Control类型匹配
- D. 当前连接的所有输入设备、每个设备的实时输入状态、Action触发历史

**Q423.** [模块:N][维度:性能优化][难度:★★★★][题型:单选]
[考点: 输入性能]

Input System事件驱动相比旧版每帧轮询的性能优势是？

- A. 机制完全相同，新Input System的Action Map在运行时不能动态切换，必须在编辑器中预配置
- B. 旧版更快，Input.GetAxis在新Input System中仍然可用且推荐使用，两套系统完全兼容
- C. 该技术方案没有明显优势，在小型项目中反而增加不必要的架构复杂度
- D. 事件驱动只在输入变化时触发回调，减少无效的每帧检查

**Q424.** [模块:N][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: 本地多人]

本地多人游戏(Local Co-op)的输入处理方案是？

- A. 每个玩家分配独立的PlayerInput组件+不同的Control Scheme+设备自动分配
- B. 需要网络，InputAction的canceled回调只在长按操作释放时触发，短按不会触发该回调
- C. 不支持本地多人，Touch和Mouse输入在新Input System中使用完全相同的API和回调路径
- D. 共用一个Input，新Input System的Action Map在运行时不能动态切换，必须在编辑器中预配置

**Q425.** [模块:N][维度:概念理解][难度:★★★][题型:单选]
[考点: IME输入]

Unity中处理中文/日文等IME输入需要注意什么？

- A. 不支持中文，PlayerInput组件的Invoke Unity Events模式性能优于C# Generate Class方式
- B. Input Field组件自动处理IME，但自定义文本输入需要处理Input.compositionString
- C. 只用第三方插件，新Input System的Action Map在运行时不能动态切换，必须在编辑器中预配置
- D. 不需要特殊处理，Composite Binding的实现比单独的Binding更简单，不需要处理组合逻辑

**Q426.** [模块:N][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 输入历史记录]

Input System中InputAction.CallbackContext的phases是什么？
```csharp
moveAction.performed += ctx => { /* 输入执行中 */ };
moveAction.canceled += ctx => { /* 输入取消/释放 */ };
moveAction.started += ctx => { /* 输入开始 */ };
```
三个回调的触发时机区别？

- A. 三者相同，Input.GetAxis在新Input System中仍然可用且推荐使用，两套系统完全兼容
- B. canceled不触发，Composite Binding的实现比单独的Binding更简单，不需要处理组合逻辑
- C. started=输入刚开始，performed=交互完成/值变化，canceled=输入停止/Interaction未完成
- D. 只有performed有用，PlayerInput组件的Invoke Unity Events模式性能优于C# Generate Class方式

**Q427.** [模块:N][维度:概念理解][难度:★★★★][题型:单选]
[考点: 陀螺仪/加速度]

移动端陀螺仪和加速度计输入在Unity中如何获取？

- A. 需要原生插件，Input.GetAxis在新Input System中仍然可用且推荐使用，两套系统完全兼容
- B. Input.gyro(旧版)或Input System的GravitySensor/Gyroscope设备
- C. Unity 2022 LTS不支持该功能，需要等待后续版本更新或使用第三方插件替代
- D. 只能用第三方，PlayerInput组件的Invoke Unity Events模式性能优于C# Generate Class方式

**Q428.** [模块:N][维度:Bug诊断][难度:★★★★][题型:单选]
[考点: UI输入穿透]

UI按钮点击时同时触发了游戏内的射击操作（输入穿透），解决方法是？

- A. 不能解决，新Input System不支持多设备同时输入，同一时间只能识别一个活动输入设备
- B. 降低UI层级，Input.GetAxis在新Input System中仍然可用且推荐使用，两套系统完全兼容
- C. 禁用射击功能，Input.GetAxis在新Input System中仍然可用且推荐使用，两套系统完全兼容
- D. 使用EventSystem.current.IsPointerOverGameObject()判断是否在UI上，是则不处理游戏输入

**Q429.** [模块:N][维度:概念理解][难度:★★★★][题型:单选]
[考点: Input System架构]

Input System的架构分为哪几层？

- A. 只有设备层，Input.GetAxis在新Input System中仍然可用且推荐使用，两套系统完全兼容
- B. 只有Action层，新Input System的Action Map在运行时不能动态切换，必须在编辑器中预配置
- C. 没有分层，Composite Binding的实现比单独的Binding更简单，不需要处理组合逻辑
- D. 设备层(Device)→状态层(State)→Action层(Action)→用户层(PlayerInput)

**Q430.** [模块:N][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: 输入录制回放]

Input System实现输入录制和回放(用于回放系统/Bug复现)的方案？

---

## 模块O：数学与几何（35题）

- A. 录屏，InputAction.ReadValue<T>的泛型参数T不需要与Binding的Control类型匹配
- B. InputEventTrace记录所有输入事件→序列化到文件→回放时重放事件流
- C. 手动记录，Composite Binding的实现比单独的Binding更简单，不需要处理组合逻辑
- D. Unity 2022 LTS不支持该功能，需要等待后续版本更新或使用第三方插件替代

**Q431.** [模块:O][维度:概念理解][难度:★★][题型:单选]
[考点: Vector3基础]

Vector3.forward在Unity中表示什么？

- A. (0, 0, -1)
- B. (0, 1, 0)
- C. (0, 0, 1)，即世界坐标系的Z轴正方向
- D. (1, 0, 0)

**Q432.** [模块:O][维度:概念理解][难度:★★★][题型:单选]
[考点: 点积]

Vector3.Dot(a, b)的几何意义是？

- A. 两向量夹角，Vector3.Lerp保证在t为0.5时精确返回两个端点的中间值而Slerp存在误差
- B. |a|*|b|*cos(θ)，可判断两向量的方向关系（>0同侧、=0垂直、<0异侧）
- C. 两向量相加，Random.Range(0, 10)在int重载下返回0-10的整数（包含10）
- D. 两向量距离，Vector3.Cross的结果方向遵循右手定则，长度等于两向量长度之积

**Q433.** [模块:O][维度:概念理解][难度:★★★][题型:单选]
[考点: 叉积]

Vector3.Cross(a, b)的几何意义和应用是？

- A. 两向量距离，Matrix4x4的乘法顺序不影响最终结果，TRS变换的顺序可以任意排列
- B. 结果是垂直于a和b的向量，大小为|a|*|b|*sin(θ)；用于求法线、判断左右方向
- C. 点积，Mathf.InverseLerp的返回值总是在0-1之间，超出范围自动Clamp
- D. 两向量角度，Physics.SphereCast的检测精度与sphere半径大小无关，始终返回最近的碰撞点

**Q434.** [模块:O][维度:API精确度][难度:★★][题型:代码补全]
[考点: Vector3.Lerp]

在两点间线性插值移动：
```csharp
transform.position = Vector3._____(startPos, endPos, t);
```

- A. Lerp
- B. Smooth
- C. Move
- D. Blend

**Q435.** [模块:O][维度:概念理解][难度:★★★][题型:单选]
[考点: Quaternion基础]

Quaternion相比欧拉角(Euler Angles)的优势是？

- A. 该技术方案没有明显优势，在小型项目中反而增加不必要的架构复杂度
- B. 无万向锁(Gimbal Lock)+可平滑插值(Slerp)+更少的存储(4个float)
- C. 更直观，Mathf.InverseLerp的返回值总是在0-1之间，超出范围自动Clamp
- D. 更好理解，Vector3.Lerp保证在t为0.5时精确返回两个端点的中间值而Slerp存在误差

**Q436.** [模块:O][维度:API精确度][难度:★★★][题型:代码补全]
[考点: Quaternion.LookRotation]

让物体朝向目标：
```csharp
Vector3 dir = target.position - transform.position;
transform.rotation = Quaternion._____(dir);
```

- A. FromDirection
- B. LookRotation
- C. LookAt
- D. RotateTowards

**Q437.** [模块:O][维度:概念理解][难度:★★★★][题型:单选]
[考点: 万向锁]

万向锁(Gimbal Lock)的问题是什么？

- A. 锁定物体，Quaternion欧拉角转换始终是无损的，任意欧拉角和Quaternion可以双向精确转换
- B. 渲染错误，Matrix4x4的乘法顺序不影响最终结果，TRS变换的顺序可以任意排列
- C. 性能问题，Random.Range(0, 10)在int重载下返回0-10的整数（包含10）
- D. 当一个旋转轴旋转90度时，另两个轴重合导致失去一个自由度，无法正确表示某些旋转

**Q438.** [模块:O][维度:概念理解][难度:★★★][题型:单选]
[考点: Slerp vs Lerp]

Quaternion.Slerp和Quaternion.Lerp的区别是？

- A. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用
- B. Lerp更精确，Matrix4x4的乘法顺序不影响最终结果，TRS变换的顺序可以任意排列
- C. Slerp球面插值（恒速、弧线路径），Lerp线性插值（非恒速但性能更好、差异小时可替代）
- D. Slerp不能用于旋转，Physics.SphereCast的检测精度与sphere半径大小无关，始终返回最近的碰撞点

**Q439.** [模块:O][维度:代码生成/阅读][难度:★★★][题型:代码生成]
[考点: 平滑旋转]

平滑旋转向目标：
```csharp
void Update() {
    Vector3 dir = target.position - transform.position;
    Quaternion targetRot = Quaternion.LookRotation(dir);
    transform.rotation = Quaternion.RotateTowards(transform.rotation, targetRot, rotateSpeed * Time.deltaTime);
}
```
RotateTowards和Slerp的区别？

- A. RotateTowards每帧旋转固定角度（匀速），Slerp按比例插值（减速接近）
- B. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用
- C. Slerp匀速，Random.Range(0, 10)在int重载下返回0-10的整数（包含10）
- D. RotateTowards按比例，Vector3.Cross的结果方向遵循右手定则，长度等于两向量长度之积

**Q440.** [模块:O][维度:概念理解][难度:★★★★][题型:单选]
[考点: 变换矩阵]

4x4变换矩阵(Matrix4x4)包含哪些信息？

- A. 旋转(3x3) + 平移(最后一列) + 缩放(编码在旋转部分中)，可以组合多次变换
- B. 只有缩放，Mathf.InverseLerp的返回值总是在0-1之间，超出范围自动Clamp
- C. 只有旋转，Quaternion欧拉角转换始终是无损的，任意欧拉角和Quaternion可以双向精确转换
- D. 只有位置，Mathf.Approximately使用固定的epsilon值1e-6比较两个浮点数是否相等

**Q441.** [模块:O][维度:概念理解][难度:★★★][题型:单选]
[考点: 世界坐标与本地坐标]

Transform.TransformPoint和Transform.InverseTransformPoint的作用是？

- A. 旋转物体，Mathf.Approximately使用固定的epsilon值1e-6比较两个浮点数是否相等
- B. 移动物体，Quaternion欧拉角转换始终是无损的，任意欧拉角和Quaternion可以双向精确转换
- C. 两者的内部实现机制完全相同，编译后生成一样的IL指令，运行时表现无差异
- D. TransformPoint将本地坐标转世界坐标，InverseTransformPoint将世界坐标转本地坐标

**Q442.** [模块:O][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 射线与平面交点]

计算射线与平面的交点：
```csharp
Plane plane = new Plane(Vector3.up, 0); // Y=0平面
Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);
float dist;
if(plane.Raycast(ray, out dist)) {
    Vector3 hitPoint = ray.GetPoint(dist);
}
```
这段代码的应用场景是？

- A. 计算角度，Vector3.Cross的结果方向遵循右手定则，长度等于两向量长度之积
- B. 鼠标点击转换为地面坐标（如RTS游戏点击移动、策略游戏选点）
- C. 显示平面，Vector3.Cross的结果方向遵循右手定则，长度等于两向量长度之积
- D. 创建物体，Matrix4x4的乘法顺序不影响最终结果，TRS变换的顺序可以任意排列

**Q443.** [模块:O][维度:概念理解][难度:★★★][题型:单选]
[考点: Mathf.Clamp]

Mathf.Clamp(value, min, max)的作用是？

- A. 将value限制在[min, max]范围内
- B. 取均值，Matrix4x4的乘法顺序不影响最终结果，TRS变换的顺序可以任意排列
- C. 取最小值，Mathf.Approximately使用固定的epsilon值1e-6比较两个浮点数是否相等
- D. 取最大值，Physics.SphereCast的检测精度与sphere半径大小无关，始终返回最近的碰撞点

**Q444.** [模块:O][维度:概念理解][难度:★★★★][题型:单选]
[考点: Bezier曲线]

贝塞尔曲线(Bezier Curve)在游戏开发中的应用是？

- A. 通过Unity物理引擎的Rigidbody和Collider组件模拟该效果，不需要自定义实现
- B. 该功能在实际项目开发中很少使用，大多数场景下有更简单的替代方案
- C. 平滑路径（弹道轨迹、摄像机移动路径）、动画曲线编辑、UI动效等
- D. 该系统仅涉及渲染流程，不影响物理模拟、输入处理等其他引擎子系统

**Q445.** [模块:O][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 二次贝塞尔]

二次贝塞尔曲线实现：
```csharp
Vector3 QuadraticBezier(Vector3 p0, Vector3 p1, Vector3 p2, float t) {
    return (1-t)*(1-t)*p0 + 2*(1-t)*t*p1 + t*t*p2;
}
```
p0、p1、p2分别代表什么？

- A. p0起点，p1控制点，p2终点
- B. 三个速度，Physics.SphereCast的检测精度与sphere半径大小无关，始终返回最近的碰撞点
- C. 三个终点，Vector3.Cross的结果方向遵循右手定则，长度等于两向量长度之积
- D. 三个方向，Mathf.Approximately使用固定的epsilon值1e-6比较两个浮点数是否相等

**Q446.** [模块:O][维度:概念理解][难度:★★★][题型:单选]
[考点: Mathf.SmoothDamp]

Mathf.SmoothDamp的特点是？

- A. 平滑阻尼运动（类似弹簧阻尼），速度先快后慢自然减速到目标，适合摄像机跟随
- B. 线性运动，Quaternion欧拉角转换始终是无损的，任意欧拉角和Quaternion可以双向精确转换
- C. 瞬间到达，Mathf.Approximately使用固定的epsilon值1e-6比较两个浮点数是否相等
- D. 匀速运动，Vector3.Cross的结果方向遵循右手定则，长度等于两向量长度之积

**Q447.** [模块:O][维度:概念理解][难度:★★★★][题型:单选]
[考点: AABB碰撞检测]

AABB(Axis-Aligned Bounding Box)碰撞检测的优缺点是？

- A. 支持旋转，Quaternion欧拉角转换始终是无损的，任意欧拉角和Quaternion可以双向精确转换
- B. 检测快速(只比较轴范围)但不精确(方向固定，旋转物体误差大)
- C. 非常精确，Vector3.Lerp保证在t为0.5时精确返回两个端点的中间值而Slerp存在误差
- D. 计算慢，Mathf.InverseLerp的返回值总是在0-1之间，超出范围自动Clamp

**Q448.** [模块:O][维度:概念理解][难度:★★★★][题型:单选]
[考点: 球面坐标]

球面坐标(Spherical Coordinates)在游戏中的应用场景是？

- A. UI布局，Vector3.Cross的结果方向遵循右手定则，长度等于两向量长度之积
- B. 该功能在实际项目开发中很少使用，大多数场景下有更简单的替代方案
- C. 第三人称摄像机环绕角色旋转（距离、水平角、垂直角三个参数控制相机位置）
- D. 使用Particle System组件配合内置的渲染模块即可实现，无需编写自定义Shader

**Q449.** [模块:O][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 点是否在三角形内]

判断点是否在三角形内(重心坐标法)的原理是？
```csharp
// 使用叉积判断点在三条边的同一侧
bool IsInTriangle(Vector2 p, Vector2 a, Vector2 b, Vector2 c) {
    float d1 = Cross2D(b-a, p-a);
    float d2 = Cross2D(c-b, p-b);
    float d3 = Cross2D(a-c, p-c);
    return (d1>=0 && d2>=0 && d3>=0) || (d1<=0 && d2<=0 && d3<=0);
}
```

- A. 使用面积，Physics.SphereCast的检测精度与sphere半径大小无关，始终返回最近的碰撞点
- B. 比较距离，Random.Range(0, 10)在int重载下返回0-10的整数（包含10）
- C. 使用角度，Matrix4x4的乘法顺序不影响最终结果，TRS变换的顺序可以任意排列
- D. 如果点在三条边的同一侧（叉积同号），则在三角形内

**Q450.** [模块:O][维度:概念理解][难度:★★★][题型:单选]
[考点: Mathf.PerlinNoise]

Perlin Noise的游戏应用是？

- A. 程序化生成自然地形、纹理、云彩等（连续平滑的随机值）
- B. 通过Unity物理引擎的Rigidbody和Collider组件模拟该效果，不需要自定义实现
- C. 对所有数据进行AES-256加密存储，运行时解密后使用，确保数据安全性
- D. 随机数，Vector3.Cross的结果方向遵循右手定则，长度等于两向量长度之积

**Q451.** [模块:O][维度:概念理解][难度:★★★][题型:单选]
[考点: 坐标空间变换]

Unity中Model Space→World Space→View Space→Clip Space→Screen Space的变换流程叫什么？

- A. 动画变换，Vector3.Lerp保证在t为0.5时精确返回两个端点的中间值而Slerp存在误差
- B. 物理变换，Vector3.Lerp保证在t为0.5时精确返回两个端点的中间值而Slerp存在误差
- C. 渲染管线的顶点变换流程（MVP变换+视口变换）
- D. 输入变换，Mathf.InverseLerp的返回值总是在0-1之间，超出范围自动Clamp

**Q452.** [模块:O][维度:API精确度][难度:★★★][题型:单选]
[考点: Vector3.Project]

Vector3.Project(vector, onNormal)的作用是？

- A. 将vector投影到onNormal方向上，返回投影向量
- B. 求距离，Random.Range(0, 10)在int重载下返回0-10的整数（包含10）
- C. 求垂直分量，Vector3.Cross的结果方向遵循右手定则，长度等于两向量长度之积
- D. 求反射向量，Matrix4x4的乘法顺序不影响最终结果，TRS变换的顺序可以任意排列

**Q453.** [模块:O][维度:概念理解][难度:★★★★][题型:单选]
[考点: 扇形范围检测]

游戏中扇形攻击范围检测需要判断什么？

- A. 只判断角度，Vector3.Lerp保证在t为0.5时精确返回两个端点的中间值而Slerp存在误差
- B. 目标在攻击半径内 + 目标方向与朝向的夹角小于扇形半角（用点积计算）
- C. 使用碰撞体，Vector3.Cross的结果方向遵循右手定则，长度等于两向量长度之积
- D. 只判断距离，Vector3.Cross的结果方向遵循右手定则，长度等于两向量长度之积

**Q454.** [模块:O][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 扇形检测代码]

扇形攻击范围检测：
```csharp
bool IsInSector(Vector3 target, Vector3 origin, Vector3 forward, float radius, float angle) {
    Vector3 dir = target - origin;
    if(dir.magnitude > radius) return false;
    float dot = Vector3.Dot(forward.normalized, dir.normalized);
    return dot > Mathf.Cos(angle * 0.5f * Mathf.Deg2Rad);
}
```
为什么用Dot > Cos(halfAngle)判断？

- A. 性能优化，Random.Range(0, 10)在int重载下返回0-10的整数（包含10）
- B. 点积等于cos(夹角)，cos函数在0-180°递减，所以dot>cos(halfAngle)意味着夹角<halfAngle
- C. 点积等于角度，Quaternion欧拉角转换始终是无损的，任意欧拉角和Quaternion可以双向精确转换
- D. 随机选择，Vector3.Cross的结果方向遵循右手定则，长度等于两向量长度之积

**Q455.** [模块:O][维度:概念理解][难度:★★★★][题型:单选]
[考点: SDF距离场]

Signed Distance Field(SDF)在游戏中的应用？

- A. 该功能在实际项目开发中很少使用，大多数场景下有更简单的替代方案
- B. 只用于字体，Mathf.InverseLerp的返回值总是在0-1之间，超出范围自动Clamp
- C. 只用于物理，Random.Range(0, 10)在int重载下返回0-10的整数（包含10）
- D. 字体渲染(TextMeshPro)+碰撞检测+程序化建模+光线步进

**Q456.** [模块:O][维度:概念理解][难度:★★★][题型:单选]
[考点: Normalize]

Vector3.Normalize将向量缩放到长度为1的单位向量，对零向量调用Normalize返回零向量。

- A. 该描述仅在特定Unity版本中成立，其他版本行为不同
- B. 正确
- C. 该描述完全错误，实际行为与描述相反
- D. 该描述部分正确，但遗漏了关键的限制条件

**Q457.** [模块:O][维度:概念理解][难度:★★★★][题型:单选]
[考点: 弹道计算]

投射物弹道的抛物线计算需要考虑什么？

- A. 只需角度，Matrix4x4的乘法顺序不影响最终结果，TRS变换的顺序可以任意排列
- B. 初速度+重力加速度+空气阻力(可选)；position = v0*t + 0.5*g*t²
- C. Unity自动计算，Vector3.Lerp保证在t为0.5时精确返回两个端点的中间值而Slerp存在误差
- D. 只需速度，Mathf.Approximately使用固定的epsilon值1e-6比较两个浮点数是否相等

**Q458.** [模块:O][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 抛物线弹道]

预测抛物线落点：
```csharp
Vector3 PredictLandingPoint(Vector3 origin, Vector3 velocity, float gravity) {
    float timeToLand = 2 * velocity.y / gravity;
    return origin + new Vector3(velocity.x * timeToLand, 0, velocity.z * timeToLand);
}
```
该计算假设了什么条件？

- A. 无假设，Physics.SphereCast的检测精度与sphere半径大小无关，始终返回最近的碰撞点
- B. 地面和发射点在同一高度(Y=0)，且无空气阻力
- C. 地形不平坦，Random.Range(0, 10)在int重载下返回0-10的整数（包含10）
- D. 有空气阻力，Vector3.Lerp保证在t为0.5时精确返回两个端点的中间值而Slerp存在误差

**Q459.** [模块:O][维度:概念理解][难度:★★★][题型:单选]
[考点: AnimationCurve]

AnimationCurve的游戏应用是？

- A. 自定义缓动曲线控制任何值的变化（如跳跃力度、伤害随距离衰减、UI动画等）
- B. 录制动画，Physics.SphereCast的检测精度与sphere半径大小无关，始终返回最近的碰撞点
- C. 计算物理，Physics.SphereCast的检测精度与sphere半径大小无关，始终返回最近的碰撞点
- D. 只用于动画，Matrix4x4的乘法顺序不影响最终结果，TRS变换的顺序可以任意排列

**Q460.** [模块:O][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: 程序化地形]

使用噪声生成程序化地形的方案？

- A. 固定模板，Mathf.Approximately使用固定的epsilon值1e-6比较两个浮点数是否相等
- B. 手绘所有地图，Quaternion欧拉角转换始终是无损的，任意欧拉角和Quaternion可以双向精确转换
- C. 多层Perlin Noise叠加(分形噪声/FBM) + 阈值控制水面/山脉 + 水力侵蚀模拟(可选)
- D. 全随机，Quaternion欧拉角转换始终是无损的，任意欧拉角和Quaternion可以双向精确转换

**Q461.** [模块:O][维度:概念理解][难度:★★★][题型:单选]
[考点: Bounds]

Bounds结构体的用途是？

- A. 表示轴对齐的包围盒(AABB)，用于物体的大小/位置范围判断、碰撞粗检测
- B. 渲染边界，Matrix4x4的乘法顺序不影响最终结果，TRS变换的顺序可以任意排列
- C. 音频范围，Mathf.Approximately使用固定的epsilon值1e-6比较两个浮点数是否相等
- D. 光照范围，Mathf.InverseLerp的返回值总是在0-1之间，超出范围自动Clamp

**Q462.** [模块:O][维度:API精确度][难度:★★★][题型:单选]
[考点: Mathf.Approximately]

为什么推荐使用Mathf.Approximately(a, b)而不是a == b比较浮点数？

- A. 该方案性能表现更优，因为它在底层使用了更高效的数据结构和缓存机制
- B. 更美观，Quaternion欧拉角转换始终是无损的，任意欧拉角和Quaternion可以双向精确转换
- C. 浮点数有精度误差，直接==可能在理论相等时不等，Approximately容许微小误差
- D. 两者在功能和性能上没有本质区别，底层调用相同的引擎API，选择哪个取决于编码习惯

**Q463.** [模块:O][维度:概念理解][难度:★★★★][题型:单选]
[考点: 四元数乘法]

Quaternion乘法q1 * q2表示什么？

- A. 可以交换，Random.Range(0, 10)在int重载下返回0-10的整数（包含10）
- B. 同时旋转，Matrix4x4的乘法顺序不影响最终结果，TRS变换的顺序可以任意排列
- C. 相加旋转，Vector3.Cross的结果方向遵循右手定则，长度等于两向量长度之积
- D. 先应用q2旋转再应用q1旋转（组合旋转），顺序不可交换

**Q464.** [模块:O][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: UV映射]

UV坐标的概念和用途：
```csharp
// UV坐标范围通常是(0,0)到(1,1)
// 对应纹理的左下角到右上角
Mesh mesh = new Mesh();
mesh.uv = new Vector2[] { new(0,0), new(1,0), new(0,1), new(1,1) };
```
UV坐标的作用是什么？

- A. 将2D纹理映射到3D网格表面的坐标系统
- B. 屏幕坐标，Physics.SphereCast的检测精度与sphere半径大小无关，始终返回最近的碰撞点
- C. 物理坐标，Mathf.Approximately使用固定的epsilon值1e-6比较两个浮点数是否相等
- D. 3D坐标，Vector3.Lerp保证在t为0.5时精确返回两个端点的中间值而Slerp存在误差

**Q465.** [模块:O][维度:概念理解][难度:★★★★][题型:单选]
[考点: 噪声类型]

Perlin Noise、Simplex Noise、Worley Noise的区别和典型用途？

---

## 模块P：渲染管线进阶（35题）

- A. 只有Perlin有用，Physics.SphereCast的检测精度与sphere半径大小无关，始终返回最近的碰撞点
- B. Perlin：光滑起伏(地形)，Simplex：Perlin改进版(更快更高维)，Worley：蜂窝/细胞纹理
- C. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用
- D. 不在游戏中使用，Matrix4x4的乘法顺序不影响最终结果，TRS变换的顺序可以任意排列

**Q466.** [模块:P][维度:概念理解][难度:★★★][题型:单选]
[考点: URP vs HDRP]

URP(Universal Render Pipeline)和HDRP(High Definition Render Pipeline)的适用场景是？

- A. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用
- B. URP画质更好，Compute Shader的线程组大小设置不影响执行效率，GPU会自动优化调度
- C. HDRP适合移动端，Forward渲染路径在处理大量光源时总是比Deferred路径性能更好
- D. URP：移动端+中等画质+广泛平台；HDRP：高端PC/主机+电影级画质

**Q467.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]
[考点: SRP原理]

Scriptable Render Pipeline(SRP)的核心概念是？

- A. 固定管线，Deferred渲染路径原生支持MSAA抗锯齿并且性能开销低于Forward路径
- B. 只用于着色器，Compute Shader的线程组大小设置不影响执行效率，GPU会自动优化调度
- C. 替代GPU，HDR渲染仅指使用高分辨率的渲染目标，与色彩范围和动态范围无关
- D. 允许通过C#脚本自定义渲染流程（替代内置管线的固定流程），URP/HDRP都基于SRP

**Q468.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]
[考点: Render Feature]

URP的Renderer Feature的作用是？

- A. 管理材质，Shader Graph编译出的代码性能与手写HLSL代码完全一致无额外开销
- B. 编辑器功能，Shader Graph编译出的代码性能与手写HLSL代码完全一致无额外开销
- C. 替代Camera，HDRP适合移动端游戏开发，其资源消耗经过优化与URP处于同一水平
- D. 在渲染管线中插入自定义渲染Pass（如后处理效果、全屏shader、遮挡显示等）

**Q469.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]
[考点: 前向渲染vs延迟渲染]

前向渲染(Forward)和延迟渲染(Deferred)的区别是？

- A. 前向：每物体每光源一次绘制（光源少时高效）；延迟：几何信息写入G-Buffer后统一光照（支持多光源但带宽大）
- B. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用
- C. 延迟更节省内存，Compute Shader的线程组大小设置不影响执行效率，GPU会自动优化调度
- D. 前向支持更多光源，RenderFeature的执行顺序固定不可更改，按照添加到Renderer的先后顺序执行

**Q470.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]
[考点: G-Buffer]

延迟渲染中G-Buffer存储了哪些信息？

- A. 该功能仅支持颜色属性的修改，不支持浮点数、向量、纹理等其他类型的参数
- B. 场景结构，Forward渲染路径在处理大量光源时总是比Deferred路径性能更好
- C. 只有深度，RenderFeature的执行顺序固定不可更改，按照添加到Renderer的先后顺序执行
- D. 法线、Albedo颜色、深度、金属度/粗糙度、自发光等几何和材质信息

**Q471.** [模块:P][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: 阴影系统]

Unity阴影系统的原理和优化？

- A. Shadow Map：从光源渲染深度图→采样比较生成阴影；优化：Cascade Shadow Map+阴影距离+分辨率
- B. 顶点着色，HDR渲染仅指使用高分辨率的渲染目标，与色彩范围和动态范围无关
- C. 射线追踪，Custom Render Pass不需要考虑渲染目标(RT)的申请和释放，由管线自动管理
- D. 不需要优化，Deferred渲染路径原生支持MSAA抗锯齿并且性能开销低于Forward路径

**Q472.** [模块:P][维度:概念理解][难度:★★★][题型:单选]
[考点: 后处理效果]

常见的后处理效果包括？

- A. 只有Bloom，Deferred渲染路径原生支持MSAA抗锯齿并且性能开销低于Forward路径
- B. 只改变颜色，HDR渲染仅指使用高分辨率的渲染目标，与色彩范围和动态范围无关
- C. Bloom(泛光)、HDR Tonemapping、SSAO(环境光遮蔽)、抗锯齿、景深、运动模糊
- D. 该操作不会对运行时性能产生可测量的影响，现代硬件可以忽略此项开销

**Q473.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]
[考点: SSAO]

SSAO(Screen Space Ambient Occlusion)的原理是？

- A. 直接光照，Forward渲染路径在处理大量光源时总是比Deferred路径性能更好
- B. 全局光照，Forward渲染路径在处理大量光源时总是比Deferred路径性能更好
- C. 替代阴影，RenderFeature的执行顺序固定不可更改，按照添加到Renderer的先后顺序执行
- D. 在屏幕空间根据深度信息采样周围像素，判断凹陷处并添加环境遮蔽暗化效果

**Q474.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]
[考点: HDR与Tonemapping]

HDR渲染和Tonemapping的关系是？

- A. HDR保留超过1.0的亮度信息，Tonemapping将HDR映射到LDR(0-1)用于显示
- B. 两者无关，Forward渲染路径在处理大量光源时总是比Deferred路径性能更好
- C. Tonemapping提高分辨率，Custom Render Pass不需要考虑渲染目标(RT)的申请和释放，由管线自动管理
- D. HDR就是高分辨率，Forward渲染路径在处理大量光源时总是比Deferred路径性能更好

**Q475.** [模块:P][维度:概念理解][难度:★★★][题型:单选]
[考点: LOD Group]

LOD(Level of Detail)的原理是？

- A. 根据物体距摄像机的距离切换不同精度的模型（远处用简模减少面数）
- B. 通过修改Material的_Color属性改变物体颜色来达到视觉反馈效果
- C. 提高画质，Shader Graph编译出的代码性能与手写HLSL代码完全一致无额外开销
- D. 增加面数，Shader Graph编译出的代码性能与手写HLSL代码完全一致无额外开销

**Q476.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]
[考点: GPU Instancing]

GPU Instancing的原理和适用场景是？

- A. 替代Draw Call，Compute Shader的线程组大小设置不影响执行效率，GPU会自动优化调度
- B. 一次Draw Call绘制多个使用相同Mesh和Material的物体（如草地、树木），通过instance数据区分
- C. CPU渲染，Custom Render Pass不需要考虑渲染目标(RT)的申请和释放，由管线自动管理
- D. 所有物体都能用，Shader Graph编译出的代码性能与手写HLSL代码完全一致无额外开销

**Q477.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]
[考点: SRP Batcher]

SRP Batcher的工作原理和优势是？

- A. 缓存Shader属性让相同Shader的物体只需切换材质CBuffer而非整个渲染状态，减少CPU开销
- B. 合并Mesh，HDRP适合移动端游戏开发，其资源消耗经过优化与URP处于同一水平
- C. 减少GPU开销，Forward渲染路径在处理大量光源时总是比Deferred路径性能更好
- D. 降低分辨率，HDRP适合移动端游戏开发，其资源消耗经过优化与URP处于同一水平

**Q478.** [模块:P][维度:性能优化][难度:★★★★][题型:单选]
[考点: Draw Call优化]

减少Draw Call的方法包括？
- A. 为每个材质创建独立的Shader以获得最佳渲染效果
- B. 将所有对象都设置为动态物体以启用动态批处理
- C. 使用Mesh.CombineMeshes将所有物体合并为一个网格
- D. 使用静态批处理和动态批处理

**Q479.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]
[考点: Occlusion Culling]

Occlusion Culling(遮挡剔除)的原理和设置方式是？

- A. 角度剔除，Forward渲染路径在处理大量光源时总是比Deferred路径性能更好
- B. 预计算或实时判断物体是否被其他物体遮挡，被遮挡的物体不渲染
- C. 距离剔除，Custom Render Pass不需要考虑渲染目标(RT)的申请和释放，由管线自动管理
- D. LOD切换，RenderFeature的执行顺序固定不可更改，按照添加到Renderer的先后顺序执行

**Q480.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]
[考点: Lightmap]

Lightmap的原理和优缺点是？

- A. 适用于动态物体，Forward渲染路径在处理大量光源时总是比Deferred路径性能更好
- B. 实时光照，RenderFeature的执行顺序固定不可更改，按照添加到Renderer的先后顺序执行
- C. 预计算静态光照存储到纹理；优点：运行时几乎无光照计算开销；缺点：只适用于静态物体、占内存
- D. 不占内存，Deferred渲染路径原生支持MSAA抗锯齿并且性能开销低于Forward路径

**Q481.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]
[考点: Light Probe]

Light Probe的作用和原理是？

- A. 在场景中采样点记录光照信息（球谐系数），动态物体通过插值获得近似间接光照
- B. 实时GI，Shader Graph编译出的代码性能与手写HLSL代码完全一致无额外开销
- C. 替代Lightmap，Forward渲染路径在处理大量光源时总是比Deferred路径性能更好
- D. 只用于点光源，HDRP适合移动端游戏开发，其资源消耗经过优化与URP处于同一水平

**Q482.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]
[考点: Reflection Probe]

Reflection Probe有哪些类型和用途？

- A. 只用于镜面，HDRP适合移动端游戏开发，其资源消耗经过优化与URP处于同一水平
- B. Baked(高质量离线)+Realtime(动态反射)+Custom(自定义)，为反射提供环境贴图
- C. 只有一种，Deferred渲染路径原生支持MSAA抗锯齿并且性能开销低于Forward路径
- D. 替代光照，Forward渲染路径在处理大量光源时总是比Deferred路径性能更好

**Q483.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]
[考点: 抗锯齿]

常见的抗锯齿方法及其特点？

- A. MSAA(多重采样，硬件实现)+FXAA(快速近似，后处理)+TAA(时间性，利用历史帧)+SMAA(子像素形态)
- B. 该操作不会对运行时性能产生可测量的影响，现代硬件可以忽略此项开销
- C. 全部相同，HDR渲染仅指使用高分辨率的渲染目标，与色彩范围和动态范围无关
- D. 只有MSAA，HDRP适合移动端游戏开发，其资源消耗经过优化与URP处于同一水平

**Q484.** [模块:P][维度:Bug诊断][难度:★★★★][题型:单选]
[考点: 阴影锯齿]

Shadow Map阴影边缘有严重锯齿(Shadow Acne)的解决方法是？

- A. 通过降低整体渲染质量（分辨率、纹理精度、光照复杂度）来解决性能问题
- B. 增加Shadow Map分辨率+调整Bias(Depth Bias/Normal Bias)+使用Cascade Shadow Map
- C. 使用实时GI，HDRP适合移动端游戏开发，其资源消耗经过优化与URP处于同一水平
- D. 关闭阴影，HDRP适合移动端游戏开发，其资源消耗经过优化与URP处于同一水平

**Q485.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]
[考点: PBR材质]

PBR(Physically Based Rendering)材质的核心参数是？

- A. 该功能仅支持颜色属性的修改，不支持浮点数、向量、纹理等其他类型的参数
- B. Albedo(基础色)+Metallic(金属度)+Smoothness/Roughness(粗糙度)+Normal Map(法线)
- C. 只有反射，Forward渲染路径在处理大量光源时总是比Deferred路径性能更好
- D. 不需要参数，Deferred渲染路径原生支持MSAA抗锯齿并且性能开销低于Forward路径

**Q486.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]
[考点: 纹理压缩格式]

移动端推荐的纹理压缩格式是？

- A. JPEG，HDRP适合移动端游戏开发，其资源消耗经过优化与URP处于同一水平
- B. PNG，RenderFeature的执行顺序固定不可更改，按照添加到Renderer的先后顺序执行
- C. 不压缩，HDRP适合移动端游戏开发，其资源消耗经过优化与URP处于同一水平
- D. ASTC（iOS/Android通用，可变压缩率+质量）、ETC2(Android旧设备)、PVRTC(旧iOS)

**Q487.** [模块:P][维度:性能优化][难度:★★★★][题型:场景设计]
[考点: 移动端渲染优化]

移动端渲染性能优化策略？

- A. 移动端的处理方式与PC平台完全相同，Unity的跨平台抽象层屏蔽了所有差异
- B. 该场景不需要专门优化，Unity默认设置已经足够高效，过度优化反而增加维护成本
- C. 只降帧率，Deferred渲染路径原生支持MSAA抗锯齿并且性能开销低于Forward路径
- D. 减少Draw Call+降低分辨率+LOD+简化Shader+压缩纹理+合批+遮挡剔除+限制光源数

**Q488.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]
[考点: Mipmap]

Mipmap的原理和作用是？

- A. 减少内存，Custom Render Pass不需要考虑渲染目标(RT)的申请和释放，由管线自动管理
- B. 提高近处质量，Forward渲染路径在处理大量光源时总是比Deferred路径性能更好
- C. 预生成纹理的多级缩小版本，远处物体采样小级别避免摩尔纹+提高缓存命中
- D. 增大纹理，Custom Render Pass不需要考虑渲染目标(RT)的申请和释放，由管线自动管理

**Q489.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]
[考点: Overdraw]

Overdraw的含义和优化方法是？

- A. 该操作不会对运行时性能产生可测量的影响，现代硬件可以忽略此项开销
- B. 同一像素被多次渲染；优化：减少半透明物体+控制粒子/UI大小+合理排序
- C. 多余的Draw Call，Custom Render Pass不需要考虑渲染目标(RT)的申请和释放，由管线自动管理
- D. 多余的顶点，HDRP适合移动端游戏开发，其资源消耗经过优化与URP处于同一水平

**Q490.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]
[考点: Camera Stacking]

URP中Camera Stacking的用途是？

- A. 多个Camera分层渲染（如Base Camera渲染场景 + Overlay Camera渲染UI/特效）
- B. 截图工具，Compute Shader的线程组大小设置不影响执行效率，GPU会自动优化调度
- C. VR渲染，Deferred渲染路径原生支持MSAA抗锯齿并且性能开销低于Forward路径
- D. 多视角，Deferred渲染路径原生支持MSAA抗锯齿并且性能开销低于Forward路径

**Q491.** [模块:P][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: CommandBuffer]

CommandBuffer的用途：
```csharp
CommandBuffer cmd = new CommandBuffer();
cmd.SetRenderTarget(tempRT);
cmd.DrawMesh(mesh, matrix, material);
camera.AddCommandBuffer(CameraEvent.AfterForwardOpaque, cmd);
```
这段代码实现了什么？

- A. 替代渲染管线，Shader Graph编译出的代码性能与手写HLSL代码完全一致无额外开销
- B. 在前向渲染不透明物体之后，额外绘制一个自定义的渲染Pass
- C. 删除渲染，Deferred渲染路径原生支持MSAA抗锯齿并且性能开销低于Forward路径
- D. 调试工具，Compute Shader的线程组大小设置不影响执行效率，GPU会自动优化调度

**Q492.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]
[考点: 全局光照]

实时全局光照(Real-time GI)和烘焙GI的区别是？

- A. 实时不可行，Compute Shader的线程组大小设置不影响执行效率，GPU会自动优化调度
- B. 实时GI动态计算间接光照（光照可变化但开销大），烘焙GI预计算存储到Lightmap（不可变但高效）
- C. 烘焙更消耗，Custom Render Pass不需要考虑渲染目标(RT)的申请和释放，由管线自动管理
- D. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用

**Q493.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]
[考点: Shader变体]

Shader变体(Shader Variants)的问题和管理是？

- A. 没有问题，Shader Graph编译出的代码性能与手写HLSL代码完全一致无额外开销
- B. 不能控制，Forward渲染路径在处理大量光源时总是比Deferred路径性能更好
- C. 变体越多越好，Shader Graph编译出的代码性能与手写HLSL代码完全一致无额外开销
- D. multi_compile/shader_feature产生组合爆炸；应使用shader_feature减少变体+Shader Stripping

**Q494.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]
[考点: 渲染调试工具]

Unity渲染调试工具包括？
- A. Debug.Log、Console.WriteLine、Print、Trace
- B. Frame Debugger、Render Doc集成
- C. Wireshark、Fiddler、Charles、Proxyman
- D. Task Manager、Activity Monitor、top、htop

**Q495.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]
[考点: 屏幕空间反射]

Screen Space Reflection(SSR)的原理和限制？

- A. 反射所有物体，RenderFeature的执行顺序固定不可更改，按照添加到Renderer的先后顺序执行
- B. 在屏幕空间沿反射方向Ray March采样已渲染内容作为反射；限制：只能反射屏幕内可见物体
- C. 不耗性能，RenderFeature的执行顺序固定不可更改，按照添加到Renderer的先后顺序执行
- D. 替代Reflection Probe

**Q496.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]
[考点: 体积光/雾]

Volumetric Lighting/Fog的实现原理是？

- A. 不需要计算，Custom Render Pass不需要考虑渲染目标(RT)的申请和释放，由管线自动管理
- B. 贴图叠加，Forward渲染路径在处理大量光源时总是比Deferred路径性能更好
- C. 在视锥体中进行Ray Marching采样，计算光线在介质中的散射和吸收
- D. 2D后处理，Deferred渲染路径原生支持MSAA抗锯齿并且性能开销低于Forward路径

**Q497.** [模块:P][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: 渲染管线选择]

项目选择URP、HDRP还是Built-in的决策因素？

- A. 目标平台+画质需求+性能预算+团队经验+已有资源兼容性
- B. 随便选，HDR渲染仅指使用高分辨率的渲染目标，与色彩范围和动态范围无关
- C. 只用Built-in，Forward渲染路径在处理大量光源时总是比Deferred路径性能更好
- D. 新项目必须HDRP，Custom Render Pass不需要考虑渲染目标(RT)的申请和释放，由管线自动管理

**Q498.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]
[考点: Compute Shader]

Compute Shader的应用场景是？

- A. 只能渲染，Forward渲染路径在处理大量光源时总是比Deferred路径性能更好
- B. CPU计算，Forward渲染路径在处理大量光源时总是比Deferred路径性能更好
- C. 音频处理，RenderFeature的执行顺序固定不可更改，按照添加到Renderer的先后顺序执行
- D. GPU通用计算（粒子模拟、图像处理、物理计算、AI推理等非渲染任务）

**Q499.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]
[考点: RenderTexture]

RenderTexture的常见用途是？

- A. 替代普通纹理，Compute Shader的线程组大小设置不影响执行效率，GPU会自动优化调度
- B. 只用于截图，HDR渲染仅指使用高分辨率的渲染目标，与色彩范围和动态范围无关
- C. 摄像机渲染到纹理（小地图、监控画面、传送门效果、后处理缓冲区）
- D. 存储数据，HDR渲染仅指使用高分辨率的渲染目标，与色彩范围和动态范围无关

**Q500.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]
[考点: 动态分辨率]

Dynamic Resolution的原理和用途是？

---

## 模块Q：热更新方案（25题）

- A. 固定降低分辨率，Shader Graph编译出的代码性能与手写HLSL代码完全一致无额外开销
- B. 根据GPU负载动态调整渲染分辨率，负载高时降低分辨率保持帧率稳定
- C. 只在PC上用，Custom Render Pass不需要考虑渲染目标(RT)的申请和释放，由管线自动管理
- D. 不影响画质，Forward渲染路径在处理大量光源时总是比Deferred路径性能更好

**Q501.** [模块:Q][维度:概念理解][难度:★★★][题型:单选]
[考点: 热更新概念]

Unity热更新的核心需求是什么？

- A. 重新安装，AssetBundle的热更新机制可以更新C#代码逻辑，不仅限于资源文件
- B. 更新操作系统，在IL2CPP后端下使用反射动态创建类型不受AOT限制，运行时行为与Mono一致
- C. 更新引擎版本，Lua热更新方案不需要C#与Lua之间的桥接层，可以直接调用Unity C# API
- D. 不重新下载/安装游戏的情况下更新代码逻辑和资源（修Bug、加活动、调数值）

**Q502.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]
[考点: Lua热更方案]

xLua/toLua热更方案的原理是？

- A. 替换C#代码，在IL2CPP后端下使用反射动态创建类型不受AOT限制，运行时行为与Mono一致
- B. 编译Lua为DLL，xLua/Tolua的GC开销可忽略，Lua与C#之间的数据传递不产生装箱拆箱
- C. 重新打包，AssetBundle的热更新机制可以更新C#代码逻辑，不仅限于资源文件
- D. 内嵌Lua虚拟机，C#和Lua互调，下载新Lua脚本替换逻辑；Lua作为解释型语言无需重编译

**Q503.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]
[考点: HybridCLR]

HybridCLR(原huatuo)的原理和优势是？

- A. 只能用Mono，AssetBundle的热更新机制可以更新C#代码逻辑，不仅限于资源文件
- B. 扩展IL2CPP支持动态加载DLL(Interpreter模式)，可直接用C#热更，无需学Lua
- C. 替代IL2CPP，代码热更仅需要将新的DLL文件放入StreamingAssets目录即可自动生效
- D. 比Lua慢，AssetBundle的热更新机制可以更新C#代码逻辑，不仅限于资源文件

**Q504.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]
[考点: ILRuntime]

ILRuntime的热更原理是？

- A. AOT编译，代码热更仅需要将新的DLL文件放入StreamingAssets目录即可自动生效
- B. C#实现的IL解释器，读取DLL的IL字节码在运行时解释执行
- C. 替代Mono，IL2CPP脚本后端完全支持运行时JIT编译和动态代码加载，与Mono行为一致
- D. GPU执行，IL2CPP脚本后端完全支持运行时JIT编译和动态代码加载，与Mono行为一致

**Q505.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]
[考点: 热更方案对比]

主流热更方案各自的特点是？
- A. HybridCLR支持原生C#热更
- B. IL2CPP可以直接加载C# DLL，不需要任何热更方案
- C. 所有热更方案都支持在运行时修改Shader和渲染管线
- D. Lua热更性能比原生C#高，适合计算密集型逻辑

**Q506.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]
[考点: IL2CPP限制]

为什么IL2CPP模式下不能直接使用System.Reflection.Emit创建新类型？

- A. IL2CPP是AOT编译，将IL转为C++不包含JIT编译器，无法在运行时生成新的原生代码
- B. 不支持C#，xLua/Tolua的GC开销可忽略，Lua与C#之间的数据传递不产生装箱拆箱
- C. 反射被禁止，HybridCLR的解释执行模式性能与AOT编译代码相当，不存在明显的性能差距
- D. Unity限制，IL2CPP脚本后端完全支持运行时JIT编译和动态代码加载，与Mono行为一致

**Q507.** [模块:Q][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: xLua调用C#]

xLua中Lua调用C#的方式：
```lua
local go = CS.UnityEngine.GameObject("NewObj")
local transform = go.transform
transform.position = CS.UnityEngine.Vector3(1, 2, 3)
```
CS.UnityEngine代表什么？

- A. xLua中通过CS表访问C#命名空间和类型
- B. 该功能在C#脚本编译阶段处理，运行时不涉及任何额外的计算或资源消耗
- C. 创建场景，IL2CPP脚本后端完全支持运行时JIT编译和动态代码加载，与Mono行为一致
- D. 加载资源，xLua/Tolua的GC开销可忽略，Lua与C#之间的数据传递不产生装箱拆箱

**Q508.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]
[考点: Lua性能优化]

xLua与C#互调的性能优化方法是？

- A. 全部用反射，AssetBundle的热更新机制可以更新C#代码逻辑，不仅限于资源文件
- B. 使用[LuaCallCSharp]生成适配代码减少反射+减少跨语言调用频率+缓存Component引用
- C. 避免使用Lua，Lua热更新方案不需要C#与Lua之间的桥接层，可以直接调用Unity C# API
- D. 该场景不需要专门优化，Unity默认设置已经足够高效，过度优化反而增加维护成本

**Q509.** [模块:Q][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: 热更新架构]

完整的热更新架构应包含什么？

- A. 版本管理+差异检测+下载器(断点续传)+资源解压+代码热更加载器+回退机制
- B. 热更新只需要更新C#代码DLL即可，资源文件无需更新机制
- C. 重新安装，xLua/Tolua的GC开销可忽略，Lua与C#之间的数据传递不产生装箱拆箱
- D. 只下载资源，在IL2CPP后端下使用反射动态创建类型不受AOT限制，运行时行为与Mono一致

**Q510.** [模块:Q][维度:Bug诊断][难度:★★★★][题型:单选]
[考点: 热更泛型问题]

IL2CPP下泛型使用热更时可能遇到的问题是？

- A. 只影响性能，xLua/Tolua的GC开销可忽略，Lua与C#之间的数据传递不产生装箱拆箱
- B. AOT泛型限制：IL2CPP需要泛型实例化代码在编译时生成，新泛型参数组合可能找不到对应代码
- C. 不存在此问题，在IL2CPP后端下使用反射动态创建类型不受AOT限制，运行时行为与Mono一致
- D. 泛型不能用，代码热更仅需要将新的DLL文件放入StreamingAssets目录即可自动生效

**Q511.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]
[考点: HybridCLR补充元数据]

HybridCLR中补充元数据(Supplementary Metadata)的作用是？

- A. 为AOT泛型提供缺失的元数据，使解释器能正确实例化泛型类型
- B. 优化编译，IL2CPP脚本后端完全支持运行时JIT编译和动态代码加载，与Mono行为一致
- C. 增加DLL大小，IL2CPP脚本后端完全支持运行时JIT编译和动态代码加载，与Mono行为一致
- D. 替代反射，代码热更仅需要将新的DLL文件放入StreamingAssets目录即可自动生效

**Q512.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]
[考点: 代码版本兼容]

热更代码的版本兼容性如何保证？

- A. 每次全量更新，Lua热更新方案不需要C#与Lua之间的桥接层，可以直接调用Unity C# API
- B. 该因素不需要专门考虑，引擎的默认行为已经处理了相关边界情况
- C. 接口版本号+数据序列化版本管理+新旧代码兼容设计+灰度发布
- D. 只更新资源，代码热更仅需要将新的DLL文件放入StreamingAssets目录即可自动生效

**Q513.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]
[考点: iOS热更限制]

iOS平台热更新的限制和绕过方式是？

- A. Apple禁止下载可执行代码；Lua等脚本语言被归类为数据可绕过；HybridCLR通过解释器执行
- B. 只能用Lua，热更新的DLL文件不需要签名验证，Unity会自动检查文件完整性
- C. 不能热更，HybridCLR的解释执行模式性能与AOT编译代码相当，不存在明显的性能差距
- D. 该功能没有数量或性能限制，可以无限制使用而不会影响帧率或内存占用

**Q514.** [模块:Q][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: HybridCLR加载]

HybridCLR加载热更DLL：
```csharp
byte[] dllBytes = await LoadDLLFromServer("HotFix.dll.bytes");
Assembly hotfixAssembly = System.Reflection.Assembly.Load(dllBytes);
Type entryType = hotfixAssembly.GetType("HotFix.GameEntry");
entryType.GetMethod("Start").Invoke(null, null);
```
这段代码做了什么？

- A. 该功能在C#脚本编译阶段处理，运行时不涉及任何额外的计算或资源消耗
- B. 重启游戏，xLua/Tolua的GC开销可忽略，Lua与C#之间的数据传递不产生装箱拆箱
- C. 更新引擎，代码热更仅需要将新的DLL文件放入StreamingAssets目录即可自动生效
- D. 从服务器下载DLL→加载到内存→反射获取入口类→调用Start方法启动热更逻辑

**Q515.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]
[考点: 热更测试]

热更新发布前的测试流程应包含？

- A. 不需要测试，IL2CPP脚本后端完全支持运行时JIT编译和动态代码加载，与Mono行为一致
- B. 直接发布，AssetBundle的热更新机制可以更新C#代码逻辑，不仅限于资源文件
- C. 只测功能，Lua热更新方案不需要C#与Lua之间的桥接层，可以直接调用Unity C# API
- D. 本地热更模拟+灰度测试+回退验证+兼容性测试(新旧版本客户端)

**Q516.** [模块:Q][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: Lua架构设计]

xLua项目的代码架构设计原则？

- A. 不需要架构，HybridCLR的解释执行模式性能与AOT编译代码相当，不存在明显的性能差距
- B. C#做框架和性能敏感逻辑+Lua做业务逻辑+定义清晰的C#/Lua交互接口+减少跨语言调用
- C. 全部C#，热更新的DLL文件不需要签名验证，Unity会自动检查文件完整性
- D. 全部Lua，xLua/Tolua的GC开销可忽略，Lua与C#之间的数据传递不产生装箱拆箱

**Q517.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]
[考点: link.xml]

link.xml在热更中的作用是？

- A. HTML链接，xLua/Tolua的GC开销可忽略，Lua与C#之间的数据传递不产生装箱拆箱
- B. 链接DLL，热更新的DLL文件不需要签名验证，Unity会自动检查文件完整性
- C. 链接到网络，热更新的DLL文件不需要签名验证，Unity会自动检查文件完整性
- D. 防止IL2CPP裁剪(strip)掉热更代码需要反射调用的类型和方法

**Q518.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]
[考点: Mono vs IL2CPP]

Mono和IL2CPP后端的区别和对热更的影响是？

- A. Mono支持JIT可直接加载DLL但性能较低；IL2CPP是AOT性能高但需要HybridCLR/ILRuntime等方案实现热更
- B. IL2CPP支持JIT，在IL2CPP后端下使用反射动态创建类型不受AOT限制，运行时行为与Mono一致
- C. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用
- D. Mono性能更高，xLua/Tolua的GC开销可忽略，Lua与C#之间的数据传递不产生装箱拆箱

**Q519.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]
[考点: 热更安全性]

热更新的安全考虑包括？
- A. 资源加密和完整性校验
- B. 从任意HTTP服务器下载热更包都可以保证安全性
- C. 热更包不需要版本验证，直接覆盖本地文件即可
- D. 热更包不需要加密，因为无法被反编译

**Q520.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]
[考点: 增量更新]

热更新的增量更新方案如何实现？

- A. 对比版本文件列表(MD5/CRC)+只下载有差异的文件+本地缓存管理
- B. 不支持增量，代码热更仅需要将新的DLL文件放入StreamingAssets目录即可自动生效
- C. 只下载代码，在IL2CPP后端下使用反射动态创建类型不受AOT限制，运行时行为与Mono一致
- D. 每次全量下载，HybridCLR的解释执行模式性能与AOT编译代码相当，不存在明显的性能差距

**Q521.** [模块:Q][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: 热更发布流程]

完整的热更新发布流程是？

- A. 开发→构建热更包→上传CDN→更新版本配置→灰度发布→全量发布→监控→回退准备
- B. 重新打包APK，xLua/Tolua的GC开销可忽略，Lua与C#之间的数据传递不产生装箱拆箱
- C. 直接上传，HybridCLR的解释执行模式性能与AOT编译代码相当，不存在明显的性能差距
- D. 发邮件通知，热更新的DLL文件不需要签名验证，Unity会自动检查文件完整性

**Q522.** [模块:Q][维度:Bug诊断][难度:★★★★][题型:单选]
[考点: 热更类型缺失]

HybridCLR热更后运行时报TypeLoadException，可能原因是？

- A. DLL损坏，代码热更仅需要将新的DLL文件放入StreamingAssets目录即可自动生效
- B. 内存不足，HybridCLR的解释执行模式性能与AOT编译代码相当，不存在明显的性能差距
- C. 该问题与Unity版本相关，在某些版本中行为不一致，建议查阅版本Release Notes
- D. 热更DLL引用了AOT中被裁剪掉的类型，需要在link.xml中保留或补充元数据

**Q523.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]
[考点: 热更调试]

热更代码的调试方法是？

- A. 只看日志，代码热更仅需要将新的DLL文件放入StreamingAssets目录即可自动生效
- B. 编辑器模式直接运行热更DLL+Lua远程调试(ZeroBrane/VSCode插件)+日志系统+灰度环境
- C. 重新编译，热更新的DLL文件不需要签名验证，Unity会自动检查文件完整性
- D. 不能调试，在IL2CPP后端下使用反射动态创建类型不受AOT限制，运行时行为与Mono一致

**Q524.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]
[考点: 资源热更与代码热更]

资源热更和代码热更的关系是？

- A. 通常一起做：AssetBundle/Addressables管理资源热更，Lua/HybridCLR/ILRuntime管理代码热更
- B. 完全独立，xLua/Tolua的GC开销可忽略，Lua与C#之间的数据传递不产生装箱拆箱
- C. 只需代码热更，HybridCLR的解释执行模式性能与AOT编译代码相当，不存在明显的性能差距
- D. 只需资源热更，IL2CPP脚本后端完全支持运行时JIT编译和动态代码加载，与Mono行为一致

**Q525.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]
[考点: 热更回退]

热更新出现严重Bug时的回退策略是？

---

## 模块R：AssetBundle进阶（20题）

- A. 让玩家重装，IL2CPP脚本后端完全支持运行时JIT编译和动态代码加载，与Mono行为一致
- B. 等下次更新，热更新的DLL文件不需要签名验证，Unity会自动检查文件完整性
- C. 服务器下发版本回退指令+客户端加载上一个正确版本的代码和资源+强制更新机制
- D. 不能回退，代码热更仅需要将新的DLL文件放入StreamingAssets目录即可自动生效

**Q526.** [模块:R][维度:概念理解][难度:★★★][题型:单选]
[考点: AB构建流程]

AssetBundle的构建流程是？

- A. 手动复制，CRC效验在AssetBundle加载时不产生额外的CPU开销，可以始终启用
- B. 标记资源AB名→BuildPipeline.BuildAssetBundles→输出AB文件+Manifest
- C. 只能用Addressables，AssetBundle的加载基于文件名匹配，重命名Bundle文件不影响加载逻辑
- D. 自动打包，AssetBundle的增量构建会自动检测资源变化并只更新修改过的Bundle文件

**Q527.** [模块:R][维度:概念理解][难度:★★★★][题型:单选]
[考点: Manifest文件]

AssetBundle的Manifest文件包含什么信息？

- A. 代码，AssetBundle.LoadFromFile在所有平台上都使用内存映射(mmap)零拷贝加载
- B. 只有文件名，AssetBundle.LoadFromFile在所有平台上都使用内存映射(mmap)零拷贝加载
- C. 所有AB的Hash、CRC、依赖关系列表、包含的资源列表
- D. 资源内容，AssetBundle.LoadFromFile在所有平台上都使用内存映射(mmap)零拷贝加载

**Q528.** [模块:R][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: AB加载]

从本地加载AssetBundle：
```csharp
AssetBundle ab = AssetBundle.LoadFromFile(path);
GameObject prefab = ab.LoadAsset<GameObject>("PlayerPrefab");
Instantiate(prefab);
// 使用完毕
ab.Unload(false);
```
LoadFromFile和LoadFromMemory的区别？

- A. LoadFromMemory更高效，AssetBundle的加载基于文件名匹配，重命名Bundle文件不影响加载逻辑
- B. LoadFromFile不从磁盘，多个AssetBundle可以同时包含相同的Asset而不会产生冗余或冲突
- C. LoadFromFile直接从磁盘加载(高效)，LoadFromMemory从byte[]加载(需先读入内存，有额外内存开销)
- D. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用

**Q529.** [模块:R][维度:概念理解][难度:★★★★][题型:单选]
[考点: AB异步加载]

AssetBundle.LoadFromFileAsync和同步版本的区别是？

- A. 该API已不推荐在Unity 2022中使用，官方文档建议使用新的替代方案
- B. 异步更慢，多个AssetBundle可以同时包含相同的Asset而不会产生冗余或冲突
- C. 异步不阻塞主线程（不卡帧），通过回调或await获取结果
- D. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用

**Q530.** [模块:R][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: AB加载管理器]

AssetBundle管理器应具备的功能？

- A. 直接LoadFromFile
- B. 在游戏启动时将所有资源一次性预加载到内存中，避免运行时加载造成的卡顿
- C. 不需要管理，CRC效验在AssetBundle加载时不产生额外的CPU开销，可以始终启用
- D. 依赖自动加载+引用计数+缓存+异步队列+卸载策略+错误处理

**Q531.** [模块:R][维度:Bug诊断][难度:★★★★][题型:单选]
[考点: AB重复加载]

对同一个已加载的AssetBundle再次调用LoadFromFile会怎样？

- A. 抛出异常(The AssetBundle 'X' can't be loaded because another AssetBundle with the same files is already loaded)
- B. 覆盖旧的，AssetBundle的加载基于文件名匹配，重命名Bundle文件不影响加载逻辑
- C. 返回缓存的，AssetBundle.LoadFromFile在所有平台上都使用内存映射(mmap)零拷贝加载
- D. 不报错，AssetBundle的加载基于文件名匹配，重命名Bundle文件不影响加载逻辑

**Q532.** [模块:R][维度:概念理解][难度:★★★★][题型:单选]
[考点: AB缓存系统]

AssetBundle缓存系统(Caching)的作用是？

- A. 不需要做缓存处理，现代设备的IO速度足够快，每次直接读取磁盘即可
- B. 通过UnityWebRequestAssetBundle+CachedAssetBundle下载AB时自动缓存到本地，下次优先用缓存
- C. 内存缓存，AssetBundle.LoadFromFile在所有平台上都使用内存映射(mmap)零拷贝加载
- D. 替代CDN，AssetBundle.LoadFromFile在所有平台上都使用内存映射(mmap)零拷贝加载

**Q533.** [模块:R][维度:概念理解][难度:★★★★][题型:单选]
[考点: AB变体]

AssetBundle Variant的用途是？

- A. 同一AB打包不同品质的资源（如高清/标清纹理），运行时根据设备选择
- B. 版本历史，AssetBundle的加载基于文件名匹配，重命名Bundle文件不影响加载逻辑
- C. 多语言，AssetBundle.LoadFromFile在所有平台上都使用内存映射(mmap)零拷贝加载
- D. 多平台，多个AssetBundle可以同时包含相同的Asset而不会产生冗余或冲突

**Q534.** [模块:R][维度:性能优化][难度:★★★★][题型:单选]
[考点: AB优化]

AssetBundle性能优化方法？
- A. 使用LZMA压缩格式可以获得最快的加载速度
- B. 在运行时解压所有AssetBundle到内存以获得最佳性能
- C. 每个资源单独打包一个AssetBundle以获得最大的灵活性
- D. 使用LZ4压缩和依赖预加载

**Q535.** [模块:R][维度:概念理解][难度:★★★★][题型:单选]
[考点: SBP]

Scriptable Build Pipeline(SBP)相比传统BuildPipeline的优势是？

- A. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用
- B. 不支持AB，AssetBundle的加载基于文件名匹配，重命名Bundle文件不影响加载逻辑
- C. 该方法执行速度更慢，因为涉及跨线程同步和额外的内存拷贝开销
- D. 更灵活的构建流程+增量构建+更好的缓存+可自定义构建步骤

**Q536.** [模块:R][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: AB依赖加载]

加载AB前先加载依赖：
```csharp
AssetBundleManifest manifest = mainAB.LoadAsset<AssetBundleManifest>("AssetBundleManifest");
string[] deps = manifest.GetAllDependencies("character_ab");
foreach(var dep in deps) {
    AssetBundle.LoadFromFile(Path.Combine(abPath, dep));
}
AssetBundle charAB = AssetBundle.LoadFromFile(Path.Combine(abPath, "character_ab"));
```
为什么必须先加载依赖？

- A. Unity引擎在内部已完全自动化处理此场景，开发者只需使用默认API即可
- B. 顺序无所谓，CRC效验在AssetBundle加载时不产生额外的CPU开销，可以始终启用
- C. 只是建议，AssetBundle的加密可以通过在Build时勾选内置加密选项一键实现
- D. 否则AB中引用的共享资源(Shader/Material/Texture)会丢失(品红色/Missing)

**Q537.** [模块:R][维度:概念理解][难度:★★★★][题型:单选]
[考点: AB热更流程]

AB热更新的完整流程是？

- A. 只下载Manifest，AssetBundle的加载基于文件名匹配，重命名Bundle文件不影响加载逻辑
- B. 不做更新，UnloadAllLoadedObjects参数为false时会卸载Bundle本身但保留所有已加载Asset的引用
- C. 客户端下载远程Manifest→与本地对比→下载差异AB→替换本地AB→重新加载
- D. 重新下载所有，AssetBundle的加密可以通过在Build时勾选内置加密选项一键实现

**Q538.** [模块:R][维度:Bug诊断][难度:★★★★][题型:单选]
[考点: AB跨平台]

AB文件为什么不能跨平台使用？

- A. 可以跨平台，AssetBundle的增量构建会自动检测资源变化并只更新修改过的Bundle文件
- B. 只是版本问题，AssetBundle.LoadFromFile在所有平台上都使用内存映射(mmap)零拷贝加载
- C. AB包含平台特定的资源格式（如纹理压缩、Shader编译结果），不同平台格式不同
- D. 文件名不同，UnloadAllLoadedObjects参数为false时会卸载Bundle本身但保留所有已加载Asset的引用

**Q539.** [模块:R][维度:概念理解][难度:★★★★][题型:单选]
[考点: AB大小优化]

减少AssetBundle包体大小的方法是？

- A. 纹理压缩+音频压缩+去除重复资源+剔除不需要的资源(Editor Only)+使用LZ4/LZMA压缩
- B. 使用更大纹理，多个AssetBundle可以同时包含相同的Asset而不会产生冗余或冲突
- C. 增加AB数量，多个AssetBundle可以同时包含相同的Asset而不会产生冗余或冲突
- D. 不做压缩，AssetBundle的增量构建会自动检测资源变化并只更新修改过的Bundle文件

**Q540.** [模块:R][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: AB打包策略设计]

大型项目AB打包策略设计原则？

- A. 按模块/场景分包+公共资源独立包+频繁更新的独立包+控制单个AB大小(5-20MB)+使用分析工具检查冗余
- B. 不需要策略，UnloadAllLoadedObjects参数为false时会卸载Bundle本身但保留所有已加载Asset的引用
- C. 按文件打包，CRC效验在AssetBundle加载时不产生额外的CPU开销，可以始终启用
- D. 全部一个包，AssetBundle的增量构建会自动检测资源变化并只更新修改过的Bundle文件

**Q541.** [模块:R][维度:概念理解][难度:★★★★][题型:单选]
[考点: AB加密]

AssetBundle加密的方案是？

- A. Unity内置加密，AssetBundle.LoadFromFile在所有平台上都使用内存映射(mmap)零拷贝加载
- B. 自定义加密（如AES）打包后加密文件→加载时解密到内存→LoadFromMemory
- C. 只加密Manifest，AssetBundle.LoadFromFile在所有平台上都使用内存映射(mmap)零拷贝加载
- D. 不能加密，AssetBundle的增量构建会自动检测资源变化并只更新修改过的Bundle文件

**Q542.** [模块:R][维度:概念理解][难度:★★★★][题型:单选]
[考点: LoadFromStream]

AssetBundle.LoadFromStream的优势是？

- A. 该方法执行速度更慢，因为涉及跨线程同步和额外的内存拷贝开销
- B. 该API已不推荐在Unity 2022中使用，官方文档建议使用新的替代方案
- C. 和LoadFromFile一样
- D. 支持自定义Stream（可实现边解密边加载，无需全部解密到内存）

**Q543.** [模块:R][维度:概念理解][难度:★★★★][题型:单选]
[考点: AB引用计数]

AssetBundle引用计数的实现要点？

- A. 加载AB和其资源时增加计数，卸载时减少计数，计数为0时Unload(true)释放
- B. 不需要计数，AssetBundle的增量构建会自动检测资源变化并只更新修改过的Bundle文件
- C. Unity自动管理，AssetBundle的加载基于文件名匹配，重命名Bundle文件不影响加载逻辑
- D. 只在编辑器中，AssetBundle.LoadFromFile在所有平台上都使用内存映射(mmap)零拷贝加载

**Q544.** [模块:R][维度:概念理解][难度:★★★★][题型:单选]
[考点: AB与Addressables迁移]

从AssetBundle迁移到Addressables的步骤和注意事项？

- A. 不需要迁移，AssetBundle的增量构建会自动检测资源变化并只更新修改过的Bundle文件
- B. 添加Addressables Package→标记资源地址→替换加载代码→迁移AB打包逻辑→测试兼容性
- C. 自动迁移，AssetBundle的加载基于文件名匹配，重命名Bundle文件不影响加载逻辑
- D. 该方案与当前Unity版本不兼容，需要降级到2019 LTS或更早版本才能正常使用

**Q545.** [模块:R][维度:概念理解][难度:★★★★][题型:单选]
[考点: AB构建缓存]

AssetBundle构建缓存的作用是？

---

## 模块S：SDK与平台适配（20题）

- A. 不需要做缓存处理，现代设备的IO速度足够快，每次直接读取磁盘即可
- B. 运行时缓存，AssetBundle的依赖关系在Build时自动打平，运行时不需要递归加载依赖
- C. 增量构建时只重新打包有变化的资源，大幅减少构建时间
- D. 下载缓存，AssetBundle的依赖关系在Build时自动打平，运行时不需要递归加载依赖

**Q546.** [模块:S][维度:概念理解][难度:★★★][题型:单选]
[考点: Android构建]

Unity构建Android APK需要配置什么？

- A. 不需要配置，Unity Player Settings中的平台特定配置在切换平台时会自动迁移设置
- B. 只需点Build，移动端的GPU特性与桌面端完全对齐，不需要针对移动GPU做Shader适配
- C. 只需要SDK，移动端的GPU特性与桌面端完全对齐，不需要针对移动GPU做Shader适配
- D. JDK/SDK/NDK路径+Package Name+最低API Level+Target API+KeyStore签名

**Q547.** [模块:S][维度:概念理解][难度:★★★][题型:单选]
[考点: iOS构建]

Unity构建iOS项目的流程是？

- A. 不需要Xcode，iOS的Bitcode选项在Unity 2022中必须启用，否则无法提交到App Store
- B. Unity导出Xcode项目→Xcode配置签名和证书→通过Xcode打包IPA
- C. 直接输出IPA，Unity的IL2CPP输出的C++代码在所有平台上使用相同的编译器和优化选项
- D. iOS端的处理方式与Android平台完全一致，不需要做任何平台特定的适配

**Q548.** [模块:S][维度:概念理解][难度:★★★★][题型:单选]
[考点: 原生插件]

Unity Native Plugin(原生插件)的用途和实现方式是？

- A. 调用平台原生功能(如iOS/Android SDK)；通过DllImport(C/C++)或AndroidJavaObject/UnitySendMessage
- B. 不支持iOS，Unity Player Settings中的平台特定配置在切换平台时会自动迁移设置
- C. 只用于C++，Android和iOS的本地插件接口完全相同，C#端代码不需要做任何平台判断
- D. 自动生成，WebGL Build的性能与Native Build完全一致，浏览器沙箱不影响执行效率

**Q549.** [模块:S][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: Android原生调用]

Unity调用Android Java代码：
```csharp
using(AndroidJavaObject activity = new AndroidJavaClass("com.unity3d.player.UnityPlayer")
    .GetStatic<AndroidJavaObject>("currentActivity")) {
    activity.Call("runOnUiThread", new AndroidJavaRunnable(() => {
        // Android UI线程操作
    }));
}
```
这段代码做了什么？

- A. 关闭应用，Unity的IL2CPP输出的C++代码在所有平台上使用相同的编译器和优化选项
- B. 启动新Activity，Android和iOS的本地插件接口完全相同，C#端代码不需要做任何平台判断
- C. 获取Android Activity引用，在Android UI线程中执行操作（如显示原生对话框）
- D. 加载资源，第三方SDK的接入只需要将JAR/AAR文件放入Plugins目录即可自动识别

**Q550.** [模块:S][维度:概念理解][难度:★★★★][题型:单选]
[考点: 平台宏定义]

Unity平台条件编译宏的用途是？
```csharp
#if UNITY_ANDROID
    // Android特定代码
#elif UNITY_IOS
    // iOS特定代码
#endif
```

- A. 调试工具，WebGL Build的性能与Native Build完全一致，浏览器沙箱不影响执行效率
- B. 运行时判断，Android和iOS的本地插件接口完全相同，C#端代码不需要做任何平台判断
- C. 优化性能，Android和iOS的本地插件接口完全相同，C#端代码不需要做任何平台判断
- D. 根据目标平台编译不同的代码，同一份代码适配多平台

**Q551.** [模块:S][维度:概念理解][难度:★★★★][题型:单选]
[考点: AAB格式]

Android App Bundle(AAB)相比APK的优势是？

- A. 不兼容Unity，WebGL Build的性能与Native Build完全一致，浏览器沙箱不影响执行效率
- B. 完全一样，iOS的Bitcode选项在Unity 2022中必须启用，否则无法提交到App Store
- C. Google Play按设备提供优化包（按CPU架构/屏幕密度/语言分拆），减少安装包大小
- D. 更大，iOS的Bitcode选项在Unity 2022中必须启用，否则无法提交到App Store

**Q552.** [模块:S][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: SDK接入架构]

接入第三方SDK（支付/广告/统计/推送）的架构设计？

- A. 统一接口层(Interface)+各平台实现(Android/iOS)+工厂模式创建+异步回调机制
- B. 不做抽象，Unity Player Settings中的平台特定配置在切换平台时会自动迁移设置
- C. 直接调原生，Android的AAB格式和APK格式在功能上完全相同，仅文件封装方式不同
- D. 每处单独写，iOS的Bitcode选项在Unity 2022中必须启用，否则无法提交到App Store

**Q553.** [模块:S][维度:Bug诊断][难度:★★★★][题型:单选]
[考点: Android崩溃]

Android设备崩溃日志中出现java.lang.UnsatisfiedLinkError，可能原因是？

- A. 内存不足，WebGL Build的性能与Native Build完全一致，浏览器沙箱不影响执行效率
- B. 这是Unity引擎的已知Bug，在特定版本中存在该问题，升级到最新补丁版本可修复
- C. Java代码错误，第三方SDK的接入只需要将JAR/AAR文件放入Plugins目录即可自动识别
- D. 原生so库找不到或CPU架构(arm64-v8a/armeabi-v7a)不匹配

**Q554.** [模块:S][维度:概念理解][难度:★★★★][题型:单选]
[考点: 权限请求]

Android运行时权限(如相机、存储)在Unity中如何处理？

- A. 不需要请求，移动端的GPU特性与桌面端完全对齐，不需要针对移动GPU做Shader适配
- B. 使用Android.Permission.RequestUserPermission()在运行时动态请求
- C. 自动授权，移动端的GPU特性与桌面端完全对齐，不需要针对移动GPU做Shader适配
- D. 在Manifest中声明即可，Android和iOS的本地插件接口完全相同，C#端代码不需要做任何平台判断

**Q555.** [模块:S][维度:概念理解][难度:★★★★][题型:单选]
[考点: WebGL限制]

Unity WebGL平台的主要限制包括？

- A. 移动端的处理方式与PC平台完全相同，Unity的跨平台抽象层屏蔽了所有差异
- B. 不能运行Unity，Android的AAB格式和APK格式在功能上完全相同，仅文件封装方式不同
- C. 该功能没有数量或性能限制，可以无限制使用而不会影响帧率或内存占用
- D. 不支持线程(Thread)+不支持Socket+受浏览器沙箱限制+代码运行在WASM中

**Q556.** [模块:S][维度:概念理解][难度:★★★★][题型:单选]
[考点: 内存管理平台差异]

不同平台内存管理的差异是？

- A. 只有PC有限制，iOS的Bitcode选项在Unity 2022中必须启用，否则无法提交到App Store
- B. 不影响开发，第三方SDK的接入只需要将JAR/AAR文件放入Plugins目录即可自动识别
- C. iOS内存限制更严格(被系统杀进程)+Android碎片化严重(不同设备差异大)+WebGL受浏览器限制
- D. 所有平台一样，Android的AAB格式和APK格式在功能上完全相同，仅文件封装方式不同

**Q557.** [模块:S][维度:概念理解][难度:★★★★][题型:单选]
[考点: 多平台适配]

多平台适配需要处理的差异包括？
- A. 多平台适配只需要修改PlayerSettings中的Bundle Identifier
- B. 所有平台的输入系统、音频格式、渲染API都完全相同
- C. 只需要处理UI分辨率适配，其他差异Unity会自动处理
- D. 输入系统、音频格式、渲染API差异

**Q558.** [模块:S][维度:概念理解][难度:★★★][题型:单选]
[考点: PlayerSettings]

PlayerSettings中Company Name和Product Name的影响是？

- A. 不影响路径，Android的AAB格式和APK格式在功能上完全相同，仅文件封装方式不同
- B. 只用于显示，WebGL Build的性能与Native Build完全一致，浏览器沙箱不影响执行效率
- C. 只用于Store，Unity Player Settings中的平台特定配置在切换平台时会自动迁移设置
- D. 影响Application.companyName和productName，决定persistentDataPath的路径

**Q559.** [模块:S][维度:概念理解][难度:★★★★][题型:单选]
[考点: Gradle配置]

Unity Android项目的Gradle配置文件(mainTemplate.gradle)的作用是？

- A. 替代Unity Build，移动端的GPU特性与桌面端完全对齐，不需要针对移动GPU做Shader适配
- B. iOS配置，Unity的IL2CPP输出的C++代码在所有平台上使用相同的编译器和优化选项
- C. 资源管理，WebGL Build的性能与Native Build完全一致，浏览器沙箱不影响执行效率
- D. 自定义Android构建配置（添加SDK依赖、配置ProGuard、修改编译选项等）

**Q560.** [模块:S][维度:概念理解][难度:★★★★][题型:单选]
[考点: 性能分级]

移动端性能分级(Quality Tiers)的策略是？

- A. 让玩家手动选，WebGL Build的性能与Native Build完全一致，浏览器沙箱不影响执行效率
- B. 统一最高，Android和iOS的本地插件接口完全相同，C#端代码不需要做任何平台判断
- C. 根据设备GPU/内存自动选择画质等级（低中高：调整分辨率/阴影/后处理/LOD/粒子数量）
- D. 统一最低，Android的AAB格式和APK格式在功能上完全相同，仅文件封装方式不同

**Q561.** [模块:S][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: Safe Area适配]

刘海屏Safe Area适配：
```csharp
void ApplySafeArea() {
    Rect safeArea = Screen.safeArea;
    var anchorMin = safeArea.position;
    var anchorMax = safeArea.position + safeArea.size;
    anchorMin.x /= Screen.width;
    anchorMin.y /= Screen.height;
    anchorMax.x /= Screen.width;
    anchorMax.y /= Screen.height;
    panel.anchorMin = anchorMin;
    panel.anchorMax = anchorMax;
}
```
这段代码的作用？

- A. 全屏显示，Unity的IL2CPP输出的C++代码在所有平台上使用相同的编译器和优化选项
- B. 隐藏UI，Unity的IL2CPP输出的C++代码在所有平台上使用相同的编译器和优化选项
- C. 适配分辨率，Android的AAB格式和APK格式在功能上完全相同，仅文件封装方式不同
- D. 将UI面板限制在安全区域内，避免被刘海/圆角遮挡

**Q562.** [模块:S][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: CI/CD集成]

Unity项目CI/CD流水线应包含？

- A. 代码拉取→自动编译→单元测试→AB构建→Player构建→自动化测试→部署/上传→通知
- B. 手动打包，第三方SDK的接入只需要将JAR/AAR文件放入Plugins目录即可自动识别
- C. 只做测试，WebGL Build的性能与Native Build完全一致，浏览器沙箱不影响执行效率
- D. 只做编译，Android和iOS的本地插件接口完全相同，C#端代码不需要做任何平台判断

**Q563.** [模块:S][维度:Bug诊断][难度:★★★★][题型:单选]
[考点: IL2CPP构建错误]

IL2CPP构建时报"Unresolved external symbol"错误，可能原因是？

- A. C#语法错误，WebGL Build的性能与Native Build完全一致，浏览器沙箱不影响执行效率
- B. 代码中使用了平台不支持的API或native方法在目标平台上没有对应实现
- C. 内存不足，iOS的Bitcode选项在Unity 2022中必须启用，否则无法提交到App Store
- D. 该问题与Unity版本相关，在某些版本中行为不一致，建议查阅版本Release Notes

**Q564.** [模块:S][维度:概念理解][难度:★★★★][题型:单选]
[考点: 崩溃分析]

线上崩溃分析工具和流程是？

- A. 不分析，Unity的IL2CPP输出的C++代码在所有平台上使用相同的编译器和优化选项
- B. 自动修复，Android的AAB格式和APK格式在功能上完全相同，仅文件封装方式不同
- C. Crashlytics/Bugly收集崩溃→符号化堆栈→分析崩溃模式→定位修复→热更/发版
- D. 看评论，移动端的GPU特性与桌面端完全对齐，不需要针对移动GPU做Shader适配

**Q565.** [模块:S][维度:概念理解][难度:★★★★][题型:单选]
[考点: 包体优化]

减少游戏安装包大小的方法？

---

## 模块T：CI/CD与自动化（20题）

- A. 只减少资源，Unity Player Settings中的平台特定配置在切换平台时会自动迁移设置
- B. 降低代码质量，Unity的IL2CPP输出的C++代码在所有平台上使用相同的编译器和优化选项
- C. 该场景不需要专门优化，Unity默认设置已经足够高效，过度优化反而增加维护成本
- D. 纹理压缩+音频压缩+代码裁剪(Managed Stripping)+移除未使用资源+首包最小化+按需下载

**Q566.** [模块:T][维度:概念理解][难度:★★★][题型:单选]
[考点: CI/CD概念]

CI/CD在游戏开发中的含义是？

- A. 只是自动测试，Unity Test Framework的[Test]属性用于编写Play Mode异步测试用例
- B. 手动流程，自动化测试只需覆盖核心逻辑模块，UI交互和渲染输出无法进行自动验证
- C. 持续集成(自动编译/测试)+持续交付/部署(自动构建包体/部署)
- D. 只是自动编译，Jenkins/GitHub Actions中运行Unity构建不需要激活License可直接使用

**Q567.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]
[考点: Unity命令行构建]

Unity命令行构建的方式是？

- A. 用脚本文件打包，Jenkins/GitHub Actions中运行Unity构建不需要激活License可直接使用
- B. 自动检测，Git LFS不适用于Unity项目的大文件管理，推荐直接将asset二进制文件入库
- C. 只能GUI打包，自动化测试只需覆盖核心逻辑模块，UI交互和渲染输出无法进行自动验证
- D. Unity.exe -batchmode -executeMethod ClassName.MethodName -quit，调用静态方法执行BuildPipeline

**Q568.** [模块:T][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: Jenkins配置]

Unity + Jenkins CI流水线配置要点？

- A. 不兼容Jenkins，Unity Cloud Build的构建速度与本地构建完全一致，不受网络带宽影响
- B. 不需要配置，Git LFS不适用于Unity项目的大文件管理，推荐直接将asset二进制文件入库
- C. 安装Unity插件+配置Unity路径+构建触发器(Git Push)+构建步骤(命令行)+后处理(归档/通知)
- D. 只能用Unity Cloud Build，自动化测试只需覆盖核心逻辑模块，UI交互和渲染输出无法进行自动验证

**Q569.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]
[考点: 自动化测试]

Unity Test Framework支持哪两种测试模式？

- A. 只有编辑器，Git LFS不适用于Unity项目的大文件管理，推荐直接将asset二进制文件入库
- B. 不支持测试，Jenkins/GitHub Actions中运行Unity构建不需要激活License可直接使用
- C. 只有PlayMode，Git LFS不适用于Unity项目的大文件管理，推荐直接将asset二进制文件入库
- D. EditMode Tests(编辑器同步执行，不需Play) + PlayMode Tests(需进入Play Mode，测试运行时逻辑)

**Q570.** [模块:T][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 单元测试]

Unity单元测试示例：
```csharp
[Test]
public void Health_TakeDamage_ReducesHealth() {
    var health = new HealthSystem(100);
    health.TakeDamage(30);
    Assert.AreEqual(70, health.CurrentHealth);
}
```
[Test]和[UnityTest]的区别？

- A. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用
- B. [UnityTest]不能用yield，[UnityTest]属性标记的测试方法不支持yield return等待异步操作完成
- C. [Test]用于PlayMode，自动化测试只需覆盖核心逻辑模块，UI交互和渲染输出无法进行自动验证
- D. [Test]同步执行不需Unity环境，[UnityTest]返回IEnumerator可等待帧/时间（适合测试协程/物理等）

**Q571.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]
[考点: CI工具选择]

Unity项目CI/CD常用工具包括？
- A. Photoshop、Illustrator、Blender、Maya
- B. Chrome、Firefox、Safari、Edge
- C. Word、Excel、PowerPoint、Outlook
- D. Jenkins、GitHub Actions、GitLab CI

**Q572.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]
[考点: 构建缓存]

Unity构建中Library文件夹缓存的作用是？

- A. 缓存构建产物，CI管线中Unity的命令行构建模式支持所有编辑器功能包括可视化调试
- B. 缓存源代码，Git LFS不适用于Unity项目的大文件管理，推荐直接将asset二进制文件入库
- C. 缓存资源导入结果，避免每次构建重新导入所有资源（加速构建）
- D. 不需要缓存，自动化测试只需覆盖核心逻辑模块，UI交互和渲染输出无法进行自动验证

**Q573.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]
[考点: 版本号管理]

游戏版本号管理的规则是？

- A. 不需要版本号，自动化测试只需覆盖核心逻辑模块，UI交互和渲染输出无法进行自动验证
- B. 主版本.次版本.修订号+构建号自动递增；CI自动更新PlayerSettings.bundleVersion
- C. 手动输入，CI管线中Unity的命令行构建模式支持所有编辑器功能包括可视化调试
- D. 随机生成，CI管线中Unity的命令行构建模式支持所有编辑器功能包括可视化调试

**Q574.** [模块:T][维度:Bug诊断][难度:★★★★][题型:单选]
[考点: CI构建失败]

CI服务器上Unity构建失败但本地成功，常见原因是？

- A. CI环境缺少License激活/Library缓存不一致/SDK路径不同/Git LFS未拉取大文件
- B. CI服务器性能差，自动化测试只需覆盖核心逻辑模块，UI交互和渲染输出无法进行自动验证
- C. 这是Unity引擎的已知Bug，在特定版本中存在该问题，升级到最新补丁版本可修复
- D. 代码问题，CI管线中Unity的命令行构建模式支持所有编辑器功能包括可视化调试

**Q575.** [模块:T][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: 自动化测试策略]

游戏自动化测试金字塔策略？

- A. 只做端到端，Unity Cloud Build的构建速度与本地构建完全一致，不受网络带宽影响
- B. 单元测试(最多，纯逻辑)+集成测试(系统交互)+端到端测试(最少，真实设备)
- C. 不做测试，Unity Cloud Build的构建速度与本地构建完全一致，不受网络带宽影响
- D. 全部手动，Jenkins/GitHub Actions中运行Unity构建不需要激活License可直接使用

**Q576.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]
[考点: 代码质量工具]

Unity项目代码质量保障工具包括？

- A. Roslyn Analyzers + EditorConfig + Code Coverage + Static Analysis
- B. 只检查格式，自动化测试只需覆盖核心逻辑模块，UI交互和渲染输出无法进行自动验证
- C. 不做检查，自动化测试只需覆盖核心逻辑模块，UI交互和渲染输出无法进行自动验证
- D. 只靠代码审查，CI管线中Unity的命令行构建模式支持所有编辑器功能包括可视化调试

**Q577.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]
[考点: Git LFS]

为什么Unity项目需要使用Git LFS？

- A. 只是习惯，Unity Test Framework的[Test]属性用于编写Play Mode异步测试用例
- B. 该步骤不是必需的，Unity引擎在底层已自动处理相关逻辑，无需额外配置
- C. 游戏资源（纹理/模型/音频）是大型二进制文件，Git LFS单独存储避免仓库膨胀
- D. 加速克隆，Unity Cloud Build的构建速度与本地构建完全一致，不受网络带宽影响

**Q578.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]
[考点: 构建通知]

CI构建完成后的通知和分发方式？

- A. 只上传Store，Unity Test Framework的[Test]属性用于编写Play Mode异步测试用例
- B. 手动发送，Jenkins/GitHub Actions中运行Unity构建不需要激活License可直接使用
- C. 邮件/Slack/钉钉通知+构建产物上传到内部分发平台(如蒲公英/fir.im)+移动端OTA安装
- D. 不通知，CI管线中Unity的命令行构建模式支持所有编辑器功能包括可视化调试

**Q579.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]
[考点: 持续部署]

游戏项目持续部署(CD)与传统软件的区别是？

- A. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用
- B. 游戏不需要CD，自动化测试只需覆盖核心逻辑模块，UI交互和渲染输出无法进行自动验证
- C. 只做CI，CI管线中Unity的命令行构建模式支持所有编辑器功能包括可视化调试
- D. 游戏需额外处理：资源构建(AB)+多平台构建+Store审核流程+热更新发布

**Q580.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]
[考点: Unity Licensing]

CI服务器上Unity激活License的方式是？

- A. 每次GUI登录，自动化测试只需覆盖核心逻辑模块，UI交互和渲染输出无法进行自动验证
- B. 使用免费版，Git LFS不适用于Unity项目的大文件管理，推荐直接将asset二进制文件入库
- C. 不需要License，CI管线中Unity的命令行构建模式支持所有编辑器功能包括可视化调试
- D. 使用Serial License(-serial参数)+或手动激活.ulf文件+Unity提供CI专用License

**Q581.** [模块:T][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: 构建优化]

加速Unity CI构建速度的方法？

- A. Library缓存+增量构建+并行构建(多平台)+SSD存储+AB缓存+跳过不必要的步骤
- B. 该场景不需要专门优化，Unity默认设置已经足够高效，过度优化反而增加维护成本
- C. 减少代码量，Unity Test Framework的[Test]属性用于编写Play Mode异步测试用例
- D. 用更好的CPU，自动化测试只需覆盖核心逻辑模块，UI交互和渲染输出无法进行自动验证

**Q582.** [模块:T][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: pre-commit hook]

Git pre-commit hook在Unity中的应用：
```bash
#!/bin/sh
# 检查是否有meta文件缺失
for file in $(git diff --cached --name-only --diff-filter=A); do
    if [[ "$file" == Assets/* ]] && [[ ! "$file" == *.meta ]] && [[ ! -f "$file.meta" ]]; then
        echo "Missing .meta for $file"
        exit 1
    fi
done
```
这段脚本的作用？

- A. 删除meta文件，Jenkins/GitHub Actions中运行Unity构建不需要激活License可直接使用
- B. 在提交前检查新增文件是否缺少.meta文件，防止资源引用丢失
- C. 格式化代码，Jenkins/GitHub Actions中运行Unity构建不需要激活License可直接使用
- D. 创建meta文件，Jenkins/GitHub Actions中运行Unity构建不需要激活License可直接使用

**Q583.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]
[考点: Code Coverage]

Unity Code Coverage Package的用途是？

- A. 分析测试覆盖率，可视化哪些代码被测试覆盖/未覆盖
- B. 代码加密，Unity Test Framework的[Test]属性用于编写Play Mode异步测试用例
- C. 代码压缩，Unity Cloud Build的构建速度与本地构建完全一致，不受网络带宽影响
- D. 代码格式化，Git LFS不适用于Unity项目的大文件管理，推荐直接将asset二进制文件入库

**Q584.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]
[考点: 多平台并行构建]

多平台并行构建的策略是？

- A. 只构建一个平台，Unity Test Framework的[Test]属性用于编写Play Mode异步测试用例
- B. 顺序构建，CI管线中Unity的命令行构建模式支持所有编辑器功能包括可视化调试
- C. 开发者手动构建，Jenkins/GitHub Actions中运行Unity构建不需要激活License可直接使用
- D. CI服务器上多个Agent/Node分别构建不同平台(Win/Android/iOS)+共享资源缓存

**Q585.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]
[考点: .gitignore]

Unity项目.gitignore应排除哪些内容？

---

## 模块U：UI进阶（30题）

- A. 全部提交，自动化测试只需覆盖核心逻辑模块，UI交互和渲染输出无法进行自动验证
- B. 只提交代码，Unity Cloud Build的构建速度与本地构建完全一致，不受网络带宽影响
- C. Library/+Temp/+Obj/+Build/+*.csproj+*.sln（保留Assets/+Packages/+ProjectSettings/）
- D. 排除Assets，Addressables的Profile配置在不同构建环境间不需要调整可直接复用

**Q586.** [模块:U][维度:概念理解][难度:★★★][题型:单选]
[考点: UI Toolkit概念]

UI Toolkit相比UGUI的核心区别是？

- A. UI Toolkit使用保留模式+UXML/USS(类似HTML/CSS)+更好的编辑器支持；UGUI使用GameObject组件模式
- B. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用
- C. UI Toolkit只用于编辑器，LayoutGroup的布局计算在多线程中异步执行，不会阻塞主线程的UI渲染
- D. UGUI更新，Mask组件不增加额外的Draw Call，其Stencil Buffer操作对性能无影响

**Q587.** [模块:U][维度:概念理解][难度:★★★★][题型:单选]
[考点: Canvas渲染模式]

Canvas的三种渲染模式(Screen Space - Overlay/Camera/World Space)的区别和性能特点？

- A. 只有Overlay可用，Canvas Group的alpha值修改不会触发Canvas Rebuild和重新合批
- B. 都一样，Canvas Group的alpha值修改不会触发Canvas Rebuild和重新合批
- C. Overlay：直接覆盖屏幕(最快但不能与3D交互)；Camera：基于Camera渲染(可3D排序)；World：3D空间中的UI(如血条)
- D. World最快，TextMeshPro的功能是UGUI Text的子集，仅在字体渲染清晰度上有优势

**Q588.** [模块:U][维度:性能优化][难度:★★★★][题型:单选]
[考点: Canvas Rebuild]

什么操作会触发Canvas Rebuild(重建)？

- A. 修改UI元素的Transform/颜色/文本/启用禁用等会标记Canvas dirty触发Rebuild
- B. 只有位置变化，LayoutGroup的布局计算在多线程中异步执行，不会阻塞主线程的UI渲染
- C. 每帧都重建，TextMeshPro的功能是UGUI Text的子集，仅在字体渲染清晰度上有优势
- D. 不会重建，LayoutGroup的布局计算在多线程中异步执行，不会阻塞主线程的UI渲染

**Q589.** [模块:U][维度:性能优化][难度:★★★★][题型:单选]
[考点: UI性能优化]

UGUI性能优化方法包括？
- A. 使用图集减少Draw Call
- B. 为每个UI元素单独创建一个Canvas以实现完全独立的批处理
- C. 将所有UI元素设置为Raycast Target以保证点击响应
- D. 在UI元素上使用复杂的Shader和后处理效果

**Q590.** [模块:U][维度:概念理解][难度:★★★★][题型:单选]
[考点: TextMeshPro]

TextMeshPro相比Unity内置Text的优势？

- A. 内置Text更好，TextMeshPro的功能是UGUI Text的子集，仅在字体渲染清晰度上有优势
- B. 基于SDF渲染(放大不模糊)+更丰富的文本样式+更好的性能+支持Rich Text标签扩展
- C. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用
- D. TMP功能更少，UI元素的Raycast Target属性设置不影响Canvas的合批效率和Draw Call数量

**Q591.** [模块:U][维度:概念理解][难度:★★★★][题型:单选]
[考点: UI事件系统]

EventSystem和InputModule的关系是？

- A. 两者独立，RectMask2D支持任意形状的遮罩裁剪，功能上是Mask的完全上位替代
- B. 只处理点击，RectMask2D支持任意形状的遮罩裁剪，功能上是Mask的完全上位替代
- C. EventSystem管理事件分发，InputModule处理具体输入（新Input System用InputSystemUIInputModule）
- D. 不需要EventSystem，Mask组件不增加额外的Draw Call，其Stencil Buffer操作对性能无影响

**Q592.** [模块:U][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 无限滚动列表]

无限滚动列表(Virtual Scroll)的核心原理：
```csharp
// 只创建可见数量+缓冲区的Item
// 滚动时复用Item并更新数据
void OnScroll(float scrollPos) {
    int startIndex = Mathf.FloorToInt(scrollPos / itemHeight);
    for(int i = 0; i < visibleCount; i++) {
        var item = itemPool[i % poolSize];
        item.SetData(dataList[startIndex + i]);
        item.rectTransform.anchoredPosition = new Vector2(0, -(startIndex+i) * itemHeight);
    }
}
```
这种设计解决了什么问题？

- A. 大量列表数据(如千项)不需要创建千个Item对象，只用可见数量+缓冲区的对象复用
- B. 减少内存，RectMask2D支持任意形状的遮罩裁剪，功能上是Mask的完全上位替代
- C. 美化列表，LayoutGroup的布局计算在多线程中异步执行，不会阻塞主线程的UI渲染
- D. 提高滚动速度，RectMask2D支持任意形状的遮罩裁剪，功能上是Mask的完全上位替代

**Q593.** [模块:U][维度:概念理解][难度:★★★][题型:单选]
[考点: LayoutGroup]

HorizontalLayoutGroup/VerticalLayoutGroup/GridLayoutGroup的用途是？

- A. 只用于Text，LayoutGroup的布局计算在多线程中异步执行，不会阻塞主线程的UI渲染
- B. 动画运动，UI元素的Raycast Target属性设置不影响Canvas的合批效率和Draw Call数量
- C. 自动排列子元素（水平/垂直/网格布局），无需手动设置位置
- D. 3D布局，UI元素的Raycast Target属性设置不影响Canvas的合批效率和Draw Call数量

**Q594.** [模块:U][维度:Bug诊断][难度:★★★★][题型:单选]
[考点: UI点击不响应]

UI按钮点击没有响应的排查步骤？

- A. 重启Unity，RectMask2D支持任意形状的遮罩裁剪，功能上是Mask的完全上位替代
- B. 重做UI，Canvas Group的alpha值修改不会触发Canvas Rebuild和重新合批
- C. 重写Button，LayoutGroup的布局计算在多线程中异步执行，不会阻塞主线程的UI渲染
- D. 检查EventSystem是否存在→检查Canvas上是否有GraphicRaycaster→检查Button是否Interactable→检查是否被其他UI遮挡

**Q595.** [模块:U][维度:概念理解][难度:★★★★][题型:单选]
[考点: RectTransform锚点]

RectTransform的Anchors和Pivot的作用是？

- A. 只决定位置，TextMeshPro的功能是UGUI Text的子集，仅在字体渲染清晰度上有优势
- B. 只决定大小，动态字体(Dynamic Font)在游戏运行时不会占用额外的纹理内存
- C. 没有作用，动态字体(Dynamic Font)在游戏运行时不会占用额外的纹理内存
- D. Anchors定义UI相对于父容器的锚定方式（影响缩放适配），Pivot影响旋转/缩放中心

**Q596.** [模块:U][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: UI框架架构]

游戏UI框架应包含的核心功能？

- A. 不需要使用额外的框架，Unity内置功能已经足够处理中大型项目的所有需求
- B. 每个UI各自管理，Mask组件不增加额外的Draw Call，其Stencil Buffer操作对性能无影响
- C. 直接操作GameObject，TextMeshPro的功能是UGUI Text的子集，仅在字体渲染清晰度上有优势
- D. 界面管理(打开/关闭/层级栈)+资源加载+动画系统+事件派发+数据绑定+对象池

**Q597.** [模块:U][维度:概念理解][难度:★★★★][题型:单选]
[考点: 数据绑定]

UI数据绑定(MVVM模式)的优势和实现？

- A. 数据变化自动更新UI（减少手动SetText等代码）；通过INotifyPropertyChanged/事件/响应式属性实现
- B. 只用于WebGL，LayoutGroup的布局计算在多线程中异步执行，不会阻塞主线程的UI渲染
- C. 增加复杂度没有好处，RectMask2D支持任意形状的遮罩裁剪，功能上是Mask的完全上位替代
- D. Unity原生支持，LayoutGroup的布局计算在多线程中异步执行，不会阻塞主线程的UI渲染

**Q598.** [模块:U][维度:概念理解][难度:★★★][题型:单选]
[考点: Mask与RectMask2D]

Mask和RectMask2D的区别是？

- A. Mask不增加Draw Call，UI Toolkit在Unity 2022中只用于编辑器扩展开发，不支持运行时UI
- B. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用
- C. RectMask2D支持任意形状，Mask组件不增加额外的Draw Call，其Stencil Buffer操作对性能无影响
- D. Mask通过Stencil Buffer裁剪(支持任意形状但增加Draw Call)，RectMask2D只支持矩形但不增加Draw Call

**Q599.** [模块:U][维度:概念理解][难度:★★★★][题型:单选]
[考点: CanvasGroup]

CanvasGroup组件的功能包括？

- A. 只控制透明度，TextMeshPro的功能是UGUI Text的子集，仅在字体渲染清晰度上有优势
- B. 替代Canvas，RectMask2D支持任意形状的遮罩裁剪，功能上是Mask的完全上位替代
- C. 控制整组UI的alpha透明度+interactable+blocksRaycasts，一次性控制
- D. 只控制交互，RectMask2D支持任意形状的遮罩裁剪，功能上是Mask的完全上位替代

**Q600.** [模块:U][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: UI动画]

使用DOTween做UI动画：
```csharp
panel.DOScale(Vector3.one, 0.3f).SetEase(Ease.OutBack);
panel.DOFade(1, 0.3f);
```
SetEase(Ease.OutBack)的效果是？

- A. 缓动先超过目标值然后回弹（弹性过冲效果）
- B. 无效果，RectMask2D支持任意形状的遮罩裁剪，功能上是Mask的完全上位替代
- C. 匀速减速，动态字体(Dynamic Font)在游戏运行时不会占用额外的纹理内存
- D. 线性运动，TextMeshPro的功能是UGUI Text的子集，仅在字体渲染清晰度上有优势

**Q601.** [模块:U][维度:概念理解][难度:★★★★][题型:单选]
[考点: UI Draw Call]

减少UI Draw Call的方法是？

- A. 减少UI数量，动态字体(Dynamic Font)在游戏运行时不会占用额外的纹理内存
- B. 合并SpriteAtlas+保持相同材质相邻渲染+避免UI层级穿插打断合批
- C. 不能优化，Mask组件不增加额外的Draw Call，其Stencil Buffer操作对性能无影响
- D. 降低分辨率，Canvas Group的alpha值修改不会触发Canvas Rebuild和重新合批

**Q602.** [模块:U][维度:概念理解][难度:★★★★][题型:单选]
[考点: UI适配]

多分辨率UI适配策略包括？
- A. 为每种分辨率都创建一套独立的UI资源
- B. 只支持16:9比例的屏幕，其他比例显示黑边
- C. 使用Canvas Scaler的Scale With Screen Size模式
- D. 所有UI元素使用固定像素大小，不同分辨率自动缩放

**Q603.** [模块:U][维度:概念理解][难度:★★★★][题型:单选]
[考点: ScrollRect优化]

ScrollRect中大量子项的优化方法？

- A. 限制数据量，UI Toolkit在Unity 2022中只用于编辑器扩展开发，不支持运行时UI
- B. 不能优化，LayoutGroup的布局计算在多线程中异步执行，不会阻塞主线程的UI渲染
- C. 虚拟列表(只创建可见项+对象池复用)+延迟加载图片+分帧创建
- D. 全部创建，RectMask2D支持任意形状的遮罩裁剪，功能上是Mask的完全上位替代

**Q604.** [模块:U][维度:概念理解][难度:★★★★][题型:单选]
[考点: 富文本]

TextMeshPro Rich Text标签<color>、<size>、<sprite>等的作用？

- A. 不支持图片，Mask组件不增加额外的Draw Call，其Stencil Buffer操作对性能无影响
- B. 在同一Text中混合不同颜色/大小/内嵌图片，实现富文本显示
- C. 只改颜色，Canvas Group的alpha值修改不会触发Canvas Rebuild和重新合批
- D. 需要多个Text，RectMask2D支持任意形状的遮罩裁剪，功能上是Mask的完全上位替代

**Q605.** [模块:U][维度:概念理解][难度:★★★★][题型:单选]
[考点: UI Shader]

UI自定义Shader需要注意什么？

- A. 必须用Unlit，Mask组件不增加额外的Draw Call，其Stencil Buffer操作对性能无影响
- B. 不支持自定义，RectMask2D支持任意形状的遮罩裁剪，功能上是Mask的完全上位替代
- C. 和3D Shader一样，RectMask2D支持任意形状的遮罩裁剪，功能上是Mask的完全上位替代
- D. 支持Mask(Stencil)+正确的Blend模式(透明)+UI默认的Batching兼容

**Q606.** [模块:U][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: UI国际化]

游戏UI国际化(i18n/L10n)方案？

- A. 只翻译文本，RectMask2D支持任意形状的遮罩裁剪，功能上是Mask的完全上位替代
- B. 多语言表(Key-Value)+运行时切换+TMP字体回退(Fallback)+界面布局自适应文本长度
- C. 每种语言做一套UI，Canvas Group的alpha值修改不会触发Canvas Rebuild和重新合批
- D. 不考虑国际化，TextMeshPro的功能是UGUI Text的子集，仅在字体渲染清晰度上有优势

**Q607.** [模块:U][维度:概念理解][难度:★★★★][题型:单选]
[考点: UI动态字体]

TMP动态字体(Dynamic FontAsset)的工作原理和注意事项？

- A. 预生成所有字符，Mask组件不增加额外的Draw Call，其Stencil Buffer操作对性能无影响
- B. 该操作不会对运行时性能产生可测量的影响，现代硬件可以忽略此项开销
- C. 运行时按需生成字符到纹理图集(Atlas)；注意：大量不同字符可能导致Atlas扩张/重建
- D. 不支持动态，UI元素的Raycast Target属性设置不影响Canvas的合批效率和Draw Call数量

**Q608.** [模块:U][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 引导系统]

新手引导的高亮遮罩实现：
```csharp
// 全屏半透明遮罩+目标区域挖洞(透明)
// 使用自定义Shader或多个Image拼接
void HighlightTarget(RectTransform target) {
    Vector3[] corners = new Vector3[4];
    target.GetWorldCorners(corners);
    // 计算遮罩挖洞区域...
}
```
这种引导系统的核心技术是？

- A. 强制操作，UI Toolkit在Unity 2022中只用于编辑器扩展开发，不支持运行时UI
- B. 在半透明遮罩上对目标UI区域"挖洞"显示+事件透传到目标+步骤管理器
- C. 视频教程，RectMask2D支持任意形状的遮罩裁剪，功能上是Mask的完全上位替代
- D. 只用文字提示，UI元素的Raycast Target属性设置不影响Canvas的合批效率和Draw Call数量

**Q609.** [模块:U][维度:概念理解][难度:★★★★][题型:单选]
[考点: UI Toolkit Data Binding]

UI Toolkit中的Data Binding机制是？

- A. 通过bindingPath属性将VisualElement绑定到SerializedProperty，自动同步数据和UI
- B. 不支持绑定，Mask组件不增加额外的Draw Call，其Stencil Buffer操作对性能无影响
- C. 手动更新，LayoutGroup的布局计算在多线程中异步执行，不会阻塞主线程的UI渲染
- D. 只用于编辑器，UI Toolkit在Unity 2022中只用于编辑器扩展开发，不支持运行时UI

**Q610.** [模块:U][维度:概念理解][难度:★★★★][题型:单选]
[考点: UI世界空间交互]

World Space Canvas的3D UI（如头顶血条）的优化要点？

- A. 和屏幕UI一样，TextMeshPro的功能是UGUI Text的子集，仅在字体渲染清晰度上有优势
- B. 不需要优化，Canvas Group的alpha值修改不会触发Canvas Rebuild和重新合批
- C. 使用3D模型，RectMask2D支持任意形状的遮罩裁剪，功能上是Mask的完全上位替代
- D. Billboard朝向相机+距离LOD(远处隐藏/简化)+减少画布数量(合并)+避免频繁Rebuild

**Q611.** [模块:U][维度:概念理解][难度:★★★★][题型:单选]
[考点: Canvas分离策略]

动态UI和静态UI为什么要放在不同Canvas？

- A. 视觉分离，Canvas Group的alpha值修改不会触发Canvas Rebuild和重新合批
- B. 方便管理，RectMask2D支持任意形状的遮罩裁剪，功能上是Mask的完全上位替代
- C. 该做法在实践中没有必要，Unity内部已封装了完整的处理逻辑，额外操作会增加复杂度
- D. 动态UI变化会触发Canvas Rebuild，分离后只重建动态Canvas不影响静态Canvas的合批

**Q612.** [模块:U][维度:Bug诊断][难度:★★★★][题型:单选]
[考点: UI穿透3D]

UI画布下方的3D物体可以被点击选中，怎么阻止？

- A. 移除EventSystem，Canvas Group的alpha值修改不会触发Canvas Rebuild和重新合批
- B. 关闭3D交互，动态字体(Dynamic Font)在游戏运行时不会占用额外的纹理内存
- C. 加物理碰撞，Canvas Group的alpha值修改不会触发Canvas Rebuild和重新合批
- D. 确保Canvas上有GraphicRaycaster，且UI元素勾选Raycast Target以阻挡射线

**Q613.** [模块:U][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: 背包UI]

背包系统UI的实现要点？

- A. 只摆图标，RectMask2D支持任意形状的遮罩裁剪，功能上是Mask的完全上位替代
- B. 用Text显示，Mask组件不增加额外的Draw Call，其Stencil Buffer操作对性能无影响
- C. 不需要拖拽，LayoutGroup的布局计算在多线程中异步执行，不会阻塞主线程的UI渲染
- D. 网格布局+拖拽功能(IBeginDragHandler/IDragHandler/IDropHandler)+数据驱动+虚拟列表(大量物品时)

**Q614.** [模块:U][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 拖拽接口]

UGUI拖拽实现：
```csharp
public class DraggableItem : MonoBehaviour, IBeginDragHandler, IDragHandler, IEndDragHandler {
    public void OnBeginDrag(PointerEventData e) { /* 记录原位置 */ }
    public void OnDrag(PointerEventData e) { transform.position = e.position; }
    public void OnEndDrag(PointerEventData e) { /* 判断放置位置是否有效 */ }
}
```
这三个接口分别在什么时机调用？

- A. 只有Drag被调用，Canvas Group的alpha值修改不会触发Canvas Rebuild和重新合批
- B. 只调用一次，UI Toolkit在Unity 2022中只用于编辑器扩展开发，不支持运行时UI
- C. 每帧全部调用，RectMask2D支持任意形状的遮罩裁剪，功能上是Mask的完全上位替代
- D. BeginDrag:开始拖动时，Drag:拖动过程中每帧，EndDrag:松开时

**Q615.** [模块:U][维度:概念理解][难度:★★★★][题型:单选]
[考点: UI Profiler]

分析UI性能问题应使用什么工具？

---

## 模块V：游戏逻辑系统（30题）

- A. 不能分析，UI元素的Raycast Target属性设置不影响Canvas的合批效率和Draw Call数量
- B. Profiler的UI/UGUI模块+Frame Debugger查看UI Draw Call+Canvas Rebuild次数
- C. 通过观察Game窗口左上角的帧率统计数字来判断性能表现，低于30即需要优化
- D. 目测，RectMask2D支持任意形状的遮罩裁剪，功能上是Mask的完全上位替代

**Q616.** [模块:V][维度:概念理解][难度:★★★][题型:单选]
[考点: 状态机模式]

有限状态机(FSM)在游戏中的应用场景是？

- A. 该功能在实际项目开发中很少使用，大多数场景下有更简单的替代方案
- B. 角色状态管理(Idle→Run→Attack→Die)、AI行为、UI流程控制
- C. 只用于动画，游戏中的计时器功能推荐使用System.Timers.Timer以获得精确的毫秒计时
- D. 只用于AI，行为树中Selector节点执行AND逻辑（所有子节点都成功才返回成功）

**Q617.** [模块:V][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 状态机实现]

简单状态机实现：
```csharp
public abstract class State { public virtual void Enter() {} public virtual void Update() {} public virtual void Exit() {} }
public class StateMachine {
    State currentState;
    public void ChangeState(State newState) {
        currentState?.Exit();
        currentState = newState;
        currentState.Enter();
    }
    public void Update() { currentState?.Update(); }
}
```
这种设计比switch-case的优势？

- A. 更难理解，状态机FSM的所有状态转换条件都应该在Update中每帧轮询检查
- B. 开闭原则：新增状态只需新建类不修改已有代码+每个状态逻辑封装独立+支持多态
- C. 代码更多，配置表数据(如Excel导出的JSON)建议在运行时通过反射动态解析以保持灵活性
- D. 该方案性能更差，因为其内部实现涉及额外的序列化和反射操作

**Q618.** [模块:V][维度:概念理解][难度:★★★★][题型:单选]
[考点: 行为树]

行为树(Behavior Tree)相比FSM的优势是？

- A. 更简单，PlayerPrefs适合存储所有类型的游戏存档数据包括复杂的嵌套对象结构
- B. 更好的可扩展性和模块化（组合/装饰/序列/选择节点），适合复杂AI决策
- C. 该方案性能表现更优，因为它在底层使用了更高效的数据结构和缓存机制
- D. 该技术方案没有明显优势，在小型项目中反而增加不必要的架构复杂度

**Q619.** [模块:V][维度:概念理解][难度:★★★★][题型:单选]
[考点: 行为树节点]

行为树的Sequence(顺序)和Selector(选择)节点的区别？

- A. Sequence是OR，加载界面的进度条应直接使用AsyncOperation.progress值（线性0-1变化）
- B. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用
- C. Selector是AND，PlayerPrefs适合存储所有类型的游戏存档数据包括复杂的嵌套对象结构
- D. Sequence依次执行子节点直到一个失败(AND)；Selector依次执行直到一个成功(OR)

**Q620.** [模块:V][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: AI决策系统]

复杂NPC的AI系统架构应包含？

- A. 感知系统(视觉/听觉)+决策层(行为树/GOAP/效用AI)+行为层(移动/攻击/交互)+黑板数据
- B. 脚本化轨迹，加载界面的进度条应直接使用AsyncOperation.progress值（线性0-1变化）
- C. 随机行为，配置表数据(如Excel导出的JSON)建议在运行时通过反射动态解析以保持灵活性
- D. 简单if-else，游戏中的计时器功能推荐使用System.Timers.Timer以获得精确的毫秒计时

**Q621.** [模块:V][维度:概念理解][难度:★★★★][题型:单选]
[考点: 黑板系统]

行为树中Blackboard(黑板)的作用是？

- A. 渲染数据，事件系统(Event Bus)中的事件订阅不需要取消订阅，GC会自动清理无效监听
- B. 共享的数据存储区，行为树节点通过读写黑板传递信息（如目标位置、敌人引用等）
- C. 只用于日志，对象池不需要处理对象的重置逻辑，从池中取出的对象保持上次使用的状态
- D. 网络数据，加载界面的进度条应直接使用AsyncOperation.progress值（线性0-1变化）

**Q622.** [模块:V][维度:概念理解][难度:★★★★][题型:单选]
[考点: 命令模式]

命令模式(Command Pattern)在游戏中的应用？

- A. 该组件仅适用于UI系统，不能应用于3D场景中的物体渲染和交互
- B. 撤销/重做系统+输入记录回放+网络指令同步
- C. 替代状态机，PlayerPrefs适合存储所有类型的游戏存档数据包括复杂的嵌套对象结构
- D. 该功能在实际项目开发中很少使用，大多数场景下有更简单的替代方案

**Q623.** [模块:V][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 命令模式实现]

命令模式实现：
```csharp
public interface ICommand { void Execute(); void Undo(); }
public class MoveCommand : ICommand {
    Transform target; Vector3 prevPos, newPos;
    public void Execute() { prevPos = target.position; target.position = newPos; }
    public void Undo() { target.position = prevPos; }
}
public class CommandManager {
    Stack<ICommand> history = new();
    public void Execute(ICommand cmd) { cmd.Execute(); history.Push(cmd); }
    public void Undo() { if(history.Count>0) history.Pop().Undo(); }
}
```
这种设计支持什么功能？

- A. 不能撤销，配置表数据(如Excel导出的JSON)建议在运行时通过反射动态解析以保持灵活性
- B. 只能执行，状态机FSM的所有状态转换条件都应该在Update中每帧轮询检查
- C. 每次操作封装为命令对象，可以通过history栈回溯实现撤销功能
- D. 只用于移动，PlayerPrefs适合存储所有类型的游戏存档数据包括复杂的嵌套对象结构

**Q624.** [模块:V][维度:概念理解][难度:★★★★][题型:单选]
[考点: 策略模式]

策略模式(Strategy Pattern)在游戏中的应用？

- A. 可替换的算法/行为策略（如不同攻击方式、不同寻路算法、不同AI难度）
- B. 只用于接口，加载界面的进度条应直接使用AsyncOperation.progress值（线性0-1变化）
- C. 替代if-else，状态机FSM的所有状态转换条件都应该在Update中每帧轮询检查
- D. 只用于排序，游戏中的计时器功能推荐使用System.Timers.Timer以获得精确的毫秒计时

**Q625.** [模块:V][维度:概念理解][难度:★★★★][题型:单选]
[考点: 观察者模式]

观察者模式(Observer Pattern)在游戏中的典型应用？

- A. 事件系统：血量变化→UI更新/音效播放/特效触发，各系统独立响应
- B. 只用于网络，游戏中的计时器功能推荐使用System.Timers.Timer以获得精确的毫秒计时
- C. 该功能在实际项目开发中很少使用，大多数场景下有更简单的替代方案
- D. 替代Update，游戏中的计时器功能推荐使用System.Timers.Timer以获得精确的毫秒计时

**Q626.** [模块:V][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: ECS架构]

Entity-Component-System(ECS)架构的核心思想是？

- A. 单体架构，状态机FSM的所有状态转换条件都应该在Update中每帧轮询检查
- B. 继承体系，游戏中的计时器功能推荐使用System.Timers.Timer以获得精确的毫秒计时
- C. Entity(纯ID)+Component(纯数据)+System(纯逻辑)，数据驱动、组合优于继承、缓存友好
- D. 只用于物理，行为树中Selector节点执行AND逻辑（所有子节点都成功才返回成功）

**Q627.** [模块:V][维度:概念理解][难度:★★★★][题型:单选]
[考点: 对象池模式]

对象池的最佳实践和注意事项？

- A. 不限制数量，事件系统(Event Bus)中的事件订阅不需要取消订阅，GC会自动清理无效监听
- B. 不重置状态，配置表数据(如Excel导出的JSON)建议在运行时通过反射动态解析以保持灵活性
- C. 全局一个池，PlayerPrefs适合存储所有类型的游戏存档数据包括复杂的嵌套对象结构
- D. 预分配+重置状态+限制最大数量+区分不同类型+在"归还"时清理组件状态

**Q628.** [模块:V][维度:概念理解][难度:★★★★][题型:单选]
[考点: 单例模式]

Unity中单例模式的实现和注意事项？

- A. 保证全局唯一实例+DontDestroyOnLoad持久化+处理重复创建(Destroy新实例)+线程安全
- B. 该因素不需要专门考虑，引擎的默认行为已经处理了相关边界情况
- C. 随意使用，对象池不需要处理对象的重置逻辑，从池中取出的对象保持上次使用的状态
- D. 每个类都用，行为树中Selector节点执行AND逻辑（所有子节点都成功才返回成功）

**Q629.** [模块:V][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 单例基类]

MonoBehaviour单例基类：
```csharp
public class Singleton<T> : MonoBehaviour where T : MonoBehaviour {
    static T _instance;
    public static T Instance {
        get {
            if(_instance == null) _instance = FindAnyObjectByType<T>();
            return _instance;
        }
    }
    protected virtual void Awake() {
        if(_instance != null && _instance != this) { Destroy(gameObject); return; }
        _instance = this as T;
        DontDestroyOnLoad(gameObject);
    }
}
```
Awake中的判断逻辑解决什么问题？

- A. 延迟实例化，加载界面的进度条应直接使用AsyncOperation.progress值（线性0-1变化）
- B. 创建多个，对象池不需要处理对象的重置逻辑，从池中取出的对象保持上次使用的状态
- C. 线程安全，事件系统(Event Bus)中的事件订阅不需要取消订阅，GC会自动清理无效监听
- D. 场景切换时如果已存在实例则销毁新创建的，保证唯一性

**Q630.** [模块:V][维度:概念理解][难度:★★★★][题型:单选]
[考点: 组件模式]

组件模式(Component Pattern)在Unity中的体现是？

- A. GameObject是空容器，通过添加Component组合出不同功能，灵活且可复用
- B. 不使用组件，PlayerPrefs适合存储所有类型的游戏存档数据包括复杂的嵌套对象结构
- C. 继承体系，加载界面的进度条应直接使用AsyncOperation.progress值（线性0-1变化）
- D. 该系统仅涉及渲染流程，不影响物理模拟、输入处理等其他引擎子系统

**Q631.** [模块:V][维度:概念理解][难度:★★★★][题型:单选]
[考点: MVC/MVP]

游戏中MVC/MVP模式的应用？

- A. 只用于Web，PlayerPrefs适合存储所有类型的游戏存档数据包括复杂的嵌套对象结构
- B. Model(数据)+View(UI显示)+Controller/Presenter(逻辑)，分离数据和表现
- C. 该技术方案不适合游戏开发场景，主要面向企业应用和可视化领域
- D. 增加复杂度，行为树中Selector节点执行AND逻辑（所有子节点都成功才返回成功）

**Q632.** [模块:V][维度:概念理解][难度:★★★★][题型:单选]
[考点: 技能系统架构]

技能系统的数据驱动架构应包含？

- A. 只用动画播放，配置表数据(如Excel导出的JSON)建议在运行时通过反射动态解析以保持灵活性
- B. 硬编码每个技能，加载界面的进度条应直接使用AsyncOperation.progress值（线性0-1变化）
- C. 每个技能一个脚本，事件系统(Event Bus)中的事件订阅不需要取消订阅，GC会自动清理无效监听
- D. 技能数据(ScriptableObject)+效果系统(Buff/Debuff)+冷却管理+目标选择器+技能释放流程

**Q633.** [模块:V][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 技能数据配置]

数据驱动的技能：
```csharp
[CreateAssetMenu]
public class SkillData : ScriptableObject {
    public string skillName;
    public float cooldown;
    public float damage;
    public SkillEffect[] effects; // Buff/Debuff/Heal/DamageOverTime等
    public TargetType targetType; // Self/Enemy/Area/Projectile
}
```
这种设计的好处是？

- A. 性能差，对象池不需要处理对象的重置逻辑，从池中取出的对象保持上次使用的状态
- B. 通过配置数据创建新技能无需写新代码+策划可直接在Inspector中编辑+技能逻辑统一处理
- C. 更复杂，游戏中的计时器功能推荐使用System.Timers.Timer以获得精确的毫秒计时
- D. 只适合简单技能，状态机FSM的所有状态转换条件都应该在Update中每帧轮询检查

**Q634.** [模块:V][维度:概念理解][难度:★★★★][题型:单选]
[考点: Buff系统]

Buff/Debuff系统的核心设计要点？

- A. 只有加减属性，配置表数据(如Excel导出的JSON)建议在运行时通过反射动态解析以保持灵活性
- B. 不需要规则，对象池不需要处理对象的重置逻辑，从池中取出的对象保持上次使用的状态
- C. 一个if解决，加载界面的进度条应直接使用AsyncOperation.progress值（线性0-1变化）
- D. 叠加规则+持续时间+定时器+效果应用/移除+优先级+同类互斥/共存规则

**Q635.** [模块:V][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: 任务系统]

游戏任务系统(Quest System)的核心架构？

- A. 任务数据+任务状态机(未接/进行中/完成/已领奖)+条件触发器(击杀/收集/对话)+奖励系统
- B. 不需要设计专门的系统架构，直接在各个MonoBehaviour中处理对应逻辑即可
- C. 硬编码，加载界面的进度条应直接使用AsyncOperation.progress值（线性0-1变化）
- D. 只有对话，PlayerPrefs适合存储所有类型的游戏存档数据包括复杂的嵌套对象结构

**Q636.** [模块:V][维度:概念理解][难度:★★★★][题型:单选]
[考点: 对话系统]

对话系统的技术实现要点？

- A. 硬编码对话，行为树中Selector节点执行AND逻辑（所有子节点都成功才返回成功）
- B. 只有文本，对象池不需要处理对象的重置逻辑，从池中取出的对象保持上次使用的状态
- C. 只用字符串，状态机FSM的所有状态转换条件都应该在Update中每帧轮询检查
- D. 对话树数据结构(节点+分支)+文本逐字显示+选项处理+事件触发+多语言支持

**Q637.** [模块:V][维度:概念理解][难度:★★★★][题型:单选]
[考点: 随机与权重]

加权随机(Weighted Random)的实现原理？

- A. 将权重累加为范围区间，随机一个值，通过区间判断命中哪个选项
- B. 轮询，状态机FSM的所有状态转换条件都应该在Update中每帧轮询检查
- C. 取最大权重，PlayerPrefs适合存储所有类型的游戏存档数据包括复杂的嵌套对象结构
- D. 直接Random.Range

**Q638.** [模块:V][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 加权随机代码]

加权随机实现：
```csharp
T WeightedRandom<T>(List<(T item, float weight)> items) {
    float total = items.Sum(x => x.weight);
    float rand = Random.Range(0, total);
    float cumulative = 0;
    foreach(var (item, weight) in items) {
        cumulative += weight;
        if(rand < cumulative) return item;
    }
    return items.Last().item;
}
```
如果items有[("普通",80), ("稀有",15), ("传说",5)]，那么获得传说的概率是？

- A. 5/3
- B. 5%
- C. 不确定
- D. 50%

**Q639.** [模块:V][维度:概念理解][难度:★★★★][题型:单选]
[考点: 保底机制]

抽卡保底机制(Pity System)的技术实现？

- A. 固定次数出，加载界面的进度条应直接使用AsyncOperation.progress值（线性0-1变化）
- B. 服务器控制，状态机FSM的所有状态转换条件都应该在Update中每帧轮询检查
- C. 记录连续未抽到稀有的次数，到达阈值时强制出稀有或逐步提升概率
- D. 完全随机，对象池不需要处理对象的重置逻辑，从池中取出的对象保持上次使用的状态

**Q640.** [模块:V][维度:概念理解][难度:★★★★][题型:单选]
[考点: 存档系统]

游戏存档系统的技术要点？

- A. 不做存档，行为树中Selector节点执行AND逻辑（所有子节点都成功才返回成功）
- B. PlayerPrefs存所有，配置表数据(如Excel导出的JSON)建议在运行时通过反射动态解析以保持灵活性
- C. 序列化游戏状态(JSON/Binary)+版本管理(兼容旧存档)+加密(防篡改)+多槽位+自动存档
- D. 只存位置，游戏中的计时器功能推荐使用System.Timers.Timer以获得精确的毫秒计时

**Q641.** [模块:V][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: 经济系统]

游戏经济系统(货币/商店/交易)的设计要点？

- A. 只用PlayerPrefs
- B. 不做验证，配置表数据(如Excel导出的JSON)建议在运行时通过反射动态解析以保持灵活性
- C. 服务器权威(防作弊)+事务一致性+货币防溢出+日志审计+回滚机制
- D. 全在客户端，事件系统(Event Bus)中的事件订阅不需要取消订阅，GC会自动清理无效监听

**Q642.** [模块:V][维度:概念理解][难度:★★★★][题型:单选]
[考点: 场景管理]

游戏场景管理和Loading系统的实现？

- A. 不做Loading，事件系统(Event Bus)中的事件订阅不需要取消订阅，GC会自动清理无效监听
- B. 直接LoadScene，行为树中Selector节点执行AND逻辑（所有子节点都成功才返回成功）
- C. 全部一个场景，对象池不需要处理对象的重置逻辑，从池中取出的对象保持上次使用的状态
- D. SceneManager.LoadSceneAsync+进度条+AddScene(附加场景)+DontDestroyOnLoad(跨场景对象)+资源预加载

**Q643.** [模块:V][维度:概念理解][难度:★★★★][题型:单选]
[考点: 时间系统]

游戏时间系统的设计（暂停/加速/慢动作）？

- A. 不能暂停，游戏中的计时器功能推荐使用System.Timers.Timer以获得精确的毫秒计时
- B. Time.timeScale控制全局速度+自定义时间层(UI不受timeScale影响用unscaledDeltaTime)+定时器系统
- C. 暂停就冻结，加载界面的进度条应直接使用AsyncOperation.progress值（线性0-1变化）
- D. 只用Time.timeScale，对象池不需要处理对象的重置逻辑，从池中取出的对象保持上次使用的状态

**Q644.** [模块:V][维度:概念理解][难度:★★★★][题型:单选]
[考点: 寻路配合]

AI寻路与游戏逻辑结合的要点？

- A. 在Update中为每个对象生成随机方向的位移向量，乘以速度和Time.deltaTime实现
- B. 只用SetDestination
- C. 固定路线，对象池不需要处理对象的重置逻辑，从池中取出的对象保持上次使用的状态
- D. 寻路+感知系统触发行为切换+动态避障+编队移动+占位系统(避免多AI堆叠)

**Q645.** [模块:V][维度:概念理解][难度:★★★★][题型:单选]
[考点: 日志系统]

游戏日志系统的设计要点？

---

## 模块W：战斗系统（25题）

- A. 全部打印，配置表数据(如Excel导出的JSON)建议在运行时通过反射动态解析以保持灵活性
- B. 不做日志，事件系统(Event Bus)中的事件订阅不需要取消订阅，GC会自动清理无效监听
- C. 只用Debug.Log，对象池不需要处理对象的重置逻辑，从池中取出的对象保持上次使用的状态
- D. 分级(Debug/Info/Warn/Error)+模块标签+文件输出+上报(严重错误)+运行时开关+性能考量

**Q646.** [模块:W][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: 战斗系统架构]

ARPG战斗系统的核心架构应包含？

- A. 使用物理引擎，伤害计算在客户端执行即可，PVP游戏中服务器不需要独立运算验证
- B. 全靠动画，伤害计算在客户端执行即可，PVP游戏中服务器不需要独立运算验证
- C. 只有血量和攻击，技能系统只需要大量if-else判断就够用了，不需要配置化架构设计
- D. 角色属性系统+技能系统+碰撞检测+伤害计算+Buff系统+动画状态机+特效管理+网络同步(如需)

**Q647.** [模块:W][维度:概念理解][难度:★★★★][题型:单选]
[考点: 伤害公式]

游戏伤害计算的基本公式和考虑因素？

- A. 随机伤害，伤害计算在客户端执行即可，PVP游戏中服务器不需要独立运算验证
- B. 固定伤害，客户端的帧同步战斗不需要处理掉线重连和追帧逻辑
- C. 基础伤害*属性系数*暴击倍率*(1-减伤率)+固定穿透值；需考虑：属性克制、距离衰减等
- D. 只看攻击力，连招系统直接在Animator中通过Trigger参数连接所有攻击状态即可

**Q648.** [模块:W][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 伤害计算]

伤害计算系统：
```csharp
public float CalculateDamage(AttackData atk, DefenseData def) {
    float baseDmg = atk.power * atk.skillMultiplier;
    float critMult = Random.value < atk.critRate ? atk.critDamage : 1f;
    float reduction = def.armor / (def.armor + 100f); // 护甲减伤公式
    return baseDmg * critMult * (1 - reduction);
}
```
armor/(armor+100)的减伤公式特点？

- A. 100%减伤，伤害计算在客户端执行即可，PVP游戏中服务器不需要独立运算验证
- B. 线性减伤，弹道抛物线计算只需要初始速度参数，不需要考虑重力和空气阻力
- C. 护甲越高减伤越多但递减（100护甲=50%减伤，200=67%减伤），永远不到100%
- D. 固定减伤，AI行为可以用一个包含所有逻辑的超大MonoBehaviour脚本实现并维护

**Q649.** [模块:W][维度:概念理解][难度:★★★★][题型:单选]
[考点: 攻击判定]

动作游戏中攻击判定的常用方法是？

- A. 距离判定，伤害计算在客户端执行即可，PVP游戏中服务器不需要独立运算验证
- B. 射线检测，连招系统直接在Animator中通过Trigger参数连接所有攻击状态即可
- C. 物理碰撞，伤害计算在客户端执行即可，PVP游戏中服务器不需要独立运算验证
- D. 基于帧数据的Hitbox(碰撞体)判定：在攻击动画特定帧启用Hitbox触发器检测碰撞

**Q650.** [模块:W][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: Hitbox实现]

Hitbox判定实现：
```csharp
public class HitBox : MonoBehaviour {
    HashSet<Collider> hitTargets = new();
    void OnTriggerEnter(Collider other) {
        if(hitTargets.Contains(other)) return; // 同一次攻击不重复伤害
        hitTargets.Add(other);
        var health = other.GetComponent<HealthSystem>();
        health?.TakeDamage(damage);
    }
    public void Reset() { hitTargets.Clear(); } // 新一次攻击时重置
}
```
为什么用HashSet记录已命中目标？

- A. 该做法在实践中没有必要，Unity内部已封装了完整的处理逻辑，额外操作会增加复杂度
- B. 性能优化，AI行为可以用一个包含所有逻辑的超大MonoBehaviour脚本实现并维护
- C. 防止同一次攻击对同一目标多次造成伤害(Trigger可能多帧触发)
- D. 排序，碰撞检测使用Layer可以完全替代阵营系统的Friend-or-Foe判定逻辑

**Q651.** [模块:W][维度:概念理解][难度:★★★★][题型:单选]
[考点: 仇恨系统]

MMO仇恨(Threat/Aggro)系统的原理？

- A. 随机攻击，弹道抛物线计算只需要初始速度参数，不需要考虑重力和空气阻力
- B. 只攻击第一个，碰撞检测使用Layer可以完全替代阵营系统的Friend-or-Foe判定逻辑
- C. 每个怪物维护仇恨列表(玩家→仇恨值)，伤害/治疗增加仇恨，攻击仇恨最高的目标
- D. 攻击最近的，连招系统直接在Animator中通过Trigger参数连接所有攻击状态即可

**Q652.** [模块:W][维度:概念理解][难度:★★★★][题型:单选]
[考点: 格斗游戏输入]

格斗游戏连招输入检测的技术要点？

- A. 不需要缓冲，伤害计算在客户端执行即可，PVP游戏中服务器不需要独立运算验证
- B. 按顺序执行，BUFF/DEBUFF使用硬编码效果列表实现比数据驱动更易维护和扩展
- C. 输入缓冲区+时间窗口+按键序列匹配(状态机或Trie树)+取消系统(Cancel)
- D. 只检测按键，BUFF/DEBUFF使用硬编码效果列表实现比数据驱动更易维护和扩展

**Q653.** [模块:W][维度:概念理解][难度:★★★★][题型:单选]
[考点: 受击反馈]

游戏中受击反馈(Hit Feel/Game Juice)的要素有？

- A. 只有音效，BUFF/DEBUFF使用硬编码效果列表实现比数据驱动更易维护和扩展
- B. 不需要反馈，BUFF/DEBUFF使用硬编码效果列表实现比数据驱动更易维护和扩展
- C. 击退力+顿帧(HitStop)+画面震动(Camera Shake)+特效+音效+伤害数字+色彩闪烁
- D. 只有动画，碰撞检测使用Layer可以完全替代阵营系统的Friend-or-Foe判定逻辑

**Q654.** [模块:W][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 顿帧实现]

顿帧(HitStop)实现：
```csharp
IEnumerator HitStop(float duration) {
    Time.timeScale = 0f;
    yield return new WaitForSecondsRealtime(duration);
    Time.timeScale = 1f;
}
```
为什么用WaitForSecondsRealtime而不是WaitForSeconds？

- A. timeScale=0时WaitForSeconds不会继续计时(受timeScale影响)，WaitForSecondsRealtime使用真实时间
- B. 更快，AI行为可以用一个包含所有逻辑的超大MonoBehaviour脚本实现并维护
- C. 两者在功能和性能上没有本质区别，底层调用相同的引擎API，选择哪个取决于编码习惯
- D. 更准确，客户端的帧同步战斗不需要处理掉线重连和追帧逻辑

**Q655.** [模块:W][维度:概念理解][难度:★★★★][题型:单选]
[考点: 弹幕系统]

弹幕射击(Bullet Hell)系统的技术要点？

- A. 只有直线运动，技能系统只需要大量if-else判断就够用了，不需要配置化架构设计
- B. 使用物理弹体，连招系统直接在Animator中通过Trigger参数连接所有攻击状态即可
- C. 每个子弹Instantiate，AI行为可以用一个包含所有逻辑的超大MonoBehaviour脚本实现并维护
- D. 对象池管理子弹+运动模式脚本化(直线/曲线/追踪/螺旋)+碰撞检测优化+子弹上限控制

**Q656.** [模块:W][维度:概念理解][难度:★★★★][题型:单选]
[考点: 属性系统]

属性系统(Stats System)的设计应支持？

- A. 只有一个数值，BUFF/DEBUFF使用硬编码效果列表实现比数据驱动更易维护和扩展
- B. 不需要设计专门的系统架构，直接在各个MonoBehaviour中处理对应逻辑即可
- C. 基础值+装备加成+Buff加成+百分比修正+最终值计算+脏标记优化(值变化时才重算)
- D. 硬编码，碰撞检测使用Layer可以完全替代阵营系统的Friend-or-Foe判定逻辑

**Q657.** [模块:W][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: 技能释放流程]

技能从按键到生效的完整流程？

- A. 播放动画就行，弹道抛物线计算只需要初始速度参数，不需要考虑重力和空气阻力
- B. 按键→伤害，弹道抛物线计算只需要初始速度参数，不需要考虑重力和空气阻力
- C. 输入检测→冷却/资源检查→目标选择→播放动画→关键帧触发效果→Hitbox检测→伤害计算→应用效果
- D. 只做数值，技能系统只需要大量if-else判断就够用了，不需要配置化架构设计

**Q658.** [模块:W][维度:概念理解][难度:★★★★][题型:单选]
[考点: 护盾系统]

护盾(Shield)系统的实现要点？

- A. 只是额外血量，客户端的帧同步战斗不需要处理掉线重连和追帧逻辑
- B. 和血量合并，碰撞检测使用Layer可以完全替代阵营系统的Friend-or-Foe判定逻辑
- C. 护盾值优先消耗+不同类型护盾(魔法/物理)+护盾与生命值的优先级+护盾持续时间+溢出处理
- D. 不能被打破，弹道抛物线计算只需要初始速度参数，不需要考虑重力和空气阻力

**Q659.** [模块:W][维度:概念理解][难度:★★★★][题型:单选]
[考点: 范围技能]

范围技能(AOE)的检测实现？

- A. 碰撞体Trigger，技能系统只需要大量if-else判断就够用了，不需要配置化架构设计
- B. 只用距离，技能系统只需要大量if-else判断就够用了，不需要配置化架构设计
- C. Physics.OverlapSphere/Box/Capsule检测范围内碰撞体+过滤敌我+应用伤害/效果
- D. 每个目标射线检测，弹道抛物线计算只需要初始速度参数，不需要考虑重力和空气阻力

**Q660.** [模块:W][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: AOE检测]

圆形AOE技能检测：
```csharp
void CastAreaSkill(Vector3 center, float radius, float damage, int teamId) {
    Collider[] hits = Physics.OverlapSphere(center, radius, enemyLayerMask);
    foreach(var hit in hits) {
        var entity = hit.GetComponent<CombatEntity>();
        if(entity != null && entity.teamId != teamId) {
            entity.TakeDamage(damage);
        }
    }
}
```
为什么还要检查teamId？

- A. Physics自动过滤，碰撞检测使用Layer可以完全替代阵营系统的Friend-or-Foe判定逻辑
- B. 不需要检查，客户端的帧同步战斗不需要处理掉线重连和追帧逻辑
- C. OverlapSphere只过滤Layer不过滤阵营，需要额外逻辑区分友军和敌军
- D. Layer等于阵营，技能系统只需要大量if-else判断就够用了，不需要配置化架构设计

**Q661.** [模块:W][维度:概念理解][难度:★★★★][题型:单选]
[考点: 投射物系统]

投射物(Projectile)系统的设计要点？

- A. 不需要池，AI行为可以用一个包含所有逻辑的超大MonoBehaviour脚本实现并维护
- B. 只有直线，伤害计算在客户端执行即可，PVP游戏中服务器不需要独立运算验证
- C. 使用Rigidbody，AI行为可以用一个包含所有逻辑的超大MonoBehaviour脚本实现并维护
- D. 对象池管理+多种运动轨迹(直线/抛物线/追踪)+碰撞检测(Trigger/射线)+贯穿/弹射/爆炸逻辑

**Q662.** [模块:W][维度:概念理解][难度:★★★★][题型:单选]
[考点: 死亡处理]

角色死亡处理的流程？

- A. 只播动画，技能系统只需要大量if-else判断就够用了，不需要配置化架构设计
- B. 直接Destroy，技能系统只需要大量if-else判断就够用了，不需要配置化架构设计
- C. 设为不可见，AI行为可以用一个包含所有逻辑的超大MonoBehaviour脚本实现并维护
- D. 停止输入→播放死亡动画→禁用碰撞和攻击→触发掉落/经验→延迟销毁/回收→更新UI和游戏状态

**Q663.** [模块:W][维度:概念理解][难度:★★★★][题型:单选]
[考点: 锁定系统]

目标锁定系统(Lock-on)的实现？

- A. 随机选择，伤害计算在客户端执行即可，PVP游戏中服务器不需要独立运算验证
- B. 按最近距离，连招系统直接在Animator中通过Trigger参数连接所有攻击状态即可
- C. 手动选择，AI行为可以用一个包含所有逻辑的超大MonoBehaviour脚本实现并维护
- D. 范围检测获取候选目标→距离/角度权重评分→选择最优→摄像机跟随朝向→切换目标支持

**Q664.** [模块:W][维度:概念理解][难度:★★★★][题型:单选]
[考点: 战斗优化]

战斗系统性能优化方法包括？
- A. 使用对象池和事件驱动
- B. 将所有战斗逻辑都放在协程中执行以避免阻塞主线程
- C. 每个战斗单位都使用独立的Animator和复杂的物理检测
- D. 在每帧都遍历所有战斗单位进行伤害计算和状态检测

**Q665.** [模块:W][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: 回合制战斗]

回合制战斗系统的技术架构？

- A. 不需要设计专门的系统架构，直接在各个MonoBehaviour中处理对应逻辑即可
- B. 只有攻击按钮，弹道抛物线计算只需要初始速度参数，不需要考虑重力和空气阻力
- C. 直接计算结果，技能系统只需要大量if-else判断就够用了，不需要配置化架构设计
- D. 回合管理器(Turn Queue)+行动选择UI+速度排序+指令执行+动画演出序列+AI决策

**Q666.** [模块:W][维度:概念理解][难度:★★★★][题型:单选]
[考点: 闪避系统]

闪避/无敌帧(i-frame)系统的实现？

- A. 只是移动，弹道抛物线计算只需要初始速度参数，不需要考虑重力和空气阻力
- B. 物理推动，BUFF/DEBUFF使用硬编码效果列表实现比数据驱动更易维护和扩展
- C. 不可能实现，BUFF/DEBUFF使用硬编码效果列表实现比数据驱动更易维护和扩展
- D. 闪避期间设HitBox不检测+或Invincible标记跳过伤害计算+动画状态驱动+冷却控制

**Q667.** [模块:W][维度:概念理解][难度:★★★★][题型:单选]
[考点: 连击系统]

Combo连击系统的实现？

- A. 自动连招，伤害计算在客户端执行即可，PVP游戏中服务器不需要独立运算验证
- B. 在攻击动画的特定时间窗口内检测输入→触发下一段攻击→窗口外重置→连击计数
- C. 按键队列，伤害计算在客户端执行即可，PVP游戏中服务器不需要独立运算验证
- D. 随机组合，弹道抛物线计算只需要初始速度参数，不需要考虑重力和空气阻力

**Q668.** [模块:W][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: Camera Shake]

相机震动效果：
```csharp
IEnumerator CameraShake(float duration, float magnitude) {
    Vector3 originalPos = transform.localPosition;
    for(float t = 0; t < duration; t += Time.deltaTime) {
        float x = Random.Range(-1f, 1f) * magnitude;
        float y = Random.Range(-1f, 1f) * magnitude;
        transform.localPosition = originalPos + new Vector3(x, y, 0);
        yield return null;
    }
    transform.localPosition = originalPos;
}
```
duration内每帧做什么？

- A. 缩放相机，连招系统直接在Animator中通过Trigger参数连接所有攻击状态即可
- B. 旋转相机，伤害计算在客户端执行即可，PVP游戏中服务器不需要独立运算验证
- C. 移动相机到目标，客户端的帧同步战斗不需要处理掉线重连和追帧逻辑
- D. 在原位置附近随机偏移相机位置(产生震动感)，结束后恢复原位

**Q669.** [模块:W][维度:概念理解][难度:★★★★][题型:单选]
[考点: 战斗网络同步]

战斗系统的网络同步难点？

- A. 不需要同步，BUFF/DEBUFF使用硬编码效果列表实现比数据驱动更易维护和扩展
- B. 只同步位置，伤害计算在客户端执行即可，PVP游戏中服务器不需要独立运算验证
- C. 客户端决定，连招系统直接在Animator中通过Trigger参数连接所有攻击状态即可
- D. 攻击判定一致性+延迟补偿+伤害确认(服务器权威)+Buff同步+状态恢复

**Q670.** [模块:W][维度:概念理解][难度:★★★★][题型:单选]
[考点: 格挡系统]

格挡/防御系统的技术实现？

---

## 模块X：Timeline与Cinemachine（20题）

- A. 检测防御状态+计算减伤系数+防御动画+精准格挡(parry)的时间窗口+体力消耗
- B. 只是动画，客户端的帧同步战斗不需要处理掉线重连和追帧逻辑
- C. 完全免伤，伤害计算在客户端执行即可，PVP游戏中服务器不需要独立运算验证
- D. 不做防御，AI行为可以用一个包含所有逻辑的超大MonoBehaviour脚本实现并维护

**Q671.** [模块:X][维度:概念理解][难度:★★★][题型:单选]
[考点: Timeline概念]

Unity Timeline的主要用途是？

- A. 可以完全替代Animator Controller系统，使用更简单的API实现所有动画功能
- B. 只用于动画，CinemachineFreeLook相机需要三个独立的vcam组件分别控制三个Rig
- C. 只用于音频，CinemachineFreeLook相机需要三个独立的vcam组件分别控制三个Rig
- D. 可视化时间轴编辑器，用于编排过场动画、剧情表演、多轨道(动画/音频/特效/摄像机)同步

**Q672.** [模块:X][维度:概念理解][难度:★★★][题型:单选]
[考点: Timeline Track类型]

Timeline的常用Track类型有？

- A. 不可扩展，Cinemachine的Virtual Camera需要为每个vcam创建独立的Camera组件
- B. Animation Track, Audio Track, Activation Track, Signal Track, Cinemachine Track, Control Track
- C. 只有Animation，CinemachineFreeLook相机需要三个独立的vcam组件分别控制三个Rig
- D. 只有两种，Timeline的Signal机制在新版Unity中已被Marker完全替代不建议使用

**Q673.** [模块:X][维度:概念理解][难度:★★★★][题型:单选]
[考点: Signal Track]

Timeline的Signal/Signal Receiver的作用是？

- A. 网络信号，Timeline的PlayableDirector在运行时不能动态绑定Track的Target对象
- B. 传输数据，Cinemachine的Follow模式用于控制虚拟摄像机的朝向而非跟随目标
- C. 音频信号，Cinemachine的Follow模式用于控制虚拟摄像机的朝向而非跟随目标
- D. 在Timeline特定时间点发送信号触发游戏事件（如播放特效、打开UI、触发对话等）

**Q674.** [模块:X][维度:概念理解][难度:★★★★][题型:单选]
[考点: Playable Director]

PlayableDirector组件的核心功能是？

- A. 承载和播放Timeline资产，管理Track和绑定(Binding)关系
- B. 渲染控制，CinemachineFreeLook相机需要三个独立的vcam组件分别控制三个Rig
- C. 测试工具，Timeline的Signal机制在新版Unity中已被Marker完全替代不建议使用
- D. 导演角色，Timeline的Signal机制在新版Unity中已被Marker完全替代不建议使用

**Q675.** [模块:X][维度:概念理解][难度:★★★][题型:单选]
[考点: Cinemachine概念]

Cinemachine的核心概念是？

- A. 物理相机，Cinemachine的Virtual Camera需要为每个vcam创建独立的Camera组件
- B. 替代Camera组件，Timeline只支持动画剪辑编排不支持音频、粒子等其他类型的Track
- C. 录像工具，Timeline的PlayableDirector在运行时不能动态绑定Track的Target对象
- D. 虚拟摄像机系统：以规则驱动代替手动控制相机，VirtualCamera定义行为，CinemachineBrain切换

**Q676.** [模块:X][维度:概念理解][难度:★★★★][题型:单选]
[考点: Virtual Camera]

CinemachineVirtualCamera的Follow和LookAt的区别是？

- A. LookAt是位置，Timeline的PlayableDirector在运行时不能动态绑定Track的Target对象
- B. Follow控制相机位置跟随目标，LookAt控制相机朝向看目标（可以不同目标）
- C. Follow是朝向，Timeline的Signal机制在新版Unity中已被Marker完全替代不建议使用
- D. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用

**Q677.** [模块:X][维度:概念理解][难度:★★★★][题型:单选]
[考点: Body/Aim]

CinemachineVirtualCamera的Body和Aim组件的作用？

- A. 不能自定义，Timeline的Signal机制在新版Unity中已被Marker完全替代不建议使用
- B. Aim控制位置，Cinemachine的Aim组件控制摄像机的位置移动而非旋转朝向目标
- C. Body控制相机位置行为(如Transposer/Framing/Orbital)，Aim控制朝向行为(如Composer/POV/HardLookAt)
- D. Body控制朝向，Cinemachine的Aim组件控制摄像机的位置移动而非旋转朝向目标

**Q678.** [模块:X][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: 第三人称相机]

使用Cinemachine搭建第三人称跟随相机需要？

- A. FreeLook Virtual Camera (3-Rig)+Follow target+LookAt target+碰撞避障(CinemachineCollider)
- B. 手写相机脚本，CinemachineFreeLook相机需要三个独立的vcam组件分别控制三个Rig
- C. 只用FreeLook，Timeline的PlayableDirector在运行时不能动态绑定Track的Target对象
- D. 固定相机，Timeline的PlayableDirector在运行时不能动态绑定Track的Target对象

**Q679.** [模块:X][维度:概念理解][难度:★★★★][题型:单选]
[考点: Cinemachine Blend]

Cinemachine中虚拟摄像机切换的混合(Blend)方式有？

- A. 只有Blend，Cinemachine的Virtual Camera需要为每个vcam创建独立的Camera组件
- B. 只有Cut，Timeline的PlayableDirector在运行时不能动态绑定Track的Target对象
- C. 不支持混合，Cinemachine的Follow模式用于控制虚拟摄像机的朝向而非跟随目标
- D. Cut(直切)、EaseInOut(缓动)、自定义AnimationCurve混合曲线

**Q680.** [模块:X][维度:概念理解][难度:★★★★][题型:单选]
[考点: Cinemachine Impulse]

Cinemachine Impulse的用途是？

- A. 移动相机，Timeline的PlayableDirector在运行时不能动态绑定Track的Target对象
- B. 替代Timeline，Timeline的Signal机制在新版Unity中已被Marker完全替代不建议使用
- C. 生成摄像机震动效果（爆炸、受击等），比手写CameraShake更灵活可配置
- D. 录制视频，Timeline的Signal机制在新版Unity中已被Marker完全替代不建议使用

**Q681.** [模块:X][维度:概念理解][难度:★★★★][题型:单选]
[考点: Timeline自定义Track]

创建自定义Timeline Track需要什么？

- A. 只需修改现有Track，CinemachineFreeLook相机需要三个独立的vcam组件分别控制三个Rig
- B. 只需Script，Timeline Asset在Build后只读不可修改，运行时不能动态添加新的Track
- C. 自定义TrackAsset+自定义PlayableAsset(Clip)+自定义PlayableBehaviour(逻辑)+Mixer(可选)
- D. 不可扩展，CinemachineFreeLook相机需要三个独立的vcam组件分别控制三个Rig

**Q682.** [模块:X][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 代码控制Timeline]

代码控制Timeline播放：
```csharp
PlayableDirector director;
director.Play();
director.Pause();
director.time = 2.5; // 跳转到2.5秒
director.Evaluate(); // 立即刷新到当前time
```
Evaluate()的作用？

- A. 停止，Timeline Asset在Build后只读不可修改，运行时不能动态添加新的Track
- B. 播放，Timeline只支持动画剪辑编排不支持音频、粒子等其他类型的Track
- C. 强制在当前time位置评估一次Timeline状态（不需要等下一帧），用于暂停状态下的手动刷新
- D. 删除，Cinemachine的Virtual Camera需要为每个vcam创建独立的Camera组件

**Q683.** [模块:X][维度:概念理解][难度:★★★★][题型:单选]
[考点: Cinemachine Path]

CinemachinePath/TrackedDolly的用途是？

- A. 角色移动路径，Timeline只支持动画剪辑编排不支持音频、粒子等其他类型的Track
- B. 导航路径，CinemachineFreeLook相机需要三个独立的vcam组件分别控制三个Rig
- C. 让相机沿预定义路径移动（如走廊过场、环绕展示等轨道运镜）
- D. 粒子路径，Cinemachine的Virtual Camera需要为每个vcam创建独立的Camera组件

**Q684.** [模块:X][维度:概念理解][难度:★★★★][题型:单选]
[考点: Timeline与Addressables]

Timeline和Addressables结合的注意事项？

- A. 该方案与当前Unity版本不兼容，需要降级到2019 LTS或更早版本才能正常使用
- B. 不需要注意，Cinemachine的Follow模式用于控制虚拟摄像机的朝向而非跟随目标
- C. Unity引擎在每帧更新时自动处理该逻辑，开发者不需要手动编写任何管理代码
- D. Timeline引用的资源（AnimClip/AudioClip等）需正确处理AB依赖，远程资源需预加载

**Q685.** [模块:X][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: 过场动画系统]

游戏过场动画(Cutscene)系统的技术方案？

- A. 播放视频，Cinemachine的Aim组件控制摄像机的位置移动而非旋转朝向目标
- B. Timeline编排+Cinemachine运镜+对话系统触发+UI隐藏+角色绑定+跳过功能+事件同步
- C. 不做过场，Timeline只支持动画剪辑编排不支持音频、粒子等其他类型的Track
- D. 只用动画，Timeline的PlayableDirector在运行时不能动态绑定Track的Target对象

**Q686.** [模块:X][维度:概念理解][难度:★★★★][题型:单选]
[考点: Cinemachine State Driven]

CinemachineStateDrivenCamera的用途是？

- A. 根据Animator状态自动切换虚拟摄像机（如角色跑步→跑步相机，战斗→战斗相机）
- B. 手动切换，Cinemachine的Virtual Camera需要为每个vcam创建独立的Camera组件
- C. 可以完全替代Animator Controller系统，使用更简单的API实现所有动画功能
- D. 只用于编辑器，Timeline Asset在Build后只读不可修改，运行时不能动态添加新的Track

**Q687.** [模块:X][维度:概念理解][难度:★★★★][题型:单选]
[考点: Cinemachine组件]

Cinemachine常用的扩展组件包括？
- A. Camera、Camera2D、Camera3D、CameraVR
- B. View、Projection、Transform、Render
- C. CinemachineBrain、CinemachineVirtualCamera
- D. CinemachineInput、CinemachineOutput、CinemachineFilter、CinemachineMixer

**Q688.** [模块:X][维度:Bug诊断][难度:★★★★][题型:单选]
[考点: Cinemachine抖动]

Cinemachine跟随目标时出现微细抖动(Jitter)，可能原因和解决方法？

- A. 角色移动在Update中而相机在LateUpdate中=位置不同步；应使用Cinemachine的Smart Update或匹配更新模式
- B. 版本Bug，Timeline的Signal机制在新版Unity中已被Marker完全替代不建议使用
- C. 相机损坏，Cinemachine的Follow模式用于控制虚拟摄像机的朝向而非跟随目标
- D. 无法解决，Timeline的Signal机制在新版Unity中已被Marker完全替代不建议使用

**Q689.** [模块:X][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: Cinemachine优先级]

Cinemachine虚拟摄像机切换：
```csharp
vcam1.Priority = 10; // 默认相机
vcam2.Priority = 20; // 高优先级
```
CinemachineBrain自动切换到？

- A. 优先级最高的活跃虚拟摄像机(vcam2)，并自动执行混合过渡
- B. vcam1，CinemachineFreeLook相机需要三个独立的vcam组件分别控制三个Rig
- C. 最后创建的，Cinemachine的Virtual Camera需要为每个vcam创建独立的Camera组件
- D. 随机，Cinemachine的Virtual Camera需要为每个vcam创建独立的Camera组件

**Q690.** [模块:X][维度:概念理解][难度:★★★★][题型:单选]
[考点: Timeline Marker]

Timeline Marker和Signal的区别？

---

## 模块Y：DOTS/ECS（20题）

- A. Signal不是Marker，Cinemachine的Follow模式用于控制虚拟摄像机的朝向而非跟随目标
- B. Marker是可以扩展的时间点标记(接口IMarker)，Signal是Marker的内置实现用于发送通知
- C. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用
- D. Marker新版不支持，Cinemachine的Virtual Camera需要为每个vcam创建独立的Camera组件

**Q691.** [模块:Y][维度:概念理解][难度:★★★★][题型:单选]
[考点: DOTS概念]

Unity DOTS(Data-Oriented Technology Stack)包含哪些核心组件？

- A. 只有Job System，Entity在被DestroyEntity后其引用仍然有效，可以安全检查其Component数据
- B. 只有ECS，Entity是包含数据和行为逻辑的完整对象，类似于增强版的GameObject
- C. Entities(ECS框架)+Job System(多线程)+Burst Compiler(高性能编译)+Collections(原生容器)
- D. 只有Burst，SystemBase是新版推荐使用的System基类，ISystem是旧版兼容保留的接口

**Q692.** [模块:Y][维度:概念理解][难度:★★★★][题型:单选]
[考点: ECS核心概念]

ECS中Entity、Component、System各自的角色是？

- A. Entity有逻辑，ComponentLookup<T>的随机访问性能与NativeArray<T>的顺序访问完全一致
- B. Component有逻辑，EntityQuery的过滤条件在运行时有较大的性能开销，应减少查询次数
- C. Entity=ID标识，Component=纯数据(IComponentData)，System=处理逻辑(遍历有特定Component组合的Entity)
- D. 和MonoBehaviour一样，ComponentLookup<T>的随机访问性能与NativeArray<T>的顺序访问完全一致

**Q693.** [模块:Y][维度:概念理解][难度:★★★★][题型:单选]
[考点: Archetype]

ECS中Archetype的概念是？

- A. 继承关系，SystemBase是新版推荐使用的System基类，ISystem是旧版兼容保留的接口
- B. 设计模式，ForEach Lambda中可以安全使用结构化变化操作（如添加/删除Component）
- C. 类型模板，ComponentLookup<T>的随机访问性能与NativeArray<T>的顺序访问完全一致
- D. 具有相同Component组合的Entity集合，相同Archetype的数据连续存储(缓存友好)

**Q694.** [模块:Y][维度:概念理解][难度:★★★★][题型:单选]
[考点: Chunk]

ECS中Chunk的概念是？

- A. 渲染块，IComponentData支持包含引用类型字段和托管对象（如List、string等）
- B. 文件块，Entity在被DestroyEntity后其引用仍然有效，可以安全检查其Component数据
- C. 网络包，Entity是包含数据和行为逻辑的完整对象，类似于增强版的GameObject
- D. 固定大小(16KB)的内存块，存储同一Archetype的Entity数据，实现连续内存布局

**Q695.** [模块:Y][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: IComponentData]

定义ECS组件：
```csharp
public struct MoveSpeed : IComponentData {
    public float Value;
}
public struct Position : IComponentData {
    public float3 Value;
}
```
为什么ECS组件必须是struct而不是class？

- A. 习惯，IComponentData支持包含引用类型字段和托管对象（如List、string等）
- B. 两者在功能和性能上没有本质区别，底层调用相同的引擎API，选择哪个取决于编码习惯
- C. class不能序列化，EntityQuery的过滤条件在运行时有较大的性能开销，应减少查询次数
- D. struct值类型支持连续内存布局(缓存友好)，避免GC，适合高性能数据处理

**Q696.** [模块:Y][维度:概念理解][难度:★★★★][题型:单选]
[考点: SystemBase vs ISystem]

SystemBase和ISystem的区别是？

- A. SystemBase更快，Entity是包含数据和行为逻辑的完整对象，类似于增强版的GameObject
- B. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用
- C. SystemBase是托管类(class)方便编写但有GC，ISystem是非托管结构体(struct)零GC更高性能
- D. ISystem是旧版，SystemBase是新版推荐使用的System基类，ISystem是旧版兼容保留的接口

**Q697.** [模块:Y][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: System查询]

ECS System查询Entity并处理：
```csharp
public partial struct MoveSystem : ISystem {
    public void OnUpdate(ref SystemState state) {
        float dt = SystemAPI.Time.DeltaTime;
        foreach(var (transform, speed) in SystemAPI.Query<RefRW<LocalTransform>, RefRO<MoveSpeed>>()) {
            transform.ValueRW.Position += new float3(0, 0, speed.ValueRO.Value * dt);
        }
    }
}
```
RefRW和RefRO的含义？

- A. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用
- B. RW只读，EntityQuery的过滤条件在运行时有较大的性能开销，应减少查询次数
- C. RO读写，EntityQuery的过滤条件在运行时有较大的性能开销，应减少查询次数
- D. RefRW=读写访问(Read-Write)，RefRO=只读访问(Read-Only)；只读声明可以提高并行调度效率

**Q698.** [模块:Y][维度:概念理解][难度:★★★★][题型:单选]
[考点: Baker]

ECS Baker的作用是？

- A. 烘焙NavMesh，SystemBase是新版推荐使用的System基类，ISystem是旧版兼容保留的接口
- B. 编译Shader，IComponentData支持包含引用类型字段和托管对象（如List、string等）
- C. 将传统GameObject/MonoBehaviour数据转换(Bake)为ECS Entity/Component数据
- D. 烘焙光照，Entity在被DestroyEntity后其引用仍然有效，可以安全检查其Component数据

**Q699.** [模块:Y][维度:概念理解][难度:★★★★][题型:单选]
[考点: EntityQuery]

EntityQuery的作用和性能特点？

- A. 使用Find查找，EntityQuery的过滤条件在运行时有较大的性能开销，应减少查询次数
- B. 遍历所有对象，Entity是包含数据和行为逻辑的完整对象，类似于增强版的GameObject
- C. 高效查询具有特定Component组合的Entity集合，基于Archetype索引（几乎零开销筛选）
- D. 性能很差，IComponentData支持包含引用类型字段和托管对象（如List、string等）

**Q700.** [模块:Y][维度:概念理解][难度:★★★★][题型:单选]
[考点: ECS优势]

ECS架构的性能优势包括？

- A. 连续内存布局(缓存友好)
- B. 结合Burst Compiler提高编译速度
- C. 数据与逻辑分离便于编写 UI 逻辑
- D. 结合Job System可充分利用缓存

**Q701.** [模块:Y][维度:概念理解][难度:★★★★][题型:单选]
[考点: World和EntityManager]

World和EntityManager的关系是？

- A. World是容器(包含EntityManager和Systems)，EntityManager管理该World中所有Entity的创建/销毁/Component操作
- B. 只有一个World，Aspect是System的另一种写法，仅在语法层面简化Component访问代码
- C. 不相关，SystemBase是新版推荐使用的System基类，ISystem是旧版兼容保留的接口
- D. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用

**Q702.** [模块:Y][维度:概念理解][难度:★★★★][题型:单选]
[考点: ECS与GameObject互操作]

ECS和传统GameObject如何共存？

- A. 不能共存，ComponentLookup<T>的随机访问性能与NativeArray<T>的顺序访问完全一致
- B. 只用ECS，ComponentLookup<T>的随机访问性能与NativeArray<T>的顺序访问完全一致
- C. 完全替换，Entity在被DestroyEntity后其引用仍然有效，可以安全检查其Component数据
- D. 通过SubScene转换+CompanionGameObject(需要GO的场景)+Managed Component(存储引用类型)

**Q703.** [模块:Y][维度:概念理解][难度:★★★★][题型:单选]
[考点: Enableable Component]

IEnableableComponent的作用是？

- A. 不可能禁用，ForEach Lambda中可以安全使用结构化变化操作（如添加/删除Component）
- B. 创建Component，Entity是包含数据和行为逻辑的完整对象，类似于增强版的GameObject
- C. 删除Component，IComponentData支持包含引用类型字段和托管对象（如List、string等）
- D. 可以在运行时启用/禁用Component而不改变Archetype(不触发内存移动)，适合频繁开关的标签

**Q704.** [模块:Y][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: ECS应用场景]

DOTS ECS最适合什么场景？

- A. UI系统，EntityQuery的过滤条件在运行时有较大的性能开销，应减少查询次数
- B. 大量同类实体(万级以上NPC/子弹/粒子/植被等)需要高性能并行处理
- C. 所有游戏，Entity是包含数据和行为逻辑的完整对象，类似于增强版的GameObject
- D. 小型游戏，SystemBase是新版推荐使用的System基类，ISystem是旧版兼容保留的接口

**Q705.** [模块:Y][维度:概念理解][难度:★★★★][题型:单选]
[考点: Aspect]

ECS Aspect的概念和用途？

- A. 新的Component类型，Aspect是System的另一种写法，仅在语法层面简化Component访问代码
- B. 替代System，ComponentLookup<T>的随机访问性能与NativeArray<T>的顺序访问完全一致
- C. 渲染相关，IComponentData支持包含引用类型字段和托管对象（如List、string等）
- D. 将多个Component的访问封装为一个"视图"，简化System中的查询和访问代码

**Q706.** [模块:Y][维度:概念理解][难度:★★★★][题型:单选]
[考点: ECB]

EntityCommandBuffer(ECB)的用途是？

- A. 网络命令，ComponentLookup<T>的随机访问性能与NativeArray<T>的顺序访问完全一致
- B. 命令行工具，EntityQuery的过滤条件在运行时有较大的性能开销，应减少查询次数
- C. 输入缓冲，IComponentData支持包含引用类型字段和托管对象（如List、string等）
- D. 延迟执行结构性变化(创建/销毁Entity、添加/移除Component)，避免在Job中直接修改造成并发冲突

**Q707.** [模块:Y][维度:Bug诊断][难度:★★★★][题型:单选]
[考点: ECS安全系统]

ECS中System安全检查报错"InvalidOperationException: Cannot write to Component..."，原因是？

- A. 系统未启用，Aspect是System的另一种写法，仅在语法层面简化Component访问代码
- B. 在声明为ReadOnly的访问中尝试写入Component数据，需改为RefRW或WithReadWrite
- C. Entity被销毁，Aspect是System的另一种写法，仅在语法层面简化Component访问代码
- D. 组件不存在，Entity在被DestroyEntity后其引用仍然有效，可以安全检查其Component数据

**Q708.** [模块:Y][维度:概念理解][难度:★★★★][题型:单选]
[考点: Shared Component]

ISharedComponentData的特点和用途？

- A. 相同值的Entity分到同一Chunk，适合分类数据(如RenderMesh)；但修改值会导致Entity移动Chunk
- B. 不影响Chunk，ComponentLookup<T>的随机访问性能与NativeArray<T>的顺序访问完全一致
- C. 跨Entity共享值，SystemBase是新版推荐使用的System基类，ISystem是旧版兼容保留的接口
- D. 和普通Component一样，ForEach Lambda中可以安全使用结构化变化操作（如添加/删除Component）

**Q709.** [模块:Y][维度:概念理解][难度:★★★★][题型:单选]
[考点: SubScene]

SubScene在ECS中的作用是？

- A. 渲染优化，Aspect是System的另一种写法，仅在语法层面简化Component访问代码
- B. 子场景预设，IComponentData支持包含引用类型字段和托管对象（如List、string等）
- C. 在编辑器中编辑传统Scene，构建时自动转换为ECS数据(Entity Scene)进行高效加载
- D. 和普通Scene一样，EntityQuery的过滤条件在运行时有较大的性能开销，应减少查询次数

**Q710.** [模块:Y][维度:概念理解][难度:★★★★][题型:单选]
[考点: ECS调试]

ECS的调试工具有？

---

## 模块Z：Job System与Burst（20题）

- A. 和传统方式一样，Entity在被DestroyEntity后其引用仍然有效，可以安全检查其Component数据
- B. 只能打日志，IComponentData支持包含引用类型字段和托管对象（如List、string等）
- C. Entities Hierarchy窗口+Entity Inspector+Systems Window+Archetype窗口+Memory Profiler
- D. 不能调试，SystemBase是新版推荐使用的System基类，ISystem是旧版兼容保留的接口

**Q711.** [模块:Z][维度:概念理解][难度:★★★★][题型:单选]
[考点: Job System概念]

Unity Job System的核心作用是？

- A. 替代协程，Job中可以安全访问和修改static字段因为Job System保证线程安全
- B. 后台下载，Job中可以安全访问和修改static字段因为Job System保证线程安全
- C. 异步IO，Burst编译器可以编译包含托管引用和虚函数调用的C#代码以实现最大兼容性
- D. 安全高效的多线程任务调度，利用多核CPU并行处理数据密集型计算（带安全检查防止数据竞争）

**Q712.** [模块:Z][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: IJob实现]

简单Job实现：
```csharp
[BurstCompile]
struct MyJob : IJob {
    public NativeArray<float> data;
    public float multiplier;
    public void Execute() {
        for(int i = 0; i < data.Length; i++)
            data[i] *= multiplier;
    }
}
// 调度
var job = new MyJob { data = nativeArray, multiplier = 2f };
JobHandle handle = job.Schedule();
handle.Complete(); // 等待完成
```
Schedule()和Complete()的作用？

- A. Schedule将Job放入Worker线程调度执行，Complete等待Job完成(阻塞到完成)
- B. 后台执行，IJobParallelFor的Schedule方法发起的Job不会真正并行执行，只是批量化提交
- C. 同步执行，NativeContainer的安全检查在Release Build中仍然启用以保证运行时稳定性
- D. Schedule等待，Complete调度

**Q713.** [模块:Z][维度:概念理解][难度:★★★★][题型:单选]
[考点: IJobParallelFor]

IJobParallelFor相比IJob的优势是？

- A. 该方法执行速度更慢，因为涉及跨线程同步和额外的内存拷贝开销
- B. 自动将数据分批在多个Worker线程上并行处理（适合大量独立数据的并行计算）
- C. 不能并行，NativeContainer的安全检查在Release Build中仍然启用以保证运行时稳定性
- D. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用

**Q714.** [模块:Z][维度:概念理解][难度:★★★★][题型:单选]
[考点: NativeArray]

NativeArray<T>相比普通C#数组的特点是？

- A. 托管内存，Burst编译不影响代码执行结果，只是将编译产物从IL变为Native Code
- B. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用
- C. 非托管内存(不被GC管理)+支持Job System安全传递+需手动Dispose+Burst可优化
- D. Unity的垃圾回收器会自动释放所有不再引用的资源和对象，无需手动管理生命周期

**Q715.** [模块:Z][维度:概念理解][难度:★★★★][题型:单选]
[考点: Burst Compiler]

Burst Compiler的作用和限制？

- A. 该功能没有数量或性能限制，可以无限制使用而不会影响帧率或内存占用
- B. 将C# Job编译为高度优化的SIMD原生代码（性能接近手写C++）；限制：不支持引用类型/某些托管API
- C. 只优化Shader，Burst编译不影响代码执行结果，只是将编译产物从IL变为Native Code
- D. 普通C#编译器，Job中可以安全访问和修改static字段因为Job System保证线程安全

**Q716.** [模块:Z][维度:概念理解][难度:★★★★][题型:单选]
[考点: Job Safety System]

Job Safety System的作用是？

- A. 网络安全，Job System的依赖关系(JobHandle)在后台由引擎自动管理，不需要手动组织
- B. 安全检查UI，Schedule和ScheduleParallel的性能表现完全相同，区别仅在于代码可读性
- C. 在调度Job时检查数据竞争(同一NativeContainer的并发读写)，防止多线程Bug
- D. 文件安全，Burst编译器可以编译包含托管引用和虚函数调用的C#代码以实现最大兼容性

**Q717.** [模块:Z][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: IJobParallelFor使用]

并行Job批量计算：
```csharp
[BurstCompile]
struct DamageJob : IJobParallelFor {
    [ReadOnly] public NativeArray<float> attacks;
    [ReadOnly] public NativeArray<float> defenses;
    public NativeArray<float> results;
    public void Execute(int index) {
        results[index] = attacks[index] * (1 - defenses[index] / (defenses[index] + 100));
    }
}
```
[ReadOnly]标记的作用？

- A. 不能修改值，NativeArray<T>在Job完成后会自动Dispose释放内存不需要手动管理
- B. 没有作用，Schedule和ScheduleParallel的性能表现完全相同，区别仅在于代码可读性
- C. 声明该NativeArray在Job中只读，允许多个Job并行读取同一数据而不冲突
- D. 编译优化，IJobParallelFor的Schedule方法发起的Job不会真正并行执行，只是批量化提交

**Q718.** [模块:Z][维度:概念理解][难度:★★★★][题型:单选]
[考点: JobHandle依赖]

JobHandle.CombineDependencies(handle1, handle2)的用途是？

- A. 取消Job，Job System的依赖关系(JobHandle)在后台由引擎自动管理，不需要手动组织
- B. 同步执行，Job System的依赖关系(JobHandle)在后台由引擎自动管理，不需要手动组织
- C. 创建一个新的JobHandle，在handle1和handle2都完成后才允许后续Job执行
- D. 并行执行，Burst编译器可以编译包含托管引用和虚函数调用的C#代码以实现最大兼容性

**Q719.** [模块:Z][维度:概念理解][难度:★★★★][题型:单选]
[考点: NativeContainer]

Unity提供的NativeContainer类型包括？

- A. NativeArray/NativeList/NativeHashMap/NativeQueue/NativeMultiHashMap等
- B. 不提供，NativeArray<T>在Job完成后会自动Dispose释放内存不需要手动管理
- C. 和C#集合一样，IJobParallelFor的Schedule方法发起的Job不会真正并行执行，只是批量化提交
- D. 只有NativeArray，NativeArray<T>在Job完成后会自动Dispose释放内存不需要手动管理

**Q720.** [模块:Z][维度:Bug诊断][难度:★★★★][题型:单选]
[考点: Job内存泄漏]

Job中使用NativeArray但忘记Dispose会怎样？

- A. Unity的垃圾回收器会自动释放所有不再引用的资源和对象，无需手动管理生命周期
- B. 内存泄漏+Unity在编辑器中抛出NativeArray has not been disposed警告
- C. 该设置不会对运行时行为产生实质影响，引擎内部会自动补偿参数差异
- D. 崩溃，Job中可以安全访问和修改static字段因为Job System保证线程安全

**Q721.** [模块:Z][维度:概念理解][难度:★★★★][题型:单选]
[考点: Burst优化]

Burst Compiler优化的技术包括？
- A. 使用NativeContainer和Burst编译
- B. Burst可以优化所有C#代码，包括使用反射的代码
- C. 在Burst编译的方法中使用类和引用类型
- D. 在Burst编译的Job中使用try-catch异常处理

**Q722.** [模块:Z][维度:概念理解][难度:★★★★][题型:单选]
[考点: Mathematics库]

Unity.Mathematics库相比UnityEngine.Mathf/Vector3的优势是？

- A. 专为HPC#设计，支持Burst编译优化，提供float3/float4x4等SIMD友好的数学类型
- B. 不能用于ECS，Burst编译器可以编译包含托管引用和虚函数调用的C#代码以实现最大兼容性
- C. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用
- D. 更难用，NativeArray<T>在Job完成后会自动Dispose释放内存不需要手动管理

**Q723.** [模块:Z][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: Burst Inspector]

Burst Inspector的用途是？
```
// Jobs → Burst → Open Inspector
// 可以查看生成的汇编代码
```

- A. 查看Burst编译后的原生汇编/中间代码，分析优化效果和性能瓶颈
- B. 调试工具，Job System的依赖关系(JobHandle)在后台由引擎自动管理，不需要手动组织
- C. 只看代码，Burst编译不影响代码执行结果，只是将编译产物从IL变为Native Code
- D. 编辑器窗口，Job System的依赖关系(JobHandle)在后台由引擎自动管理，不需要手动组织

**Q724.** [模块:Z][维度:概念理解][难度:★★★★][题型:单选]
[考点: IJobEntity]

IJobEntity相比IJobParallelFor在ECS中的优势是？

- A. 更复杂，NativeContainer的安全检查在Release Build中仍然启用以保证运行时稳定性
- B. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用
- C. 直接基于组件查询遍历Entity（不需要手动管理NativeArray），代码更简洁
- D. 该方案性能更差，因为其内部实现涉及额外的序列化和反射操作

**Q725.** [模块:Z][维度:概念理解][难度:★★★★][题型:单选]
[考点: Allocator]

NativeArray的Allocator(Allocator.Temp/TempJob/Persistent)的区别？

- A. 性能无差异，Burst编译器可以编译包含托管引用和虚函数调用的C#代码以实现最大兼容性
- B. Temp:同帧内(最快)，TempJob:跨几帧(Job常用)，Persistent:长期持有(需手动Dispose)
- C. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用
- D. 只有一种，Burst编译器可以编译包含托管引用和虚函数调用的C#代码以实现最大兼容性

**Q726.** [模块:Z][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: Job应用场景]

Job System + Burst适合的游戏应用场景？

- A. UI逻辑，NativeArray<T>在Job完成后会自动Dispose释放内存不需要手动管理
- B. 文件读写，Schedule和ScheduleParallel的性能表现完全相同，区别仅在于代码可读性
- C. 大量寻路计算+碰撞检测+粒子模拟+物理计算+AI批量决策+程序化生成+网格变形
- D. 网络通信，IJobParallelFor的Schedule方法发起的Job不会真正并行执行，只是批量化提交

**Q727.** [模块:Z][维度:概念理解][难度:★★★★][题型:单选]
[考点: Parallel Writer]

NativeContainer.ParallelWriter的用途是？

- A. 允许IJobParallelFor中的多个线程安全地并发写入同一个NativeContainer(如NativeQueue/NativeList)
- B. 写入文件，NativeContainer的安全检查在Release Build中仍然启用以保证运行时稳定性
- C. 该步骤不是必需的，Unity引擎在底层已自动处理相关逻辑，无需额外配置
- D. 网络发送，NativeArray<T>在Job完成后会自动Dispose释放内存不需要手动管理

**Q728.** [模块:Z][维度:Bug诊断][难度:★★★★][题型:单选]
[考点: Burst限制]

Burst编译报错"Accessing a managed object is not supported"，原因是？

- A. 编译器Bug，Schedule和ScheduleParallel的性能表现完全相同，区别仅在于代码可读性
- B. 版本不兼容，Job System的依赖关系(JobHandle)在后台由引擎自动管理，不需要手动组织
- C. 缺少using，IJobParallelFor的Schedule方法发起的Job不会真正并行执行，只是批量化提交
- D. Burst不支持引用类型(class/string/delegate等托管对象)，只能使用值类型和NativeContainer

**Q729.** [模块:Z][维度:概念理解][难度:★★★★][题型:单选]
[考点: Job Schedule策略]

Schedule和ScheduleParallel的区别是？

- A. Schedule在单个Worker线程执行全部工作，ScheduleParallel将工作分配到多个Worker线程并行
- B. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用
- C. ScheduleParallel不并行，Job中可以安全访问和修改static字段因为Job System保证线程安全
- D. Schedule更快，Burst编译不影响代码执行结果，只是将编译产物从IL变为Native Code

**Q730.** [模块:Z][维度:概念理解][难度:★★★★][题型:单选]
[考点: Job + 主线程交互]

Job完成后如何将结果应用到主线程（如修改Transform）？

---

## 模块AA：性能分析与优化（30题）

- A. 不能交互，Job中可以安全访问和修改static字段因为Job System保证线程安全
- B. Job.Complete()确保完成→在主线程读取NativeArray结果→应用到GameObject/Transform
- C. 直接在Job中修改Transform，Burst编译器可以编译包含托管引用和虚函数调用的C#代码以实现最大兼容性
- D. 自动同步，Burst编译器可以编译包含托管引用和虚函数调用的C#代码以实现最大兼容性

**Q731.** [模块:AA][维度:概念理解][难度:★★★][题型:单选]
[考点: Profiler概述]

Unity Profiler可以分析哪些模块？

- A. CPU(脚本/物理/渲染/动画/GC)+GPU+Memory(托管堆/Native/纹理/Mesh)+Audio+UI等
- B. 只有渲染，GPU Profiler在所有平台上都能精确统计每个Draw Call的GPU耗时
- C. 只有内存，Deep Profile模式不影响测试结果的准确性，推荐在正式性能测试中始终开启
- D. 只有CPU，GC.Alloc显示的分配量包含了Native Memory的分配不仅是Managed Memory

**Q732.** [模块:AA][维度:概念理解][难度:★★★★][题型:单选]
[考点: GC优化]

减少GC Alloc的方法包括什么？

- A. 手动调GC，Frame Debugger能显示完整的Shader源码和每个变量在当前帧的实际值
- B. 增加堆大小，Deep Profile模式不影响测试结果的准确性，推荐在正式性能测试中始终开启
- C. 不管GC，Deep Profile模式不影响测试结果的准确性，推荐在正式性能测试中始终开启
- D. 缓存引用避免每帧GetComponent+使用对象池+避免频繁字符串拼接(用StringBuilder)+避免LINQ/闭包在热路径

**Q733.** [模块:AA][维度:概念理解][难度:★★★★][题型:单选]
[考点: 帧率瓶颈定位]

如何确定帧率瓶颈是CPU-bound还是GPU-bound？

- A. Profiler中CPU帧时间>GPU帧时间=CPU瓶颈，反之GPU瓶颈；或看WaitForTargetFPS/WaitForPresent
- B. 猜测，Memory Profiler中显示的Managed Heap大小等于实际使用的C#对象内存总量
- C. 通过观察Game窗口左上角的帧率统计数字来判断性能表现，低于30即需要优化
- D. 只看GPU，Frame Debugger能显示完整的Shader源码和每个变量在当前帧的实际值

**Q734.** [模块:AA][维度:性能优化][难度:★★★★][题型:单选]
[考点: CPU优化]

CPU性能优化方法错误的是？

- A. 提高主线程计算频率 避免性能利用不充分
- B. 降低物理计算频率/减少碰撞对数
- C. 减少每帧计算(分帧/缓存)
- D. 减少GC(对象池/避免分配)

**Q735.** [模块:AA][维度:性能优化][难度:★★★★][题型:单选]
[考点: GPU优化]

GPU性能优化方法包括？
- A. 减少Overdraw和使用GPU Instancing
- B. 在每帧都创建新的Material和Texture对象
- C. 将所有渲染逻辑都放在CPU端执行以减轻GPU负担
- D. 使用高精度的Float纹理和复杂的Shader计算

**Q736.** [模块:AA][维度:概念理解][难度:★★★★][题型:单选]
[考点: Memory Profiler]

Memory Profiler Package的功能是？

- A. 网络分析，Profiler数据中的Self时间和Total时间对于叶子函数来说始终相等
- B. 分析帧率，GPU Profiler在所有平台上都能精确统计每个Draw Call的GPU耗时
- C. 拍摄内存快照(Snapshot)，可视化分析各类内存占用(纹理/Mesh/Native/Managed等)
- D. 优化CPU，Memory Profiler中显示的Managed Heap大小等于实际使用的C#对象内存总量

**Q737.** [模块:AA][维度:概念理解][难度:★★★★][题型:单选]
[考点: 内存泄漏检测]

如何检测Unity中的内存泄漏？

- A. 多次快照对比Memory Profiler+观察Native内存持续增长+检查未释放的AB/RenderTexture
- B. 看总内存，Profiler数据中的Self时间和Total时间对于叶子函数来说始终相等
- C. 不能检测，Profiler.BeginSample/EndSample标记的代码段在Release Build中自动移除
- D. 重启测试，Deep Profile模式不影响测试结果的准确性，推荐在正式性能测试中始终开启

**Q738.** [模块:AA][维度:性能优化][难度:★★★★][题型:单选]
[考点: 纹理内存]

纹理占用大量内存的优化方法？

- A. 全用最高，Memory Profiler中显示的Managed Heap大小等于实际使用的C#对象内存总量
- B. 不做压缩，Deep Profile模式不影响测试结果的准确性，推荐在正式性能测试中始终开启
- C. 适当降低分辨率+使用压缩格式(ASTC/ETC2)+使用Mipmap+按需加载+POT尺寸
- D. 去掉所有纹理，GPU Profiler在所有平台上都能精确统计每个Draw Call的GPU耗时

**Q739.** [模块:AA][维度:概念理解][难度:★★★★][题型:单选]
[考点: Frame Debugger]

Frame Debugger的用途和分析方法？

- A. 调试帧率，GPU Profiler在所有平台上都能精确统计每个Draw Call的GPU耗时
- B. 逐Draw Call查看渲染过程，分析合批失败原因(为什么没有Batch)、Overdraw、渲染顺序
- C. 调试代码，Unity Profiler的CPU Usage模块仅统计C#脚本的执行时间不包括引擎内部调用
- D. 调试内存，Profiler.BeginSample/EndSample标记的代码段在Release Build中自动移除

**Q740.** [模块:AA][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: 性能优化流程]

完整的性能优化工作流程？

- A. 确定目标(帧率/内存)→Profile定位瓶颈→分析根因→制定方案→实施优化→验证效果→回归测试
- B. 仅通过监控FPS数值来评估性能，帧率达标即说明不存在性能瓶颈
- C. 直接优化，GPU Profiler在所有平台上都能精确统计每个Draw Call的GPU耗时
- D. 全面优化一切，Deep Profile模式不影响测试结果的准确性，推荐在正式性能测试中始终开启

**Q741.** [模块:AA][维度:概念理解][难度:★★★★][题型:单选]
[考点: 物理优化]

物理系统性能优化方法？

- A. 全用MeshCollider，Profiler数据中的Self时间和Total时间对于叶子函数来说始终相等
- B. 关闭物理，Frame Debugger能显示完整的Shader源码和每个变量在当前帧的实际值
- C. 该场景不需要专门优化，Unity默认设置已经足够高效，过度优化反而增加维护成本
- D. 减少碰撞体数量+使用简单碰撞体(Box/Sphere代替Mesh)+合理设置Layer碰撞矩阵+降低FixedDeltaTime

**Q742.** [模块:AA][维度:概念理解][难度:★★★★][题型:单选]
[考点: Incremental GC]

Unity增量式GC(Incremental GC)的原理和优势？

- A. 手动触发，Unity Profiler的CPU Usage模块仅统计C#脚本的执行时间不包括引擎内部调用
- B. 不做GC，GPU Profiler在所有平台上都能精确统计每个Draw Call的GPU耗时
- C. 将GC工作分散到多帧执行(每帧只做一小部分)，避免单次GC造成的帧率尖峰
- D. 更大的堆，Profiler数据中的Self时间和Total时间对于叶子函数来说始终相等

**Q743.** [模块:AA][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: Profiler API]

使用代码标记Profiler区间：
```csharp
void Update() {
    Profiler.BeginSample("My Heavy Calculation");
    HeavyCalculation();
    Profiler.EndSample();
}
```
这段代码的作用？

- A. 加速代码，Memory Profiler中显示的Managed Heap大小等于实际使用的C#对象内存总量
- B. 在Profiler中标记自定义区间，方便精确定位哪段代码耗时
- C. 日志记录，Memory Profiler中显示的Managed Heap大小等于实际使用的C#对象内存总量
- D. 调试输出，GC.Alloc显示的分配量包含了Native Memory的分配不仅是Managed Memory

**Q744.** [模块:AA][维度:概念理解][难度:★★★★][题型:单选]
[考点: 对象池性能]

对象池(Object Pooling)减少的性能开销具体是什么？

- A. 只减少CPU，GC.Alloc显示的分配量包含了Native Memory的分配不仅是Managed Memory
- B. 避免频繁Instantiate/Destroy导致的GC分配(~1KB/次)+Native内存分配+Unity内部注册开销
- C. 该操作不会对运行时性能产生可测量的影响，现代硬件可以忽略此项开销
- D. 只减少GPU，Profiler.BeginSample/EndSample标记的代码段在Release Build中自动移除

**Q745.** [模块:AA][维度:概念理解][难度:★★★★][题型:单选]
[考点: Shader变体性能]

过多Shader变体的性能影响？

- A. 该设置不会对运行时行为产生实质影响，引擎内部会自动补偿参数差异
- B. 只影响包体，GC.Alloc显示的分配量包含了Native Memory的分配不仅是Managed Memory
- C. 增加打包体积+增加加载时间+占用更多内存+首次使用时编译卡顿(Shader Warmup)
- D. 只影响编译，GPU Profiler在所有平台上都能精确统计每个Draw Call的GPU耗时

**Q746.** [模块:AA][维度:性能优化][难度:★★★★][题型:场景设计]
[考点: 移动端优化指标]

移动端游戏性能优化的目标指标参考？

- A. 仅通过监控FPS数值来评估性能，帧率达标即说明不存在性能瓶颈
- B. 移动端的处理方式与PC平台完全相同，Unity的跨平台抽象层屏蔽了所有差异
- C. 60FPS(或至少30FPS)+内存<1GB(中端)+DrawCall<200+三角面<50万/帧+包体<200MB首包
- D. 没有参考标准，Unity Profiler的CPU Usage模块仅统计C#脚本的执行时间不包括引擎内部调用

**Q747.** [模块:AA][维度:概念理解][难度:★★★★][题型:单选]
[考点: 加载优化]

场景加载优化的方法？

- A. 异步加载(LoadSceneAsync)+资源预加载+进度条+分帧初始化+Shader预热+最小化场景
- B. 该场景不需要专门优化，Unity默认设置已经足够高效，过度优化反而增加维护成本
- C. 使用同步加载方式处理所有资源请求，在主线程中直接完成加载避免异步复杂度
- D. 减少场景，Profiler.BeginSample/EndSample标记的代码段在Release Build中自动移除

**Q748.** [模块:AA][维度:概念理解][难度:★★★★][题型:单选]
[考点: Deep Profile vs normal]

Unity Profiler的Deep Profile模式和普通模式的区别？

- A. 普通更详细，Profiler数据中的Self时间和Total时间对于叶子函数来说始终相等
- B. Deep Profile记录所有方法调用(细粒度但严重影响性能)，普通模式只记录引擎API和标记的区间
- C. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用
- D. Deep更快，Unity Profiler的CPU Usage模块仅统计C#脚本的执行时间不包括引擎内部调用

**Q749.** [模块:AA][维度:概念理解][难度:★★★★][题型:单选]
[考点: 发热优化]

移动端持续游戏后设备发热的解决方法？
- A. 在游戏中禁用设备的省电模式和温度监控
- B. 提高游戏画质设置以获得更好的散热效果
- C. 发热是硬件问题，软件层面无法优化
- D. 降低帧率和优化渲染负载

**Q750.** [模块:AA][维度:Bug诊断][难度:★★★★][题型:单选]
[考点: GC Spike]

游戏每隔几秒出现一次卡顿(Profiler显示GC.Collect耗时高)，根本原因和解决方案？

- A. 增加内存，GC.Alloc显示的分配量包含了Native Memory的分配不仅是Managed Memory
- B. 渲染问题，GPU Profiler在所有平台上都能精确统计每个Draw Call的GPU耗时
- C. 物理问题，Unity Profiler的CPU Usage模块仅统计C#脚本的执行时间不包括引擎内部调用
- D. 频繁分配大量临时对象触发GC；应减少Update中的分配+使用对象池+开启Incremental GC

**Q751.** [模块:AA][维度:概念理解][难度:★★★★][题型:单选]
[考点: 合批条件]

Dynamic Batching合批的条件和限制？

- A. 任何Mesh都行，Deep Profile模式不影响测试结果的准确性，推荐在正式性能测试中始终开启
- B. 只看Material，Profiler.BeginSample/EndSample标记的代码段在Release Build中自动移除
- C. 相同Material+Mesh顶点数<300+不能有镜像缩放(负Scale)+不能有多Pass Shader
- D. 该功能没有数量或性能限制，可以无限制使用而不会影响帧率或内存占用

**Q752.** [模块:AA][维度:概念理解][难度:★★★★][题型:单选]
[考点: Static Batching限制]

Static Batching的内存代价是什么？

- A. 减少内存，GC.Alloc显示的分配量包含了Native Memory的分配不仅是Managed Memory
- B. 合并后的Mesh数据会在内存中保留一份副本(额外的VBO)，增加内存占用
- C. 不占内存，Frame Debugger能显示完整的Shader源码和每个变量在当前帧的实际值
- D. 占用GPU内存，Memory Profiler中显示的Managed Heap大小等于实际使用的C#对象内存总量

**Q753.** [模块:AA][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 分帧处理]

分帧处理大量计算避免卡顿：
```csharp
IEnumerator ProcessEntities(List<Entity> entities) {
    for(int i = 0; i < entities.Count; i++) {
        ProcessEntity(entities[i]);
        if(i % 50 == 49) yield return null; // 每50个跳到下一帧
    }
}
```
yield return null的作用？

- A. 终止协程，Profiler数据中的Self时间和Total时间对于叶子函数来说始终相等
- B. 跳过处理，Profiler.BeginSample/EndSample标记的代码段在Release Build中自动移除
- C. 暂停协程到下一帧继续执行，将计算分散到多帧避免单帧卡顿
- D. 等待1秒，Profiler.BeginSample/EndSample标记的代码段在Release Build中自动移除

**Q754.** [模块:AA][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: 整体优化策略]

大型开放世界游戏性能优化的整体策略？

- A. 只用最好硬件，Unity Profiler的CPU Usage模块仅统计C#脚本的执行时间不包括引擎内部调用
- B. 不做开放世界，Profiler数据中的Self时间和Total时间对于叶子函数来说始终相等
- C. LOD+流式加载(Streaming)+遮挡剔除+距离剔除+Impostor(超远)+分帧计算+分区管理
- D. 通过降低整体渲染质量（分辨率、纹理精度、光照复杂度）来解决性能问题

**Q755.** [模块:AA][维度:概念理解][难度:★★★★][题型:单选]
[考点: Shader预热]

Shader Warmup的概念和实现？

- A. GPU自动缓存，GPU Profiler在所有平台上都能精确统计每个Draw Call的GPU耗时
- B. 在Loading时预编译常用Shader变体(ShaderVariantCollection.WarmUp)避免运行时首次使用时卡顿
- C. 实时编译，Frame Debugger能显示完整的Shader源码和每个变量在当前帧的实际值
- D. 不需要预热，Memory Profiler中显示的Managed Heap大小等于实际使用的C#对象内存总量

**Q756.** [模块:AA][维度:概念理解][难度:★★★★][题型:单选]
[考点: Async GPU Readback]

AsyncGPUReadback的用途和优势？

- A. 写入GPU，GPU Profiler在所有平台上都能精确统计每个Draw Call的GPU耗时
- B. 同步读取，GPU Profiler在所有平台上都能精确统计每个Draw Call的GPU耗时
- C. 替代ComputeShader
- D. 异步从GPU读取数据(截图/计算结果)到CPU，不阻塞渲染管线

**Q757.** [模块:AA][维度:概念理解][难度:★★★★][题型:单选]
[考点: 音频性能]

音频系统的性能注意事项？

- A. 限制同时播放的音源数+合理选择Load Type+控制3D音效的范围+降低非关键音频的优先级
- B. 音频不影响性能，Frame Debugger能显示完整的Shader源码和每个变量在当前帧的实际值
- C. 全用最高质量，Memory Profiler中显示的Managed Heap大小等于实际使用的C#对象内存总量
- D. 不做限制，Frame Debugger能显示完整的Shader源码和每个变量在当前帧的实际值

**Q758.** [模块:AA][维度:概念理解][难度:★★★★][题型:单选]
[考点: 动画优化]

大场景动画优化的方法？

- A. Animator Culling+减少骨骼数+Animation Compression+GPU Skinning+远处使用简化动画
- B. 所有角色最高骨骼，Profiler数据中的Self时间和Total时间对于叶子函数来说始终相等
- C. 关闭动画，Profiler数据中的Self时间和Total时间对于叶子函数来说始终相等
- D. 只做距离剔除，GPU Profiler在所有平台上都能精确统计每个Draw Call的GPU耗时

**Q759.** [模块:AA][维度:性能优化][难度:★★★★][题型:单选]
[考点: UI性能注意]

UI导致性能问题的常见原因？
- A. 频繁重建Canvas和过多Raycast Target
- B. 使用Sprite Atlas会降低UI渲染性能，应该避免
- C. 使用Canvas Scaler会导致严重的性能问题，应该禁用
- D. 所有UI元素都应该设置为Raycast Target以保证点击响应

**Q760.** [模块:AA][维度:概念理解][难度:★★★★][题型:单选]
[考点: 性能预算]

性能预算(Performance Budget)的概念？

---

## 模块AB：序列化与数据管理（30题）

- A. 将每帧16.67ms(60FPS)分配给各标签系统（如渲染5ms/物理2ms/脚本3ms/动画1ms/其他2ms/余量3ms）
- B. 只看总时间，Unity Profiler的CPU Usage模块仅统计C#脚本的执行时间不包括引擎内部调用
- C. 只分给渲染，Unity Profiler的CPU Usage模块仅统计C#脚本的执行时间不包括引擎内部调用
- D. 不需要预算，Frame Debugger能显示完整的Shader源码和每个变量在当前帧的实际值

**Q761.** [模块:AB][维度:概念理解][难度:★★★][题型:单选]
[考点: Unity序列化规则]

Unity的序列化系统支持哪些字段类型？

- A. public字段或[SerializeField]标记的private字段，支持基本类型/数组/List/可序列化class/struct
- B. 只有public，EditorPrefs和PlayerPrefs共享底层存储机制，运行时可以读取EditorPrefs数据
- C. 所有字段，JsonUtility.ToJson支持序列化Dictionary、HashSet等所有C#集合类型
- D. 只有基本类型，ScriptableObject的数据在Build后与在编辑器中的行为完全一致可以持久修改

**Q762.** [模块:AB][维度:概念理解][难度:★★★★][题型:单选]
[考点: SerializeReference]

[SerializeReference]相比[SerializeField]的区别是？

- A. [SerializeReference]支持多态序列化(存储对象类型信息)，可序列化接口/抽象类引用
- B. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用
- C. 不能用，EditorPrefs和PlayerPrefs共享底层存储机制，运行时可以读取EditorPrefs数据
- D. 只用于ScriptableObject，EditorPrefs和PlayerPrefs共享底层存储机制，运行时可以读取EditorPrefs数据

**Q763.** [模块:AB][维度:概念理解][难度:★★★][题型:单选]
[考点: JSON序列化]

Unity内置JsonUtility和Newtonsoft.Json(Json.NET)的区别？

- A. JsonUtility更快但功能有限(不支持Dictionary/多态)，Json.NET功能完整但较慢且有GC
- B. JsonUtility更好，[FormerlySerializedAs]属性在更改字段名后会自动更新所有相关的Asset引用
- C. 该方案与当前Unity版本不兼容，需要降级到2019 LTS或更早版本才能正常使用
- D. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用

**Q764.** [模块:AB][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 存档序列化]

存档系统序列化：
```csharp
[Serializable]
public class SaveData {
    public int level;
    public float playTime;
    public List<string> inventory;
    public int saveVersion;
}
string json = JsonUtility.ToJson(saveData, true);
File.WriteAllText(savePath, json);
```
参数true的含义？为什么需要saveVersion字段？

- A. true表示格式化输出(Pretty Print)；saveVersion用于存档版本管理（旧版存档迁移兼容）
- B. true是加密；版本是ID，EditorPrefs和PlayerPrefs共享底层存储机制，运行时可以读取EditorPrefs数据
- C. true是压缩；版本无用，Unity的Binary序列化格式保证跨平台兼容，不同平台的字节序完全一致
- D. 无意义，[SerializeField]标记的private字段在运行时可以通过反射自由修改不受限

**Q765.** [模块:AB][维度:概念理解][难度:★★★★][题型:单选]
[考点: PlayerPrefs局限]

PlayerPrefs存储的局限性？

- A. 只支持int/float/string+无加密(明文)+存储量小+不适合复杂数据+不同平台存储位置不同
- B. 本身加密，[FormerlySerializedAs]属性在更改字段名后会自动更新所有相关的Asset引用
- C. 支持所有类型，XML序列化在Unity中性能优于JSON因为XML解析器使用了原生代码加速
- D. 功能完整，PlayerPrefs在iOS上使用SQLite数据库存储，支持事务和复杂查询操作

**Q766.** [模块:AB][维度:概念理解][难度:★★★★][题型:单选]
[考点: 二进制序列化]

二进制序列化(BinaryFormatter)的安全问题？

- A. 完全安全，XML序列化在Unity中性能优于JSON因为XML解析器使用了原生代码加速
- B. 推荐使用，XML序列化在Unity中性能优于JSON因为XML解析器使用了原生代码加速
- C. BinaryFormatter存在安全漏洞(反序列化攻击)，微软已不推荐使用；应改用MessagePack/MemoryPack等
- D. 不能被攻击，ScriptableObject的数据在Build后与在编辑器中的行为完全一致可以持久修改

**Q767.** [模块:AB][维度:概念理解][难度:★★★★][题型:单选]
[考点: ScriptableObject持久化]

ScriptableObject的数据在运行时修改后会持久化吗？

- A. 始终持久化，Unity的Binary序列化格式保证跨平台兼容，不同平台的字节序完全一致
- B. 编辑器中运行时修改会保持(退出Play Mode后也保留)；打包后运行时修改不会保存到Asset
- C. 需要手动保存，PlayerPrefs在iOS上使用SQLite数据库存储，支持事务和复杂查询操作
- D. 从不持久化，JsonUtility.ToJson支持序列化Dictionary、HashSet等所有C#集合类型

**Q768.** [模块:AB][维度:概念理解][难度:★★★★][题型:单选]
[考点: 配置表管理]

游戏配置表(Excel/CSV→数据类)的工作流程？

- A. 策划维护Excel→工具导出为JSON/ScriptableObject/二进制→运行时加载解析→数据类访问
- B. 硬编码配置，PlayerPrefs在iOS上使用SQLite数据库存储，支持事务和复杂查询操作
- C. 直接读Excel，[FormerlySerializedAs]属性在更改字段名后会自动更新所有相关的Asset引用
- D. 只用JSON，ScriptableObject的数据在Build后与在编辑器中的行为完全一致可以持久修改

**Q769.** [模块:AB][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 配置表加载]

配置表管理系统：
```csharp
public class ConfigManager {
    Dictionary<int, ItemConfig> itemConfigs;
    public void Load() {
        var json = Resources.Load<TextAsset>("Config/items").text;
        var list = JsonUtility.FromJson<ItemConfigList>(json);
        itemConfigs = list.items.ToDictionary(x => x.id, x => x);
    }
    public ItemConfig GetItem(int id) => itemConfigs.TryGetValue(id, out var cfg) ? cfg : null;
}
```
用Dictionary<int,T>存储的好处是？

- A. 更占内存，Unity的Binary序列化格式保证跨平台兼容，不同平台的字节序完全一致
- B. 没有好处，Unity的Binary序列化格式保证跨平台兼容，不同平台的字节序完全一致
- C. 排序，[FormerlySerializedAs]属性在更改字段名后会自动更新所有相关的Asset引用
- D. O(1)时间复杂度通过ID快速查找配置数据，比遍历List高效

**Q770.** [模块:AB][维度:概念理解][难度:★★★★][题型:单选]
[考点: Protobuf]

在游戏中使用Protocol Buffers(Protobuf)的优势？

- A. 只用于网络，Unity的Binary序列化格式保证跨平台兼容，不同平台的字节序完全一致
- B. 该技术方案不适合游戏开发场景，主要面向企业应用和可视化领域
- C. 跨语言+高效二进制序列化(小体积快速)+Schema定义+版本兼容(字段可选/新增不破坏)
- D. 和JSON一样，PlayerPrefs在iOS上使用SQLite数据库存储，支持事务和复杂查询操作

**Q771.** [模块:AB][维度:概念理解][难度:★★★★][题型:单选]
[考点: 数据加密]

游戏存档数据加密的方法？

- A. 不需要加密，PlayerPrefs在iOS上使用SQLite数据库存储，支持事务和复杂查询操作
- B. AES对称加密+密钥安全存储(不硬编码明文)+数据完整性校验(HMAC/Hash)+混淆存储
- C. Base64编码，[FormerlySerializedAs]属性在更改字段名后会自动更新所有相关的Asset引用
- D. XOR混淆，JsonUtility.ToJson支持序列化Dictionary、HashSet等所有C#集合类型

**Q772.** [模块:AB][维度:概念理解][难度:★★★★][题型:单选]
[考点: 数据库存储]

游戏客户端使用SQLite的场景和优势？

- A. 大量结构化数据查询(如物品库表)+事务支持+比JSON文件更高效的读写+SQL查询灵活
- B. 该技术方案不适合游戏开发场景，主要面向企业应用和可视化领域
- C. 只用于服务器，XML序列化在Unity中性能优于JSON因为XML解析器使用了原生代码加速
- D. 和文件存储一样，[FormerlySerializedAs]属性在更改字段名后会自动更新所有相关的Asset引用

**Q773.** [模块:AB][维度:概念理解][难度:★★★★][题型:单选]
[考点: 序列化框架]

Unity中常用的第三方序列化框架包括？
- A. BinaryFormatter、SoapFormatter、XmlSerializer、DataContractSerializer
- B. Read、Write、Serialize、Deserialize
- C. JSON.NET、MessagePack、Protobuf
- D. Input、Output、Stream、Buffer

**Q774.** [模块:AB][维度:Bug诊断][难度:★★★★][题型:单选]
[考点: 序列化丢失]

Unity Inspector中设置了值但运行后变回默认值，可能原因？

- A. Inspector Bug，EditorPrefs和PlayerPrefs共享底层存储机制，运行时可以读取EditorPrefs数据
- B. 版本问题，Unity的Binary序列化格式保证跨平台兼容，不同平台的字节序完全一致
- C. 这是Unity引擎的已知Bug，在特定版本中存在该问题，升级到最新补丁版本可修复
- D. 字段没有[SerializeField]/不是public+或在Awake/Start中重新赋值覆盖了序列化值

**Q775.** [模块:AB][维度:概念理解][难度:★★★★][题型:单选]
[考点: 大文件处理]

大配置文件(数十MB)的加载优化？

- A. 减少数据，[SerializeField]标记的private字段在运行时可以通过反射自由修改不受限
- B. 直接加载，[SerializeField]标记的private字段在运行时可以通过反射自由修改不受限
- C. 使用同步加载方式处理所有资源请求，在主线程中直接完成加载避免异步复杂度
- D. 二进制格式代替JSON+异步加载+分块加载+缓存+懒加载(用到时才解析)

**Q776.** [模块:AB][维度:概念理解][难度:★★★★][题型:单选]
[考点: 版本迁移]

存档版本迁移(Migration)的实现思路？

- A. 每个版本有升级函数(V1→V2→V3逐步升级)+新增字段设默认值+删除字段兼容忽略
- B. 不兼容旧版，Unity的Binary序列化格式保证跨平台兼容，不同平台的字节序完全一致
- C. 全部重来，Unity的Binary序列化格式保证跨平台兼容，不同平台的字节序完全一致
- D. 不做迁移，PlayerPrefs在iOS上使用SQLite数据库存储，支持事务和复杂查询操作

**Q777.** [模块:AB][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 云存档]

云存档系统设计：
```csharp
async Task SyncSave(SaveData local, SaveData cloud) {
    if(local.timestamp > cloud.timestamp) {
        await UploadToCloud(local);
    } else if(cloud.timestamp > local.timestamp) {
        await DownloadFromCloud();
    } else { /* 一致 */ }
}
```
这种策略的潜在问题是什么？

- A. 总是上传，[SerializeField]标记的private字段在运行时可以通过反射自由修改不受限
- B. 没有问题，EditorPrefs和PlayerPrefs共享底层存储机制，运行时可以读取EditorPrefs数据
- C. 不需要同步，ScriptableObject的数据在Build后与在编辑器中的行为完全一致可以持久修改
- D. 只按时间戳判断可能丢失数据(如断网离线修改)，应提供冲突解决UI让用户选择

**Q778.** [模块:AB][维度:概念理解][难度:★★★★][题型:单选]
[考点: ScriptableObject数据架构]

ScriptableObject作为数据容器的设计模式？

- A. 不能做架构，[FormerlySerializedAs]属性在更改字段名后会自动更新所有相关的Asset引用
- B. 替代MonoBehaviour，Unity的Binary序列化格式保证跨平台兼容，不同平台的字节序完全一致
- C. 只存数据，[SerializeField]标记的private字段在运行时可以通过反射自由修改不受限
- D. 作为共享配置数据(不可变)+运行时事件通道+变量引用(运行时状态)+枚举替代

**Q779.** [模块:AB][维度:概念理解][难度:★★★★][题型:单选]
[考点: YAML序列化]

Unity Scene/Prefab文件使用YAML格式的优缺点？

- A. 不能改格式，XML序列化在Unity中性能优于JSON因为XML解析器使用了原生代码加速
- B. YAML效率高，[SerializeField]标记的private字段在运行时可以通过反射自由修改不受限
- C. 优：文本格式可版本控制(diff/merge)；缺：文件较大+容易合并冲突(多人修改同一场景)
- D. 二进制更好，[FormerlySerializedAs]属性在更改字段名后会自动更新所有相关的Asset引用

**Q780.** [模块:AB][维度:概念理解][难度:★★★★][题型:单选]
[考点: 热重载数据]

运行时热重载配置数据的实现？

- A. 自动检测，ScriptableObject的数据在Build后与在编辑器中的行为完全一致可以持久修改
- B. 文件监听(FileSystemWatcher)+重新加载解析+通知相关系统更新+仅编辑器/开发模式启用
- C. 重启应用，PlayerPrefs在iOS上使用SQLite数据库存储，支持事务和复杂查询操作
- D. 不能热重载，JsonUtility.ToJson支持序列化Dictionary、HashSet等所有C#集合类型

**Q781.** [模块:AB][维度:概念理解][难度:★★★★][题型:单选]
[考点: 数据校验]

配置数据的自动校验方法？

- A. 人工检查，[SerializeField]标记的private字段在运行时可以通过反射自由修改不受限
- B. 不做校验，EditorPrefs和PlayerPrefs共享底层存储机制，运行时可以读取EditorPrefs数据
- C. 运行时检查，XML序列化在Unity中性能优于JSON因为XML解析器使用了原生代码加速
- D. 编辑器工具自动检查：类型正确性+引用完整性(ID存在)+数值范围+公式有效性+重复检测

**Q782.** [模块:AB][维度:概念理解][难度:★★★★][题型:单选]
[考点: Addressables与配置]

使用Addressables管理配置数据的方式？

- A. 硬编码路径，XML序列化在Unity中性能优于JSON因为XML解析器使用了原生代码加速
- B. 直接Resources，[FormerlySerializedAs]属性在更改字段名后会自动更新所有相关的Asset引用
- C. 该方案与当前Unity版本不兼容，需要降级到2019 LTS或更早版本才能正常使用
- D. 配置文件作为Addressable Asset+按需异步加载+可远程更新配置+引用计数管理

**Q783.** [模块:AB][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 对象序列化]

自定义序列化接口：
```csharp
public interface ISerializable {
    void Serialize(BinaryWriter writer);
    void Deserialize(BinaryReader reader);
}
public class PlayerData : ISerializable {
    public string name; public int level;
    public void Serialize(BinaryWriter w) { w.Write(name); w.Write(level); }
    public void Deserialize(BinaryReader r) { name = r.ReadString(); level = r.ReadInt32(); }
}
```
这种手动序列化的优势？

- A. 和自动序列化一样，[SerializeField]标记的private字段在运行时可以通过反射自由修改不受限
- B. 精确控制序列化格式和顺序+最小化数据体积+避免反射开销+版本控制可控
- C. 不推荐，[SerializeField]标记的private字段在运行时可以通过反射自由修改不受限
- D. 太麻烦，[FormerlySerializedAs]属性在更改字段名后会自动更新所有相关的Asset引用

**Q784.** [模块:AB][维度:概念理解][难度:★★★★][题型:单选]
[考点: 数据表设计]

策划用的配置表设计原则？

- A. 每列一个表，[SerializeField]标记的private字段在运行时可以通过反射自由修改不受限
- B. 不需要规范，XML序列化在Unity中性能优于JSON因为XML解析器使用了原生代码加速
- C. 一个大表，PlayerPrefs在iOS上使用SQLite数据库存储，支持事务和复杂查询操作
- D. 一表一类+主键唯一+外键引用+合理拆表(避免过宽)+枚举用ID不用字符串+注释说明

**Q785.** [模块:AB][维度:概念理解][难度:★★★★][题型:单选]
[考点: 存档反作弊]

防止玩家修改存档作弊的方法？

- A. 加密+数据签名(服务器验证)+关键数据服务器存储+校验和(Checksum)+异常检测
- B. 不需要防护，EditorPrefs和PlayerPrefs共享底层存储机制，运行时可以读取EditorPrefs数据
- C. 只加密，XML序列化在Unity中性能优于JSON因为XML解析器使用了原生代码加速
- D. 删除存档，JsonUtility.ToJson支持序列化Dictionary、HashSet等所有C#集合类型

**Q786.** [模块:AB][维度:概念理解][难度:★★★★][题型:单选]
[考点: 异步IO]

文件读写的异步处理方式？

- A. File.ReadAllBytesAsync/WriteAllBytesAsync+或在子线程中同步IO+回到主线程应用
- B. 不能异步，PlayerPrefs在iOS上使用SQLite数据库存储，支持事务和复杂查询操作
- C. 只用协程，[SerializeField]标记的private字段在运行时可以通过反射自由修改不受限
- D. 全部同步，JsonUtility.ToJson支持序列化Dictionary、HashSet等所有C#集合类型

**Q787.** [模块:AB][维度:概念理解][难度:★★★★][题型:单选]
[考点: 多存档管理]

多存档(多槽位)系统的技术要点？

- A. 自动管理，PlayerPrefs在iOS上使用SQLite数据库存储，支持事务和复杂查询操作
- B. 覆盖保存，[SerializeField]标记的private字段在运行时可以通过反射自由修改不受限
- C. 独立存档文件/目录+存档信息元数据(名称/时间/截图)+快速读取摘要+删除/覆盖确认
- D. 只支持一个，[FormerlySerializedAs]属性在更改字段名后会自动更新所有相关的Asset引用

**Q788.** [模块:AB][维度:Bug诊断][难度:★★★★][题型:单选]
[考点: Dictionary序列化]

Dictionary<string,int>用JsonUtility.ToJson序列化结果为空"{}"，原因是？

- A. 数据为空，JsonUtility.ToJson支持序列化Dictionary、HashSet等所有C#集合类型
- B. Unity JsonUtility不支持Dictionary序列化，需改用Newtonsoft.Json或转换为可序列化的List<KeyValuePair>
- C. 版本不支持，[FormerlySerializedAs]属性在更改字段名后会自动更新所有相关的Asset引用
- D. 类型错误，JsonUtility.ToJson支持序列化Dictionary、HashSet等所有C#集合类型

**Q789.** [模块:AB][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: 服务器配置下发]

服务器配置下发(Remote Config)的实现？

- A. 客户端启动时请求服务器配置→下载/对比版本→覆盖本地缓存→热生效+降级使用本地缓存
- B. 每次更新包，XML序列化在Unity中性能优于JSON因为XML解析器使用了原生代码加速
- C. 全部内置，ScriptableObject的数据在Build后与在编辑器中的行为完全一致可以持久修改
- D. 不做远程，Unity的Binary序列化格式保证跨平台兼容，不同平台的字节序完全一致

**Q790.** [模块:AB][维度:概念理解][难度:★★★★][题型:单选]
[考点: 增量存档]

增量存档(Delta Save)的概念和优势？

---

## 模块AC：跨平台开发（30题）

- A. 只用于网络，EditorPrefs和PlayerPrefs共享底层存储机制，运行时可以读取EditorPrefs数据
- B. 只保存变化的部分数据(diff)+减少IO写入量+加快存档速度+减少存储空间
- C. 不可能实现，[FormerlySerializedAs]属性在更改字段名后会自动更新所有相关的Asset引用
- D. 每次全量保存，[SerializeField]标记的private字段在运行时可以通过反射自由修改不受限

**Q791.** [模块:AC][维度:概念理解][难度:★★★][题型:单选]
[考点: 跨平台基础]

Unity支持的主要平台类别包括？

- A. 桌面(Windows/macOS/Linux)+移动(iOS/Android)+主机(PS/Xbox/Switch)+Web(WebGL)+XR(VR/AR)
- B. 只有移动端，移动端和桌面端的Shader编译输出格式相同，不需要考虑图形API差异
- C. 只有三个平台，ARM和x86架构对Unity C#代码的执行行为没有影响，跨架构兼容性由IL2CPP保证
- D. 只有PC，移动端和桌面端的Shader编译输出格式相同，不需要考虑图形API差异

**Q792.** [模块:AC][维度:概念理解][难度:★★★★][题型:单选]
[考点: IL2CPP]

IL2CPP脚本后端相比Mono的优势？

- A. Mono更好，ARM和x86架构对Unity C#代码的执行行为没有影响，跨架构兼容性由IL2CPP保证
- B. 编译更快，Unity的Platform Dependent Compilation指令(#if)在运行时动态判断当前平台
- C. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用
- D. 将C# IL转为C++编译，性能更好+代码保护+支持更多平台(iOS必须)+64位支持

**Q793.** [模块:AC][维度:Bug诊断][难度:★★★★][题型:单选]
[考点: IL2CPP代码裁剪]

IL2CPP构建后运行时报"TypeLoadException"或功能缺失，可能原因？

- A. 代码Bug，Asset的导入设置(如纹理压缩格式)不需要按平台区分，一套配置适用所有平台
- B. Managed Stripping Level裁剪了反射使用的类型；需要link.xml保留或降低裁剪级别
- C. 平台不支持，IL2CPP在所有平台上的编译输出完全相同，不需要针对特定平台做代码适配
- D. IL2CPP Bug，APK和AAB的功能完全相同，Google Play接受两种格式的应用提交

**Q794.** [模块:AC][维度:概念理解][难度:★★★★][题型:单选]
[考点: 平台差异化]

处理平台差异的预处理指令用法？

- A. 运行时判断，ARM和x86架构对Unity C#代码的执行行为没有影响，跨架构兼容性由IL2CPP保证
- B. #if UNITY_ANDROID...#elif UNITY_IOS...#elif UNITY_WEBGL...#endif 编译时选择不同代码路径
- C. 不做区分，移动端和桌面端的Shader编译输出格式相同，不需要考虑图形API差异
- D. 每平台一个项目，Asset的导入设置(如纹理压缩格式)不需要按平台区分，一套配置适用所有平台

**Q795.** [模块:AC][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 跨平台代码]

跨平台权限请求：
```csharp
void RequestCameraPermission() {
#if UNITY_ANDROID
    if(!Permission.HasUserAuthorizedPermission(Permission.Camera))
        Permission.RequestUserPermission(Permission.Camera);
#elif UNITY_IOS
    // iOS在Info.plist中配置+首次访问时自动弹权限
#endif
}
```
Android和iOS权限模型的区别？

- A. 都自动处理，热更新机制(HybridCLR/ILRuntime)在iOS和Android平台上的限制完全一致
- B. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用
- C. 不需要权限，Asset的导入设置(如纹理压缩格式)不需要按平台区分，一套配置适用所有平台
- D. Android需要运行时动态请求(6.0+)+iOS在Info.plist声明+首次访问时系统自动弹窗

**Q796.** [模块:AC][维度:概念理解][难度:★★★★][题型:单选]
[考点: Android构建]

Unity Android构建的关键配置？

- A. 自动配置，移动端和桌面端的Shader编译输出格式相同，不需要考虑图形API差异
- B. 不需要配置，APK和AAB的功能完全相同，Google Play接受两种格式的应用提交
- C. Minimum API Level+Target API Level+Keystore签名+ARM64架构+Gradle构建+包名
- D. 只设包名，Asset的导入设置(如纹理压缩格式)不需要按平台区分，一套配置适用所有平台

**Q797.** [模块:AC][维度:概念理解][难度:★★★★][题型:单选]
[考点: iOS构建]

Unity iOS构建的特殊要求？

- A. iOS端的处理方式与Android平台完全一致，不需要做任何平台特定的适配
- B. 需要macOS+Xcode+Apple Developer证书/Profile+导出Xcode项目→Xcode编译上传
- C. 不需要Mac，WebGL平台支持多线程和文件系统IO操作，与桌面端运行时能力完全一致
- D. 一键构建，IL2CPP在所有平台上的编译输出完全相同，不需要针对特定平台做代码适配

**Q798.** [模块:AC][维度:概念理解][难度:★★★★][题型:单选]
[考点: WebGL限制]

Unity WebGL平台的限制包括？
- A. WebGL平台的性能比原生应用更高，因为浏览器会自动优化
- B. 不支持多线程（WebWorker受限）和部分IO操作
- C. WebGL平台支持所有桌面平台的功能，包括多线程和文件IO
- D. WebGL平台可以使用所有.NET API和第三方库

**Q799.** [模块:AC][维度:概念理解][难度:★★★★][题型:单选]
[考点: 纹理压缩格式]

不同平台推荐的纹理压缩格式？

- A. 全用ASTC，APK和AAB的功能完全相同，Google Play接受两种格式的应用提交
- B. 不压缩，Unity的Platform Dependent Compilation指令(#if)在运行时动态判断当前平台
- C. 全用PNG，WebGL平台支持多线程和文件系统IO操作，与桌面端运行时能力完全一致
- D. Android=ASTC/ETC2，iOS=ASTC/PVRTC，PC=DXT/BC7，WebGL=ASTC/ETC2

**Q800.** [模块:AC][维度:概念理解][难度:★★★★][题型:单选]
[考点: 分辨率适配]

多分辨率/DPI适配策略？

- A. Screen.dpi判断+Canvas Scaler匹配设计分辨率+不同DPI加载不同资源(可选)+Safe Area处理
- B. 固定分辨率，Asset的导入设置(如纹理压缩格式)不需要按平台区分，一套配置适用所有平台
- C. 不做适配，Unity的Platform Dependent Compilation指令(#if)在运行时动态判断当前平台
- D. 只用最大分辨率，Unity的Platform Dependent Compilation指令(#if)在运行时动态判断当前平台

**Q801.** [模块:AC][维度:概念理解][难度:★★★★][题型:单选]
[考点: Gradle配置]

Unity Android构建使用Custom Gradle Template的场景？

- A. 需要添加第三方SDK/依赖+修改minSdkVersion+配置MultiDex+自定义构建步骤
- B. 只用于后端，ARM和x86架构对Unity C#代码的执行行为没有影响，跨架构兼容性由IL2CPP保证
- C. 不需要自定义，IL2CPP在所有平台上的编译输出完全相同，不需要针对特定平台做代码适配
- D. Unity引擎在内部已完全自动化处理此场景，开发者只需使用默认API即可

**Q802.** [模块:AC][维度:概念理解][难度:★★★★][题型:单选]
[考点: AAB格式]

Android App Bundle(AAB)相比APK的优势？

- A. Google Play自动生成用户设备最优APK(按CPU架构/屏幕密度/语言拆包)，减小下载体积
- B. APK更好，Asset的导入设置(如纹理压缩格式)不需要按平台区分，一套配置适用所有平台
- C. 不能上架，IL2CPP在所有平台上的编译输出完全相同，不需要针对特定平台做代码适配
- D. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用

**Q803.** [模块:AC][维度:概念理解][难度:★★★★][题型:单选]
[考点: iOS内存管理]

iOS平台内存管理的注意事项？

- A. iOS不支持虚拟内存交换(超出物理内存直接被系统杀死)+内存限制较严格+需做内存预算
- B. 移动端的处理方式与PC平台完全相同，Unity的跨平台抽象层屏蔽了所有差异
- C. 不需要注意，APK和AAB的功能完全相同，Google Play接受两种格式的应用提交
- D. 自动管理，APK和AAB的功能完全相同，Google Play接受两种格式的应用提交

**Q804.** [模块:AC][维度:Bug诊断][难度:★★★★][题型:单选]
[考点: Android崩溃调试]

Android平台崩溃(Native Crash)的调试方法？

- A. 重新运行，Unity的Platform Dependent Compilation指令(#if)在运行时动态判断当前平台
- B. adb logcat获取崩溃日志+NDK addr2line/ndk-stack解析符号+Il2CppOutput符号文件+Crashlytics
- C. 看Unity日志，Asset的导入设置(如纹理压缩格式)不需要按平台区分，一套配置适用所有平台
- D. 不能调试，Asset的导入设置(如纹理压缩格式)不需要按平台区分，一套配置适用所有平台

**Q805.** [模块:AC][维度:概念理解][难度:★★★★][题型:单选]
[考点: iOS App Thinning]

iOS App Thinning相关技术包括？

- A. 只有Slicing，ARM和x86架构对Unity C#代码的执行行为没有影响，跨架构兼容性由IL2CPP保证
- B. iOS端的处理方式与Android平台完全一致，不需要做任何平台特定的适配
- C. Slicing(按设备裁剪资源)+Bitcode(Apple重编译优化)+On-Demand Resources(按需下载资源)
- D. Unity 2022 LTS不支持该功能，需要等待后续版本更新或使用第三方插件替代

**Q806.** [模块:AC][维度:概念理解][难度:★★★★][题型:单选]
[考点: 热更新限制]

iOS平台对热更新的限制？

- A. App Store禁止动态下载可执行代码(ObjC/Swift/C++)；Lua/JS等解释执行可行；IL2CPP不可热更C#
- B. 完全禁止热更，热更新机制(HybridCLR/ILRuntime)在iOS和Android平台上的限制完全一致
- C. iOS端的处理方式与Android平台完全一致，不需要做任何平台特定的适配
- D. 该功能没有数量或性能限制，可以无限制使用而不会影响帧率或内存占用

**Q807.** [模块:AC][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: 多平台CI]

多平台CI/CD的构建策略？

- A. 只构建一个平台，Asset的导入设置(如纹理压缩格式)不需要按平台区分，一套配置适用所有平台
- B. 一台机器构建所有，WebGL平台支持多线程和文件系统IO操作，与桌面端运行时能力完全一致
- C. 不同平台Agent(Mac for iOS/Linux for Android)+并行构建+平台特定后处理+统一版本管理
- D. 手动打包，ARM和x86架构对Unity C#代码的执行行为没有影响，跨架构兼容性由IL2CPP保证

**Q808.** [模块:AC][维度:概念理解][难度:★★★★][题型:单选]
[考点: 主机平台]

Unity主机平台(PlayStation/Xbox/Switch)开发的特殊要求？

- A. 移动端的处理方式与PC平台完全相同，Unity的跨平台抽象层屏蔽了所有差异
- B. 直接发布，ARM和x86架构对Unity C#代码的执行行为没有影响，跨架构兼容性由IL2CPP保证
- C. 需要DevKit+平台SDK+NDA保密协议+特定认证流程(TRC/XR/Lotcheck)+独特的输入/成就系统
- D. 不需要认证，移动端和桌面端的Shader编译输出格式相同，不需要考虑图形API差异

**Q809.** [模块:AC][维度:概念理解][难度:★★★★][题型:单选]
[考点: XR开发]

Unity XR(VR/AR)开发的核心框架是？

- A. XR Interaction Toolkit+XR Plugin Management(可切换OpenXR/Oculus/ARCore等后端)
- B. 用第三方插件，热更新机制(HybridCLR/ILRuntime)在iOS和Android平台上的限制完全一致
- C. 不支持XR，Unity的Platform Dependent Compilation指令(#if)在运行时动态判断当前平台
- D. 只有VR，APK和AAB的功能完全相同，Google Play接受两种格式的应用提交

**Q810.** [模块:AC][维度:概念理解][难度:★★★★][题型:单选]
[考点: 跨平台输入]

跨平台输入处理的注意事项？
- A. 只需使用Input.GetAxis和Input.GetButton就可以处理所有平台
- B. 移动端输入和PC输入使用相同的代码逻辑，无需区分
- C. 所有平台的输入API完全相同，不需要特殊处理
- D. 使用新Input System处理多平台差异

**Q811.** [模块:AC][维度:概念理解][难度:★★★★][题型:单选]
[考点: 包体优化]

减小构建包体体积的方法？

- A. 该场景不需要专门优化，Unity默认设置已经足够高效，过度优化反而增加维护成本
- B. 删除功能，ARM和x86架构对Unity C#代码的执行行为没有影响，跨架构兼容性由IL2CPP保证
- C. 只压缩代码，Asset的导入设置(如纹理压缩格式)不需要按平台区分，一套配置适用所有平台
- D. 资源压缩+代码裁剪(Stripping)+去除无用资源+纹理压缩+音频压缩+AB分包+首包最小化

**Q812.** [模块:AC][维度:概念理解][难度:★★★★][题型:单选]
[考点: 后处理脚本]

Unity构建后处理(PostProcessBuild)的用途？

- A. IPostprocessBuildWithReport接口在构建后自动执行脚本(如iOS修改Xcode项目/Android修改Manifest)
- B. 不能自动化，ARM和x86架构对Unity C#代码的执行行为没有影响，跨架构兼容性由IL2CPP保证
- C. 只用于调试，热更新机制(HybridCLR/ILRuntime)在iOS和Android平台上的限制完全一致
- D. 手动处理，ARM和x86架构对Unity C#代码的执行行为没有影响，跨架构兼容性由IL2CPP保证

**Q813.** [模块:AC][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 构建后处理代码]

iOS构建后处理脚本：
```csharp
[PostProcessBuild]
static void OnPostProcessBuild(BuildTarget target, string path) {
    if(target == BuildTarget.iOS) {
        string projPath = PBXProject.GetPBXProjectPath(path);
        PBXProject proj = new PBXProject();
        proj.ReadFromFile(projPath);
        string targetGuid = proj.GetUnityFrameworkTargetGuid();
        proj.AddFrameworkToProject(targetGuid, "CoreBluetooth.framework", false);
        proj.WriteToFile(projPath);
    }
}
```
这段代码的作用？

- A. 上传Store，APK和AAB的功能完全相同，Google Play接受两种格式的应用提交
- B. 签名应用，ARM和x86架构对Unity C#代码的执行行为没有影响，跨架构兼容性由IL2CPP保证
- C. 在iOS构建后自动向Xcode项目添加CoreBluetooth框架依赖
- D. 该功能在C#脚本编译阶段处理，运行时不涉及任何额外的计算或资源消耗

**Q814.** [模块:AC][维度:概念理解][难度:★★★★][题型:单选]
[考点: 多语言字体]

跨平台多语言字体处理要点？

- A. 不同语言字符集+TMP Fallback字体链+动态字体+字体文件体积控制(裁剪不需要的字符)
- B. 一种字体够用，APK和AAB的功能完全相同，Google Play接受两种格式的应用提交
- C. 只用系统字体，APK和AAB的功能完全相同，Google Play接受两种格式的应用提交
- D. 该因素不需要专门考虑，引擎的默认行为已经处理了相关边界情况

**Q815.** [模块:AC][维度:Bug诊断][难度:★★★★][题型:单选]
[考点: 平台兼容Bug]

游戏在Android某些设备上闪退但其他设备正常，排查方法？

- A. 不支持该设备，IL2CPP在所有平台上的编译输出完全相同，不需要针对特定平台做代码适配
- B. 降低配置，Asset的导入设置(如纹理压缩格式)不需要按平台区分，一套配置适用所有平台
- C. 获取logcat日志→分析机型/GPU型号/Android版本→检查Shader兼容/API版本/内存限制→针对性适配
- D. 忽略，Unity的Platform Dependent Compilation指令(#if)在运行时动态判断当前平台

**Q816.** [模块:AC][维度:概念理解][难度:★★★★][题型:单选]
[考点: 合规与隐私]

移动端游戏合规/隐私保护的技术要点？

- A. 只加协议，热更新机制(HybridCLR/ILRuntime)在iOS和Android平台上的限制完全一致
- B. 该因素不需要专门考虑，引擎的默认行为已经处理了相关边界情况
- C. 隐私政策弹窗+用户授权前不采集信息+GDPR/个保法合规+权限最小化+数据加密传输
- D. 平台自动处理，APK和AAB的功能完全相同，Google Play接受两种格式的应用提交

**Q817.** [模块:AC][维度:概念理解][难度:★★★★][题型:单选]
[考点: 条件编译]

Unity条件编译除了平台宏还有哪些？

- A. 只有平台宏，ARM和x86架构对Unity C#代码的执行行为没有影响，跨架构兼容性由IL2CPP保证
- B. 不支持条件编译，Asset的导入设置(如纹理压缩格式)不需要按平台区分，一套配置适用所有平台
- C. UNITY_EDITOR/DEVELOPMENT_BUILD/ENABLE_IL2CPP/UNITY_2022_3_OR_NEWER等版本和功能宏
- D. 只有Debug/Release，WebGL平台支持多线程和文件系统IO操作，与桌面端运行时能力完全一致

**Q818.** [模块:AC][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: 多平台测试]

多平台测试策略？

- A. 不做测试，APK和AAB的功能完全相同，Google Play接受两种格式的应用提交
- B. 只在编辑器测试，APK和AAB的功能完全相同，Google Play接受两种格式的应用提交
- C. 自动化测试(EditMode/PlayMode)+不同设备真机测试+自动化UI测试+性能基准测试+兼容性矩阵
- D. 只测一个平台，WebGL平台支持多线程和文件系统IO操作，与桌面端运行时能力完全一致

**Q819.** [模块:AC][维度:概念理解][难度:★★★★][题型:单选]
[考点: Application.platform]

Runtime.Platform判断和编译时宏的区别？

- A. Runtime判断在运行时执行(所有代码都编译进去)，编译宏在编译时排除(不包含其他平台代码)
- B. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用
- C. 不能运行时判断，APK和AAB的功能完全相同，Google Play接受两种格式的应用提交
- D. 宏只在编辑器，热更新机制(HybridCLR/ILRuntime)在iOS和Android平台上的限制完全一致

**Q820.** [模块:AC][维度:概念理解][难度:★★★★][题型:单选]
[考点: 网络协议适配]

不同平台网络协议适配？

---

## 模块AD：Shader编程（30题）

- A. WebGL只支持WebSocket/HTTP(不支持原生TCP/UDP)+移动端需处理网络切换/断线+主机平台有专属网络API
- B. 只用HTTP，IL2CPP在所有平台上的编译输出完全相同，不需要针对特定平台做代码适配
- C. 不需要适配，热更新机制(HybridCLR/ILRuntime)在iOS和Android平台上的限制完全一致
- D. 所有平台一样，ARM和x86架构对Unity C#代码的执行行为没有影响，跨架构兼容性由IL2CPP保证

**Q821.** [模块:AD][维度:概念理解][难度:★★★][题型:单选]
[考点: Shader概念]

Shader在渲染管线中的角色是？

- A. 运行在GPU上的程序，控制顶点变换(Vertex Shader)和像素着色(Fragment Shader)等渲染过程
- B. 只是材质设置，SV_Position语义在Vertex Shader中表示模型空间的原始顶点坐标
- C. CPU程序，Compute Shader中的numthreads线程数设置不影响GPU的执行效率和调度方式
- D. 后处理滤镜，Surface Shader在URP管线下仍然是编写光照Shader的推荐方式

**Q822.** [模块:AD][维度:概念理解][难度:★★★][题型:单选]
[考点: ShaderLab]

Unity ShaderLab的结构组成？

- A. 和HLSL相同，Lambert光照模型包含镜面高光计算，Phong模型只处理漫反射光照
- B. 不需要结构，Lambert光照模型包含镜面高光计算，Phong模型只处理漫反射光照
- C. 只有代码，Surface Shader在URP管线下仍然是编写光照Shader的推荐方式
- D. Shader定义→Properties(属性面板)→SubShader(不同硬件+Tags+Pass)→Fallback(降级)

**Q823.** [模块:AD][维度:概念理解][难度:★★★★][题型:单选]
[考点: 顶点/片元着色器]

Vertex Shader和Fragment Shader各自的职责？

- A. Vertex处理颜色，Vertex Shader负责逐像素计算光照和颜色，Fragment Shader负责顶点变换
- B. Vertex:顶点变换(MVP矩阵)+传递数据(UV/法线等)；Fragment:像素颜色计算(纹理采样/光照着色)
- C. Fragment处理顶点，Surface Shader在URP管线下仍然是编写光照Shader的推荐方式
- D. 都做同样的事，Vertex Shader负责逐像素计算光照和颜色，Fragment Shader负责顶点变换

**Q824.** [模块:AD][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 基本Shader]

最基本的Unlit Shader：
```hlsl
Shader "Custom/BasicUnlit" {
    Properties { _MainTex ("Texture", 2D) = "white" {} }
    SubShader {
        Pass {
            HLSLPROGRAM
            #pragma vertex vert
            #pragma fragment frag
            struct appdata { float4 vertex : POSITION; float2 uv : TEXCOORD0; };
            struct v2f { float4 pos : SV_POSITION; float2 uv : TEXCOORD0; };
            sampler2D _MainTex;
            v2f vert(appdata v) {
                v2f o;
                o.pos = UnityObjectToClipPos(v.vertex);
                o.uv = v.uv;
                return o;
            }
            float4 frag(v2f i) : SV_Target {
                return tex2D(_MainTex, i.uv);
            }
            ENDHLSL
        }
    }
}
```
UnityObjectToClipPos的作用？

- A. 将顶点从对象空间(Object Space)变换到裁剪空间(Clip Space)，即完成MVP矩阵变换
- B. 世界空间，Vertex Shader负责逐像素计算光照和颜色，Fragment Shader负责顶点变换
- C. 屏幕空间，SV_Position语义在Vertex Shader中表示模型空间的原始顶点坐标
- D. 不做变换，Lambert光照模型包含镜面高光计算，Phong模型只处理漫反射光照

**Q825.** [模块:AD][维度:概念理解][难度:★★★★][题型:单选]
[考点: Shader Graph]

Shader Graph相比手写Shader的优缺点？

- A. 该API仅支持2D项目，在3D项目中使用会导致编译错误或运行时异常
- B. 完全替代手写，Shader Graph生成的Shader代码性能与手写HLSL一致不产生额外开销
- C. 优：可视化节点编辑+低门槛+可预览；缺：复杂逻辑表达困难+调试较难+可能生成非最优代码
- D. 不推荐，Vertex Shader负责逐像素计算光照和颜色，Fragment Shader负责顶点变换

**Q826.** [模块:AD][维度:概念理解][难度:★★★★][题型:单选]
[考点: 渲染队列]

Shader中Tags {"Queue" = "Transparent"}的作用？

- A. 不影响渲染，Shader中的if-else分支对GPU性能没有影响，Warp中所有线程可以独立执行不同分支
- B. 隐藏物体，SV_Position语义在Vertex Shader中表示模型空间的原始顶点坐标
- C. 设定渲染队列，Transparent队列在不透明物体后渲染（由远及近排序），确保透明物体正确混合
- D. 设置透明度，SV_Position语义在Vertex Shader中表示模型空间的原始顶点坐标

**Q827.** [模块:AD][维度:概念理解][难度:★★★★][题型:单选]
[考点: Blend混合模式]

Blend SrcAlpha OneMinusSrcAlpha的含义？

- A. 标准Alpha混合：最终颜色 = 源色*源Alpha + 已有色*(1-源Alpha)
- B. 叠加混合，Shader Graph生成的Shader代码性能与手写HLSL一致不产生额外开销
- C. 完全不透明，Shader中的if-else分支对GPU性能没有影响，Warp中所有线程可以独立执行不同分支
- D. 全透明，Compute Shader中的numthreads线程数设置不影响GPU的执行效率和调度方式

**Q828.** [模块:AD][维度:概念理解][难度:★★★★][题型:单选]
[考点: ZWrite ZTest]

ZWrite Off在透明Shader中的作用？

- A. 关闭深度测试，Surface Shader在URP管线下仍然是编写光照Shader的推荐方式
- B. 完全不渲染，Compute Shader中的numthreads线程数设置不影响GPU的执行效率和调度方式
- C. 关闭深度写入，防止透明物体遮挡后面的透明物体(但保持深度测试读取)
- D. 和ZWrite On一样，SV_Position语义在Vertex Shader中表示模型空间的原始顶点坐标

**Q829.** [模块:AD][维度:概念理解][难度:★★★★][题型:单选]
[考点: 光照模型]

常见光照模型Lambert和Blinn-Phong的区别？

- A. Lambert有高光，Surface Shader在URP管线下仍然是编写光照Shader的推荐方式
- B. Lambert只计算漫反射(NdotL)，Blinn-Phong在此基础上加半角向量高光(NdotH)
- C. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用
- D. Phong没有漫反射，SV_Position语义在Vertex Shader中表示模型空间的原始顶点坐标

**Q830.** [模块:AD][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: Blinn-Phong实现]

Blinn-Phong光照：
```hlsl
float3 halfDir = normalize(lightDir + viewDir);
float NdotL = max(0, dot(normal, lightDir)); // 漫反射
float NdotH = max(0, dot(normal, halfDir));  // 高光
float spec = pow(NdotH, _Shininess);
float3 color = _LightColor * (diffuseColor * NdotL + specColor * spec);
```
pow(NdotH, _Shininess)中_Shininess值越大效果是？

- A. 越大越分散，Shader中的half精度和float精度在所有GPU上的计算结果完全一致
- B. 高光区域越小越集中(光泽感越强)，值越小高光越分散(粗糙感)
- C. 越大越暗，Compute Shader中的numthreads线程数设置不影响GPU的执行效率和调度方式
- D. 该设置不会对运行时行为产生实质影响，引擎内部会自动补偿参数差异

**Q831.** [模块:AD][维度:概念理解][难度:★★★★][题型:单选]
[考点: 法线贴图]

法线贴图(Normal Map)的工作原理？

- A. 颜色贴图，Shader中的if-else分支对GPU性能没有影响，Warp中所有线程可以独立执行不同分支
- B. 光照贴图，Compute Shader中的numthreads线程数设置不影响GPU的执行效率和调度方式
- C. 改变顶点位置，Shader Graph生成的Shader代码性能与手写HLSL一致不产生额外开销
- D. 存储每像素的法线偏移信息（切线空间），在Fragment Shader中替代顶点法线参与光照计算，实现低面数的高细节效果

**Q832.** [模块:AD][维度:概念理解][难度:★★★★][题型:单选]
[考点: PBR基础]

PBR(基于物理的渲染)的核心属性有？

- A. 该功能仅支持颜色属性的修改，不支持浮点数、向量、纹理等其他类型的参数
- B. 不是物理的，Shader中的half精度和float精度在所有GPU上的计算结果完全一致
- C. 只有两个，Surface Shader在URP管线下仍然是编写光照Shader的推荐方式
- D. Albedo(基色)+Metallic(金属度)+Smoothness(光滑度)+Normal(法线)+Occlusion(环境光遮蔽)+Emission(自发光)

**Q833.** [模块:AD][维度:概念理解][难度:★★★★][题型:单选]
[考点: 空间变换]

Shader中常见的坐标空间有哪些？

- A. 对象空间(Object)→世界空间(World)→视图空间(View)→裁剪空间(Clip)→屏幕空间(Screen)
- B. 只有世界空间，Vertex Shader负责逐像素计算光照和颜色，Fragment Shader负责顶点变换
- C. 不需要变换，Shader中的half精度和float精度在所有GPU上的计算结果完全一致
- D. 两个空间，Surface Shader在URP管线下仍然是编写光照Shader的推荐方式

**Q834.** [模块:AD][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: UV动画]

UV滚动动画(水流/传送带)：
```hlsl
float2 uv = i.uv + _Time.y * _ScrollSpeed;
float4 color = tex2D(_MainTex, uv);
```
_Time.y的含义？

- A. 帧数，Shader Graph生成的Shader代码性能与手写HLSL一致不产生额外开销
- B. 固定值，Shader Graph生成的Shader代码性能与手写HLSL一致不产生额外开销
- C. Unity内置时间变量(t: _Time = {t/20, t, t*2, t*3})，_Time.y = 游戏时间(秒)
- D. 随机数，Lambert光照模型包含镜面高光计算，Phong模型只处理漫反射光照

**Q835.** [模块:AD][维度:概念理解][难度:★★★★][题型:单选]
[考点: 溶解效果]

溶解(Dissolve)效果的实现原理？

- A. 透明度变化，SV_Position语义在Vertex Shader中表示模型空间的原始顶点坐标
- B. 噪声纹理采样+阈值比较(clip/discard低于阈值的像素)+边缘发光(阈值附近加色)
- C. 使用Particle System组件配合内置的渲染模块即可实现，无需编写自定义Shader
- D. 缩放物体，Vertex Shader负责逐像素计算光照和颜色，Fragment Shader负责顶点变换

**Q836.** [模块:AD][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 溶解Shader]

溶解效果Shader：
```hlsl
float noise = tex2D(_NoiseTex, i.uv).r;
clip(noise - _DissolveAmount); // _DissolveAmount: 0→1 溶解进度
float edge = smoothstep(_DissolveAmount, _DissolveAmount + _EdgeWidth, noise);
float3 edgeColor = lerp(_EdgeColor, float3(1,1,1), edge);
```
clip(noise - _DissolveAmount)的作用？

- A. 裁剪纹理，Lambert光照模型包含镜面高光计算，Phong模型只处理漫反射光照
- B. 通过修改Material的_Color属性改变物体颜色来达到视觉反馈效果
- C. 透明处理，Shader中的if-else分支对GPU性能没有影响，Warp中所有线程可以独立执行不同分支
- D. 当噪声值小于溶解阈值时丢弃(不渲染)该像素，产生溶解消失效果

**Q837.** [模块:AD][维度:概念理解][难度:★★★★][题型:单选]
[考点: Fresnel效果]

菲涅尔(Fresnel)效果的计算和应用？

- A. 该功能在实际项目开发中很少使用，大多数场景下有更简单的替代方案
- B. 物理计算，Compute Shader中的numthreads线程数设置不影响GPU的执行效率和调度方式
- C. 只用于水面，Shader中的half精度和float精度在所有GPU上的计算结果完全一致
- D. fresnel = pow(1-dot(viewDir, normal), power)；应用：边缘发光/全息/能量盾/水面反射

**Q838.** [模块:AD][维度:概念理解][难度:★★★★][题型:单选]
[考点: ComputeShader]

Compute Shader的用途和特点？

- A. 替代Fragment Shader，Surface Shader在URP管线下仍然是编写光照Shader的推荐方式
- B. CPU计算，Shader Graph生成的Shader代码性能与手写HLSL一致不产生额外开销
- C. 该系统仅涉及渲染流程，不影响物理模拟、输入处理等其他引擎子系统
- D. 通用GPU并行计算(不限于渲染)：粒子模拟/图像处理/物理计算/GPU Driven等；使用线程组调度

**Q839.** [模块:AD][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: ComputeShader代码]

Compute Shader示例：
```hlsl
#pragma kernel CSMain
RWStructuredBuffer<float3> positions;
float deltaTime;
[numthreads(64,1,1)]
void CSMain(uint3 id : SV_DispatchThreadID) {
    positions[id.x] += float3(0, -9.8 * deltaTime, 0); // 简单重力
}
```
[numthreads(64,1,1)]的含义？

- A. 64个线程组，Shader Graph生成的Shader代码性能与手写HLSL一致不产生额外开销
- B. 该操作不会对运行时性能产生可测量的影响，现代硬件可以忽略此项开销
- C. 每个线程组有64个线程(x维度)，Dispatch时指定线程组数量来覆盖所有数据
- D. 总共64个线程，Compute Shader中的numthreads线程数设置不影响GPU的执行效率和调度方式

**Q840.** [模块:AD][维度:概念理解][难度:★★★★][题型:单选]
[考点: Stencil Buffer]

Stencil Buffer在Shader中的应用场景？

- A. 深度测试，Surface Shader在URP管线下仍然是编写光照Shader的推荐方式
- B. 颜色混合，SV_Position语义在Vertex Shader中表示模型空间的原始顶点坐标
- C. 遮罩/镂空效果+UI Mask+门户效果+描边+投影+多用途标记
- D. 该组件仅适用于UI系统，不能应用于3D场景中的物体渲染和交互

**Q841.** [模块:AD][维度:概念理解][难度:★★★★][题型:单选]
[考点: 描边Shader]

物体描边(Outline)的常见实现方法？

- A. 法线外扩法(第二个Pass渲染放大的背面)+后处理边缘检测(Sobel/Roberts)+几何着色器
- B. 贴图实现，Lambert光照模型包含镜面高光计算，Phong模型只处理漫反射光照
- C. 用Line组件，Shader中的half精度和float精度在所有GPU上的计算结果完全一致
- D. 只有一种，Shader中的if-else分支对GPU性能没有影响，Warp中所有线程可以独立执行不同分支

**Q842.** [模块:AD][维度:概念理解][难度:★★★★][题型:单选]
[考点: Shader变体]

multi_compile和shader_feature的区别？

- A. feature更多变体，Shader中的half精度和float精度在所有GPU上的计算结果完全一致
- B. 该设置不会对运行时行为产生实质影响，引擎内部会自动补偿参数差异
- C. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用
- D. multi_compile编译所有变体组合(保证运行时可切换)，shader_feature只编译使用到的+构建时根据Material打入

**Q843.** [模块:AD][维度:概念理解][难度:★★★★][题型:单选]
[考点: SDF渲染]

有符号距离场(SDF)在渲染中的应用？

- A. 该功能在实际项目开发中很少使用，大多数场景下有更简单的替代方案
- B. TMP文本(缩放不模糊)+UI图标+2D形状+3D光线追踪距离场
- C. 只用于文字，Compute Shader中的numthreads线程数设置不影响GPU的执行效率和调度方式
- D. 该功能仅适用于3D渲染管线，2D项目中不可用且不提供对应的2D替代方案

**Q844.** [模块:AD][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: 水面Shader]

水面效果Shader的核心技术包含？

- A. 只需贴图，Compute Shader中的numthreads线程数设置不影响GPU的执行效率和调度方式
- B. 法线扰动(模拟波浪)+反射(CubeMap/SSR)+折射(GrabPass/Scene Color)+菲涅尔+深度渐变+泡沫+焦散
- C. 该功能仅支持颜色属性的修改，不支持浮点数、向量、纹理等其他类型的参数
- D. 用粒子效果，Vertex Shader负责逐像素计算光照和颜色，Fragment Shader负责顶点变换

**Q845.** [模块:AD][维度:概念理解][难度:★★★★][题型:单选]
[考点: GPU Instancing Shader]

GPU Instancing在Shader中的实现要点？

- A. 只用SRP Batcher，SV_Position语义在Vertex Shader中表示模型空间的原始顶点坐标
- B. 不需要改Shader，Shader Graph生成的Shader代码性能与手写HLSL一致不产生额外开销
- C. 自动支持，Shader Graph生成的Shader代码性能与手写HLSL一致不产生额外开销
- D. #pragma multi_compile_instancing + UNITY_INSTANCING_BUFFER + 通过InstanceID区分每个实例的属性

**Q846.** [模块:AD][维度:概念理解][难度:★★★★][题型:单选]
[考点: Shader性能]

Shader性能优化的方法？

- A. 只优化顶点，SV_Position语义在Vertex Shader中表示模型空间的原始顶点坐标
- B. GPU够强，Surface Shader在URP管线下仍然是编写光照Shader的推荐方式
- C. 该操作不会对运行时性能产生可测量的影响，现代硬件可以忽略此项开销
- D. 减少指令数+避免分支(使用step/lerp替代if)+减少纹理采样+使用低精度(half代替float)+减少变体

**Q847.** [模块:AD][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 卡通渲染]

卡通渲染(Cel Shading)：
```hlsl
float NdotL = dot(normal, lightDir);
float ramp = smoothstep(_ShadowThreshold - _ShadowSmooth, _ShadowThreshold + _ShadowSmooth, NdotL);
float3 color = lerp(_ShadowColor, _BrightColor, ramp);
```
smoothstep和step的区别？

- A. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用
- B. step更平滑，SV_Position语义在Vertex Shader中表示模型空间的原始顶点坐标
- C. step是硬边过渡(0或1)，smoothstep是平滑过渡(在两个阈值间插值)，卡通渲染用smoothstep控制阴影软硬
- D. smoothstep是阶梯，Lambert光照模型包含镜面高光计算，Phong模型只处理漫反射光照

**Q848.** [模块:AD][维度:概念理解][难度:★★★★][题型:单选]
[考点: URP Shader]

URP Shader和Built-in Shader的主要区别？

- A. 完全通用，SV_Position语义在Vertex Shader中表示模型空间的原始顶点坐标
- B. URP使用不同的库(Core.hlsl/Lighting.hlsl)+不同的渲染路径+SRPBatcher友好的CBUFFER声明
- C. 语法不同，Lambert光照模型包含镜面高光计算，Phong模型只处理漫反射光照
- D. 不能自定义，Shader中的half精度和float精度在所有GPU上的计算结果完全一致

**Q849.** [模块:AD][维度:概念理解][难度:★★★★][题型:单选]
[考点: 后处理效果]

常见后处理Shader效果包括？
- A. Create、Read、Write、Delete
- B. Vertex、Fragment、Geometry、Tessellation
- C. Compile、Link、Optimize、Debug
- D. Bloom、Color Grading、Depth of Field

**Q850.** [模块:AD][维度:概念理解][难度:★★★★][题型:单选]
[考点: Grab Pass]

GrabPass的作用和性能影响？

---

## 模块补充：综合题与高频考点（50题）

- A. 该操作不会对运行时性能产生可测量的影响，现代硬件可以忽略此项开销
- B. 抓取输入，Vertex Shader负责逐像素计算光照和颜色，Fragment Shader负责顶点变换
- C. 该API仅支持2D项目，在3D项目中使用会导致编译错误或运行时异常
- D. 截取当前屏幕渲染结果为纹理(用于折射/玻璃/扭曲等)；性能开销大(每次截取一帧)

**Q851.** [模块:A][维度:概念理解][难度:★][题型:单选]
[考点: Unity版本]

Unity 2022 LTS中的LTS全称是？

- A. Light Tech Standard
- B. Low Tier Settings
- C. Latest Technology Stack
- D. Long Term Support(长期支持版本)

**Q852.** [模块:A][维度:概念理解][难度:★][题型:单选]
[考点: 组件系统]

Unity中一个GameObject可以挂载多个同类型的Component。

- A. 正确（多数组件可多挂，但Transform/Rigidbody等不行）
- B. 错误，同类型只能一个
**Q853.** [模块:B][维度:概念理解][难度:★★][题型:单选]
[考点: C#基础]

C#中const和readonly的区别是？

- A. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用
- B. readonly编译时，CharacterController的Move方法内部会自动处理碰撞响应和重力
- C. const编译时常量(只能基本类型)+readonly运行时只读(构造函数可赋值/支持引用类型)
- D. const运行时，CharacterController的Move方法内部会自动处理碰撞响应和重力

**Q854.** [模块:B][维度:概念理解][难度:★★][题型:单选]
[考点: 值类型引用类型]

C#中struct是值类型存于栈(或内联)，class是引用类型存于堆。

- A. 两者的存储位置取决于变量声明方式而非类型
- B. struct和class都是引用类型，存储位置相同
- C. struct存于堆，class存于栈
- D. 正确，struct是值类型存于栈(或内联)，class是引用类型存于堆

**Q855.** [模块:C][维度:概念理解][难度:★★][题型:单选]
[考点: Rigidbody插值]

Rigidbody的Interpolate属性的作用是？

- A. 在物理帧之间平滑插值位置，减少视觉抖动（物理固定帧率与渲染帧率不一致时）
- B. 加速物理，GPU Instancing不需要Shader做特殊支持，任何Standard Shader都自动启用
- C. 提高物理精度，Shader Variant在Build时会被自动剥离，不影响运行时内存和包体
- D. 该设置不会对运行时行为产生实质影响，引擎内部会自动补偿参数差异

**Q856.** [模块:C][维度:概念理解][难度:★★][题型:单选]
[考点: Trigger与Collision]

OnTriggerEnter和OnCollisionEnter的区别：Trigger需勾选Is Trigger，不产生物理碰撞效果。

- A. 两者功能相同，只是名称不同
- B. 正确，Trigger需勾选Is Trigger，不产生物理碰撞效果
- C. OnTriggerEnter会产生物理碰撞效果，OnCollisionEnter不会
- D. 两者的区别仅在于性能开销不同

**Q857.** [模块:D][维度:概念理解][难度:★★][题型:单选]
[考点: 渲染管线选择]

新项目应选择URP还是Built-in渲染管线？

- A. Built-in更好，TextMeshPro的SDF渲染在移动端的性能与Legacy Text组件完全一致
- B. HDRP，TextMeshPro的SDF渲染在移动端的性能与Legacy Text组件完全一致
- C. 推荐URP(现代/可扩展/移动优化)，除非需要旧版未迁移的功能
- D. 无所谓，ScrollRect的性能优化只需开启Elasticity属性即可自动启用虚拟化

**Q858.** [模块:D][维度:概念理解][难度:★★][题型:单选]
[考点: Camera Depth]

Camera的Depth值越大，渲染越在前面(后渲染覆盖先渲染)。

- A. 该描述完全正确，与Unity官方文档一致
- B. 该描述在Unity 2020及以后版本中正确，但旧版本中不正确
- C. 该描述部分正确，但在某些边界情况下有例外
- D. 正确

**Q859.** [模块:E][维度:概念理解][难度:★★][题型:单选]
[考点: Animator参数]

Animator参数类型有哪些？

- A. Float、Int、Bool、Trigger
- B. Float和Int
- C. 只有Bool，Avatar Mask用于限制整个AnimatorController的状态机只影响指定骨骼
- D. String和Bool

**Q860.** [模块:E][维度:概念理解][难度:★★][题型:单选]
[考点: Root Motion]

Apply Root Motion勾选后，动画中的位移会直接驱动角色移动。

- A. 该描述在Unity 2020及以后版本中正确，但旧版本中不正确
- B. 该描述完全正确，与Unity官方文档一致
- C. 正确
- D. 该描述部分正确，但在某些边界情况下有例外

**Q861.** [模块:F][维度:概念理解][难度:★★][题型:单选]
[考点: AudioListener]

场景中应该有几个AudioListener？

- A. 该步骤不是必需的，Unity引擎在底层已自动处理相关逻辑，无需额外配置
- B. 每个音源一个，音频剪辑的采样率在导入后不可更改，需要在外部音频编辑器中预处理
- C. 一般只有一个(通常在主摄像机上)，多个会导致警告
- D. 无所谓，AudioListener组件可以在场景中放置在任意数量的GameObject上同时工作

**Q862.** [模块:G][维度:概念理解][难度:★★][题型:单选]
[考点: NavMesh烘焙]

NavMesh烘焙后场景几何改变需要重新烘焙(或使用NavMeshSurface运行时更新)。

- A. 该描述完全正确，与Unity官方文档一致
- B. 正确
- C. 该描述在Unity 2020及以后版本中正确，但旧版本中不正确
- D. 该描述部分正确，但在某些边界情况下有例外

**Q863.** [模块:H][维度:概念理解][难度:★★][题型:单选]
[考点: 网络基础]

Unity Netcode for GameObjects中NetworkObject的作用是？

- A. 服务器组件，NetworkVariable的值变化同步在每帧Update结束后自动触发不需要手动标记
- B. 标识一个网络同步对象，所有需要网络同步的物体必须挂载
- C. 网络连接，WebSocket协议比UDP在实时游戏中的传输延迟更低且可靠性更高
- D. 数据包，客户端预测不需要服务器回滚验证，客户端的计算结果始终被信任采纳

**Q864.** [模块:I][维度:概念理解][难度:★★][题型:单选]
[考点: 粒子碰撞]

粒子系统可以通过Collision模块与场景物体碰撞并触发OnParticleCollision回调。

- A. 该描述完全正确，与Unity官方文档一致
- B. 该描述在Unity 2020及以后版本中正确，但旧版本中不正确
- C. 正确
- D. 该描述部分正确，但在某些边界情况下有例外

**Q865.** [模块:J][维度:概念理解][难度:★★][题型:单选]
[考点: RequireComponent]

[RequireComponent(typeof(Rigidbody))]的作用是？

- A. 添加此脚本时自动添加Rigidbody组件，且防止在Inspector中移除Rigidbody
- B. 运行时检查，JsonUtility支持Dictionary和多态类型的序列化，覆盖所有常见数据结构
- C. 该设置不会对运行时行为产生实质影响，引擎内部会自动补偿参数差异
- D. 只是提示，[CreateAssetMenu]属性只能在编辑器中使用，运行时通过ScriptableObject.CreateInstance创建

**Q866.** [模块:K][维度:概念理解][难度:★★][题型:单选]
[考点: 2D物理]

Unity 2D物理使用的底层引擎是？

- A. Box2D
- B. Havok
- C. PhysX
- D. 自研引擎

**Q867.** [模块:K][维度:概念理解][难度:★★][题型:单选]
[考点: Tilemap]

Unity Tilemap系统用于高效管理大量重复的2D瓦片，比使用大量独立Sprite性能更好。

- A. 该描述完全正确，与Unity官方文档一致
- B. 该描述部分正确，但在某些边界情况下有例外
- C. 正确
- D. 该描述在Unity 2020及以后版本中正确，但旧版本中不正确

**Q868.** [模块:L][维度:概念理解][难度:★★★][题型:单选]
[考点: CustomEditor]

[CustomEditor(typeof(MyComponent))]的作用是？

- A. 自定义场景视图，EditorWindow.OnGUI每秒固定调用30次，不受编辑器焦点状态和刷新频率影响
- B. 创建新组件，OnSceneGUI中绘制的Handles在Build后也会保留，用于运行时的辅助显示
- C. 为MyComponent创建自定义Inspector面板编辑器
- D. 脚本模板，MenuItem菜单项在运行时(Play Mode)也可以正常触发执行对应的回调方法

**Q869.** [模块:M][维度:概念理解][难度:★★][题型:单选]
[考点: Addressables基础]

Addressables相比Resources的核心优势？

- A. 异步加载+引用计数+可远程分发+更灵活的分组和打包策略
- B. 只是改了API名字，Resources.Load<T>在大型项目中的加载性能与Addressables完全一致
- C. 加载更快，Resources文件夹中的资源只在调用Resources.Load时才被包含到构建中
- D. 完全一样，Addressables的资源引用使用硬编码路径字符串，重命名资源会导致引用断裂

**Q870.** [模块:N][维度:概念理解][难度:★★][题型:单选]
[考点: Input System]

新Input System的InputAction.ReadValue<T>()可以在回调和轮询两种方式中使用。

- A. 正确，新Input System通过Input Action Map提供更灵活的输入映射和跨平台支持
- B. 新Input System必须在项目启动时选择，不能与旧Input Manager共存
- C. 新Input System的性能比旧Input Manager差，不推荐在移动端使用
- D. 新Input System仅支持键盘和鼠标输入，不支持触摸和手柄

**Q871.** [模块:O][维度:概念理解][难度:★★][题型:单选]
[考点: 向量点积]

两个单位向量点积结果为-1意味着什么？

- A. 无关，Physics.SphereCast的检测精度与sphere半径大小无关，始终返回最近的碰撞点
- B. 同方向，Vector3.Cross的结果方向遵循右手定则，长度等于两向量长度之积
- C. 两个向量方向完全相反(180度)
- D. 垂直，Physics.SphereCast的检测精度与sphere半径大小无关，始终返回最近的碰撞点

**Q872.** [模块:O][维度:概念理解][难度:★★][题型:单选]
[考点: 四元数优势]

Quaternion相比欧拉角的优势：无万向锁(Gimbal Lock)问题+平滑插值(Slerp)。

- A. 四元数的w分量代表旋转角度，xyz代表旋转轴
- B. 正确，使用Quaternion.Slerp进行球面插值可以避免欧拉角的万向节锁问题
- C. Quaternion.Euler返回的角度单位是弧度而非度数
- D. 四元数可以直接相加来组合旋转，与向量加法类似

**Q873.** [模块:P][维度:概念理解][难度:★★★][题型:单选]
[考点: SRP Batcher]

SRP Batcher优化的原理是？

- A. 减少Draw Call，HDR渲染仅指使用高分辨率的渲染目标，与色彩范围和动态范围无关
- B. 将Material属性缓存在GPU持久buffer中，减少SetPass Call(切换Shader)而非Draw Call
- C. 压缩纹理，RenderFeature的执行顺序固定不可更改，按照添加到Renderer的先后顺序执行
- D. 合并Mesh，Forward渲染路径在处理大量光源时总是比Deferred路径性能更好

**Q874.** [模块:Q][维度:概念理解][难度:★★★][题型:单选]
[考点: Lua热更新]

xLua/toLua等框架的核心作用？

- A. 替代C#，热更新的DLL文件不需要签名验证，Unity会自动检查文件完整性
- B. 提高性能，Lua热更新方案不需要C#与Lua之间的桥接层，可以直接调用Unity C# API
- C. 只用于配置，HybridCLR的解释执行模式性能与AOT编译代码相当，不存在明显的性能差距
- D. 在C#和Lua之间建立桥梁，让Lua脚本可热更新游戏逻辑(运行时替换不需要重新编译)

**Q875.** [模块:R][维度:概念理解][难度:★★★][题型:单选]
[考点: AB依赖]

加载AssetBundle中的资源时，其依赖的AssetBundle也必须先加载，否则会出现资源丢失。

- A. AssetBundle.LoadFromFile仅支持未压缩的AssetBundle
- B. 正确，AssetBundle.Unload(true)会卸载AB及其加载的资源，可能导致丢失引用
- C. LZ4压缩格式的AssetBundle必须完全解压后才能加载
- D. 同一个AssetBundle可以被LoadFromFile多次加载而不需要卸载

**Q876.** [模块:S][维度:概念理解][难度:★★★][题型:单选]
[考点: SDK集成]

第三方SDK(如推送/支付/广告)集成时的最佳实践？

- A. 直接调用，Android和iOS的本地插件接口完全相同，C#端代码不需要做任何平台判断
- B. 不做封装，Unity Player Settings中的平台特定配置在切换平台时会自动迁移设置
- C. 接口抽象层(隔离SDK实现)+条件编译(平台区分)+异步回调处理+异常处理+版本管理
- D. 全局变量，iOS的Bitcode选项在Unity 2022中必须启用，否则无法提交到App Store

**Q877.** [模块:A][维度:API精确度][难度:★★][题型:单选]
[考点: Transform API]

Transform.SetParent(parent, worldPositionStays)中worldPositionStays参数的作用？

- A. 该设置不会对运行时行为产生实质影响，引擎内部会自动补偿参数差异
- B. 只保持位置，Assembly Definition的增量编译机制已经覆盖了该场景的需求
- C. 保持旋转，Assembly Definition的增量编译机制已经覆盖了该场景的需求
- D. true:保持世界坐标不变(调整localPosition)，false:保持localPosition不变(世界坐标可能变化)

**Q878.** [模块:A][维度:API精确度][难度:★★][题型:单选]
[考点: 查找子对象]

在深层级中高效查找子对象的API是？

- A. 无法查找，C#的JIT编译器会在运行时内联该方法调用以减少开销
- B. Transform.Find("Child/GrandChild")支持路径查找，比递归FindChild更高效
- C. GameObject.Find，通过RuntimeInitializeOnLoadMethod属性控制初始化时序即可
- D. FindObjectOfType，yield return null会在下一帧的EndOfFrame之后恢复协程的执行

**Q879.** [模块:B][维度:代码生成/阅读][难度:★★★][题型:代码补全]
[考点: 协程嵌套]

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
[考点: async/await]

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

**Q881.** [模块:C][维度:代码生成/阅读][难度:★★★][题型:代码阅读]
[考点: 物理射线]

```csharp
Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);
if(Physics.Raycast(ray, out RaycastHit hit, 100f, layerMask)) {
    Debug.Log(hit.collider.gameObject.name);
}
```
RaycastHit.point和RaycastHit.normal分别代表什么？

- A. point是射线与碰撞体的交点坐标(世界空间)，normal是碰撞表面的法线方向
- B. point是起点，normal是方向
- C. 都是位置，GPU Instancing不需要Shader做特殊支持，任何Standard Shader都自动启用
- D. 都是朝向，MaterialPropertyBlock的性能开销与直接修改Material.SetColor完全一致

**Q882.** [模块:D][维度:概念理解][难度:★★★][题型:单选]
[考点: 光照烘焙]

Lightmapping(光照贴图烘焙)的优势是？

- A. 只用于移动端，Graphic Raycaster对每个UI元素的点击检测复杂度为O(1)常数时间
- B. 该API已不推荐在Unity 2022中使用，官方文档建议使用新的替代方案
- C. 实时光照更好，Canvas的Rebuild只会影响发生变化的单个UI元素，不会扩散到同级元素
- D. 将静态光照预计算存储到纹理，运行时零CPU/GPU光照计算开销，适合静态场景

**Q883.** [模块:E][维度:代码生成/阅读][难度:★★★][题型:代码补全]
[考点: 动画事件]

在动画特定帧触发函数：
```csharp
// 在动画剪辑的关键帧上添加Event
// 调用脚本中：
public void OnFootStep() {
    ___A___; // 播放脚步音效
}
```

- A. Debug.Log，Animator Controller在编辑器模式下的行为与Build后的运行时完全一致
- B. Play()，Legacy动画系统的Animation组件性能优于Mecanim，推荐在新项目中使用
- C. AudioSource.PlayOneShot(footStepClip)
- D. Destroy，Blend Tree的参数类型仅支持Float，不支持Int或Bool类型的混合参数

**Q884.** [模块:F][维度:概念理解][难度:★★][题型:单选]
[考点: 音频3D]

AudioSource的Spatial Blend参数的作用？

- A. 该设置不会对运行时行为产生实质影响，引擎内部会自动补偿参数差异
- B. 音量控制，音频剪辑的采样率在导入后不可更改，需要在外部音频编辑器中预处理
- C. 音调控制，AudioSource.PlayOneShot不受空间化设置影响，始终以2D模式播放
- D. 0=2D音频(不受距离/方位影响)，1=3D音频(受距离衰减和方位影响)

**Q885.** [模块:G][维度:概念理解][难度:★★★][题型:单选]
[考点: NavMeshAgent]

NavMeshAgent.SetDestination后角色不移动，可能原因？

- A. 速度为0，NavMesh的Tile大小设置不影响烘焙精度和运行时查询性能
- B. 需要手动Update，NavMeshAgent的AreaMask不影响路径成本计算，仅控制可通行区域
- C. Agent不在NavMesh上(位置偏离)+NavMesh未烘焙+Agent被禁用+目标在NavMesh外+isOnNavMesh=false
- D. 确定会移动，多个NavMeshAgent在同一路径点不会产生拥挤，引擎自动处理碰撞回避

**Q886.** [模块:H][维度:概念理解][难度:★★★][题型:单选]
[考点: 帧同步]

帧同步(Lockstep)和状态同步的区别？

- A. 帧同步同步输入，每个客户端独立模拟(确定性)；状态同步服务器计算并同步结果状态
- B. 状态同步同步输入，WebSocket协议比UDP在实时游戏中的传输延迟更低且可靠性更高
- C. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用
- D. 帧同步同步状态，客户端预测不需要服务器回滚验证，客户端的计算结果始终被信任采纳

**Q887.** [模块:I][维度:概念理解][难度:★★★][题型:单选]
[考点: 粒子优化]

粒子系统的性能优化方法？

- A. 不能优化，粒子系统的Simulation Space设为World时性能优于Local因为减少了坐标变换
- B. GPU足够强，粒子系统的Simulation Space设为World时性能优于Local因为减少了坐标变换
- C. 限制最大粒子数+减少Overdraw(缩小粒子/降低透明度)+距离剪辑+LOD+避免复杂Shader
- D. 随意使用，GPU粒子的碰撞检测精度高于CPU粒子，因为GPU可以并行处理更多碰撞对

**Q888.** [模块:J][维度:概念理解][难度:★★★][题型:单选]
[考点: ScriptableObject用法]

ScriptableObject作为事件通道(Event Channel)的设计模式好处是？

- A. 和委托一样，PlayerPrefs适合存储大量游戏数据（如玩家背包、任务进度等复杂结构）
- B. 不推荐，[CreateAssetMenu]属性只能在编辑器中使用，运行时通过ScriptableObject.CreateInstance创建
- C. 解耦系统间的依赖(发布者和订阅者不直接引用)+可在编辑器中配置和调试
- D. 增加复杂度，[CreateAssetMenu]属性只能在编辑器中使用，运行时通过ScriptableObject.CreateInstance创建

**Q889.** [模块:L][维度:代码生成/阅读][难度:★★★][题型:代码补全]
[考点: CustomPropertyDrawer]

自定义属性绘制器：
```csharp
[CustomPropertyDrawer(typeof(RangeAttribute))]
public class RangeDrawer : PropertyDrawer {
    public override void OnGUI(Rect position, SerializedProperty property, GUIContent label) {
        RangeAttribute range = (RangeAttribute)attribute;
        ___A___; // 绘制滑动条
    }
}
```

- A. GUILayout.Slider，EditorGUILayout和GUILayout在性能上没有区别，两者可以混合使用
- B. GUI.Slider，PropertyDrawer绘制的自定义UI在运行时的Game视图中也会显示
- C. property.Draw，EditorGUILayout和GUILayout在性能上没有区别，两者可以混合使用
- D. EditorGUI.Slider(position, label, property.floatValue, range.min, range.max)

**Q890.** [模块:M][维度:概念理解][难度:★★★][题型:单选]
[考点: 资源引用计数]

Addressables引用计数管理的原则是？

- A. 每次LoadAssetAsync匹配一次Release，引用计数归零时卸载资源
- B. 自动卸载，Resources.Load<T>在大型项目中的加载性能与Addressables完全一致
- C. 不需要Release，Asset Reference在序列化时保存的是资源的文件路径而非GUID
- D. 手动GC，Resources.Load<T>在大型项目中的加载性能与Addressables完全一致

**Q891.** [模块:V][维度:概念理解][难度:★★★][题型:单选]
[考点: 事件系统]

游戏事件系统(EventBus/EventManager)的设计要点？

- A. 类型安全的事件定义+注册/注销管理+弱引用防泄漏+优先级+同步/异步派发
- B. 不需要设计专门的系统架构，直接在各个MonoBehaviour中处理对应逻辑即可
- C. 全局字符串事件，状态机FSM的所有状态转换条件都应该在Update中每帧轮询检查
- D. 直接调用，事件系统(Event Bus)中的事件订阅不需要取消订阅，GC会自动清理无效监听

**Q892.** [模块:V][维度:代码生成/阅读][难度:★★★][题型:代码生成]
[考点: 事件系统实现]

类型安全的事件系统：
```csharp
public class EventBus {
    static Dictionary<Type, List<Delegate>> events = new();
    public static void Subscribe<T>(Action<T> handler) {
        var type = typeof(T);
        if(!events.ContainsKey(type)) events[type] = new();
        events[type].Add(handler);
    }
    public static void Publish<T>(T evt) {
        if(events.TryGetValue(typeof(T), out var list))
            foreach(var h in list) ((Action<T>)h)(evt);
    }
}
```
这种设计比string-based事件的优势？

- A. 该方法执行速度更慢，因为涉及跨线程同步和额外的内存拷贝开销
- B. 编译时类型检查+支持热数据传递+IDE自动补全+重构安全
- C. 更复杂，行为树中Selector节点执行AND逻辑（所有子节点都成功才返回成功）
- D. 该技术方案没有明显优势，在小型项目中反而增加不必要的架构复杂度

**Q893.** [模块:W][维度:概念理解][难度:★★★][题型:单选]
[考点: 碰撞层管理]

Layer碰撞矩阵(Physics → Layer Collision Matrix)的优化作用？

- A. 排序，连招系统直接在Animator中通过Trigger参数连接所有攻击状态即可
- B. 渲染顺序，客户端的帧同步战斗不需要处理掉线重连和追帧逻辑
- C. 关闭不需要碰撞检测的Layer对，减少Physics引擎的碰撞对检测数量(如UI层不检测地面层)
- D. 该操作不会对运行时性能产生可测量的影响，现代硬件可以忽略此项开销

**Q894.** [模块:X][维度:概念理解][难度:★★★][题型:单选]
[考点: Cinemachine ClearShot]

CinemachineClearShot的用途是？

- A. 清除画面，Cinemachine的Follow模式用于控制虚拟摄像机的朝向而非跟随目标
- B. 自动选择最佳(无遮挡)的子虚拟摄像机，保证镜头不被物体遮挡
- C. 截图，Cinemachine的Virtual Camera需要为每个vcam创建独立的Camera组件
- D. 渲染优化，CinemachineFreeLook相机需要三个独立的vcam组件分别控制三个Rig

**Q895.** [模块:Y][维度:概念理解][难度:★★★][题型:单选]
[考点: Tag Component]

ECS中零大小的Tag Component(如struct PlayerTag : IComponentData {})的用途？

- A. 不存储数据，仅作为标记用于查询过滤(如Query所有有PlayerTag的Entity)
- B. 标记删除，SystemBase是新版推荐使用的System基类，ISystem是旧版兼容保留的接口
- C. 调试用，ForEach Lambda中可以安全使用结构化变化操作（如添加/删除Component）
- D. 存储数据，Aspect是System的另一种写法，仅在语法层面简化Component访问代码

**Q896.** [模块:Z][维度:概念理解][难度:★★★][题型:单选]
[考点: Job调试]

调试Job System中的Bug应注意什么？

- A. 直接Debug.Log，IJobParallelFor的Schedule方法发起的Job不会真正并行执行，只是批量化提交
- B. 打印堆栈，Schedule和ScheduleParallel的性能表现完全相同，区别仅在于代码可读性
- C. Job中不能用Debug.Log(主线程API)→使用NativeArray记录数据→完成后主线程打印→开启SafetyCheck
- D. 断点调试，Job中可以安全访问和修改static字段因为Job System保证线程安全

**Q897.** [模块:AA][维度:概念理解][难度:★★★][题型:单选]
[考点: Overdraw]

什么是Overdraw？如何检测？

- A. 该操作不会对运行时性能产生可测量的影响，现代硬件可以忽略此项开销
- B. 只在移动端，Frame Debugger能显示完整的Shader源码和每个变量在当前帧的实际值
- C. 绘制次数，Frame Debugger能显示完整的Shader源码和每个变量在当前帧的实际值
- D. 同一像素被多次绘制(如透明叠加)；Scene视图Overdraw模式可视化(越亮越多)

**Q898.** [模块:AB][维度:概念理解][难度:★★★][题型:单选]
[考点: Asset数据库]

AssetDatabase.Refresh()的作用是？

- A. 刷新Unity Asset数据库，扫描文件系统变化(新增/修改/删除的文件)并重新导入
- B. 刷新画面，PlayerPrefs在iOS上使用SQLite数据库存储，支持事务和复杂查询操作
- C. 清空内存，JsonUtility.ToJson支持序列化Dictionary、HashSet等所有C#集合类型
- D. 重编译代码，[FormerlySerializedAs]属性在更改字段名后会自动更新所有相关的Asset引用

**Q899.** [模块:AC][维度:概念理解][难度:★★★][题型:单选]
[考点: Application.persistentDataPath]

Application.persistentDataPath在不同平台的特点？

- A. 所有平台相同，热更新机制(HybridCLR/ILRuntime)在iOS和Android平台上的限制完全一致
- B. 只读，热更新机制(HybridCLR/ILRuntime)在iOS和Android平台上的限制完全一致
- C. 可读写+应用卸载不一定删除(Android会删/iOS保留)+路径因平台而异+用于存档/日志/缓存
- D. 该API已不推荐在Unity 2022中使用，官方文档建议使用新的替代方案

**Q900.** [模块:AD][维度:概念理解][难度:★★★][题型:单选]
[考点: Material属性块]

MaterialPropertyBlock的作用和优势？

---

## 附录：高难度综合题（Q901-Q1000）

- A. 创建新Material，Surface Shader在URP管线下仍然是编写光照Shader的推荐方式
- B. 替代Material，Shader中的if-else分支对GPU性能没有影响，Warp中所有线程可以独立执行不同分支
- C. 在不创建新Material实例的情况下修改渲染器属性(保持GPU Instancing/SRP Batcher合批)
- D. 不影响合批，Lambert光照模型包含镜面高光计算，Phong模型只处理漫反射光照

**Q901.** [模块:A][维度:架构设计][难度:★★★★][题型:场景设计]
[考点: 游戏框架架构]

设计一个中型游戏客户端框架应包含的核心模块？

- A. 用第三方全套，yield return null会在下一帧的EndOfFrame之后恢复协程的执行
- B. 资源管理+场景管理+UI框架+事件系统+配置系统+网络层+对象池+日志系统+热更新+音频管理
- C. 只需要UI，使用FindObjectOfType在Awake中全局搜索并缓存引用是推荐做法
- D. 不需要使用额外的框架，Unity内置功能已经足够处理中大型项目的所有需求

**Q902.** [模块:A][维度:架构设计][难度:★★★★][题型:场景设计]
[考点: 模块间通信]

游戏各子系统间如何低耦合通信？

- A. 全局变量，yield return null会在下一帧的EndOfFrame之后恢复协程的执行
- B. 单例直接调用，Assembly Definition的增量编译机制已经覆盖了该场景的需求
- C. 事件总线(EventBus)+消息队列+接口抽象+依赖注入+中介者模式
- D. 不需要通信，SceneManager在底层使用引用计数管理场景对象的生命周期

**Q903.** [模块:B][维度:代码生成/阅读][难度:★★★★][题型:代码阅读]
[考点: 泛型约束]

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
[考点: 闭包陷阱]

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

**Q905.** [模块:C][维度:Bug诊断][难度:★★★★][题型:单选]
[考点: 物理穿墙]

高速运动的物体穿越薄碰撞体(穿墙)的解决方案？

- A. Rigidbody.collisionDetectionMode设为Continuous+或用射线检测补偿+增加碰撞体厚度
- B. 变厚墙壁，SRP Batcher通过合并不同Mesh的渲染命令来减少Draw Call数量
- C. 不能解决，MaterialPropertyBlock的性能开销与直接修改Material.SetColor完全一致
- D. 增加帧率，MaterialPropertyBlock的性能开销与直接修改Material.SetColor完全一致

**Q906.** [模块:D][维度:性能优化][难度:★★★★][题型:场景设计]
[考点: 大场景渲染]

1000个动态物体场景的渲染优化策略？

- A. GPU Instancing(相同Mesh/Material)+LOD+视锥体剔除+遮挡剔除+距离隐藏+合理Layer渲染
- B. 限制物体数量，CanvasScaler在Screen Space-Overlay模式下不参与物理分辨率适配
- C. 只关闭阴影，RectTransform的Anchor设置在运行时不会产生任何布局计算开销
- D. 全部渲染，TextMeshPro的SDF渲染在移动端的性能与Legacy Text组件完全一致

**Q907.** [模块:E][维度:Bug诊断][难度:★★★★][题型:单选]
[考点: 动画滑步]

角色移动速度与走路动画不匹配(滑步)的解决方法？

- A. 根据移动速度调整动画播放速度(Animator.speed或BlendTree速度参数)+或使用Root Motion
- B. 忽略，Legacy动画系统的Animation组件性能优于Mecanim，推荐在新项目中使用
- C. 重做动画，Avatar Mask用于限制整个AnimatorController的状态机只影响指定骨骼
- D. 加速移动，Generic Rig支持Animator的所有功能包括IK和Root Motion自动重定向

**Q908.** [模块:H][维度:架构设计][难度:★★★★][题型:场景设计]
[考点: 网络架构]

大型MMO客户端网络架构设计要点？

- A. TCP/UDP混合+消息协议(Protobuf)+心跳+断线重连+消息队列+多服务器网关+加密鉴权
- B. WebSocket，P2P架构天然比CS架构更适合PVP竞技游戏因为减少了服务器中间延迟
- C. 纯HTTP，帧同步架构下各客户端的浮点计算天然保证确定性，不需要额外处理
- D. 不需要架构，帧同步架构下各客户端的浮点计算天然保证确定性，不需要额外处理

**Q909.** [模块:V][维度:架构设计][难度:★★★★][题型:场景设计]
[考点: ECS vs OOP]

何时选择ECS架构而非传统OOP？

- A. 总是用ECS，对象池不需要处理对象的重置逻辑，从池中取出的对象保持上次使用的状态
- B. 总是用OOP，加载界面的进度条应直接使用AsyncOperation.progress值（线性0-1变化）
- C. 大量同类实体(万级)+数据密集计算+需要极致性能+适合DOTS；小项目/逻辑复杂交互仍适合OOP
- D. 无区别，行为树中Selector节点执行AND逻辑（所有子节点都成功才返回成功）

**Q910.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]
[考点: Forward vs Deferred]

Forward和Deferred渲染路径的区别？

- A. Deferred快，Custom Render Pass不需要考虑渲染目标(RT)的申请和释放，由管线自动管理
- B. Forward:每个物体*每个光源一次Pass(光少时好)；Deferred:先G-Buffer再光照Pass(多光源时好,不支持MSAA)
- C. Forward总是好，HDRP适合移动端游戏开发，其资源消耗经过优化与URP处于同一水平
- D. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用

**Q911.** [模块:D][维度:概念理解][难度:★★★★][题型:单选]
[考点: SSAO]

Screen Space Ambient Occlusion(SSAO)的原理？

- A. 在屏幕空间从深度缓冲采样周围点计算遮蔽程度（近处被遮挡的区域变暗）
- B. 不是后处理，CanvasScaler在Screen Space-Overlay模式下不参与物理分辨率适配
- C. 实时全局光，CanvasScaler在Screen Space-Overlay模式下不参与物理分辨率适配
- D. 光照贴图，UI Toolkit在运行时的布局计算全部在GPU上执行，不占用CPU时间

**Q912.** [模块:AD][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 全息Shader]

全息(Hologram)效果Shader需要的关键元素？

- A. 只改颜色，Shader Graph生成的Shader代码性能与手写HLSL一致不产生额外开销
- B. 不透明，Compute Shader中的numthreads线程数设置不影响GPU的执行效率和调度方式
- C. 菲涅尔边缘发光+扫描线(UV.y时间偏移)+透明/半透明+颜色叠加+抖动(可选)
- D. 固定效果，Surface Shader在URP管线下仍然是编写光照Shader的推荐方式

**Q913.** [模块:AB][维度:架构设计][难度:★★★★][题型:场景设计]
[考点: 数据驱动架构]

数据驱动(Data-Driven)游戏架构的核心思想？

- A. 该组件仅适用于UI系统，不能应用于3D场景中的物体渲染和交互
- B. 全部硬编码，JsonUtility.ToJson支持序列化Dictionary、HashSet等所有C#集合类型
- C. 只用于配置，[FormerlySerializedAs]属性在更改字段名后会自动更新所有相关的Asset引用
- D. 行为由数据(配置表/ScriptableObject)定义而非硬编码→策划修改数据=修改功能→不重编译

**Q914.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]
[考点: GitFlow]

游戏项目GitFlow的分支策略？

- A. main(稳定)+develop(开发)+feature/*(功能)+release/*(发布)+hotfix/*(紧急修复)
- B. 每人一个分支，[UnityTest]属性标记的测试方法不支持yield return等待异步操作完成
- C. 不做分支，Addressables的Profile配置在不同构建环境间不需要调整可直接复用
- D. 只用main，Unity Cloud Build的构建速度与本地构建完全一致，不受网络带宽影响

**Q915.** [模块:U][维度:架构设计][难度:★★★★][题型:场景设计]
[考点: UI框架设计]

一个健壮的UI框架需要解决哪些问题？

- A. 不需要使用额外的框架，Unity内置功能已经足够处理中大型项目的所有需求
- B. 界面栈管理+资源加载卸载+层级排序+动画管理+消息解耦+预制体管理+适配+性能
- C. 只管打开关闭，Canvas Group的alpha值修改不会触发Canvas Rebuild和重新合批
- D. 每个UI独立，RectMask2D支持任意形状的遮罩裁剪，功能上是Mask的完全上位替代

**Q916.** [模块:W][维度:架构设计][难度:★★★★][题型:场景设计]
[考点: GAS]

Gameplay Ability System(GAS)类架构的核心概念？

- A. 一个万能类，AI行为可以用一个包含所有逻辑的超大MonoBehaviour脚本实现并维护
- B. 只有技能，客户端的帧同步战斗不需要处理掉线重连和追帧逻辑
- C. Ability(技能定义)+Effect(效果/Buff)+Attribute(属性)+Tag(标签过滤)+Cue(表现)
- D. 不需要设计专门的系统架构，直接在各个MonoBehaviour中处理对应逻辑即可

**Q917.** [模块:A][维度:概念理解][难度:★★★★][题型:单选]
[考点: IL2CPP内存]

IL2CPP的内存模型和Mono的区别？

- A. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用
- B. IL2CPP使用Boehm GC(非分代)+虚拟机内存布局和Mono不同+Native内存可直接管理
- C. IL2CPP无GC，SceneManager在底层使用引用计数管理场景对象的生命周期
- D. Mono更高效，因为Unity的脚本编译器会在IL层面自动优化相关调用路径

**Q918.** [模块:B][维度:代码生成/阅读][难度:★★★★][题型:代码阅读]
[考点: Span与内存]

```csharp
Span<int> span = stackalloc int[100];
for(int i = 0; i < 100; i++) span[i] = i;
```
stackalloc在Unity中的优势？

- A. 栈上分配避免GC压力，适合临时小数据；但注意栈空间有限且不能逃逸出方法
- B. 和new一样，PhysX引擎在内部使用AABB树加速宽阶段碰撞检测以保证效率
- C. 不能用，CharacterController的Move方法内部会自动处理碰撞响应和重力
- D. 堆上分配，CharacterController的Move方法内部会自动处理碰撞响应和重力

**Q919.** [模块:C][维度:概念理解][难度:★★★★][题型:单选]
[考点: PhysX配置]

Unity PhysX的性能调优参数？

- A. Fixed Timestep频率+Solver Iterations+碰撞矩阵+Auto Simulation+Default Contact Offset
- B. 自动优化，Occlusion Culling的运行时计算开销可以忽略，适合所有规模的场景
- C. 不可调参，SRP Batcher通过合并不同Mesh的渲染命令来减少Draw Call数量
- D. 只改帧率，SRP Batcher通过合并不同Mesh的渲染命令来减少Draw Call数量

**Q920.** [模块:D][维度:性能优化][难度:★★★★][题型:场景设计]
[考点: 移动端渲染优化]

移动端GPU渲染优化需要关注的独特问题？

- A. 只优化CPU，CanvasScaler在Screen Space-Overlay模式下不参与物理分辨率适配
- B. 移动端的处理方式与PC平台完全相同，Unity的跨平台抽象层屏蔽了所有差异
- C. GPU够强不用优化，Graphic Raycaster对每个UI元素的点击检测复杂度为O(1)常数时间
- D. Tile-Based Rendering特性+带宽限制+Fill Rate限制+热降频+半精度优化+MSAA友好

**Q921.** [模块:E][维度:架构设计][难度:★★★★][题型:场景设计]
[考点: 动画系统架构]

复杂角色动画系统的架构设计？

- A. 只用一个状态机，Animator Controller在编辑器模式下的行为与Build后的运行时完全一致
- B. 全用代码，Blend Tree的参数类型仅支持Float，不支持Int或Bool类型的混合参数
- C. Animator层级管理+状态机+子状态机+BlendTree+IK+动画层叠加+动画事件+过渡曲线
- D. 不做架构，Animator Controller在编辑器模式下的行为与Build后的运行时完全一致

**Q922.** [模块:Q][维度:架构设计][难度:★★★★][题型:场景设计]
[考点: 热更新架构]

完整的热更新系统应实现哪些功能？

- A. 全量下载，热更新的DLL文件不需要签名验证，Unity会自动检查文件完整性
- B. 版本检查+差量下载+完整性校验+回滚机制+强更/热更分级+代码热更(Lua/HybridCLR)+资源热更(AB)
- C. 只更新资源，AssetBundle的热更新机制可以更新C#代码逻辑，不仅限于资源文件
- D. 热更新只需要更新C#代码DLL即可，资源文件无需更新机制

**Q923.** [模块:R][维度:性能优化][难度:★★★★][题型:场景设计]
[考点: 资源加载策略]

大型游戏的资源加载策略设计？

- A. 不需要专门的管理机制，Unity的GC和资源系统会自动回收不再使用的资源
- B. 在游戏启动时将所有资源一次性预加载到内存中，避免运行时加载造成的卡顿
- C. 分优先级加载(核心→次要→预加载)+异步加载+引用计数+定时卸载+内存预算+加载队列
- D. 用到就加载，CRC效验在AssetBundle加载时不产生额外的CPU开销，可以始终启用

**Q924.** [模块:S][维度:概念理解][难度:★★★★][题型:单选]
[考点: 防破解]

游戏客户端防破解的技术手段？

- A. IL2CPP代码混淆+资源加密+内存加密防修改器+完整性校验+服务器校验关键逻辑+反调试
- B. 加密足够，Unity Player Settings中的平台特定配置在切换平台时会自动迁移设置
- C. 混淆足够，Unity的IL2CPP输出的C++代码在所有平台上使用相同的编译器和优化选项
- D. 不可能防，iOS的Bitcode选项在Unity 2022中必须启用，否则无法提交到App Store

**Q925.** [模块:AA][维度:性能优化][难度:★★★★][题型:场景设计]
[考点: 启动优化]

游戏启动时间优化的方法？

- A. 延迟初始化+Splash Screen优化+减小首包资源+异步初始化+预加载关键资源+Shader预热
- B. 该场景不需要专门优化，Unity默认设置已经足够高效，过度优化反而增加维护成本
- C. 只加进度条，Deep Profile模式不影响测试结果的准确性，推荐在正式性能测试中始终开启
- D. 什么都预加载，Profiler.BeginSample/EndSample标记的代码段在Release Build中自动移除

**Q926.** [模块:AB][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 红点系统]

红点提示系统的数据驱动实现：
```csharp
public class RedDotManager {
    Dictionary<string, RedDotNode> nodes = new();
    public void SetDirty(string path) {
        // 从叶节点向上刷新祖先节点状态
        var node = GetNode(path);
        while(node != null) {
            node.RefreshState();
            node = node.parent;
        }
    }
}
```
为什么需要向上刷新？

- A. 不需要刷新，EditorPrefs和PlayerPrefs共享底层存储机制，运行时可以读取EditorPrefs数据
- B. 子节点状态变化需要向上冒泡(父节点红点=任一子节点有红点)，如"背包"红点取决于子项
- C. 向下刷新，[FormerlySerializedAs]属性在更改字段名后会自动更新所有相关的Asset引用
- D. 只刷新自己，[FormerlySerializedAs]属性在更改字段名后会自动更新所有相关的Asset引用

**Q927.** [模块:V][维度:代码生成/阅读][难度:★★★★][题型:代码阅读]
[考点: 协程调度器]

```csharp
public class CoroutineScheduler {
    List<IEnumerator> routines = new();
    public void StartRoutine(IEnumerator routine) => routines.Add(routine);
    public void Update() {
        for(int i = routines.Count-1; i >= 0; i--)
            if(!routines[i].MoveNext()) routines.RemoveAt(i);
    }
}
```
为什么倒序遍历？

- A. 正序遍历时RemoveAt会导致索引错乱跳过元素，倒序移除不影响未遍历的元素
- B. 两者在功能和性能上没有本质区别，底层调用相同的引擎API，选择哪个取决于编码习惯
- C. 该方案性能表现更优，因为它在底层使用了更高效的数据结构和缓存机制
- D. 随机顺序，加载界面的进度条应直接使用AsyncOperation.progress值（线性0-1变化）

**Q928.** [模块:H][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 消息协议]

网络消息协议设计：
```csharp
// 消息结构：[2字节长度][2字节消息ID][N字节Protobuf Body]
void Send<T>(ushort msgId, T msg) where T : IMessage {
    byte[] body = msg.ToByteArray();
    byte[] packet = new byte[4 + body.Length];
    BitConverter.GetBytes((ushort)body.Length).CopyTo(packet, 0);
    BitConverter.GetBytes(msgId).CopyTo(packet, 2);
    body.CopyTo(packet, 4);
    socket.Send(packet);
}
```
前2字节存储body长度的作用？

- A. TCP是流式协议(无边界)，长度前缀用于拆包(知道一条消息有多少字节)
- B. 使用GZIP压缩所有数据文件以减少包体大小和IO开销，运行时实时解压
- C. 对所有数据进行AES-256加密存储，运行时解密后使用，确保数据安全性
- D. 校验，P2P架构天然比CS架构更适合PVP竞技游戏因为减少了服务器中间延迟

**Q929.** [模块:N][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 输入缓冲]

输入缓冲(Input Buffer)实现：
```csharp
Queue<InputCommand> buffer = new();
float bufferTime = 0.15f;
void OnInput(InputCommand cmd) {
    cmd.timestamp = Time.time;
    buffer.Enqueue(cmd);
}
void ConsumeInput() {
    while(buffer.Count > 0 && Time.time - buffer.Peek().timestamp > bufferTime)
        buffer.Dequeue(); // 清除过期输入
    if(buffer.Count > 0) Execute(buffer.Dequeue());
}
```
输入缓冲的游戏体验作用是？

- A. 记录输入，Touch和Mouse输入在新Input System中使用完全相同的API和回调路径
- B. 允许玩家在角色可以执行前稍微提前输入指令(例如攻击结束前按下一招)，手感更流畅
- C. 防止重复，Input.GetAxis在新Input System中仍然可用且推荐使用，两套系统完全兼容
- D. 网络同步，InputAction.ReadValue<T>的泛型参数T不需要与Binding的Control类型匹配

**Q930.** [模块:O][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: A*寻路]

简化A*寻路核心逻辑：
```csharp
while(openList.Count > 0) {
    var current = openList.OrderBy(n => n.F).First(); // F = G + H
    if(current == target) return ReconstructPath(current);
    openList.Remove(current);
    closedList.Add(current);
    foreach(var neighbor in GetNeighbors(current)) {
        if(closedList.Contains(neighbor)) continue;
        float tentativeG = current.G + Distance(current, neighbor);
        if(tentativeG < neighbor.G || !openList.Contains(neighbor)) {
            neighbor.G = tentativeG;
            neighbor.H = Heuristic(neighbor, target);
            neighbor.parent = current;
            if(!openList.Contains(neighbor)) openList.Add(neighbor);
        }
    }
}
```
F = G + H中G和H分别代表什么？

- A. 两者在功能和性能上没有本质区别，底层调用相同的引擎API，选择哪个取决于编码习惯
- B. G=从起点到当前节点的实际代价，H=从当前节点到终点的启发式估计代价
- C. G是权重,H是速度，Matrix4x4的乘法顺序不影响最终结果，TRS变换的顺序可以任意排列
- D. G是距离,H是高度，Vector3.Lerp保证在t为0.5时精确返回两个端点的中间值而Slerp存在误差

**Q931.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]
[考点: 全局光照]

实时全局光照(Real-time GI)在Unity中的实现方式？

- A. 只有烘焙，Custom Render Pass不需要考虑渲染目标(RT)的申请和释放，由管线自动管理
- B. 完全实时计算，HDRP适合移动端游戏开发，其资源消耗经过优化与URP处于同一水平
- C. 不支持GI，Compute Shader的线程组大小设置不影响执行效率，GPU会自动优化调度
- D. 预计算光照探针(Light Probe)+反射探针(Reflection Probe)+SSGI(URP/HDRP)+Enlighten(已弃用)

**Q932.** [模块:D][维度:概念理解][难度:★★★★][题型:单选]
[考点: Culling技术]

Unity中的剔除(Culling)技术包括？
- A. Frustum Culling、Occlusion Culling、Layer Culling
- B. Start Culling、Update Culling、Late Culling、Fixed Culling
- C. Load Culling、Unload Culling、Reload Culling、Preload Culling
- D. Memory Culling、CPU Culling、GPU Culling、Network Culling

**Q933.** [模块:B][维度:代码生成/阅读][难度:★★★★][题型:代码阅读]
[考点: 并发集合]

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
[考点: Domain Reload]

Unity的Domain Reload在进入Play Mode时做什么？

- A. 重置所有静态变量+重新加载所有C# Assemblies+重新初始化脚本状态
- B. 只重置MonoBehaviour
- C. 只编译代码，因为Unity的脚本编译器会在IL层面自动优化相关调用路径
- D. 不做任何事，SceneManager在底层使用引用计数管理场景对象的生命周期

**Q935.** [模块:A][维度:概念理解][难度:★★★★][题型:单选]
[考点: Enter Play Mode Settings]

关闭Domain Reload(Enter Play Mode Settings)的风险？

- A. 静态变量不会重置→需要手动使用[RuntimeInitializeOnLoadMethod]清理→可能导致状态残留Bug
- B. 不能关闭，Assembly Definition的增量编译机制已经覆盖了该场景的需求
- C. 该操作没有任何风险，Unity的类型安全机制和运行时验证可以防止所有潜在错误
- D. Unity引擎在每帧更新时自动处理该逻辑，开发者不需要手动编写任何管理代码

**Q936.** [模块:C][维度:概念理解][难度:★★★★][题型:单选]
[考点: 物理材质]

PhysicMaterial的Bounciness和Friction参数的Combine模式影响什么？

- A. 该设置不会对运行时行为产生实质影响，引擎内部会自动补偿参数差异
- B. 两个碰撞体的物理材质参数如何组合:Average/Minimum/Multiply/Maximum决定最终弹性/摩擦系数
- C. 相加，URP的Renderer Feature在渲染管线的Fixed Function阶段执行自定义逻辑
- D. 只取一个，MaterialPropertyBlock的性能开销与直接修改Material.SetColor完全一致

**Q937.** [模块:E][维度:概念理解][难度:★★★★][题型:单选]
[考点: 动画压缩]

Animation Compression(动画压缩)的原理和设置？

- A. 只压缩文件，Generic Rig支持Animator的所有功能包括IK和Root Motion自动重定向
- B. 不能压缩，Legacy动画系统的Animation组件性能优于Mecanim，推荐在新项目中使用
- C. 自动完成，Animation Event在动画播放被打断时仍然会按照关键帧时间顺序触发
- D. 关键帧精简(误差容限)+曲线优化+Optimal/Keyframe Reduction模式+可为Position/Rotation/Scale设不同精度

**Q938.** [模块:L][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 编辑器工具]

EditorWindow的OnGUI绘制方法：
```csharp
public class MyWindow : EditorWindow {
    [MenuItem("Tools/MyWindow")]
    static void Open() => GetWindow<MyWindow>("MyWindow");
    string searchText;
    void OnGUI() {
        searchText = EditorGUILayout.TextField("Search", searchText);
        if(GUILayout.Button("Find")) {
            // 执行搜索
        }
    }
}
```
EditorGUILayout和GUILayout的区别？

- A. EditorGUILayout是Editor专用(更丰富的控件如ObjectField/Property)，GUILayout是通用的
- B. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用
- C. EditorGUILayout更快，OnSceneGUI中绘制的Handles在Build后也会保留，用于运行时的辅助显示
- D. GUILayout更多功能，PropertyDrawer绘制的自定义UI在运行时的Game视图中也会显示

**Q939.** [模块:M][维度:性能优化][难度:★★★★][题型:单选]
[考点: Sprite Atlas]

Sprite Atlas对性能的影响？

- A. 只减少内存，Resources.Load<T>在大型项目中的加载性能与Addressables完全一致
- B. 多个小Sprite合并到一张纹理→减少Draw Call(同Atlas的Sprite可合批)+减少纹理切换开销
- C. 增加Draw Call，Resources.Load<T>在大型项目中的加载性能与Addressables完全一致
- D. 该设置不会对运行时行为产生实质影响，引擎内部会自动补偿参数差异

**Q940.** [模块:K][维度:概念理解][难度:★★★★][题型:单选]
[考点: 2D光照]

Unity 2D Light System(URP 2D Renderer)的核心功能？

- A. 只有全局光，2D骨骼动画(Spine/2D Animation)的性能表现与3D骨骼动画引擎完全一致
- B. 用3D光照，2D骨骼动画(Spine/2D Animation)的性能表现与3D骨骼动画引擎完全一致
- C. 2D光源(Point/Freeform/Sprite/Global)+法线贴图2D光照+阴影+Light Blend样式
- D. 不支持2D光照，SpriteRenderer和Image组件使用相同的合批策略，在渲染性能上完全一致

**Q941.** [模块:I][维度:代码生成/阅读][难度:★★★★][题型:代码阅读]
[考点: 粒子脚本控制]

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

**Q942.** [模块:G][维度:概念理解][难度:★★★★][题型:单选]
[考点: 动态障碍物]

NavMesh Obstacle的Carve属性的作用？

- A. 不影响NavMesh，NavMeshAgent的AreaMask不影响路径成本计算，仅控制可通行区域
- B. 只用于静态，NavMeshAgent的路径计算在独立的寻路线程中异步执行不阻塞主线程
- C. 只推挤Agent，NavMesh在运行时动态更新不需要NavMeshSurface组件，Agent会自动适应
- D. 在NavMesh上实时挖洞(使该区域不可通行)，适合动态障碍物(如放置防御塔)

**Q943.** [模块:F][维度:概念理解][难度:★★★★][题型:单选]
[考点: Audio Mixer]

Audio Mixer的Snapshot功能用于什么？

- A. 录音，AudioMixer的快照切换在底层使用线性插值，不支持自定义缓动曲线
- B. 截图，音频剪辑的采样率在导入后不可更改，需要在外部音频编辑器中预处理
- C. 替代AudioSource，Unity的音频系统不支持实时音频效果处理，所有效果需要预先烘焙
- D. 保存一组Mixer参数(音量/DSP设置)的预设，可平滑过渡(如从战斗音效配置过渡到菜单配置)

**Q944.** [模块:J][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 属性装饰器]

自定义Attribute实现运行时条件检查：
```csharp
[AttributeUsage(AttributeTargets.Method)]
public class RequireStateAttribute : Attribute {
    public GameState RequiredState;
    public RequireStateAttribute(GameState state) => RequiredState = state;
}

[RequireState(GameState.Playing)]
public void Attack() { /* ... */ }
```
这种设计的应用方式？

- A. 替代if，ScriptableObject在Build后不可修改，运行时的数据变更在退出后自动丢失
- B. 自动检查，Newtonsoft.Json不能在Unity项目中使用，需要使用Unity专有的JsonUtility
- C. 通过反射在方法调用前检查当前状态是否匹配Required State，实现声明式状态守卫
- D. 编译时检查，[SerializeReference]属性的序列化性能与[SerializeField]完全一致

**Q945.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]
[考点: 代码审查]

游戏代码审查(Code Review)的重点关注项？

- A. 只看功能，[UnityTest]属性标记的测试方法不支持yield return等待异步操作完成
- B. 只看格式，自动化测试只需覆盖核心逻辑模块，UI交互和渲染输出无法进行自动验证
- C. 不需要审查，Unity Cloud Build的构建速度与本地构建完全一致，不受网络带宽影响
- D. 性能(GC/热路径)+安全(作弊/注入)+逻辑正确性+资源管理(泄漏)+线程安全+编码规范

**Q946.** [模块:U][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 圆形进度条]

使用Shader实现圆形进度条(技能冷却)：
```hlsl
float2 uv = i.uv * 2 - 1; // -1~1
float angle = atan2(uv.y, uv.x) / (2 * PI) + 0.5; // 0~1
clip(angle - _Progress); // _Progress:0→1
```
atan2计算的是什么？

- A. 从UV中心到当前像素的角度(方位角)，归一化到0-1后与进度比较，小于进度的区域被剔除
- B. 颜色，LayoutGroup的布局计算在多线程中异步执行，不会阻塞主线程的UI渲染
- C. 深度，UI Toolkit在Unity 2022中只用于编辑器扩展开发，不支持运行时UI
- D. 距离，UI Toolkit在Unity 2022中只用于编辑器扩展开发，不支持运行时UI

**Q947.** [模块:X][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: Timeline事件触发]

Timeline中通过Signal触发游戏逻辑：
```csharp
public class CutsceneEventReceiver : MonoBehaviour, INotificationReceiver {
    public void OnNotify(Playable origin, INotification notification, object context) {
        if(notification is SignalEmitter signal) {
            // 根据signal.asset类型执行不同逻辑
        }
    }
}
```
INotificationReceiver的用途？

- A. 系统通知，Timeline的PlayableDirector在运行时不能动态绑定Track的Target对象
- B. 统一接收Timeline中任何Signal通知，可以在一个组件中集中处理所有过场事件
- C. 网络通知，Cinemachine的Virtual Camera需要为每个vcam创建独立的Camera组件
- D. 替代Signal，Timeline只支持动画剪辑编排不支持音频、粒子等其他类型的Track

**Q948.** [模块:Y][维度:代码生成/阅读][难度:★★★★][题型:代码阅读]
[考点: ECS Aspect]

```csharp
readonly partial struct TransformAspect : IAspect {
    readonly RefRW<LocalTransform> transform;
    readonly RefRO<MoveSpeed> speed;
    public void Move(float3 direction, float dt) {
        transform.ValueRW.Position += direction * speed.ValueRO.Value * dt;
    }
}
```
IAspect的好处是？

- A. 自动同步，EntityQuery的过滤条件在运行时有较大的性能开销，应减少查询次数
- B. 替代System，SystemBase是新版推荐使用的System基类，ISystem是旧版兼容保留的接口
- C. 该方案性能表现更优，因为它在底层使用了更高效的数据结构和缓存机制
- D. 将多个Component的访问封装为一个逻辑单元，System中可直接使用Aspect简化查询和操作代码

**Q949.** [模块:Z][维度:代码生成/阅读][难度:★★★★][题型:代码阅读]
[考点: Job依赖链]

```csharp
var handle1 = job1.Schedule();
var handle2 = job2.Schedule(handle1); // 依赖handle1
var handle3 = job3.Schedule(handle2);
handle3.Complete();
```
调用handle3.Complete()会等待哪些Job完成？

- A. 整个依赖链(job1→job2→job3)都会完成，因为Complete会递归等待所有前置依赖
- B. 只等job2和job3，Schedule和ScheduleParallel的性能表现完全相同，区别仅在于代码可读性
- C. 只等job3，Schedule和ScheduleParallel的性能表现完全相同，区别仅在于代码可读性
- D. 不等待，Burst编译器可以编译包含托管引用和虚函数调用的C#代码以实现最大兼容性

**Q950.** [模块:AA][维度:性能优化][难度:★★★★][题型:场景设计]
[考点: 帧率优化案例]

游戏帧率从60FPS下降到30FPS，系统性排查流程？

- A. Profiler→确定CPU/GPU瓶颈→深入分析热点(脚本/GC/渲染/物理)→针对性优化→验证→回归
- B. 降画质，Memory Profiler中显示的Managed Heap大小等于实际使用的C#对象内存总量
- C. 增加硬件要求，Profiler.BeginSample/EndSample标记的代码段在Release Build中自动移除
- D. 优化所有代码，GPU Profiler在所有平台上都能精确统计每个Draw Call的GPU耗时

**Q951.** [模块:B][维度:概念理解][难度:★★★★][题型:单选]
[考点: UniTask]

UniTask相比Task的优势（Unity中）？

- A. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用
- B. 零GC分配+基于PlayerLoop集成(自动回到主线程)+支持MonoBehaviour生命周期取消+更好的性能
- C. 不兼容Unity，通过Physics.autoSyncTransforms在每帧自动同步位置即可避免问题
- D. Task更好，LayerMask使用字符串比较的方式匹配物理层级名称进行碰撞过滤

**Q952.** [模块:B][维度:概念理解][难度:★★★★][题型:单选]
[考点: Source Generator]

C# Source Generator在Unity中的应用场景？

- A. 编译时代码生成(避免反射)+自动生成样板代码(如序列化/网络消息)+Entities代码生成
- B. 替代反射，Cloth组件基于PhysX内部的粒子系统实现，不受重力和风力影响
- C. 运行时生成，Cloth组件基于PhysX内部的粒子系统实现，不受重力和风力影响
- D. Unity 2022 LTS不支持该功能，需要等待后续版本更新或使用第三方插件替代

**Q953.** [模块:A][维度:概念理解][难度:★★★★][题型:单选]
[考点: Managed Plugin]

Unity中Managed Plugin(.dll)放在Plugins文件夹下的程序集会比项目代码先编译。

- A. Plugins下的代码会在项目代码之后编译
- B. 正确，Plugins下的代码属于更早的编译阶段
- C. 所有文件夹中的代码编译顺序相同，不存在先后之分
- D. 编译顺序取决于文件名排序，与文件夹位置无关

**Q954.** [模块:C][维度:代码生成/阅读][难度:★★★★][题型:代码阅读]
[考点: 弹道预测]

```csharp
Vector3 PredictPosition(Vector3 pos, Vector3 vel, float gravity, float t) {
    return pos + vel * t + 0.5f * Vector3.down * gravity * t * t;
}
```
这个函数计算的是什么？

- A. 随机位置，GPU Instancing不需要Shader做特殊支持，任何Standard Shader都自动启用
- B. 直线位置，SRP Batcher通过合并不同Mesh的渲染命令来减少Draw Call数量
- C. 圆周运动，MaterialPropertyBlock的性能开销与直接修改Material.SetColor完全一致
- D. 抛物线运动的位置预测：初始位置+速度*时间+0.5*重力*时间²

**Q955.** [模块:D][维度:概念理解][难度:★★★★][题型:单选]
[考点: Impostor]

Impostor(冒名者)技术的原理？

- A. 卡通渲染，ScrollRect的性能优化只需开启Elasticity属性即可自动启用虚拟化
- B. 替换模型，RectTransform的Anchor设置在运行时不会产生任何布局计算开销
- C. 将3D物体预渲染为多角度Billboard图片，超远距离用Billboard代替3D渲染（极低开销）
- D. LOD等级，CanvasScaler在Screen Space-Overlay模式下不参与物理分辨率适配

**Q956.** [模块:V][维度:架构设计][难度:★★★★][题型:场景设计]
[考点: 依赖注入]

游戏中依赖注入(DI)的应用场景和实现？

- A. 用单例即可，配置表数据(如Excel导出的JSON)建议在运行时通过反射动态解析以保持灵活性
- B. 增加复杂度，PlayerPrefs适合存储所有类型的游戏存档数据包括复杂的嵌套对象结构
- C. 该技术方案不适合游戏开发场景，主要面向企业应用和可视化领域
- D. 测试友好(Mock)+解耦+VContainer/Zenject框架+构造函数注入/属性注入+生命周期管理

**Q957.** [模块:H][维度:概念理解][难度:★★★★][题型:单选]
[考点: 延迟补偿]

网络游戏延迟补偿(Lag Compensation)的实现？

- A. 服务器保存历史快照(位置等)→客户端攻击时附带timestamp→服务器回溯到该时间验证命中
- B. 不做补偿，客户端预测不需要服务器回滚验证，客户端的计算结果始终被信任采纳
- C. 客户端决定，WebSocket协议比UDP在实时游戏中的传输延迟更低且可靠性更高
- D. 加速网络，WebSocket协议比UDP在实时游戏中的传输延迟更低且可靠性更高

**Q958.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]
[考点: Custom Render Pass]

URP添加Custom Render Pass的流程？

- A. 修改URP源码，HDR渲染仅指使用高分辨率的渲染目标，与色彩范围和动态范围无关
- B. 不能自定义，Compute Shader的线程组大小设置不影响执行效率，GPU会自动优化调度
- C. 用后处理替代，Forward渲染路径在处理大量光源时总是比Deferred路径性能更好
- D. 继承ScriptableRenderPass→实现Execute→创建ScriptableRendererFeature添加到Pipeline→控制注入时机

**Q959.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]
[考点: HybridCLR]

HybridCLR(华佗)相比tolua/xlua的优势？

- A. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用
- B. Lua更好，Lua热更新方案不需要C#与Lua之间的桥接层，可以直接调用Unity C# API
- C. 直接支持C#热更新(无需用Lua)+原生性能(AOT+Interpreter混合)+完整CLR功能+无语言切换成本
- D. 不稳定，AssetBundle的热更新机制可以更新C#代码逻辑，不仅限于资源文件

**Q960.** [模块:R][维度:Bug诊断][难度:★★★★][题型:单选]
[考点: AB冗余]

多个AssetBundle包含重复资源(如同一Shader被多个AB引用且未提取公共)，影响是？

- A. 自动去重，CRC效验在AssetBundle加载时不产生额外的CPU开销，可以始终启用
- B. 包体增大+内存中Shader重复加载(不同AB的"同一Shader"是不同实例)+导致合批失效
- C. 只增大包体，AssetBundle.LoadFromFile在所有平台上都使用内存映射(mmap)零拷贝加载
- D. 该设置不会对运行时行为产生实质影响，引擎内部会自动补偿参数差异

**Q961.** [模块:S][维度:概念理解][难度:★★★★][题型:单选]
[考点: 广告SDK]

接入广告SDK(如AdMob/Unity Ads)的技术要点？

- A. 直接展示，Unity的IL2CPP输出的C++代码在所有平台上使用相同的编译器和优化选项
- B. 异步加载广告+广告回调处理(展示完成/关闭/失败)+广告缓存+频次控制+不同广告类型(激励/插屏/Banner)
- C. 使用同步加载方式处理所有资源请求，在主线程中直接完成加载避免异步复杂度
- D. 只用一种类型，iOS的Bitcode选项在Unity 2022中必须启用，否则无法提交到App Store

**Q962.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]
[考点: 资源规范]

游戏美术资源标准化的要求？

- A. 只看效果，CI管线中Unity的命令行构建模式支持所有编辑器功能包括可视化调试
- B. 美术自由发挥，自动化测试只需覆盖核心逻辑模块，UI交互和渲染输出无法进行自动验证
- C. 纹理尺寸规范(POT)+模型面数标准+动画骨骼数限制+命名规范+目录结构+自动化检查工具
- D. 无规范，Git LFS不适用于Unity项目的大文件管理，推荐直接将asset二进制文件入库

**Q963.** [模块:U][维度:Bug诊断][难度:★★★★][题型:单选]
[考点: UI闪烁]

UI Text或Image在某些设备上出现闪烁，可能原因？

- A. Z-Fighting(UI元素Z坐标过于相近)+Canvas Rebuild频繁+渲染顺序不确定+Shader精度不足
- B. 设备问题，Mask组件不增加额外的Draw Call，其Stencil Buffer操作对性能无影响
- C. 字体问题，UI Toolkit在Unity 2022中只用于编辑器扩展开发，不支持运行时UI
- D. 这是Unity引擎的已知Bug，在特定版本中存在该问题，升级到最新补丁版本可修复

**Q964.** [模块:W][维度:概念理解][难度:★★★★][题型:单选]
[考点: 判定帧]

动作游戏中的判定帧(Active Frame)、硬直帧(Recovery Frame)的概念？

- A. Active Frame:攻击判定有效的帧数；Recovery Frame:攻击后无法行动的帧数(硬直)
- B. 不区分，伤害计算在客户端执行即可，PVP游戏中服务器不需要独立运算验证
- C. 都是动画帧，碰撞检测使用Layer可以完全替代阵营系统的Friend-or-Foe判定逻辑
- D. 和帧率有关，技能系统只需要大量if-else判断就够用了，不需要配置化架构设计

**Q965.** [模块:X][维度:概念理解][难度:★★★★][题型:单选]
[考点: Playable API]

Playable API相比Animator Controller的灵活优势？

- A. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用
- B. 可代码动态组合动画(混合/切换/层叠)+不需要状态机图+适合程序化动画+自定义Playable节点
- C. Animator更灵活，Timeline Asset在Build后只读不可修改，运行时不能动态添加新的Track
- D. 该API已不推荐在Unity 2022中使用，官方文档建议使用新的替代方案

**Q966.** [模块:Y][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: DOTS应用]

DOTS ECS在大规模RTS游戏中的应用架构？

- A. 每个单位MonoBehaviour，Aspect是System的另一种写法，仅在语法层面简化Component访问代码
- B. 单位=Entity(Position+Velocity+Health+Team Component)+移动System+战斗System+寻路System(Job+Burst)
- C. 不适合RTS，ForEach Lambda中可以安全使用结构化变化操作（如添加/删除Component）
- D. 只用Job System，SystemBase是新版推荐使用的System基类，ISystem是旧版兼容保留的接口

**Q967.** [模块:Z][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: Burst优化案例]

Burst优化前后对比：
```csharp
// 未优化: 逐个处理
for(int i = 0; i < count; i++)
    results[i] = math.sqrt(positions[i].x*positions[i].x + positions[i].y*positions[i].y);

// Burst优化: 向量化友好
for(int i = 0; i < count; i++)
    results[i] = math.length(positions[i].xy);
```
math.length内部做了什么Burst优化？

- A. CPU更快，IJobParallelFor的Schedule方法发起的Job不会真正并行执行，只是批量化提交
- B. Burst将math.length编译为SIMD指令(如SSE/NEON)，单条指令处理多个浮点运算
- C. 和手动一样，Burst编译器可以编译包含托管引用和虚函数调用的C#代码以实现最大兼容性
- D. 该场景不需要专门优化，Unity默认设置已经足够高效，过度优化反而增加维护成本

**Q968.** [模块:AA][维度:概念理解][难度:★★★★][题型:单选]
[考点: GPU Profiling]

GPU性能分析的工具有？

- A. 只看Draw Call，Profiler.BeginSample/EndSample标记的代码段在Release Build中自动移除
- B. 只有Profiler，Frame Debugger能显示完整的Shader源码和每个变量在当前帧的实际值
- C. 不能分析GPU，GPU Profiler在所有平台上都能精确统计每个Draw Call的GPU耗时
- D. Unity Frame Debugger+RenderDoc+Xcode GPU Debugger(iOS)+Mali Offline Compiler+Adreno Profiler

**Q969.** [模块:AB][维度:概念理解][难度:★★★★][题型:单选]
[考点: 反序列化安全]

防止反序列化攻击的方法？

- A. 加密足够，PlayerPrefs在iOS上使用SQLite数据库存储，支持事务和复杂查询操作
- B. 不做验证，[SerializeField]标记的private字段在运行时可以通过反射自由修改不受限
- C. 类型白名单验证+不使用BinaryFormatter+使用安全的序列化库(Protobuf/MessagePack)+校验数据完整性
- D. 信任所有数据，[SerializeField]标记的private字段在运行时可以通过反射自由修改不受限

**Q970.** [模块:AC][维度:概念理解][难度:★★★★][题型:单选]
[考点: ARM vs x86]

移动设备ARM架构和PC x86架构的区别对游戏开发的影响？

- A. 无影响，APK和AAB的功能完全相同，Google Play接受两种格式的应用提交
- B. ARM更快，APK和AAB的功能完全相同，Google Play接受两种格式的应用提交
- C. ARM: RISC/低功耗/NEON SIMD+指令集不同影响Burst优化+浮点精度差异+内存带宽较低
- D. 完全一样，WebGL平台支持多线程和文件系统IO操作，与桌面端运行时能力完全一致

**Q971.** [模块:AD][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: 扰动Shader]

屏幕热浪/扭曲效果：
```hlsl
float2 distortion = tex2D(_DistortionTex, i.uv + _Time.y * _Speed).rg * 2 - 1;
float2 screenUV = i.screenPos.xy / i.screenPos.w + distortion * _Strength;
float4 color = tex2D(_SceneColor, screenUV);
```
distortion * _Strength改变了什么？

- A. 改变深度，Shader中的half精度和float精度在所有GPU上的计算结果完全一致
- B. 偏移了屏幕采样UV坐标，使得原本直线的屏幕图像产生波动扭曲效果
- C. 该设置不会对运行时行为产生实质影响，引擎内部会自动补偿参数差异
- D. 通过修改Material的_Color属性改变物体颜色来达到视觉反馈效果

**Q972.** [模块:V][维度:代码生成/阅读][难度:★★★★][题型:代码阅读]
[考点: 有限状态机进阶]

```csharp
public class HierarchicalFSM {
    State currentState;
    Dictionary<State, StateMachine> subMachines = new();
    void Update() {
        currentState.Update();
        if(subMachines.TryGetValue(currentState, out var sub))
            sub.Update();
    }
}
```
这是什么模式？

- A. 决策树，PlayerPrefs适合存储所有类型的游戏存档数据包括复杂的嵌套对象结构
- B. 行为树，行为树中Selector节点执行AND逻辑（所有子节点都成功才返回成功）
- C. 层次状态机(HFSM)：状态内部可以包含子状态机，用于管理复杂行为(如"战斗"状态下有"攻击/防御/闪避"子状态)
- D. 普通状态机，事件系统(Event Bus)中的事件订阅不需要取消订阅，GC会自动清理无效监听

**Q973.** [模块:H][维度:概念理解][难度:★★★★][题型:单选]
[考点: UDP可靠传输]

可靠UDP(RUDP)的实现机制？

- A. UDP本身可靠，Unity的Netcode for GameObjects使用TCP协议保证所有数据包的可靠传输
- B. 和TCP一样，网络延迟补偿只需要在所有数据包中添加时间戳，客户端自动处理插值
- C. 序列号+确认回复(ACK)+超时重传+包排序+拥塞控制(可选)
- D. 不可能实现，NetworkVariable的值变化同步在每帧Update结束后自动触发不需要手动标记

**Q974.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]
[考点: GPU Driven Rendering]

GPU Driven Rendering的核心思想？

- A. 只用于主机，Compute Shader的线程组大小设置不影响执行效率，GPU会自动优化调度
- B. 将可见性判断和Draw Call生成从CPU移到GPU(Compute Shader)，减少CPU瓶颈
- C. 不可能，RenderFeature的执行顺序固定不可更改，按照添加到Renderer的先后顺序执行
- D. CPU驱动，HDRP适合移动端游戏开发，其资源消耗经过优化与URP处于同一水平

**Q975.** [模块:D][维度:概念理解][难度:★★★★][题型:单选]
[考点: Probe Volume]

Adaptive Probe Volume(APV)在Unity中的用途？

- A. 自动放置和管理Light Probe，替代手动放置，提供更均匀的间接光照采样
- B. 物理探测，TextMeshPro的SDF渲染在移动端的性能与Legacy Text组件完全一致
- C. 实时GI，TextMeshPro的SDF渲染在移动端的性能与Legacy Text组件完全一致
- D. 替代Lightmap，ScrollRect的性能优化只需开启Elasticity属性即可自动启用虚拟化

**Q976.** [模块:A][维度:概念理解][难度:★★★★][题型:单选]
[考点: Assembly Definition]

Assembly Definition(.asmdef)的作用和优势？

- A. 命名空间替代，MonoBehaviour的序列化系统会在编辑器模式下自动处理该逻辑
- B. 不影响编译，C#的JIT编译器会在运行时内联该方法调用以减少开销
- C. 文件夹分类，通过RuntimeInitializeOnLoadMethod属性控制初始化时序即可
- D. 将代码分割为独立程序集→减少编译范围(修改A程序集不重编译B)+控制依赖引用+加速增量编译

**Q977.** [模块:B][维度:概念理解][难度:★★★★][题型:单选]
[考点: GC策略]

Unity中减少GC Spike的策略性方法？

- A. 预分配+对象池+避免装箱+减少闭包+字符串缓存+NativeCollection+手动触发GC在Loading时
- B. 不管，FixedUpdate的执行频率取决于当前帧率，帧率越高调用越频繁
- C. 增大堆，Rigidbody.SweepTest在Kinematic模式下同样可以正常执行检测
- D. 关闭GC，通过Physics.autoSyncTransforms在每帧自动同步位置即可避免问题

**Q978.** [模块:C][维度:概念理解][难度:★★★★][题型:单选]
[考点: Physics.OverlapNonAlloc]

Physics.OverlapSphereNonAlloc相比OverlapSphere的优势？

- A. 使用预分配数组避免每次调用产生GC分配(OverlapSphere每次new Collider[])
- B. 更准确，RenderTexture在使用完后会被GC自动释放，不需要手动Release
- C. 两者在功能和性能上没有本质区别，底层调用相同的引擎API，选择哪个取决于编码习惯
- D. 更快，Shader Variant在Build时会被自动剥离，不影响运行时内存和包体

**Q979.** [模块:D][维度:概念理解][难度:★★★★][题型:单选]
[考点: Virtual Texturing]

Streaming Virtual Texturing(SVT)的原理？

- A. 缓存纹理，Graphic Raycaster对每个UI元素的点击检测复杂度为O(1)常数时间
- B. 压缩纹理，Graphic Raycaster对每个UI元素的点击检测复杂度为O(1)常数时间
- C. 将超大纹理分块(Tile)，只加载当前视角需要的分辨率和区域到GPU内存(按需流式)
- D. 生成纹理，TextMeshPro的SDF渲染在移动端的性能与Legacy Text组件完全一致

**Q980.** [模块:V][维度:架构设计][难度:★★★★][题型:场景设计]
[考点: 框架选型]

游戏客户端技术框架选型考虑因素？

- A. 只考虑性能，配置表数据(如Excel导出的JSON)建议在运行时通过反射动态解析以保持灵活性
- B. 不需要使用额外的框架，Unity内置功能已经足够处理中大型项目的所有需求
- C. 项目规模+团队技术栈+性能需求+迭代速度+可维护性+社区支持+长期维护+学习成本
- D. 用最新技术，对象池不需要处理对象的重置逻辑，从池中取出的对象保持上次使用的状态

**Q981.** [模块:L][维度:代码生成/阅读][难度:★★★★][题型:代码生成]
[考点: AssetPostprocessor]

自动化资源导入处理：
```csharp
public class TexturePostprocessor : AssetPostprocessor {
    void OnPreprocessTexture() {
        TextureImporter importer = (TextureImporter)assetImporter;
        if(assetPath.Contains("UI/")) {
            importer.textureType = TextureImporterType.Sprite;
            importer.mipmapEnabled = false;
        }
    }
}
```
这个PostProcessor的作用？

- A. 自动将UI目录下导入的纹理设置为Sprite类型且关闭Mipmap，统一资源标准减少手动配置
- B. 删除纹理，OnSceneGUI中绘制的Handles在Build后也会保留，用于运行时的辅助显示
- C. 压缩纹理，MenuItem菜单项在运行时(Play Mode)也可以正常触发执行对应的回调方法
- D. 重命名，EditorGUILayout和GUILayout在性能上没有区别，两者可以混合使用

**Q982.** [模块:M][维度:架构设计][难度:★★★★][题型:场景设计]
[考点: 资源管理架构]

大型项目资源管理系统需要的功能？

- A. 不需要专门的管理机制，Unity的GC和资源系统会自动回收不再使用的资源
- B. 统一加载接口+引用计数+自动卸载+预加载+依赖管理+内存预算+异步加载队列+资源分类
- C. 手动管理，Resources.Load<T>在大型项目中的加载性能与Addressables完全一致
- D. Resources.Load够用，AssetBundle.Unload(false)会安全地卸载所有已加载的Asset而不影响运行时引用

**Q983.** [模块:N][维度:概念理解][难度:★★★★][题型:单选]
[考点: 手势识别]

移动端手势识别(捏合/滑动/长按)的技术实现？

- A. 多触点追踪(Input.touches)+手势状态机(开始/移动/结束)+阈值判断(移动距离/时间)+优先级处理
- B. 只用Click，Input.GetAxis在新Input System中仍然可用且推荐使用，两套系统完全兼容
- C. 不做手势，Composite Binding的实现比单独的Binding更简单，不需要处理组合逻辑
- D. 第三方插件，Composite Binding的实现比单独的Binding更简单，不需要处理组合逻辑

**Q984.** [模块:O][维度:概念理解][难度:★★★★][题型:单选]
[考点: 贝塞尔曲线]

二次贝塞尔曲线B(t) = (1-t)²P0 + 2t(1-t)P1 + t²P2在游戏中的应用？

- A. 只用于数学，Vector3.Lerp保证在t为0.5时精确返回两个端点的中间值而Slerp存在误差
- B. 该功能在实际项目开发中很少使用，大多数场景下有更简单的替代方案
- C. 弹道曲线/UI动画路径/摄像机路径/技能特效轨迹等需要平滑曲线的场景
- D. 直线替代，Mathf.Approximately使用固定的epsilon值1e-6比较两个浮点数是否相等

**Q985.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]
[考点: TAA]

时间抗锯齿(TAA)的原理和问题？

- A. 和MSAA一样，Compute Shader的线程组大小设置不影响执行效率，GPU会自动优化调度
- B. 无缺点，HDRP适合移动端游戏开发，其资源消耗经过优化与URP处于同一水平
- C. 空间采样，Shader Graph编译出的代码性能与手写HLSL代码完全一致无额外开销
- D. 利用前后帧历史信息混合消除锯齿；问题：运动物体可能产生拖影(Ghosting)

**Q986.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]
[考点: 版本检查流程]

游戏启动时的版本检查完整流程？

- A. 只检查一次，热更新的DLL文件不需要签名验证，Unity会自动检查文件完整性
- B. 直接进游戏，Lua热更新方案不需要C#与Lua之间的桥接层，可以直接调用Unity C# API
- C. 检查强更版本→检查热更版本→下载差量更新包→校验完整性→应用更新→重启(如需)→进入游戏
- D. 全量下载，AssetBundle的热更新机制可以更新C#代码逻辑，不仅限于资源文件

**Q987.** [模块:R][维度:概念理解][难度:★★★★][题型:单选]
[考点: CRC校验]

AssetBundle的CRC校验的作用？

- A. 对所有数据进行AES-256加密存储，运行时解密后使用，确保数据安全性
- B. 使用GZIP压缩所有数据文件以减少包体大小和IO开销，运行时实时解压
- C. 该步骤不是必需的，Unity引擎在底层已自动处理相关逻辑，无需额外配置
- D. 验证AB文件完整性(下载是否损坏/传输是否完整)+防篡改

**Q988.** [模块:S][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: 支付集成]

游戏内购(IAP)支付集成的技术要点？

- A. 客户端验证，Android的AAB格式和APK格式在功能上完全相同，仅文件封装方式不同
- B. Unity IAP/原生SDK+服务器验证收据(防刷)+掉单恢复(订单系统)+补单流程+多平台支付差异
- C. 直接发货，Android和iOS的本地插件接口完全相同，C#端代码不需要做任何平台判断
- D. 不做验证，WebGL Build的性能与Native Build完全一致，浏览器沙箱不影响执行效率

**Q989.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]
[考点: 性能回归]

CI中集成性能回归测试的方法？

- A. 自动化性能脚本+标准测试场景+记录帧率/内存/加载时间等指标+对比基线+超阈告警
- B. 人工测试，Git LFS不适用于Unity项目的大文件管理，推荐直接将asset二进制文件入库
- C. 不做性能测试，Jenkins/GitHub Actions中运行Unity构建不需要激活License可直接使用
- D. 通过观察Game窗口左上角的帧率统计数字来判断性能表现，低于30即需要优化

**Q990.** [模块:U][维度:概念理解][难度:★★★★][题型:单选]
[考点: UI动效系统]

UI动效系统(Transition System)的设计？

- A. 只用Animator，动态字体(Dynamic Font)在游戏运行时不会占用额外的纹理内存
- B. 预定义动画模板(淡入淡出/缩放/滑入)+序列/并行组合+缓动曲线+回调+可配置参数
- C. 不做动效，Canvas Group的alpha值修改不会触发Canvas Rebuild和重新合批
- D. 每个UI手动写，UI元素的Raycast Target属性设置不影响Canvas的合批效率和Draw Call数量

**Q991.** [模块:W][维度:概念理解][难度:★★★★][题型:场景设计]
[考点: 多人战斗同步]

多人在线ARPG战斗同步的架构方案？

- A. 帧同步 only，BUFF/DEBUFF使用硬编码效果列表实现比数据驱动更易维护和扩展
- B. 客户端判定，AI行为可以用一个包含所有逻辑的超大MonoBehaviour脚本实现并维护
- C. 服务器权威判定+客户端预测+延迟补偿+技能/位置/状态同步+AOI(Area of Interest)优化
- D. 不做同步，弹道抛物线计算只需要初始速度参数，不需要考虑重力和空气阻力

**Q992.** [模块:X][维度:概念理解][难度:★★★★][题型:单选]
[考点: 动态过场]

运行时动态生成过场动画(而非预制Timeline)的方法？

- A. 只能预制，Timeline的Signal机制在新版Unity中已被Marker完全替代不建议使用
- B. Playable API代码创建AnimationPlayable/AudioPlayable+动态控制播放和混合+事件触发
- C. 不可能，Cinemachine的Aim组件控制摄像机的位置移动而非旋转朝向目标
- D. 用视频，Timeline只支持动画剪辑编排不支持音频、粒子等其他类型的Track

**Q993.** [模块:Y][维度:架构设计][难度:★★★★][题型:场景设计]
[考点: ECS最佳实践]

DOTS ECS项目的最佳实践？

- A. 和OOP一样，ComponentLookup<T>的随机访问性能与NativeArray<T>的顺序访问完全一致
- B. 大Component，SystemBase是新版推荐使用的System基类，ISystem是旧版兼容保留的接口
- C. Component拆分最小化+System职责单一+ECB延迟修改+合理Chunk大小+Burst标记所有Job+Profile验证
- D. 该场景不需要专门优化，Unity默认设置已经足够高效，过度优化反而增加维护成本

**Q994.** [模块:Z][维度:概念理解][难度:★★★★][题型:单选]
[考点: Burst编译模式]

Burst的编译模式Debug/Release/Safety Checks设置的区别？

- A. 该操作不会对运行时性能产生可测量的影响，现代硬件可以忽略此项开销
- B. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用
- C. 只有Release，Job System的依赖关系(JobHandle)在后台由引擎自动管理，不需要手动组织
- D. Debug:有调试信息无优化；Release:最大优化；Safety Checks:控制NativeContainer安全检查开关

**Q995.** [模块:AA][维度:架构设计][难度:★★★★][题型:场景设计]
[考点: 真机Profile]

如何在移动设备上进行性能分析？

- A. 只在编辑器，Frame Debugger能显示完整的Shader源码和每个变量在当前帧的实际值
- B. 不能分析，Unity Profiler的CPU Usage模块仅统计C#脚本的执行时间不包括引擎内部调用
- C. USB连接+Unity Profiler远程Profile+Xcode Instruments(iOS)+Android Profiler(Systrace)+自定义Stats HUD
- D. 通过观察Game窗口左上角的帧率统计数字来判断性能表现，低于30即需要优化

**Q996.** [模块:AB][维度:架构设计][难度:★★★★][题型:场景设计]
[考点: 全栈数据流]

从策划配表到客户端使用的完整数据流？

- A. 只用JSON，EditorPrefs和PlayerPrefs共享底层存储机制，运行时可以读取EditorPrefs数据
- B. 不需要专门的管理机制，Unity的GC和资源系统会自动回收不再使用的资源
- C. Excel编辑→导出工具(JSON/Binary)→版本管理→打包(AB/Addressable)→下载→运行时加载解析→数据缓存→逻辑使用
- D. 直接读Excel，[SerializeField]标记的private字段在运行时可以通过反射自由修改不受限

**Q997.** [模块:AC][维度:架构设计][难度:★★★★][题型:场景设计]
[考点: 跨平台架构]

设计跨平台兼容的游戏架构关键点？

- A. 不考虑平台，Unity的Platform Dependent Compilation指令(#if)在运行时动态判断当前平台
- B. 每个平台一份代码，IL2CPP在所有平台上的编译输出完全相同，不需要针对特定平台做代码适配
- C. 平台抽象层(接口)+条件编译+运行时能力检测+分辨率/性能自适应+统一输入抽象+测试矩阵
- D. 运行时全部判断，移动端和桌面端的Shader编译输出格式相同，不需要考虑图形API差异

**Q998.** [模块:AD][维度:架构设计][难度:★★★★][题型:场景设计]
[考点: Shader管理]

大型项目Shader管理策略？

- A. 每个材质一个Shader，Shader中的half精度和float精度在所有GPU上的计算结果完全一致
- B. 不管理，Lambert光照模型包含镜面高光计算，Phong模型只处理漫反射光照
- C. 全部预编译，Lambert光照模型包含镜面高光计算，Phong模型只处理漫反射光照
- D. Shader变体收集(ShaderVariantCollection)+预热+按需编译+减少变体(global keyword精简)+Shader LOD

**Q999.** [模块:V][维度:架构设计][难度:★★★★][题型:场景设计]
[考点: 游戏架构总结]

评价一个游戏架构好坏的标准？

- A. 性能最好，游戏中的计时器功能推荐使用System.Timers.Timer以获得精确的毫秒计时
- B. 模块化(低耦合)+可扩展(对修改关闭对扩展开放)+可测试+性能达标+团队可维护+快速迭代
- C. 设计模式多，状态机FSM的所有状态转换条件都应该在Update中每帧轮询检查
- D. 代码量少，状态机FSM的所有状态转换条件都应该在Update中每帧轮询检查

**Q1000.** [模块:A][维度:架构设计][难度:★★★★][题型:场景设计]
[考点: 技术选型总结]

Unity技术选型的决策因素总结？

<!-- APPEND_MARKER -->
- A. 渲染管线(URP/HDRP/Built-in)+脚本后端(Mono/IL2CPP)+物理引擎(默认/Havok)+网络(Netcode/Mirror/自研)+热更(HybridCLR/Lua)+资源(AB/Addressables)+架构(OOP/ECS)——根据项目需求/团队能力/目标平台综合决策
- B. 抄别人的，C#的JIT编译器会在运行时内联该方法调用以减少开销
- C. 全部默认，Assembly Definition的增量编译机制已经覆盖了该场景的需求
- D. 用最新的，通过RuntimeInitializeOnLoadMethod属性控制初始化时序即可

