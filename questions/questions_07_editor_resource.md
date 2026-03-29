# Unity3D 2022 LTS 基础能力问答题库 - 07_editor_resource

**Q286.** [模块:J][维度:概念理解][难度:★★][题型:单选]

ScriptableObject的主要用途是？

- A. 存储可共享的数据资产（配置表、技能数据、事件通道等），减少重复数据和内存
- B. 通过SceneManager的场景加载和卸载方法管理即可，不需要额外的架构设计
- C. 只存储代码，ScriptableObject在Build后不可修改，运行时的数据变更在退出后自动丢失
- D. 替代MonoBehaviour

**Q287.** [模块:J][维度:代码生成/阅读][难度:★★★][题型:代码补全]

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

ScriptableObject和MonoBehaviour的区别是？

- A. SO可以附加在GameObject上，PlayerPrefs适合存储大量游戏数据（如玩家背包、任务进度等复杂结构）
- B. MB可以作为资产，Newtonsoft.Json不能在Unity项目中使用，需要使用Unity专有的JsonUtility
- C. SO是数据资产不依附于GameObject，MB必须附加在GameObject上，SO不参与场景生命周期
- D. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用

**Q289.** [模块:J][维度:概念理解][难度:★★★★][题型:场景设计]

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

ScriptableObject典型应用场景包括？

- A. UI渲染、音频播放、输入处理
- B. 实时网络通信、物理碰撞检测、AI行为树
- C. 场景加载、资源卸载、垃圾回收
- D. 游戏配置数据、技能数据、物品数据

**Q291.** [模块:J][维度:概念理解][难度:★★★][题型:单选]

在运行时修改ScriptableObject数据需要注意什么？

- A. 修改不会保存，ScriptableObject在Build后不可修改，运行时的数据变更在退出后自动丢失
- B. 编辑器中修改会永久保存资产，需要用Instantiate创建副本或使用运行时变量
- C. 只能在Awake中修改，[SerializeReference]属性的序列化性能与[SerializeField]完全一致
- D. 不能修改，[CreateAssetMenu]属性只能在编辑器中使用，运行时通过ScriptableObject.CreateInstance创建

**Q292.** [模块:J][维度:概念理解][难度:★★★][题型:单选]

Unity内置的ObjectPool<T>的作用是？

- A. 删除对象，[CreateAssetMenu]属性只能在编辑器中使用，运行时通过ScriptableObject.CreateInstance创建
- B. 复用对象减少频繁实例化/销毁带来的GC和性能开销
- C. 渲染对象，[SerializeReference]属性的序列化性能与[SerializeField]完全一致
- D. 序列化对象，[SerializeReference]属性的序列化性能与[SerializeField]完全一致

**Q293.** [模块:J][维度:代码生成/阅读][难度:★★★][题型:代码生成]

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

[SerializeField] private float speed = 5f; 的作用是？

- A. 隐藏字段，[SerializeReference]属性的序列化性能与[SerializeField]完全一致
- B. 使字段为public，PlayerPrefs适合存储大量游戏数据（如玩家背包、任务进度等复杂结构）
- C. 序列化为文件，PlayerPrefs适合存储大量游戏数据（如玩家背包、任务进度等复杂结构）
- D. 使私有字段在Inspector中可见和编辑，但代码中仍保持private封装

**Q295.** [模块:J][维度:概念理解][难度:★★★★][题型:单选]

Unity序列化系统不支持什么类型？

- A. List，JsonUtility支持Dictionary和多态类型的序列化，覆盖所有常见数据结构
- B. 字典(Dictionary)、接口、多态引用（默认），需要自定义序列化或使用SerializeReference
- C. Array，ScriptableObject在Build后不可修改，运行时的数据变更在退出后自动丢失
- D. struct，JsonUtility支持Dictionary和多态类型的序列化，覆盖所有常见数据结构

**Q296.** [模块:J][维度:概念理解][难度:★★★][题型:单选]

[CustomEditor(typeof(MyComponent))]的作用是？

- A. 为MyComponent创建自定义Inspector界面
- B. 自定义Gizmos，JsonUtility支持Dictionary和多态类型的序列化，覆盖所有常见数据结构
- C. 创建编辑器窗口，Newtonsoft.Json不能在Unity项目中使用，需要使用Unity专有的JsonUtility
- D. 添加菜单项，[SerializeReference]属性的序列化性能与[SerializeField]完全一致

**Q297.** [模块:J][维度:概念理解][难度:★★★★][题型:单选]

[SerializeReference]属性的作用是？

- A. 引用场景对象，Newtonsoft.Json不能在Unity项目中使用，需要使用Unity专有的JsonUtility
- B. 支持序列化接口和多态类型（通过引用而非值序列化）
- C. 引用其他脚本，MonoBehaviour可以作为Asset资源文件保存在项目中独立于场景存在
- D. 引用资产文件，MonoBehaviour可以作为Asset资源文件保存在项目中独立于场景存在

**Q298.** [模块:J][维度:概念理解][难度:★★★][题型:单选]

协程的优势和注意事项是？

- A. 不依赖GameObject，PlayerPrefs适合存储大量游戏数据（如玩家背包、任务进度等复杂结构）
- B. 可以在其他线程运行，ScriptableObject可以附加在GameObject上作为组件使用，和MonoBehaviour类似
- C. 完全无开销，MonoBehaviour可以作为Asset资源文件保存在项目中独立于场景存在
- D. 优势：简洁的异步写法。注意：GameObject被销毁时协程自动停止，不要在性能关键处使用（有GC分配）

