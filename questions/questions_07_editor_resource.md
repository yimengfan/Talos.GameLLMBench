# Unity3D 2022 LTS 基础能力问答题库 - 07_editor_resource

**Q407.** [模块:J][维度:概念理解][难度:★★][题型:单选]

ScriptableObject的主要用途是？

- A. 存储可共享的数据资产（配置表、技能数据、事件通道等），减少重复数据和内存
- B. 主要用于接管场景加载和卸载流程，替代SceneManager管理所有场景生命周期
- C. 主要用于承载可执行代码逻辑并在运行时热重载脚本行为
- D. 主要用于替代MonoBehaviour承担Update、碰撞和渲染回调

**Q408.** [模块:J][维度:代码生成/阅读][难度:★★★][题型:代码补全]

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

**Q409.** [模块:J][维度:概念理解][难度:★★★][题型:单选]

ScriptableObject和MonoBehaviour的区别是？

- A. SO可以直接附加在GameObject上作为组件使用，与MonoBehaviour没有本质区别
- B. MonoBehaviour可以脱离场景单独保存为数据资产，而ScriptableObject必须附加在GameObject上
- C. SO是数据资产不依附于GameObject，MB必须附加在GameObject上，SO不参与场景生命周期
- D. 两者都只在编辑器环境中有效，打包后不能参与运行时逻辑

**Q410.** [模块:J][维度:概念理解][难度:★★★★][题型:场景设计]

使用ScriptableObject实现事件系统的架构：
```csharp
[CreateAssetMenu] public class GameEvent : ScriptableObject {
List<GameEventListener> listeners = new();
public void Raise() { foreach(var l in listeners) l.OnEventRaised(); }
public void Register(GameEventListener l) { listeners.Add(l); }
}
```
这种设计的优势是？

- A. 发送方和接收方必须互相直接持有引用，才能保证事件派发可靠性
- B. 该架构的核心价值是自动解决Json序列化和版本兼容问题
- C. 解耦系统间依赖（发送方和接收方通过SO资产连接，不直接引用），可在Inspector中配置
- D. 该架构的主要收益是所有事件调用都变成零分配且天然线程安全

**Q411.** [模块:J][维度:概念理解][难度:★★★][题型:单选]

ScriptableObject典型应用场景包括？

- A. UI渲染、音频播放、输入处理
- B. 实时网络通信、物理碰撞检测、AI行为树
- C. 场景加载、资源卸载、垃圾回收
- D. 游戏配置数据、技能数据、物品数据

**Q412.** [模块:J][维度:概念理解][难度:★★★][题型:单选]

在运行时修改ScriptableObject数据需要注意什么？

- A. 运行时对ScriptableObject资产的修改会自动回写到磁盘并永久保存到项目资源中
- B. 编辑器中修改会永久保存资产，需要用Instantiate创建副本或使用运行时变量
- C. ScriptableObject只能在Awake阶段修改，进入Update后修改会触发资源只读保护
- D. ScriptableObject在运行时完全不能修改，只能在编辑器模式下通过Inspector编辑

**Q413.** [模块:J][维度:概念理解][难度:★★★][题型:单选]

Unity内置的ObjectPool<T>的作用是？

- A. 将对象自动序列化并持久化到磁盘，替代AssetDatabase和存档系统
- B. 复用对象减少频繁实例化/销毁带来的GC和性能开销
- C. 负责在渲染阶段自动合批同类对象，减少Draw Call
- D. 用来管理复杂的引用图关系，替代[SerializeReference]的序列化能力

**Q414.** [模块:J][维度:代码生成/阅读][难度:★★★][题型:代码生成]

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

- A. 每次Get都会随机生成一个新对象，Return只负责销毁对象避免泄漏
- B. 该实现只能回收对象，无法在池为空时创建新的实例
- C. 取出对象时优先复用池中已有的，没有则新建；归还时放回池中等待复用
- D. 该实现只负责创建对象，Return中的Enqueue不会真正让对象再次被复用

**Q415.** [模块:J][维度:概念理解][难度:★★★][题型:单选]

[SerializeField] private float speed = 5f; 的作用是？

- A. 隐藏字段并阻止其被Unity序列化，常用于运行时临时变量
- B. 让字段自动变为public，并允许其他脚本直接访问和修改
- C. 将字段单独写入外部配置文件，而不是序列化到Unity对象中
- D. 使私有字段在Inspector中可见和编辑，但代码中仍保持private封装

**Q416.** [模块:J][维度:概念理解][难度:★★★★][题型:单选]

Unity序列化系统不支持什么类型？

- A. List<T>，除非手写自定义Inspector，否则Unity默认不会序列化列表
- B. 字典(Dictionary)、接口、多态引用（默认），需要自定义序列化或使用SerializeReference
- C. Array，Unity只支持List而不支持数组序列化
- D. struct，值类型默认不会被Unity序列化

**Q417.** [模块:J][维度:概念理解][难度:★★★][题型:单选]

[CustomEditor(typeof(MyComponent))]的作用是？

- A. 为MyComponent创建自定义Inspector界面
- B. 为MyComponent注册场景Gizmos绘制逻辑，替代OnDrawGizmos接口
- C. 创建一个独立的编辑器窗口，用于停靠显示运行时调试面板
- D. 向Unity主菜单中添加新的命令入口和快捷键