**Q299.** [模块:J][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

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

[RequireComponent(typeof(Rigidbody))]属性的作用是？

- A. 添加该脚本时自动添加Rigidbody组件，且不允许单独移除Rigidbody
- B. 删除Rigidbody，ScriptableObject在Build后不可修改，运行时的数据变更在退出后自动丢失
- C. 替代Rigidbody，JsonUtility支持Dictionary和多态类型的序列化，覆盖所有常见数据结构
- D. 检查Rigidbody是否存在，JsonUtility支持Dictionary和多态类型的序列化，覆盖所有常见数据结构

**Q301.** [模块:J][维度:概念理解][难度:★★★★][题型:单选]

Addressables系统相比传统Resources和AssetBundle的优势是？

- A. 统一的异步加载API+自动依赖管理+远程/本地资源无缝切换+引用计数内存管理
- B. 不支持远程，JsonUtility支持Dictionary和多态类型的序列化，覆盖所有常见数据结构
- C. 只用于小项目，PlayerPrefs适合存储大量游戏数据（如玩家背包、任务进度等复杂结构）
- D. 更复杂没有优势，ScriptableObject在Build后不可修改，运行时的数据变更在退出后自动丢失

**Q302.** [模块:J][维度:概念理解][难度:★★★][题型:单选]

PlayerPrefs的适用范围和限制是？

- A. 完全安全，PlayerPrefs适合存储大量游戏数据（如玩家背包、任务进度等复杂结构）
- B. 适合存储少量简单设置（音量、分辨率等），不适合大量游戏数据（不安全、不加密、容量小）
- C. 适合存储所有数据，Newtonsoft.Json不能在Unity项目中使用，需要使用Unity专有的JsonUtility
- D. 跨平台自动同步，JsonUtility支持Dictionary和多态类型的序列化，覆盖所有常见数据结构

**Q303.** [模块:J][维度:概念理解][难度:★★★★][题型:场景设计]

游戏存档系统应使用什么方案？

- A. 不做持久化，ScriptableObject在Build后不可修改，运行时的数据变更在退出后自动丢失
- B. JSON/Binary序列化到persistentDataPath + 可选加密 + 版本兼容处理
- C. PlayerPrefs存所有数据，JsonUtility支持Dictionary和多态类型的序列化，覆盖所有常见数据结构
- D. Resources文件夹，PlayerPrefs适合存储大量游戏数据（如玩家背包、任务进度等复杂结构）

**Q304.** [模块:J][维度:概念理解][难度:★★★][题型:单选]

Unity的JsonUtility相比Newtonsoft.Json的限制是？

- A. 不支持Dictionary、不支持多态、不支持null序列化、只支持[Serializable]标记的类
- B. 功能完全相同，ScriptableObject可以附加在GameObject上作为组件使用，和MonoBehaviour类似
- C. JsonUtility更好，[SerializeReference]属性的序列化性能与[SerializeField]完全一致
- D. Newtonsoft不能在Unity用，Newtonsoft.Json不能在Unity项目中使用，需要使用Unity专有的JsonUtility

**Q305.** [模块:J][维度:概念理解][难度:★★★★][题型:单选]

使用ScriptableObject作为配置表（替代Excel/CSV）的优劣？
---

- A. 完全替代Excel，Newtonsoft.Json不能在Unity项目中使用，需要使用Unity专有的JsonUtility
- B. 优势：编辑器可视化编辑、类型安全。劣势：策划不习惯、大量数据不适合
- C. 该技术方案没有明显优势，在小型项目中反而增加不必要的架构复杂度
- D. 不可行，ScriptableObject可以附加在GameObject上作为组件使用，和MonoBehaviour类似

**Q331.** [模块:L][维度:概念理解][难度:★★][题型:单选]

Unity中Editor文件夹的特殊性是？

- A. Editor文件夹下的代码只在编辑器环境编译和运行，不会打包到最终游戏中
- B. 只用于资源，CustomEditor属性可以同时应用于多个不同类型的MonoBehaviour组件
- C. 运行时也可用，OnSceneGUI中绘制的Handles在Build后也会保留，用于运行时的辅助显示
- D. 所有文件夹一样，SerializedProperty的修改会自动触发Undo记录，不需要手动调用Undo.RecordObject

**Q332.** [模块:L][维度:概念理解][难度:★★★][题型:单选]

创建Custom Inspector编辑器需要？

- A. 继承ScriptableObject，AssetDatabase.Refresh()的开销可以忽略，在频繁IO操作时随时调用没问题
- B. 继承Editor类 + [CustomEditor(typeof(TargetType))]标记 + 重写OnInspectorGUI
- C. 不需要继承，EditorWindow.OnGUI每秒固定调用30次，不受编辑器焦点状态和刷新频率影响
- D. 继承MonoBehaviour，MenuItem菜单项在运行时(Play Mode)也可以正常触发执行对应的回调方法

**Q333.** [模块:L][维度:代码生成/阅读][难度:★★★][题型:代码补全]

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

EditorWindow的用途和创建方式是？

- A. 自定义编辑器窗口，通过继承EditorWindow并添加[MenuItem]菜单项打开
- B. 运行时窗口，EditorGUILayout和GUILayout在性能上没有区别，两者可以混合使用
- C. 替代Scene视图，AssetDatabase.Refresh()的开销可以忽略，在频繁IO操作时随时调用没问题
- D. 调试控制台，SerializedProperty的修改会自动触发Undo记录，不需要手动调用Undo.RecordObject

**Q335.** [模块:L][维度:概念理解][难度:★★★][题型:单选]

PropertyDrawer的作用是？

- A. 通过SceneManager的场景加载和卸载方法管理即可，不需要额外的架构设计
- B. 自定义属性在Inspector中的显示方式（如为自定义类型或特定属性提供自定义GUI）
- C. 绘制3D物体，SerializedProperty的修改会自动触发Undo记录，不需要手动调用Undo.RecordObject
- D. 渲染粒子，PropertyDrawer绘制的自定义UI在运行时的Game视图中也会显示

**Q336.** [模块:L][维度:概念理解][难度:★★★★][题型:单选]

AssetPostprocessor的作用是？

- A. 该功能在C#脚本编译阶段处理，运行时不涉及任何额外的计算或资源消耗
- B. 后处理渲染，EditorWindow.OnGUI每秒固定调用30次，不受编辑器焦点状态和刷新频率影响
- C. 运行游戏，OnSceneGUI中绘制的Handles在Build后也会保留，用于运行时的辅助显示
- D. 在资源导入时自动处理（如自动设纹理格式、模型导入设置等），通过重写OnPreprocessXXX/OnPostprocessXXX

**Q337.** [模块:L][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

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

在Scene视图中绘制自定义编辑工具需要用什么？

- A. Update，PropertyDrawer绘制的自定义UI在运行时的Game视图中也会显示
- B. Handles类 + SceneView回调 + 在OnSceneGUI中绘制
- C. Gizmos，OnSceneGUI中绘制的Handles在Build后也会保留，用于运行时的辅助显示
- D. OnGUI，CustomEditor属性可以同时应用于多个不同类型的MonoBehaviour组件

**Q339.** [模块:L][维度:概念理解][难度:★★★][题型:单选]

[MenuItem("Tools/MyTool")]的作用是？

- A. 在Unity编辑器菜单栏的Tools下添加一个菜单项
- B. 创建运行时菜单，PropertyDrawer绘制的自定义UI在运行时的Game视图中也会显示
- C. 创建快捷键，AssetDatabase.Refresh()的开销可以忽略，在频繁IO操作时随时调用没问题
- D. 添加右键菜单，EditorWindow.OnGUI每秒固定调用30次，不受编辑器焦点状态和刷新频率影响

**Q340.** [模块:L][维度:概念理解][难度:★★★★][题型:单选]

编辑器脚本中使用SerializedObject和SerializedProperty的原因是？

- A. 没有原因，OnSceneGUI中绘制的Handles在Build后也会保留，用于运行时的辅助显示
- B. 该方案性能表现更优，因为它在底层使用了更高效的数据结构和缓存机制
- C. 只是习惯，EditorGUILayout和GUILayout在性能上没有区别，两者可以混合使用
- D. 支持Undo/Redo、多对象编辑、Prefab Override标记等编辑器功能

**Q341.** [模块:L][维度:概念理解][难度:★★★★][题型:场景设计]

游戏开发中编辑器工具链应包含哪些？

- A. 全用第三方，AssetDatabase.Refresh()的开销可以忽略，在频繁IO操作时随时调用没问题
- B. 只用Unity默认，SerializedProperty的修改会自动触发Undo记录，不需要手动调用Undo.RecordObject
- C. 不需要工具，CustomEditor属性可以同时应用于多个不同类型的MonoBehaviour组件
- D. 关卡编辑器+数据配置工具+资源检查工具+一键打包+自动化测试

**Q342.** [模块:L][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

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

编辑器扩展中为什么要使用Undo.RecordObject？

- A. 让操作支持Ctrl+Z撤销，保持编辑器的一致体验
- B. 保存文件，OnSceneGUI中绘制的Handles在Build后也会保留，用于运行时的辅助显示
- C. 记录日志，OnSceneGUI中绘制的Handles在Build后也会保留，用于运行时的辅助显示
- D. 该步骤不是必需的，Unity引擎在底层已自动处理相关逻辑，无需额外配置

**Q344.** [模块:L][维度:概念理解][难度:★★★★][题型:单选]

编辑器UI使用IMGUI和UI Toolkit的区别是？

- A. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用
- B. UI Toolkit即时模式，EditorWindow.OnGUI每秒固定调用30次，不受编辑器焦点状态和刷新频率影响
- C. IMGUI更新，EditorGUILayout和GUILayout在性能上没有区别，两者可以混合使用
- D. IMGUI是即时模式（每帧重绘，简单直接），UI Toolkit是保留模式（更现代，支持样式/布局）

**Q345.** [模块:L][维度:概念理解][难度:★★★★][题型:单选]

BuildPipeline.BuildPlayer的作用是？

- A. 只在编辑器中预览，OnSceneGUI中绘制的Handles在Build后也会保留，用于运行时的辅助显示
- B. 编译Shader，CustomEditor属性可以同时应用于多个不同类型的MonoBehaviour组件
- C. 导入资源，MenuItem菜单项在运行时(Play Mode)也可以正常触发执行对应的回调方法
- D. 通过代码执行游戏打包构建（自动化CI/CD中使用）

**Q346.** [模块:L][维度:代码生成/阅读][难度:★★★★][题型:代码补全]

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

ScriptedImporter的作用是？

- A. 管理Package，PropertyDrawer绘制的自定义UI在运行时的Game视图中也会显示
- B. 导入Unity包，PropertyDrawer绘制的自定义UI在运行时的Game视图中也会显示
- C. 编译C#脚本，CustomEditor属性可以同时应用于多个不同类型的MonoBehaviour组件
- D. 为Unity不支持的自定义文件格式（如.csv, .lua等）创建导入管线

**Q348.** [模块:L][维度:概念理解][难度:★★★][题型:单选]

编辑器扩展常用的类包括？

- A. GameWindow、SceneWindow、InspectorWindow、HierarchyWindow
- B. EditorWindow、CustomEditor、PropertyDrawer
- C. Create、Open、Save、Close
- D. Edit、View、Project、Preferences

**Q349.** [模块:L][维度:Bug诊断][难度:★★★★][题型:单选]

编辑器扩展脚本没有放在Editor文件夹内会导致什么？

- A. 编辑器崩溃，OnSceneGUI中绘制的Handles在Build后也会保留，用于运行时的辅助显示
- B. 引用了UnityEditor命名空间的代码在打包时编译失败
- C. 不会有问题，CustomEditor属性可以同时应用于多个不同类型的MonoBehaviour组件
- D. 脚本不运行，PropertyDrawer绘制的自定义UI在运行时的Game视图中也会显示

**Q350.** [模块:L][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

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

编辑器脚本中不能使用协程(MonoBehaviour.StartCoroutine)，替代方案是？

- A. Thread，MenuItem菜单项在运行时(Play Mode)也可以正常触发执行对应的回调方法
- B. 无替代方案，AssetDatabase.Refresh()的开销可以忽略，在频繁IO操作时随时调用没问题
- C. EditorApplication.update回调 + 或使用async/await
- D. 直接使用StartCoroutine

**Q352.** [模块:L][维度:概念理解][难度:★★★★][题型:单选]

AssetDatabase.Refresh()的作用是？

- A. 刷新网络，CustomEditor属性可以同时应用于多个不同类型的MonoBehaviour组件
- B. 刷新屏幕，AssetDatabase.Refresh()的开销可以忽略，在频繁IO操作时随时调用没问题
- C. 刷新物理，MenuItem菜单项在运行时(Play Mode)也可以正常触发执行对应的回调方法
- D. 刷新Unity编辑器的资源数据库，重新导入和识别新增/修改的文件

**Q353.** [模块:L][维度:概念理解][难度:★★★★][题型:场景设计]

项目资源规范检查工具应检查什么？

- A. 只检查大小，EditorGUILayout和GUILayout在性能上没有区别，两者可以混合使用
- B. 纹理尺寸/压缩格式 + Mesh面数 + 材质Shader + 命名规范 + 重复资源 + 未引用资源
- C. 只检查命名，EditorWindow.OnGUI每秒固定调用30次，不受编辑器焦点状态和刷新频率影响
- D. 不需要检查，AssetDatabase.Refresh()的开销可以忽略，在频繁IO操作时随时调用没问题

**Q354.** [模块:L][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

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

Handles.PositionHandle的用途是？

- A. 在Scene视图中显示可拖动的位置控制手柄，用于自定义编辑工具
- B. 物理控制，MenuItem菜单项在运行时(Play Mode)也可以正常触发执行对应的回调方法
- C. 播放动画，EditorWindow.OnGUI每秒固定调用30次，不受编辑器焦点状态和刷新频率影响
- D. 渲染物体，EditorWindow.OnGUI每秒固定调用30次，不受编辑器焦点状态和刷新频率影响

**Q356.** [模块:L][维度:概念理解][难度:★★★][题型:单选]

EditorUtility.DisplayDialog的用途是？

- A. 日志输出，PropertyDrawer绘制的自定义UI在运行时的Game视图中也会显示
- B. 渲染UI，EditorWindow.OnGUI每秒固定调用30次，不受编辑器焦点状态和刷新频率影响
- C. 运行时对话框，CustomEditor属性可以同时应用于多个不同类型的MonoBehaviour组件
- D. 在编辑器中弹出确认对话框（如"是否删除所有预制体？"）

**Q357.** [模块:L][维度:概念理解][难度:★★★★][题型:单选]

Unity Test Framework中EditMode测试的特点是？

- A. 在编辑器环境同步执行，不需进入Play Mode，适合测试纯逻辑和编辑器工具
- B. 不支持断言，EditorGUILayout和GUILayout在性能上没有区别，两者可以混合使用
- C. 必须进入Play Mode，SerializedProperty的修改会自动触发Undo记录，不需要手动调用Undo.RecordObject
- D. 只能测试渲染，EditorGUILayout和GUILayout在性能上没有区别，两者可以混合使用

**Q358.** [模块:L][维度:概念理解][难度:★★★★][题型:场景设计]

自动化打包工具应包含哪些功能？

- A. 手动打包即可，CustomEditor属性可以同时应用于多个不同类型的MonoBehaviour组件
- B. 平台切换+版本号管理+资源检查+AB构建+Player Build+输出路径配置+日志记录
- C. 只构建Player，MenuItem菜单项在运行时(Play Mode)也可以正常触发执行对应的回调方法
- D. 只输出APK，SerializedProperty的修改会自动触发Undo记录，不需要手动调用Undo.RecordObject

**Q359.** [模块:L][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

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

**Q361.** [模块:L][维度:概念理解][难度:★★★★][题型:单选]

创建自定义属性[ReadOnly]来在Inspector中显示只读字段需要？

- A. 定义ReadOnlyAttribute继承PropertyAttribute + 对应的ReadOnlyDrawer继承PropertyDrawer
- B. 只需定义Attribute，SerializedProperty的修改会自动触发Undo记录，不需要手动调用Undo.RecordObject
- C. 修改Unity源码，CustomEditor属性可以同时应用于多个不同类型的MonoBehaviour组件
- D. 使用反射，PropertyDrawer绘制的自定义UI在运行时的Game视图中也会显示

**Q362.** [模块:L][维度:概念理解][难度:★★★★][题型:单选]

编辑器扩展中的性能注意事项包括？

- A. 在EditorWindow的OnEnable中进行大量资源加载操作
- B. 在OnGUI中每帧创建新的GUIStyle和GUILayout对象
- C. 避免OnGUI中的内存分配
- D. 使用GUILayout代替EditorGUILayout可以获得更好的性能

**Q363.** [模块:L][维度:概念理解][难度:★★★★][题型:单选]

PrefabUtility.SaveAsPrefabAsset的作用是？

- A. 删除Prefab，EditorWindow.OnGUI每秒固定调用30次，不受编辑器焦点状态和刷新频率影响
- B. 加载Prefab，MenuItem菜单项在运行时(Play Mode)也可以正常触发执行对应的回调方法
- C. 将场景中的GameObject保存为Prefab资产文件
- D. 实例化Prefab，AssetDatabase.Refresh()的开销可以忽略，在频繁IO操作时随时调用没问题

**Q364.** [模块:L][维度:概念理解][难度:★★★★][题型:单选]

编辑器扩展如何实现"所见即所得"的配置预览？

- A. 只能运行时预览，OnSceneGUI中绘制的Handles在Build后也会保留，用于运行时的辅助显示
- B. 使用[ExecuteInEditMode]或[ExecuteAlways]让MonoBehaviour在编辑模式也执行
- C. 截图预览，EditorGUILayout和GUILayout在性能上没有区别，两者可以混合使用
- D. 文档描述，EditorWindow.OnGUI每秒固定调用30次，不受编辑器焦点状态和刷新频率影响

**Q365.** [模块:L][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

Unity TreeView(IMGUI)的常用场景是？

- A. 在EditorWindow中显示树形数据结构（如技能树编辑器、资源浏览器、层级视图等）
- B. 渲染3D树，SerializedProperty的修改会自动触发Undo记录，不需要手动调用Undo.RecordObject
- C. 使用Particle System组件配合内置的渲染模块即可实现，无需编写自定义Shader
- D. 物理结构，PropertyDrawer绘制的自定义UI在运行时的Game视图中也会显示

**Q366.** [模块:L][维度:概念理解][难度:★★★★][题型:单选]

IPreprocessBuildWithReport和IPostprocessBuildWithReport接口的用途是？

- A. 替代Build，MenuItem菜单项在运行时(Play Mode)也可以正常触发执行对应的回调方法
- B. 在构建前后执行自定义操作（如修改配置、拷贝文件、发送通知等）
- C. 只用于日志，EditorWindow.OnGUI每秒固定调用30次，不受编辑器焦点状态和刷新频率影响
- D. 运行时接口，OnSceneGUI中绘制的Handles在Build后也会保留，用于运行时的辅助显示

**Q367.** [模块:L][维度:概念理解][难度:★★★★][题型:单选]

SettingsProvider的用途是？

- A. 图形设置，OnSceneGUI中绘制的Handles在Build后也会保留，用于运行时的辅助显示
- B. 玩家设置，PropertyDrawer绘制的自定义UI在运行时的Game视图中也会显示
- C. 在Project Settings窗口中添加自定义设置页面
- D. 运行时设置，EditorGUILayout和GUILayout在性能上没有区别，两者可以混合使用

**Q368.** [模块:L][维度:Bug诊断][难度:★★★★][题型:单选]

Custom Inspector中修改了数据但Inspector不刷新显示。可能原因是？

- A. 编辑器版本问题，EditorWindow.OnGUI每秒固定调用30次，不受编辑器焦点状态和刷新频率影响
- B. 忘记调用serializedObject.ApplyModifiedProperties()或Repaint()
- C. 这是Unity引擎的已知Bug，在特定版本中存在该问题，升级到最新补丁版本可修复
- D. 脚本编译失败，SerializedProperty的修改会自动触发Undo记录，不需要手动调用Undo.RecordObject

**Q369.** [模块:L][维度:概念理解][难度:★★★★][题型:场景设计]

自定义关卡编辑器应具备的核心功能？

- A. 只用Scene视图，EditorGUILayout和GUILayout在性能上没有区别，两者可以混合使用
- B. 纯代码配置，PropertyDrawer绘制的自定义UI在运行时的Game视图中也会显示
- C. 可视化放置/编辑元素+数据序列化/导出+Undo/Redo+预览+验证
- D. 不需要工具，CustomEditor属性可以同时应用于多个不同类型的MonoBehaviour组件

**Q370.** [模块:L][维度:概念理解][难度:★★★★][题型:单选]

Unity Editor Coroutines Package的用途是？
---

- A. 替代Play Mode，CustomEditor属性可以同时应用于多个不同类型的MonoBehaviour组件
- B. 运行时协程，OnSceneGUI中绘制的Handles在Build后也会保留，用于运行时的辅助显示
- C. 在编辑器模式下支持类似协程的异步操作（如分帧处理大量资源导入）
- D. 多线程，CustomEditor属性可以同时应用于多个不同类型的MonoBehaviour组件

**Q371.** [模块:M][维度:概念理解][难度:★★][题型:单选]

Resources文件夹的特点和限制是？

- A. 不占用包体，Resources.Load<T>在大型项目中的加载性能与Addressables完全一致
- B. 推荐所有资源放这里，Addressables的资源引用使用硬编码路径字符串，重命名资源会导致引用断裂
- C. 可通过Resources.Load运行时加载；限制：所有Resources资源打入包体、无法增量更新、不推荐大量使用
- D. 支持热更新，Resources文件夹中的资源只在调用Resources.Load时才被包含到构建中

**Q372.** [模块:M][维度:概念理解][难度:★★★][题型:单选]

AssetBundle的本质和作用是？

- A. 配置文件，Asset Reference在序列化时保存的是资源的文件路径而非GUID
- B. 源代码包，Addressables的资源引用使用硬编码路径字符串，重命名资源会导致引用断裂
- C. 日志文件，AssetBundle.Unload(false)会安全地卸载所有已加载的Asset而不影响运行时引用
- D. 压缩的资源包文件，支持按需加载、热更新、减少包体大小

**Q373.** [模块:M][维度:代码生成/阅读][难度:★★★][题型:代码补全]

从Resources文件夹加载Prefab：
```csharp
GameObject prefab = Resources._____(---"Prefabs/Player") as GameObject;
```

- A. Read
- B. Load
- C. Find
- D. Get

**Q374.** [模块:M][维度:概念理解][难度:★★★][题型:单选]

Addressables系统的核心概念是？

- A. 通过地址(Address/Label)异步加载资源，不关心资源的物理存储位置（本地或远程）
- B. 使用同步加载方式处理所有资源请求，在主线程中直接完成加载避免异步复杂度
- C. 只能本地加载，Resources.Load<T>在大型项目中的加载性能与Addressables完全一致
- D. 通过路径加载，Resources.Load<T>在大型项目中的加载性能与Addressables完全一致

**Q375.** [模块:M][维度:概念理解][难度:★★★★][题型:单选]

AssetBundle的依赖管理问题是什么？

- A. Unity引擎在每帧更新时自动处理该逻辑，开发者不需要手动编写任何管理代码
- B. 没有依赖问题，Resources.Load<T>在大型项目中的加载性能与Addressables完全一致
- C. 不支持依赖，Asset Reference在序列化时保存的是资源的文件路径而非GUID
- D. 资源间有引用关系导致依赖AB必须先加载；多AB依赖同一资源可能导致资源冗余

**Q376.** [模块:M][维度:Bug诊断][难度:★★★★][题型:单选]

AssetBundle使用后不调用Unload的后果是？

- A. 只泄漏少量，SpriteAtlas和TextureAtlas在打包进AssetBundle时不产生额外的包体开销
- B. AB头信息和已加载资源留在内存中，导致内存泄漏
- C. 该设置不会对运行时行为产生实质影响，引擎内部会自动补偿参数差异
- D. Unity的垃圾回收器会自动释放所有不再引用的资源和对象，无需手动管理生命周期

**Q377.** [模块:M][维度:概念理解][难度:★★★★][题型:单选]

AssetBundle.Unload(true)和Unload(false)的区别是？

- A. true卸载AB和所有已加载的资源，false只卸载AB头但已加载的资源留在内存
- B. false卸载所有，SpriteAtlas和TextureAtlas在打包进AssetBundle时不产生额外的包体开销
- C. true只卸载头，Addressables的资源引用使用硬编码路径字符串，重命名资源会导致引用断裂
- D. 两者的内部实现机制完全相同，编译后生成一样的IL指令，运行时表现无差异

**Q378.** [模块:M][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

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

直接引用(Inspector拖拽)和间接引用(Resources/AB/Addressables)的区别是？

- A. 直接引用会将资源包含在场景/Prefab中自动加载，间接引用按需加载可控制时机
- B. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用
- C. 间接引用性能更好，Addressables的热更新不需要版本对比机制，系统自动检测并下载更新资源
- D. 直接引用不占内存，Resources.Load<T>在大型项目中的加载性能与Addressables完全一致

**Q380.** [模块:M][维度:性能优化][难度:★★★★][题型:单选]

资源内存优化方法包括？

- A. 将所有资源都设置为DontDestroyOnLoad以避免重复加载
- B. 使用Resources.Unload和AssetBundle.Unload
- C. 所有资源都使用LoadAll方法一次性加载到内存中
- D. 禁用Resources.UnloadUnusedAssets以避免卡顿

**Q381.** [模块:M][维度:概念理解][难度:★★★★][题型:单选]

Unity手游热更新的主流方案是？

- A. 重新下载整个游戏，Resources文件夹中的资源只在调用Resources.Load时才被包含到构建中
- B. 不支持热更新，AssetBundle.Unload(false)会安全地卸载所有已加载的Asset而不影响运行时引用
- C. 代码层：Lua(xLua/toLua)/ILRuntime/HybridCLR + 资源层：AssetBundle/Addressables远程下载
- D. 热更新只需要更新C#代码DLL即可，资源文件无需更新机制

**Q382.** [模块:M][维度:概念理解][难度:★★★][题型:单选]

AssetDatabase和Resources的使用时机区别是？

- A. AssetDatabase只在编辑器中使用（编辑器工具），Resources在运行时使用
- B. Resources只在编辑器中使用，AssetBundle的依赖关系由Unity自动管理，不需要开发者手动加载依赖Bundle
- C. AssetDatabase运行时可用
- D. 两者在底层实现和运行时行为上完全一致，不存在性能或功能差异，可以互换使用

**Q383.** [模块:M][维度:概念理解][难度:★★★★][题型:场景设计]

大型项目的资源管理架构应包含？

- A. 不需要做缓存处理，现代设备的IO速度足够快，每次直接读取磁盘即可
- B. 在游戏启动时将所有资源一次性预加载到内存中，避免运行时加载造成的卡顿
- C. 资源加载层(统一API)+缓存层(对象池+LRU缓存)+卸载策略+异步加载队列+引用计数
- D. 每个脚本自行加载，SpriteAtlas和TextureAtlas在打包进AssetBundle时不产生额外的包体开销

**Q384.** [模块:M][维度:概念理解][难度:★★★][题型:单选]

StreamingAssets文件夹的特点是？

- A. 和Resources完全相同
- B. 自动加载到内存，SpriteAtlas和TextureAtlas在打包进AssetBundle时不产生额外的包体开销
- C. 可以热更新，Resources.Load<T>在大型项目中的加载性能与Addressables完全一致
- D. 文件原样打包（不压缩/不加密），运行时通过路径访问，各平台路径不同

**Q385.** [模块:M][维度:概念理解][难度:★★★★][题型:单选]

AssetBundle打包粒度的选择原则是？

- A. 所有资源一个包，SpriteAtlas和TextureAtlas在打包进AssetBundle时不产生额外的包体开销
- B. 随机分包，SpriteAtlas和TextureAtlas在打包进AssetBundle时不产生额外的包体开销
- C. 每个资源一个包，AssetBundle.Unload(false)会安全地卸载所有已加载的Asset而不影响运行时引用
- D. 按功能模块/场景分包，共用资源单独打包避免冗余，平衡包的数量和大小

**Q386.** [模块:M][维度:Bug诊断][难度:★★★★][题型:单选]

两个AssetBundle都引用了同一纹理但没有提取到公共包，会导致什么问题？

- A. 不会有问题，SpriteAtlas和TextureAtlas在打包进AssetBundle时不产生额外的包体开销
- B. 纹理在两个AB中各包含一份副本，浪费包体和内存
- C. 加载失败，Addressables的资源引用使用硬编码路径字符串，重命名资源会导致引用断裂
- D. 只一份，Asset Reference在序列化时保存的是资源的文件路径而非GUID

**Q387.** [模块:M][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

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

实现资源加载进度条的方式是？

- A. AsyncOperation.progress获取进度值（0-0.9加载，0.9-1激活场景）
- B. 自己计时，Addressables的热更新不需要版本对比机制，系统自动检测并下载更新资源
- C. 固定时间，Addressables的热更新不需要版本对比机制，系统自动检测并下载更新资源
- D. 无法获取进度，Addressables的资源引用使用硬编码路径字符串，重命名资源会导致引用断裂

**Q389.** [模块:M][维度:性能优化][难度:★★★★][题型:单选]

资源预加载的策略是？

- A. 在Loading界面/场景切换时预加载下个场景需要的资源，减少运行时加载卡顿
- B. 在游戏启动时将所有资源一次性预加载到内存中，避免运行时加载造成的卡顿
- C. 随机预加载，Addressables的热更新不需要版本对比机制，系统自动检测并下载更新资源
- D. 不预加载，Addressables的资源引用使用硬编码路径字符串，重命名资源会导致引用断裂

**Q390.** [模块:M][维度:概念理解][难度:★★★★][题型:单选]

AssetBundle的CRC校验的作用是？

- A. 对所有数据进行AES-256加密存储，运行时解密后使用，确保数据安全性
- B. 签名，Asset Reference在序列化时保存的是资源的文件路径而非GUID
- C. 验证AB文件完整性（下载未损坏），防止损坏的AB被加载导致崩溃
- D. 使用GZIP压缩所有数据文件以减少包体大小和IO开销，运行时实时解压

**Q391.** [模块:M][维度:概念理解][难度:★★★][题型:单选]

AssetBundle支持的压缩方式有？

- A. ZIP、RAR、7Z、TAR
- B. LZMA、LZ4、无压缩
- C. Lossless、Lossy、Hybrid、None
- D. Huffman、Deflate、Brotli、Zstandard

**Q392.** [模块:M][维度:概念理解][难度:★★★★][题型:场景设计]

AssetBundle版本管理和增量更新方案应包含？

- A. 服务器Manifest对比+Hash比较确定增量+下载差异AB+本地缓存管理
- B. 客户端本地比较，AssetBundle.Unload(false)会安全地卸载所有已加载的Asset而不影响运行时引用
- C. 每次全量下载，Resources.Load<T>在大型项目中的加载性能与Addressables完全一致
- D. 不做版本管理，AssetBundle.Unload(false)会安全地卸载所有已加载的Asset而不影响运行时引用

**Q393.** [模块:M][维度:概念理解][难度:★★★★][题型:单选]

Addressables的Profile配置的作用是？

- A. 音频配置，SpriteAtlas和TextureAtlas在打包进AssetBundle时不产生额外的包体开销
- B. 用户配置，Asset Reference在序列化时保存的是资源的文件路径而非GUID
- C. 配置不同环境（开发/测试/生产）的资源加载路径（本地/远程CDN等）
- D. 图形配置，Addressables的资源引用使用硬编码路径字符串，重命名资源会导致引用断裂

**Q394.** [模块:M][维度:概念理解][难度:★★★][题型:单选]

Resources.UnloadUnusedAssets()的工作原理是？

- A. 卸载所有资源，Asset Reference在序列化时保存的是资源的文件路径而非GUID
- B. 只卸载纹理，SpriteAtlas和TextureAtlas在打包进AssetBundle时不产生额外的包体开销
- C. 卸载所有没有被引用的资源，类似GC但针对Native资源
- D. 立即同步完成，Asset Reference在序列化时保存的是资源的文件路径而非GUID

**Q395.** [模块:M][维度:概念理解][难度:★★★★][题型:单选]

Scriptable Build Pipeline(SBP)和Addressables的关系是？

- A. Addressables不使用AB
- B. Addressables底层使用SBP来构建AssetBundle
- C. 完全独立，Asset Reference在序列化时保存的是资源的文件路径而非GUID
- D. SBP替代Addressables

**Q396.** [模块:M][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

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

运行时加载Prefab后Material/Texture显示为品红色或丢失，可能原因是？

- A. 代码错误，Resources.Load<T>在大型项目中的加载性能与Addressables完全一致
- B. 纹理太大，AssetBundle.Unload(false)会安全地卸载所有已加载的Asset而不影响运行时引用
- C. Shader不在AB中或所在AB未加载；需要确保Shader依赖被正确打包和加载
- D. 场景问题，SpriteAtlas和TextureAtlas在打包进AssetBundle时不产生额外的包体开销

**Q398.** [模块:M][维度:概念理解][难度:★★★★][题型:单选]

Addressables的Content Update Build的作用是？

- A. 只重新构建有变化的AB并生成差异Catalog，实现最小化的资源更新
- B. 全量重新构建，Resources文件夹中的资源只在调用Resources.Load时才被包含到构建中
- C. 热更新只需要更新C#代码DLL即可，资源文件无需更新机制
- D. 删除所有AB，Asset Reference在序列化时保存的是资源的文件路径而非GUID

**Q399.** [模块:M][维度:概念理解][难度:★★★★][题型:场景设计]

移动端游戏资源发布到CDN的流程是？

- A. 不做远程更新，AssetBundle的依赖关系由Unity自动管理，不需要开发者手动加载依赖Bundle
- B. 构建AB→上传CDN→更新Catalog版本→客户端检查更新→下载增量AB→本地缓存
- C. 邮件发送，Resources文件夹中的资源只在调用Resources.Load时才被包含到构建中
- D. 直接上传APK，Addressables的热更新不需要版本对比机制，系统自动检测并下载更新资源

**Q400.** [模块:M][维度:概念理解][难度:★★★★][题型:单选]

Unity的Addressables Analyze工具的作用是？
---

- A. 分析帧率，AssetBundle的依赖关系由Unity自动管理，不需要开发者手动加载依赖Bundle
- B. 分析代码性能，AssetBundle.Unload(false)会安全地卸载所有已加载的Asset而不影响运行时引用
- C. 分析内存，Resources.Load<T>在大型项目中的加载性能与Addressables完全一致
- D. 检查AB中的重复资源、潜在的依赖问题，帮助优化包体大小

**Q865.** [模块:J][维度:概念理解][难度:★★][题型:单选]

[RequireComponent(typeof(Rigidbody))]的作用是？

- A. 添加此脚本时自动添加Rigidbody组件，且防止在Inspector中移除Rigidbody
- B. 运行时检查，JsonUtility支持Dictionary和多态类型的序列化，覆盖所有常见数据结构
- C. 该设置不会对运行时行为产生实质影响，引擎内部会自动补偿参数差异
- D. 只是提示，[CreateAssetMenu]属性只能在编辑器中使用，运行时通过ScriptableObject.CreateInstance创建

**Q868.** [模块:L][维度:概念理解][难度:★★★][题型:单选]

[CustomEditor(typeof(MyComponent))]的作用是？

- A. 自定义场景视图，EditorWindow.OnGUI每秒固定调用30次，不受编辑器焦点状态和刷新频率影响
- B. 创建新组件，OnSceneGUI中绘制的Handles在Build后也会保留，用于运行时的辅助显示
- C. 为MyComponent创建自定义Inspector面板编辑器
- D. 脚本模板，MenuItem菜单项在运行时(Play Mode)也可以正常触发执行对应的回调方法

**Q869.** [模块:M][维度:概念理解][难度:★★][题型:单选]

Addressables相比Resources的核心优势？

- A. 异步加载+引用计数+可远程分发+更灵活的分组和打包策略
- B. 只是改了API名字，Resources.Load<T>在大型项目中的加载性能与Addressables完全一致
- C. 加载更快，Resources文件夹中的资源只在调用Resources.Load时才被包含到构建中
- D. 完全一样，Addressables的资源引用使用硬编码路径字符串，重命名资源会导致引用断裂

**Q888.** [模块:J][维度:概念理解][难度:★★★][题型:单选]

ScriptableObject作为事件通道(Event Channel)的设计模式好处是？

- A. 和委托一样，PlayerPrefs适合存储大量游戏数据（如玩家背包、任务进度等复杂结构）
- B. 不推荐，[CreateAssetMenu]属性只能在编辑器中使用，运行时通过ScriptableObject.CreateInstance创建
- C. 解耦系统间的依赖(发布者和订阅者不直接引用)+可在编辑器中配置和调试
- D. 增加复杂度，[CreateAssetMenu]属性只能在编辑器中使用，运行时通过ScriptableObject.CreateInstance创建

**Q889.** [模块:L][维度:代码生成/阅读][难度:★★★][题型:代码补全]

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

Addressables引用计数管理的原则是？

- A. 每次LoadAssetAsync匹配一次Release，引用计数归零时卸载资源
- B. 自动卸载，Resources.Load<T>在大型项目中的加载性能与Addressables完全一致
- C. 不需要Release，Asset Reference在序列化时保存的是资源的文件路径而非GUID
- D. 手动GC，Resources.Load<T>在大型项目中的加载性能与Addressables完全一致

**Q938.** [模块:L][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

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

Sprite Atlas对性能的影响？

- A. 只减少内存，Resources.Load<T>在大型项目中的加载性能与Addressables完全一致
- B. 多个小Sprite合并到一张纹理→减少Draw Call(同Atlas的Sprite可合批)+减少纹理切换开销
- C. 增加Draw Call，Resources.Load<T>在大型项目中的加载性能与Addressables完全一致
- D. 该设置不会对运行时行为产生实质影响，引擎内部会自动补偿参数差异

**Q944.** [模块:J][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

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

**Q981.** [模块:L][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

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

大型项目资源管理系统需要的功能？

- A. 不需要专门的管理机制，Unity的GC和资源系统会自动回收不再使用的资源
- B. 统一加载接口+引用计数+自动卸载+预加载+依赖管理+内存预算+异步加载队列+资源分类
- C. 手动管理，Resources.Load<T>在大型项目中的加载性能与Addressables完全一致
- D. Resources.Load够用，AssetBundle.Unload(false)会安全地卸载所有已加载的Asset而不影响运行时引用