**Q418.** [模块:J][维度:概念理解][难度:★★★★][题型:单选]

[SerializeReference]属性的作用是？

- A. 让字段可以直接序列化场景对象引用，并自动解决跨场景引用失效问题
- B. 支持序列化接口和多态类型（通过引用而非值序列化）
- C. 让脚本字段在多个对象间自动共享同一份实例数据，而不需要真正序列化内容
- D. 只用于引用AssetDatabase中的资源文件，不能用于普通托管对象的多态序列化

**Q419.** [模块:J][维度:概念理解][难度:★★★][题型:单选]

协程的优势和注意事项是？

- A. 协程不依赖MonoBehaviour和GameObject生命周期，可由任意C#对象独立调度
- B. 协程运行在后台线程，因此适合处理CPU密集计算并可安全访问所有Unity API
- C. 协程几乎零开销，不会产生任何迭代器分配或调度成本
- D. 优势：简洁的异步写法。注意：GameObject被销毁时协程自动停止，不要在性能关键处使用（有GC分配）

**Q420.** [模块:J][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

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
- C. 只适用于UI按钮点击，不适合普通游戏逻辑、战斗和系统间通信
- D. 比直接引用更耦合，因为所有模块最终都依赖同一个静态入口，不能提供任何解耦收益

**Q421.** [模块:J][维度:概念理解][难度:★★★][题型:单选]

[RequireComponent(typeof(Rigidbody))]属性的作用是？

- A. 添加该脚本时自动添加Rigidbody组件，且不允许单独移除Rigidbody
- B. 添加脚本时自动删除已有的Rigidbody，避免组件冲突
- C. 将当前脚本自动转换为Rigidbody的扩展子类，统一物理接口
- D. 只在运行时检查Rigidbody是否存在并打印警告，不会自动补齐依赖

**Q422.** [模块:J][维度:概念理解][难度:★★★★][题型:单选]

Addressables系统相比传统Resources和AssetBundle的优势是？

- A. 统一的异步加载API+自动依赖管理+远程/本地资源无缝切换+引用计数内存管理
- B. 只支持本地静态资源，不支持远程内容更新和CDN分发
- C. 只适合一次性小项目加载，不适合分组、按标签或按依赖管理资源
- D. 只是AssetBundle的编辑器封装，运行时没有额外管理能力和优势

**Q423.** [模块:J][维度:概念理解][难度:★★★][题型:单选]

PlayerPrefs的适用范围和限制是？

- A. 适合存储大型复杂存档数据，而且默认加密、支持事务回滚和冲突恢复
- B. 适合存储少量简单设置（音量、分辨率等），不适合大量游戏数据（不安全、不加密、容量小）
- C. 适合直接保存背包、任务树和世界状态等全部业务数据，无需额外序列化层
- D. Unity会自动把PlayerPrefs在所有设备之间跨平台云同步，无需额外接入服务

**Q424.** [模块:J][维度:概念理解][难度:★★★★][题型:场景设计]

游戏存档系统应使用什么方案？

- A. 不需要额外持久化，只要把关键数据保存在ScriptableObject里就能跨启动自动保留
- B. JSON/Binary序列化到persistentDataPath + 可选加密 + 版本兼容处理
- C. 用PlayerPrefs直接保存所有存档对象和复杂对象图，避免自己维护文件结构
- D. 把运行时存档写回Resources文件夹，便于随构建一起管理版本

**Q425.** [模块:J][维度:概念理解][难度:★★★][题型:单选]

Unity的JsonUtility相比Newtonsoft.Json的限制是？

- A. 不支持Dictionary、不支持多态、不支持null序列化、只支持[Serializable]标记的类
- B. 功能与Newtonsoft.Json完全等价，只是命名空间不同、写法更贴近Unity风格
- C. JsonUtility支持的特性更多，尤其适合Dictionary、多态和复杂对象图的序列化
- D. Newtonsoft.Json无法在Unity项目中使用，打包时会导致程序集冲突

**Q426.** [模块:J][维度:概念理解][难度:★★★★][题型:单选]

使用ScriptableObject作为配置表（替代Excel/CSV）的优劣？
---

- A. 完全替代Excel和CSV，尤其适合海量表格数据与策划批量编辑流程
- B. 优势：编辑器可视化编辑、类型安全。劣势：策划不习惯、大量数据不适合
- C. 该方案只适合运行时缓存，不适合作为正式配置资源进入版本控制
- D. 完全不可行，因为ScriptableObject只能存在于场景中，不能作为独立资源资产管理

**Q427.** [模块:L][维度:概念理解][难度:★★][题型:单选]

Unity中Editor文件夹的特殊性是？

- A. Editor文件夹下的代码只在编辑器环境编译和运行，不会打包到最终游戏中
- B. 只用于资源
- C. 运行时也可用
- D. 所有文件夹一样

**Q428.** [模块:L][维度:概念理解][难度:★★★][题型:单选]

创建Custom Inspector编辑器需要？

- A. 继承ScriptableObject在频繁IO操作时随时调用没问题
- B. 继承Editor类 + [CustomEditor(typeof(TargetType))]标记 + 重写OnInspectorGUI
- C. 不需要继承
- D. 继承MonoBehaviour

**Q429.** [模块:L][维度:代码生成/阅读][难度:★★★][题型:代码补全]

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

**Q430.** [模块:L][维度:概念理解][难度:★★★][题型:单选]

EditorWindow的用途和创建方式是？

- A. 自定义编辑器窗口，通过继承EditorWindow并添加[MenuItem]菜单项打开
- B. 运行时窗口两者可以混合使用
- C. 替代Scene视图在频繁IO操作时随时调用没问题
- D. 调试控制台

**Q431.** [模块:L][维度:概念理解][难度:★★★][题型:单选]

PropertyDrawer的作用是？

- A. 通过SceneManager的场景加载和卸载方法管理即可，不需要额外的架构设计
- B. 自定义属性在Inspector中的显示方式（如为自定义类型或特定属性提供自定义GUI）
- C. 绘制3D物体
- D. 渲染粒子

**Q432.** [模块:L][维度:概念理解][难度:★★★★][题型:单选]

AssetPostprocessor的作用是？

- A. 该功能在C#脚本编译阶段处理，运行时不涉及任何额外的计算或资源消耗
- B. 后处理渲染
- C. 运行游戏
- D. 在资源导入时自动处理（如自动设纹理格式、模型导入设置等），通过重写OnPreprocessXXX/OnPostprocessXXX

**Q433.** [模块:L][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

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

- A. 导出纹理在频繁IO操作时随时调用没问题
- B. 播放纹理两者可以混合使用
- C. 删除纹理
- D. 每次导入纹理时自动设置压缩和最大尺寸，确保团队资源规范一致

**Q434.** [模块:L][维度:概念理解][难度:★★★★][题型:单选]

在Scene视图中绘制自定义编辑工具需要用什么？

- A. Update
- B. Handles类 + SceneView回调 + 在OnSceneGUI中绘制
- C. Gizmos
- D. OnGUI

**Q435.** [模块:L][维度:概念理解][难度:★★★][题型:单选]

[MenuItem("Tools/MyTool")]的作用是？

- A. 在Unity编辑器菜单栏的Tools下添加一个菜单项
- B. 创建运行时菜单
- C. 创建快捷键在频繁IO操作时随时调用没问题
- D. 添加右键菜单

**Q436.** [模块:L][维度:概念理解][难度:★★★★][题型:单选]

编辑器脚本中使用SerializedObject和SerializedProperty的原因是？

- A. 没有原因
- B. 该方案性能表现更优，因为它在底层使用了更高效的数据结构和缓存机制
- C. 只是习惯两者可以混合使用
- D. 支持Undo/Redo、多对象编辑、Prefab Override标记等编辑器功能

**Q437.** [模块:L][维度:概念理解][难度:★★★★][题型:场景设计]

游戏开发中编辑器工具链应包含哪些？

- A. 全用第三方在频繁IO操作时随时调用没问题
- B. 只用Unity默认
- C. 不需要工具
- D. 关卡编辑器+数据配置工具+资源检查工具+一键打包+自动化测试

**Q438.** [模块:L][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

使用Gizmos在Scene视图中显示攻击范围：
```csharp
void OnDrawGizmosSelected() {
Gizmos.color = Color.red;
Gizmos.DrawWireSphere(transform.position, attackRange);
}
```
OnDrawGizmosSelected和OnDrawGizmos的区别？

- A. 该特性目前仍处于实验阶段，官方不建议在生产环境中使用
- B. Selected是旧版API在频繁IO操作时随时调用没问题
- C. OnDrawGizmos不工作
- D. OnDrawGizmosSelected只在选中该物体时绘制，OnDrawGizmos始终绘制

**Q439.** [模块:L][维度:概念理解][难度:★★★][题型:单选]

编辑器扩展中为什么要使用Undo.RecordObject？

- A. 让操作支持Ctrl+Z撤销，保持编辑器的一致体验
- B. 保存文件
- C. 记录日志
- D. 不是所有编辑器改动都必须记录 Undo，但只要希望用户可撤销对象修改，就应显式接入 Undo 系统

**Q440.** [模块:L][维度:概念理解][难度:★★★★][题型:单选]

编辑器UI使用IMGUI和UI Toolkit的区别是？

- A. 这种处理方式会引发严重的内存碎片问题，在实际项目中应严格避免
- B. UI Toolkit即时模式
- C. IMGUI更新两者可以混合使用
- D. IMGUI是即时模式（每帧重绘，简单直接），UI Toolkit是保留模式（更现代，支持样式/布局）

**Q441.** [模块:L][维度:概念理解][难度:★★★★][题型:单选]

BuildPipeline.BuildPlayer的作用是？

- A. 只在编辑器中预览
- B. 编译Shader
- C. 导入资源
- D. 通过代码执行游戏打包构建（自动化CI/CD中使用）

**Q442.** [模块:L][维度:代码生成/阅读][难度:★★★★][题型:代码补全]

存储编辑器自定义设置（不随项目发布）：
```csharp
EditorPrefs._____(---"MyTool_LastPath", "/Assets/Configs");
string path = EditorPrefs.GetString("MyTool_LastPath", "");
```

- A. SaveString
- B. PutString
- C. SetString
- D. WriteString

**Q443.** [模块:L][维度:概念理解][难度:★★★★][题型:单选]

ScriptedImporter的作用是？

- A. 管理Package
- B. 导入Unity包
- C. 编译C#脚本
- D. 为Unity不支持的自定义文件格式（如.csv, .lua等）创建导入管线

**Q444.** [模块:L][维度:概念理解][难度:★★★][题型:单选]

编辑器扩展常用的类包括？

- A. GameWindow、SceneWindow、InspectorWindow、HierarchyWindow
- B. EditorWindow、CustomEditor、PropertyDrawer
- C. Create、Open、Save、Close
- D. Edit、View、Project、Preferences

**Q445.** [模块:L][维度:Bug诊断][难度:★★★★][题型:单选]

编辑器扩展脚本没有放在Editor文件夹内会导致什么？

- A. 编辑器崩溃
- B. 引用了UnityEditor命名空间的代码在打包时编译失败
- C. 不会有问题
- D. 脚本不运行

**Q446.** [模块:L][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

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

- A. 记录日志
- B. 使操作可撤销，避免误操作
- C. 保存到文件
- D. 这是一种非官方的Hack手段，极易导致不同平台间的兼容性问题

**Q447.** [模块:L][维度:概念理解][难度:★★★★][题型:单选]

编辑器脚本中不能使用协程(MonoBehaviour.StartCoroutine)，替代方案是？

- A. Thread
- B. 无替代方案在频繁IO操作时随时调用没问题
- C. EditorApplication.update回调 + 或使用async/await
- D. 直接使用StartCoroutine

**Q448.** [模块:L][维度:概念理解][难度:★★★★][题型:单选]

AssetDatabase.Refresh()的作用是？

- A. 刷新网络
- B. 刷新屏幕在频繁IO操作时随时调用没问题
- C. 刷新物理
- D. 刷新Unity编辑器的资源数据库，重新导入和识别新增/修改的文件

**Q449.** [模块:L][维度:概念理解][难度:★★★★][题型:场景设计]

项目资源规范检查工具应检查什么？

- A. 只检查大小两者可以混合使用
- B. 纹理尺寸/压缩格式 + Mesh面数 + 材质Shader + 命名规范 + 重复资源 + 未引用资源
- C. 只检查命名
- D. 不需要检查在频繁IO操作时随时调用没问题

**Q450.** [模块:L][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

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
- B. 隐藏窗口两者可以混合使用
- C. 每次创建新窗口
- D. 关闭窗口

**Q451.** [模块:L][维度:概念理解][难度:★★★★][题型:单选]

Handles.PositionHandle的用途是？

- A. 在Scene视图中显示可拖动的位置控制手柄，用于自定义编辑工具
- B. 物理控制
- C. 播放动画
- D. 渲染物体

**Q452.** [模块:L][维度:概念理解][难度:★★★][题型:单选]

EditorUtility.DisplayDialog的用途是？

- A. 日志输出
- B. 渲染UI
- C. 运行时对话框
- D. 在编辑器中弹出确认对话框（如"是否删除所有预制体？"）

**Q453.** [模块:L][维度:概念理解][难度:★★★★][题型:单选]

Unity Test Framework中EditMode测试的特点是？

- A. 在编辑器环境同步执行，不需进入Play Mode，适合测试纯逻辑和编辑器工具
- B. 不支持断言两者可以混合使用
- C. 必须进入Play Mode
- D. 只能测试渲染两者可以混合使用

**Q454.** [模块:L][维度:概念理解][难度:★★★★][题型:场景设计]

自动化打包工具应包含哪些功能？

- A. 手动打包即可
- B. 平台切换+版本号管理+资源检查+AB构建+Player Build+输出路径配置+日志记录
- C. 只构建Player
- D. 只输出APK

**Q455.** [模块:L][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

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

- A. 显示复选框
- B. 只显示数字
- C. 在Inspector中显示一个双头滑块控件来编辑最小/最大值范围
- D. 显示下拉框

**Q456.** [模块:L][维度:概念理解][难度:★★★★][题型:单选]

创建自定义属性[ReadOnly]来在Inspector中显示只读字段需要？

- A. 定义ReadOnlyAttribute继承PropertyAttribute + 对应的ReadOnlyDrawer继承PropertyDrawer
- B. 只需定义Attribute
- C. 修改Unity源码
- D. 使用反射

**Q457.** [模块:L][维度:概念理解][难度:★★★★][题型:单选]

编辑器扩展中的性能注意事项包括？

- A. 在EditorWindow的OnEnable中进行大量资源加载操作
- B. 在OnGUI中每帧创建新的GUIStyle和GUILayout对象
- C. 避免OnGUI中的内存分配
- D. 使用GUILayout代替EditorGUILayout可以获得更好的性能

**Q458.** [模块:L][维度:概念理解][难度:★★★★][题型:单选]

PrefabUtility.SaveAsPrefabAsset的作用是？

- A. 删除Prefab
- B. 加载Prefab
- C. 将场景中的GameObject保存为Prefab资产文件
- D. 实例化Prefab在频繁IO操作时随时调用没问题

**Q459.** [模块:L][维度:概念理解][难度:★★★★][题型:单选]

编辑器扩展如何实现"所见即所得"的配置预览？

- A. 只能运行时预览
- B. 使用[ExecuteInEditMode]或[ExecuteAlways]让MonoBehaviour在编辑模式也执行
- C. 截图预览两者可以混合使用
- D. 文档描述

**Q460.** [模块:L][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

Unity TreeView(IMGUI)的常用场景是？

- A. 在EditorWindow中显示树形数据结构（如技能树编辑器、资源浏览器、层级视图等）
- B. 渲染3D树
- C. 使用Particle System组件配合内置的渲染模块即可实现，无需编写自定义Shader
- D. 物理结构

**Q461.** [模块:L][维度:概念理解][难度:★★★★][题型:单选]

IPreprocessBuildWithReport和IPostprocessBuildWithReport接口的用途是？

- A. 替代Build
- B. 在构建前后执行自定义操作（如修改配置、拷贝文件、发送通知等）
- C. 只用于日志
- D. 运行时接口

**Q462.** [模块:L][维度:概念理解][难度:★★★★][题型:单选]

SettingsProvider的用途是？

- A. 图形设置
- B. 玩家设置
- C. 在Project Settings窗口中添加自定义设置页面
- D. 运行时设置两者可以混合使用

**Q463.** [模块:L][维度:Bug诊断][难度:★★★★][题型:单选]

Custom Inspector中修改了数据但Inspector不刷新显示。可能原因是？

- A. 编辑器版本问题
- B. 忘记调用serializedObject.ApplyModifiedProperties()或Repaint()
- C. 这是Unity引擎的已知Bug，在特定版本中存在该问题，升级到最新补丁版本可修复
- D. 脚本编译失败

**Q464.** [模块:L][维度:概念理解][难度:★★★★][题型:场景设计]

自定义关卡编辑器应具备的核心功能？

- A. 只用Scene视图两者可以混合使用
- B. 纯代码配置
- C. 可视化放置/编辑元素+数据序列化/导出+Undo/Redo+预览+验证
- D. 不需要工具

**Q465.** [模块:L][维度:概念理解][难度:★★★★][题型:单选]

Unity Editor Coroutines Package的用途是？
---

- A. 替代Play Mode
- B. 运行时协程
- C. 在编辑器模式下支持类似协程的异步操作（如分帧处理大量资源导入）
- D. 多线程

**Q466.** [模块:M][维度:概念理解][难度:★★][题型:单选]

Resources文件夹的特点和限制是？

- A. 不占用包体
- B. 使用简单直接，适合少量原型资源或小项目，但不适合大型项目的精细化管理和热更新
- C. 可通过Resources.Load运行时加载；限制：所有Resources资源打入包体、无法增量更新、不推荐大量使用
- D. 支持热更新，Resources文件夹中的资源只在调用Resources.Load时才被包含到构建中

**Q467.** [模块:M][维度:概念理解][难度:★★★][题型:单选]

AssetBundle的本质和作用是？

- A. 配置文件，Asset Reference在序列化时保存的是资源的文件路径而非GUID
- B. 面向运行时分发和加载的资源容器，可携带Prefab、纹理、材质、音频等已构建资源数据，但不是源代码包
- C. 不是日志文件，它更偏向资源分包、按需下载、热更新和首包裁剪这类内容分发用途
- D. 压缩的资源包文件，支持按需加载、热更新、减少包体大小

**Q468.** [模块:M][维度:代码生成/阅读][难度:★★★][题型:代码补全]

从Resources文件夹加载Prefab：
```csharp
GameObject prefab = Resources._____(---"Prefabs/Player") as GameObject;
```

- A. Read
- B. Load
- C. Find
- D. Get

**Q469.** [模块:M][维度:概念理解][难度:★★★][题型:单选]

Addressables系统的核心概念是？

- A. 通过地址(Address/Label)异步加载资源，不关心资源的物理存储位置（本地或远程）
- B. 使用同步加载方式处理所有资源请求，在主线程中直接完成加载避免异步复杂度
- C. 只能本地加载
- D. 通过路径加载

**Q470.** [模块:M][维度:概念理解][难度:★★★★][题型:单选]

AssetBundle的依赖管理问题是什么？

- A. 依赖问题主要只影响编辑器打包阶段，运行时加载时通常不会再暴露出来
- B. 没有依赖问题
- C. 依赖关系只会影响Addressables，原生AssetBundle在运行时不会涉及共享资源引用管理
- D. 资源间有引用关系导致依赖AB必须先加载；多AB依赖同一资源可能导致资源冗余

**Q471.** [模块:M][维度:Bug诊断][难度:★★★★][题型:单选]

AssetBundle使用后不调用Unload的后果是？

- A. 只泄漏少量
- B. AB头信息和已加载资源留在内存中，导致内存泄漏
- C. 引擎内部会自动补偿参数差异
- D. Unity运行时通常会在场景切换后自动回收未释放的Bundle和其依赖资源，不会长期占用内存

**Q472.** [模块:M][维度:概念理解][难度:★★★★][题型:单选]

AssetBundle.Unload(true)和Unload(false)的区别是？

- A. true卸载AB和所有已加载的资源，false只卸载AB头但已加载的资源留在内存
- B. false卸载所有
- C. true只释放Bundle本体，运行中的实例对象通常还要结合引用关系和资源清理策略一起考虑
- D. 两者都会释放Bundle，只是是否连同已加载资源一起回收的范围不同

**Q473.** [模块:M][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

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

- A. 不需要Release
- B. 只是一个完成通知标记，资源本身的卸载时机完全由底层Bundle系统独立决定
- C. Addressables使用引用计数管理内存，Release减少引用计数，计数为0时自动卸载资源
- D. 会立即删除已实例化对象和底层资源，因此通常应在Instantiate之前就尽快调用

**Q474.** [模块:M][维度:概念理解][难度:★★★][题型:单选]

直接引用(Inspector拖拽)和间接引用(Resources/AB/Addressables)的区别是？

- A. 直接引用会将资源包含在场景/Prefab中自动加载，间接引用按需加载可控制时机
- B. 相关功能仅在旧版Unity中支持，最新版本已将其移除
- C. 间接引用一定性能更好，因为资源总能在真正访问时才加载且不会被场景静态依赖带入首包
- D. 直接引用不占内存

**Q475.** [模块:M][维度:性能优化][难度:★★★★][题型:单选]

资源内存优化方法包括？

- A. 将所有资源都设置为DontDestroyOnLoad以避免重复加载
- B. 使用Resources.Unload和AssetBundle.Unload
- C. 所有资源都使用LoadAll方法一次性加载到内存中
- D. 禁用Resources.UnloadUnusedAssets以避免卡顿

**Q476.** [模块:M][维度:概念理解][难度:★★★★][题型:单选]

Unity手游热更新的主流方案是？

- A. 主要还是重新下载整包或资源分包覆盖，脚本热更通常不是手游项目的主流方案
- B. 运行时不太支持真正热更新，更多只是把预置资源拆到远端重新下载替换
- C. 代码层：Lua(xLua/toLua)/ILRuntime/HybridCLR + 资源层：AssetBundle/Addressables远程下载
- D. 热更新只需要更新C#代码DLL即可，资源文件无需更新机制

**Q477.** [模块:M][维度:概念理解][难度:★★★][题型:单选]

AssetDatabase和Resources的使用时机区别是？

- A. AssetDatabase只在编辑器中使用（编辑器工具），Resources在运行时使用
- B. Resources主要也是编辑器工具链接口，正式运行时通常不会直接参与资源读取路径
- C. AssetDatabase运行时可用
- D. 两者主要区别只在API入口不同，实际使用时机没有非常严格的编辑器/运行时边界

**Q478.** [模块:M][维度:概念理解][难度:★★★★][题型:场景设计]

大型项目的资源管理架构应包含？

- A. 缓存层不是核心，现代设备IO足够快，重点更多在统一命名和目录结构管理
- B. 启动时全量预加载通常最稳定，因为能彻底避免运行中出现依赖遗漏和异步竞争问题
- C. 资源加载层(统一API)+缓存层(对象池+LRU缓存)+卸载策略+异步加载队列+引用计数
- D. 每个脚本自行加载

**Q479.** [模块:M][维度:概念理解][难度:★★★][题型:单选]

StreamingAssets文件夹的特点是？

- A. 更接近一个可直接访问的原始文件目录，通常用于存放视频、配置或平台原生需要读取的文件
- B. 自动加载到内存
- C. 可以热更新
- D. 文件原样打包（不压缩/不加密），运行时通过路径访问，各平台路径不同

**Q480.** [模块:M][维度:概念理解][难度:★★★★][题型:单选]

AssetBundle打包粒度的选择原则是？

- A. 所有资源一个包
- B. 随机分包
- C. 每个资源一个包能把热更新粒度做到最细，但需要谨慎评估依赖数量和运行时管理成本
- D. 按功能模块/场景分包，共用资源单独打包避免冗余，平衡包的数量和大小

**Q481.** [模块:M][维度:Bug诊断][难度:★★★★][题型:单选]

两个AssetBundle都引用了同一纹理但没有提取到公共包，会导致什么问题？

- A. 不会有问题
- B. 纹理在两个AB中各包含一份副本，浪费包体和内存
- C. 更常见的是公共纹理会被某个Bundle自动提升成运行时共享依赖，而不是直接导致加载失败
- D. Unity不会自动提公共包，但如果构建规则命中共享依赖分析，仍可能只保留一份资源副本

**Q482.** [模块:M][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

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

- A. 发现Catalog更新后会要求重启资源系统，后续资源通常要在下次启动时才按新配置加载
- B. 主要是提前下载所有远端资源依赖，避免真正使用资源时再触发下载等待
- C. 更新Catalog时会顺带清理旧的本地缓存资源，保证旧版本资源不会再被引用到
- D. 检查Catalog是否有更新，有则下载最新Catalog实现资源的远程热更新

**Q483.** [模块:M][维度:概念理解][难度:★★★][题型:单选]

实现资源加载进度条的方式是？

- A. AsyncOperation.progress获取进度值（0-0.9加载，0.9-1激活场景）
- B. 自己计时做假进度通常最稳妥，因为不同资源系统上报的实际进度往往不连续且不可直接映射
- C. 固定时间条只适合演示，正式项目一般还要叠加阶段权重或异步操作的真实完成度
- D. 很多资源系统能拿到完成度，只是有时需要自己把多个子任务进度做聚合显示

**Q484.** [模块:M][维度:性能优化][难度:★★★★][题型:单选]

资源预加载的策略是？

- A. 在Loading界面/场景切换时预加载下个场景需要的资源，减少运行时加载卡顿
- B. 在游戏启动时将所有资源一次性预加载到内存中，避免运行时加载造成的卡顿
- C. 可基于玩家路径、即将打开的UI或高频资源清单做有针对性的分阶段预加载，而不是随机选择
- D. 也可以完全不预加载，但前提通常是运行时访问频率低、资源足够小且允许瞬时加载抖动

**Q485.** [模块:M][维度:概念理解][难度:★★★★][题型:单选]

AssetBundle的CRC校验的作用是？

- A. 对所有数据进行AES-256加密存储，运行时解密后使用，确保数据安全性
- B. 签名，Asset Reference在序列化时保存的是资源的文件路径而非GUID
- C. 验证AB文件完整性（下载未损坏），防止损坏的AB被加载导致崩溃
- D. 使用GZIP压缩所有数据文件以减少包体大小和IO开销，运行时实时解压

**Q486.** [模块:M][维度:概念理解][难度:★★★][题型:单选]

AssetBundle支持的压缩方式有？

- A. ZIP、RAR、7Z、TAR
- B. LZMA、LZ4、无压缩
- C. Lossless、Lossy、Hybrid、None
- D. Huffman、Deflate、Brotli、Zstandard

**Q487.** [模块:M][维度:概念理解][难度:★★★★][题型:场景设计]

AssetBundle版本管理和增量更新方案应包含？

- A. 服务器Manifest对比+Hash比较确定增量+下载差异AB+本地缓存管理
- B. 可以完全在客户端本地比较文件时间戳和大小决定是否下载，不一定非要依赖服务端Manifest
- C. 每次全量下载
- D. 也可以不做复杂版本管理，只要资源命名规则稳定并允许全量覆盖更新即可

**Q488.** [模块:M][维度:概念理解][难度:★★★★][题型:单选]

Addressables的Profile配置的作用是？

- A. 音频配置
- B. 更像一组环境变量模板，可统一切换本地、测试、生产等资源地址与构建参数
- C. 配置不同环境（开发/测试/生产）的资源加载路径（本地/远程CDN等）
- D. 主要不是图形配置，但也常被用来区分不同质量档位或平台的远端内容入口地址

**Q489.** [模块:M][维度:概念理解][难度:★★★][题型:单选]

Resources.UnloadUnusedAssets()的工作原理是？

- A. 尝试卸载当前没有被场景、脚本或静态引用持有的资源对象，而不是无差别清空全部已加载资源
- B. 只卸载纹理
- C. 卸载所有没有被引用的资源，类似GC但针对Native资源
- D. 这是一个异步清理过程，通常要等引擎遍历引用关系后才能真正完成资源释放

**Q490.** [模块:M][维度:概念理解][难度:★★★★][题型:单选]

Scriptable Build Pipeline(SBP)和Addressables的关系是？

- A. Addressables不使用AB
- B. Addressables底层使用SBP来构建AssetBundle
- C. 不是完全独立，但SBP更多负责构建流程抽象，Addressables则负责运行时定位、分组和更新管理
- D. SBP替代Addressables

**Q491.** [模块:M][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

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

- A. 看起来更复杂，但它能把多个使用方共享同一资源的生命周期显式表达出来，避免随意卸载
- B. 重点不是延迟加载，而是把“谁还在用这份资源”这件事变成可统计、可回收的管理逻辑
- C. 精确控制资源生命周期，只有当所有使用者都释放后才真正卸载，避免提前卸载或泄漏
- D. 线程安全

**Q492.** [模块:M][维度:Bug诊断][难度:★★★★][题型:单选]

运行时加载Prefab后Material/Texture显示为品红色或丢失，可能原因是？

- A. 代码错误
- B. 纹理尺寸过大本身更常见的是内存或加载压力问题，品红色通常更应优先排查Shader/依赖资源缺失
- C. Shader不在AB中或所在AB未加载；需要确保Shader依赖被正确打包和加载
- D. 场景问题

**Q493.** [模块:M][维度:概念理解][难度:★★★★][题型:单选]

Addressables的Content Update Build的作用是？

- A. 只重新构建有变化的AB并生成差异Catalog，实现最小化的资源更新
- B. 它不是简单全量重构建，而是会在保留既有内容状态的前提下只产出需要更新的远端内容信息
- C. 它解决的是资源内容更新而不是代码热更，两者通常仍需分别设计发布链路
- D. 也不会删除所有AB，更多是更新Catalog和必要的差异包让客户端增量下载

**Q494.** [模块:M][维度:概念理解][难度:★★★★][题型:场景设计]

移动端游戏资源发布到CDN的流程是？

- A. 如果不做远程更新，CDN只剩下载整包安装器的意义，不再承担细粒度资源分发职责
- B. 构建AB→上传CDN→更新Catalog版本→客户端检查更新→下载增量AB→本地缓存
- C. 邮件分发显然不适用，但本质上仍需要一个可追踪版本、可校验缓存的远端分发流程
- D. 直接上传APK只能覆盖整包发版，不能替代资源CDN的增量更新与缓存复用能力

**Q495.** [模块:M][维度:概念理解][难度:★★★★][题型:单选]

Unity的Addressables Analyze工具的作用是？
---

- A. 不是性能分析工具，它更偏向检查资源分组、依赖、重复打包和更新策略方面的问题
- B. 也不分析代码性能，而是帮助找出资源构建层面的冗余、Bundle依赖和布局风险
- C. 分析内存
- D. 检查AB中的重复资源、潜在的依赖问题，帮助优化包体大小

**Q496.** [模块:J][维度:概念理解][难度:★★][题型:单选]

[RequireComponent(typeof(Rigidbody))]的作用是？

- A. 添加此脚本时自动添加Rigidbody组件，且防止在Inspector中移除Rigidbody
- B. 只有在游戏运行时首次启用该组件时才会动态补加Rigidbody
- C. 引擎内部会自动补偿参数差异
- D. 只是给Inspector显示提示文字，不会真正约束或补齐依赖组件

**Q497.** [模块:L][维度:概念理解][难度:★★★][题型:单选]

[CustomEditor(typeof(MyComponent))]的作用是？

- A. 自定义场景视图
- B. 创建新组件
- C. 为MyComponent创建自定义Inspector面板编辑器
- D. 脚本模板

**Q498.** [模块:M][维度:概念理解][难度:★★][题型:单选]

Addressables相比Resources的核心优势？

- A. 异步加载+引用计数+可远程分发+更灵活的分组和打包策略
- B. 只是改了API名字
- C. 不一定总是更快，但它把构建、寻址、远端更新和生命周期管理能力统一到了同一套工作流里
- D. 也不是完全一样，Addressables的优势更多在于分组、异步、远端内容和依赖管理而不是单纯换API

**Q499.** [模块:J][维度:概念理解][难度:★★★][题型:单选]

ScriptableObject作为事件通道(Event Channel)的设计模式好处是？

- A. 和普通委托没有本质区别，主要价值只是减少代码文件数量
- B. 不推荐，因为事件通道只能在编辑器模式下工作，构建后无法在运行时广播事件
- C. 解耦系统间的依赖(发布者和订阅者不直接引用)+可在编辑器中配置和调试
- D. 会显著增加系统耦合，因为所有发布者和订阅者都必须直接依赖同一个具体组件实例

**Q500.** [模块:L][维度:代码生成/阅读][难度:★★★][题型:代码补全]

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

- A. GUILayout.Slider两者可以混合使用
- B. GUI.Slider
- C. property.Draw两者可以混合使用
- D. EditorGUI.Slider(position, label, property.floatValue, range.min, range.max)

**Q501.** [模块:M][维度:概念理解][难度:★★★][题型:单选]

Addressables引用计数管理的原则是？

- A. 每次LoadAssetAsync匹配一次Release，引用计数归零时卸载资源
- B. 自动卸载
- C. 不需要Release，Asset Reference在序列化时保存的是资源的文件路径而非GUID
- D. 手动GC

**Q502.** [模块:L][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

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
- B. 该属性的修改必须在Awake阶段完成，运行时动态修改无效
- C. EditorGUILayout更快
- D. GUILayout更多功能

**Q503.** [模块:M][维度:性能优化][难度:★★★★][题型:单选]

Sprite Atlas对性能的影响？

- A. 只减少内存
- B. 多个小Sprite合并到一张纹理→减少Draw Call(同Atlas的Sprite可合批)+减少纹理切换开销
- C. 增加Draw Call
- D. 引擎内部会自动补偿参数差异

**Q504.** [模块:J][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

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

- A. 用属性本身直接替代运行时状态判断，标记后方法会自动只在正确状态下执行
- B. 只要加上这个特性，CLR就会在每次方法调用时自动检查当前状态并阻止非法调用
- C. 通过反射在方法调用前检查当前状态是否匹配Required State，实现声明式状态守卫
- D. 编译时检查，[SerializeReference]属性的序列化性能与[SerializeField]完全一致

**Q505.** [模块:L][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

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
- B. 删除纹理
- C. 压缩纹理
- D. 重命名两者可以混合使用

**Q506.** [模块:M][维度:架构设计][难度:★★★★][题型:场景设计]

大型项目资源管理系统需要的功能？

- A. 不需要专门的管理机制，Unity的GC和资源系统会自动回收不再使用的资源
- B. 统一加载接口+引用计数+自动卸载+预加载+依赖管理+内存预算+异步加载队列+资源分类
- C. 手动管理
- D. 小项目里 `Resources.Load` 也许能工作，但大型项目通常仍需要统一寻址、依赖、缓存和卸载策略来控成本

