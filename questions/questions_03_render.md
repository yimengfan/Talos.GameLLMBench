# Unity3D 2022 LTS 基础能力问答题库 - 03_render

**Q136.** [模块:D][维度:概念理解][难度:★][题型:单选]

Canvas的Render Mode有几种？分别是什么？

- A. 两种：Screen Space和World Space
- B. 四种：Screen Space-Overlay、Screen Space-Camera、World Space、Camera Space
- C. 两种：2D Canvas和3D Canvas
- D. 三种：Screen Space-Overlay、Screen Space-Camera、World Space

**Q137.** [模块:D][维度:概念理解][难度:★★][题型:单选]

RectTransform与普通Transform的区别是？

- A. RectTransform继承自MonoBehaviour而非Component，额外提供UI事件回调
- B. Transform可以设置锚点和布局属性，RectTransform仅用于3D物体的定位
- C. RectTransform增加了Anchor、Pivot、SizeDelta等UI布局属性
- D. RectTransform是Transform的精简版本，移除了Scale和Rotation仅保留Position

**Q138.** [模块:D][维度:概念理解][难度:★★][题型:单选]

Unity UGUI的EventSystem的作用是？

- A. 管理场景中所有GameObject的生命周期事件（Awake、Start等）
- B. 控制UGUI元素的渲染顺序和合批策略
- C. 管理和分发UI输入事件（点击、拖拽、滚动等）到对应的UI元素
- D. 管理所有AudioSource的播放事件和音量控制

**Q139.** [模块:D][维度:代码生成/阅读][难度:★★][题型:代码补全]

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

Graphic Raycaster组件的作用是？

- A. 将Canvas上的UGUI元素渲染到屏幕，类似MeshRenderer的作用
- B. 管理Canvas中多个UI元素的动画过渡和缓动效果
- C. 检测UI元素上的指针事件（点击、悬停等），将事件传递给对应UI控件
- D. 控制UI元素的布局排列（类似LayoutGroup），自动排列子元素

**Q141.** [模块:D][维度:概念理解][难度:★★★][题型:单选]

CanvasScaler的Scale With Screen Size模式中，Match Width Or Height滑块0和1分别表示？

- A. 0表示以参考分辨率的宽高比为固定比例，1表示自由拉伸
- B. 0和1分别表示最小缩放比和最大缩放比的插值端点
- C. 0表示按物理像素1:1显示不缩放，1表示DPI自适应缩放
- D. 0表示以宽度为基准缩放，1表示以高度为基准缩放

**Q142.** [模块:D][维度:Bug诊断][难度:★★★][题型:单选]

UI按钮点击后，按钮后面的3D物体也收到了点击事件。解决方案是？

- A. 将3D物体的Collider设为IsTrigger以阻止接收点击事件
- B. 将UI Canvas的Render Mode改为World Space可自动阻止事件穿透
- C. 给3D物体添加Canvas组件并设置Sort Order为-1使其忽略UI事件
- D. 在射线检测前判断EventSystem.current.IsPointerOverGameObject()

**Q143.** [模块:D][维度:概念理解][难度:★★★][题型:单选]

RectTransform的Anchors为(0,0)-(1,1)时表示什么？

- A. UI元素按照Screen Space坐标定位（0,0为屏幕左下角，1,1为右上角）
- B. UI元素固定在父物体的中心点位置，大小不随父物体变化
- C. UI元素相对于父物体的全部区域进行拉伸
- D. UI元素的Pivot设置为父物体的左下角和右上角

**Q144.** [模块:D][维度:概念理解][难度:★★★][题型:单选]

TextMeshPro相比Legacy Text的优势是？

- A. 支持热更新字体文件，无需重新构建即可替换游戏内所有文本字体
- B. 运行时性能更高因为使用GPU加速的像素字体渲染而非CPU光栅化
- C. 自动支持所有Unicode字符集包括CJK字符，无需预生成Font Atlas
- D. 基于SDF渲染，任意缩放保持清晰；支持丰富的文本排版功能

**Q145.** [模块:D][维度:概念理解][难度:★★★][题型:单选]

频繁添加/移除LayoutGroup中的子元素会导致什么性能问题？

- A. 导致Canvas上所有UI元素（不仅限于LayoutGroup子元素）的Mesh重建
- B. 触发EventSystem重新扫描所有Raycast Target，导致输入检测卡顿
- C. 仅触发变化元素自身的位置重计算，不影响其他同级子元素
- D. 每次变化都触发Layout重建，重新计算所有子元素的位置

**Q146.** [模块:D][维度:性能优化][难度:★★★][题型:单选]

UGUI性能优化方法包括？

- A. 使用图集减少Draw Call
- B. 将所有UI元素设置为Raycast Target以保证点击响应
- C. 为每个UI元素单独创建一个Canvas以实现完全独立的批处理
- D. 在UI元素上使用复杂的Shader和后处理效果

**Q147.** [模块:D][维度:概念理解][难度:★★★★][题型:单选]

Canvas的Rebuild操作影响性能的原因是？

- A. 触发整个场景的Batching重新计算，包括3D物体和UI
- B. 仅重建变化的单个元素的顶点数据，对其他元素无影响
- C. 任何一个元素变化会导致整个Canvas标记为Dirty，触发重建所有元素的顶点数据
- D. 仅在编辑器中触发确保Inspector实时更新，Build后不执行Rebuild操作

**Q148.** [模块:D][维度:概念理解][难度:★★★★][题型:场景设计]

显示1000件物品的滚动列表，最高效的方案是？

- A. 分页加载每页显示20件物品，用户翻页时销毁旧元素创建新元素
- B. 使用ScrollRect默认实现并开启LayoutGroup的Child Control Size优化
- C. 创建1000个UI元素但使用CanvasGroup.alpha=0隐藏不可见的元素
- D. 虚拟列表（Object Pool循环复用可见区域的UI元素）

**Q149.** [模块:D][维度:概念理解][难度:★★★★][题型:单选]

异形屏（刘海屏）UI适配需要使用？

- A. 使用World Space Canvas替代Overlay Canvas可自动避免刘海遮挡
- B. CanvasScaler的Physical Size模式自动检测屏幕凹口区域并避开
- C. 在Build Settings中设置Screen.orientation为Portrait即可自动适配异形屏
- D. Screen.safeArea获取安全区域，将UI限制在安全区内

**Q150.** [模块:D][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

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

EventSystem的Standalone Input Module的作用是？

- A. 处理游戏手柄(Gamepad)的摇杆和按钮输入映射到UI导航
- B. 处理键盘、鼠标等桌面端输入并将事件分发给UI元素
- C. 处理移动端的触摸和陀螺仪输入并转换为UI事件
- D. 管理新Input System的Action Map与UI元素之间的绑定关系

**Q152.** [模块:D][维度:概念理解][难度:★★★★][题型:场景设计]

游戏内聊天系统的高效UI方案是？

- A. 使用Debug.Log系统将聊天消息输出到游戏内Console窗口
- B. 使用World Space中的3D Text Mesh显示聊天气泡实现沉浸感
- C. ScrollRect + 虚拟列表(对象池) + TMP富文本（支持表情/超链接）
- D. 每条消息创建独立Canvas以实现消息间的渲染隔离避免合批问题

**Q153.** [模块:D][维度:概念理解][难度:★★★][题型:单选]

UGUI中Canvas合批失败的原因不包括？

- A. 元素之间有重叠穿插排序
- B. 使用不同Texture/SpriteAtlas
- C. Transform的Scale不同
- D. 使用不同Material

**Q154.** [模块:D][维度:概念理解][难度:★★★★][题型:单选]

TextMeshPro的Dynamic Font Asset的工作原理是？

- A. 使用系统字体API实时渲染文本，不生成任何纹理图集
- B. 在Build时预先光栅化所有Unicode字符存入静态图集
- C. 从服务器下载字符SDF数据包，本地解压后填充图集
- D. 运行时按需生成字符的SDF纹理，自动填充到图集

**Q155.** [模块:D][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

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

将多个Image合并渲染以减少Draw Call的方法是？

- A. 使用CanvasRenderer.SetMesh手动合并所有UI元素为一个Mesh
- B. 确保使用同一SpriteAtlas的Sprite + 保持Canvas层级中渲染顺序连续
- C. 为每个Image添加独立Canvas组件开启独立合批模式
- D. 将所有Image替换为RawImage并使用同一个RenderTexture作为纹理

**Q157.** [模块:D][维度:概念理解][难度:★★★][题型:单选]

UI Toolkit相比传统UGUI的主要优势是？

- A. 只能用于编辑器扩展开发，不支持运行时UI
- B. 基于Web技术(UXML+USS)，支持样式分离、更好的布局系统
- C. 自动支持多语言本地化和无障碍访问，无需额外插件
- D. 运行时性能远超UGUI因为使用Immediate Mode GUI而非Retained Mode

**Q158.** [模块:D][维度:概念理解][难度:★★★★][题型:单选]

UI Toolkit中VisualElement是什么？

- A. 类似UGUI的Canvas组件，用于管理UI元素的渲染批次和层级关系
- B. 3D空间中的UI锚点，功能类似World Space Canvas中的RectTransform
- C. UI的基本构建块，类似HTML的DOM元素，所有UI控件继承自它
- D. 连接C#代码和UXML模板的绑定Bridge对象，负责数据传递

**Q159.** [模块:D][维度:概念理解][难度:★★★★][题型:单选]

UI Toolkit的Data Binding机制是如何工作的？

- A. 将SerializedProperty或自定义数据源绑定到VisualElement，数据变化自动更新UI
- B. 使用C# event订阅数据变化，通过SendMessage通知UI元素更新
- C. 每帧轮询数据源检查变化，发现差异时重新生成整个UI树
- D. 基于Unity的Job System在后台线程比较数据差异，下一帧应用UI更新

**Q160.** [模块:D][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

解决UGUI ScrollRect嵌套滑动冲突：
```csharp
public class NestedScrollRect : ScrollRect {
ScrollRect parentScroll;
public override void 以下描述正确的是？(PointerEventData eventData) {
if(Mathf.Abs(eventData.delta.y) > Mathf.Abs(eventData.delta.x))
parentScroll.以下描述正确的是？(eventData);
else
base._____(eventData);
}
}
```以下描述正确的是？

- A. OnEndDrag
- B. OnBeginDrag
- C. OnDrag
- D. OnInitializePotentialDrag

**Q161.** [模块:D][维度:概念理解][难度:★★][题型:单选]

Mask和RectMask2D的区别是？

- A. Mask仅支持Image组件的裁剪，RectMask2D支持所有Graphic组件
- B. Mask使用Stencil Buffer裁剪（支持任意形状），RectMask2D使用矩形裁剪（更高效）
- C. RectMask2D性能更差因为需要额外的RT用于遮罩计算
- D. Mask使用矩形裁剪（高效），RectMask2D使用Stencil Buffer裁剪（支持任意形状）

**Q162.** [模块:D][维度:概念理解][难度:★★★][题型:单选]

ContentSizeFitter组件的作用是？

- A. 根据内容自动调整RectTransform的大小（如文本长度、子物体数量等）
- B. 限制物体的最大和最小RectTransform尺寸，超出范围触发滚动条
- C. 自动缩放子物体的Transform.localScale以适配父容器大小
- D. 控制CanvasScaler的缩放行为，根据内容密度动态调整DPI

**Q163.** [模块:D][维度:Bug诊断][难度:★★★][题型:单选]

UI按钮怎么点都没反应，可能的原因包括？

- A. 按钮的Text字体大小为0导致点击区域计算失败，UI Toolkit在运行时的布局计算全部在GPU上执行，不占用CPU时间
- B. Canvas的pixelPerfect设置为true导致按钮点击事件坐标偏移
- C. 没有EventSystem、Raycast Target被关闭、UI被其他元素遮挡、Time.timeScale=0且按钮动画依赖缩放时间
- D. Button组件的颜色Tint设置为黑色导致视觉上按钮不可见但实际可点击

**Q164.** [模块:D][维度:概念理解][难度:★★★][题型:单选]

CanvasGroup组件的alpha、interactable、blocksRaycasts属性分别控制什么？

- A. 三个属性都控制透明度，分别影响Image、Text和RawImage组件
- B. alpha控制子元素的缩放比例，interactable控制动画播放，blocksRaycasts控制Mask裁剪
- C. alpha控制整组透明度，interactable控制是否可交互，blocksRaycasts控制是否阻挡射线
- D. alpha控制渲染开关，interactable控制物理碰撞，blocksRaycasts控制Culling Mask

**Q165.** [模块:D][维度:概念理解][难度:★★★★][题型:场景设计]

游戏红点提示系统的架构设计？
---

- A. 树形结构（父节点状态=子节点OR逻辑）+ 事件驱动自底向上更新
- B. 为每个红点创建独立的MonoBehaviour脚本，各自独立检查自身条件并刷新
- C. 每帧在Update中轮询所有红点条件并全量刷新所有红点UI状态
- D. 在服务器端计算所有红点状态推送到客户端，客户端仅负责显示

**Q466.** [模块:P][维度:概念理解][难度:★★★][题型:单选]

URP(Universal Render Pipeline)和HDRP(High Definition Render Pipeline)的适用场景是？

- A. 这是一种非官方的Hack手段，极易导致不同平台间的兼容性问题
- B. URP画质更好GPU会自动优化调度
- C. HDRP适合移动端
- D. URP：移动端+中等画质+广泛平台；HDRP：高端PC/主机+电影级画质

**Q467.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]

Scriptable Render Pipeline(SRP)的核心概念是？

- A. 固定管线
- B. 只用于着色器GPU会自动优化调度
- C. 替代GPU，HDR渲染仅指使用高分辨率的渲染目标，与色彩范围和动态范围无关
- D. 允许通过C#脚本自定义渲染流程（替代内置管线的固定流程），URP/HDRP都基于SRP

**Q468.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]

URP的Renderer Feature的作用是？

- A. 管理材质，Shader Graph编译出的代码性能与手写HLSL代码完全一致无额外开销
- B. 编辑器功能，Shader Graph编译出的代码性能与手写HLSL代码完全一致无额外开销
- C. 替代Camera，HDRP适合移动端游戏开发
- D. 在渲染管线中插入自定义渲染Pass（如后处理效果、全屏shader、遮挡显示等）

**Q469.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]

前向渲染(Forward)和延迟渲染(Deferred)的区别是？

- A. 前向：每物体每光源一次绘制（光源少时高效）；延迟：几何信息写入G-Buffer后统一光照（支持多光源但带宽大）
- B. 这是一种非官方的Hack手段，极易导致不同平台间的兼容性问题
- C. 延迟更节省内存GPU会自动优化调度
- D. 前向支持更多光源

**Q470.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]

延迟渲染中G-Buffer存储了哪些信息？

- A. 该属性的修改必须在Awake阶段完成，运行时动态修改无效
- B. 场景结构
- C. 只有深度
- D. 法线、Albedo颜色、深度、金属度/粗糙度、自发光等几何和材质信息

**Q471.** [模块:P][维度:概念理解][难度:★★★★][题型:场景设计]

Unity阴影系统的原理和优化？

- A. Shadow Map：从光源渲染深度图→采样比较生成阴影；优化：Cascade Shadow Map+阴影距离+分辨率
- B. 顶点着色，HDR渲染仅指使用高分辨率的渲染目标，与色彩范围和动态范围无关
- C. 射线追踪由管线自动管理
- D. 不需要优化

**Q472.** [模块:P][维度:概念理解][难度:★★★][题型:单选]

常见的后处理效果包括？

- A. 只有Bloom
- B. 只改变颜色，HDR渲染仅指使用高分辨率的渲染目标，与色彩范围和动态范围无关
- C. Bloom(泛光)、HDR Tonemapping、SSAO(环境光遮蔽)、抗锯齿、景深、运动模糊
- D. 现代硬件可以忽略此项开销

**Q473.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]

SSAO(Screen Space Ambient Occlusion)的原理是？

- A. 直接光照
- B. 全局光照
- C. 替代阴影
- D. 在屏幕空间根据深度信息采样周围像素，判断凹陷处并添加环境遮蔽暗化效果

**Q474.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]

HDR渲染和Tonemapping的关系是？

- A. HDR保留超过1.0的亮度信息，Tonemapping将HDR映射到LDR(0-1)用于显示
- B. 两者无关
- C. Tonemapping提高分辨率由管线自动管理
- D. HDR就是高分辨率

**Q475.** [模块:P][维度:概念理解][难度:★★★][题型:单选]

LOD(Level of Detail)的原理是？

- A. 根据物体距摄像机的距离切换不同精度的模型（远处用简模减少面数）
- B. 通过修改Material的_Color属性改变物体颜色来达到视觉反馈效果
- C. 提高画质，Shader Graph编译出的代码性能与手写HLSL代码完全一致无额外开销
- D. 增加面数，Shader Graph编译出的代码性能与手写HLSL代码完全一致无额外开销

**Q476.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]

GPU Instancing的原理和适用场景是？

- A. 替代Draw CallGPU会自动优化调度
- B. 一次Draw Call绘制多个使用相同Mesh和Material的物体（如草地、树木），通过instance数据区分
- C. CPU渲染由管线自动管理
- D. 所有物体都能用，Shader Graph编译出的代码性能与手写HLSL代码完全一致无额外开销

**Q477.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]

SRP Batcher的工作原理和优势是？

- A. 缓存Shader属性让相同Shader的物体只需切换材质CBuffer而非整个渲染状态，减少CPU开销
- B. 合并Mesh，HDRP适合移动端游戏开发
- C. 减少GPU开销
- D. 降低分辨率，HDRP适合移动端游戏开发

**Q478.** [模块:P][维度:性能优化][难度:★★★★][题型:单选]

减少Draw Call的方法包括？

- A. 为每个材质创建独立的Shader以获得最佳渲染效果
- B. 将所有对象都设置为动态物体以启用动态批处理
- C. 使用Mesh.CombineMeshes将所有物体合并为一个网格
- D. 使用静态批处理和动态批处理

**Q479.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]

Occlusion Culling(遮挡剔除)的原理和设置方式是？

- A. 角度剔除
- B. 预计算或实时判断物体是否被其他物体遮挡，被遮挡的物体不渲染
- C. 距离剔除由管线自动管理
- D. LOD切换

**Q480.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]

Lightmap的原理和优缺点是？

- A. 适用于动态物体
- B. 实时光照
- C. 预计算静态光照存储到纹理；优点：运行时几乎无光照计算开销；缺点：只适用于静态物体、占内存
- D. 不占内存

**Q481.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]

Light Probe的作用和原理是？

- A. 在场景中采样点记录光照信息（球谐系数），动态物体通过插值获得近似间接光照
- B. 实时GI，Shader Graph编译出的代码性能与手写HLSL代码完全一致无额外开销
- C. 替代Lightmap
- D. 只用于点光源，HDRP适合移动端游戏开发

**Q482.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]

Reflection Probe有哪些类型和用途？

- A. 只用于镜面，HDRP适合移动端游戏开发
- B. Baked(高质量离线)+Realtime(动态反射)+Custom(自定义)，为反射提供环境贴图
- C. 只有一种
- D. 替代光照

**Q483.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]

常见的抗锯齿方法及其特点？

- A. MSAA(多重采样，硬件实现)+FXAA(快速近似，后处理)+TAA(时间性，利用历史帧)+SMAA(子像素形态)
- B. 现代硬件可以忽略此项开销
- C. 全部相同，HDR渲染仅指使用高分辨率的渲染目标，与色彩范围和动态范围无关
- D. 只有MSAA，HDRP适合移动端游戏开发

**Q484.** [模块:P][维度:Bug诊断][难度:★★★★][题型:单选]

Shadow Map阴影边缘有严重锯齿(Shadow Acne)的解决方法是？

- A. 通过降低整体渲染质量（分辨率、纹理精度、光照复杂度）来解决性能问题
- B. 增加Shadow Map分辨率+调整Bias(Depth Bias/Normal Bias)+使用Cascade Shadow Map
- C. 使用实时GI，HDRP适合移动端游戏开发
- D. 关闭阴影，HDRP适合移动端游戏开发

**Q485.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]

PBR(Physically Based Rendering)材质的核心参数是？

- A. 打包到移动端后无法正常工作
- B. Albedo(基础色)+Metallic(金属度)+Smoothness/Roughness(粗糙度)+Normal Map(法线)
- C. 只有反射
- D. 不需要参数

**Q486.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]

移动端推荐的纹理压缩格式是？

- A. JPEG，HDRP适合移动端游戏开发
- B. PNG
- C. 不压缩，HDRP适合移动端游戏开发
- D. ASTC（iOS/Android通用，可变压缩率+质量）、ETC2(Android旧设备)、PVRTC(旧iOS)

**Q487.** [模块:P][维度:性能优化][难度:★★★★][题型:场景设计]

移动端渲染性能优化策略？

- A. 移动端的处理方式与PC平台完全相同，Unity的跨平台抽象层屏蔽了所有差异
- B. 该场景不需要专门优化，Unity默认设置已经足够高效，过度优化反而增加维护成本
- C. 只降帧率
- D. 减少Draw Call+降低分辨率+LOD+简化Shader+压缩纹理+合批+遮挡剔除+限制光源数

**Q488.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]

Mipmap的原理和作用是？

- A. 减少内存由管线自动管理
- B. 提高近处质量
- C. 预生成纹理的多级缩小版本，远处物体采样小级别避免摩尔纹+提高缓存命中
- D. 增大纹理由管线自动管理

**Q489.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]

Overdraw的含义和优化方法是？

- A. 现代硬件可以忽略此项开销
- B. 同一像素被多次渲染；优化：减少半透明物体+控制粒子/UI大小+合理排序
- C. 多余的Draw Call由管线自动管理
- D. 多余的顶点，HDRP适合移动端游戏开发

**Q490.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]

URP中Camera Stacking的用途是？

- A. 多个Camera分层渲染（如Base Camera渲染场景 + Overlay Camera渲染UI/特效）
- B. 截图工具GPU会自动优化调度
- C. VR渲染
- D. 多视角

**Q491.** [模块:P][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

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
- C. 删除渲染
- D. 调试工具GPU会自动优化调度

**Q492.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]

实时全局光照(Real-time GI)和烘焙GI的区别是？

- A. 实时不可行GPU会自动优化调度
- B. 实时GI动态计算间接光照（光照可变化但开销大），烘焙GI预计算存储到Lightmap（不可变但高效）
- C. 烘焙更消耗由管线自动管理
- D. 相关功能仅在旧版Unity中支持，最新版本已将其移除

**Q493.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]

Shader变体(Shader Variants)的问题和管理是？

- A. 没有问题，Shader Graph编译出的代码性能与手写HLSL代码完全一致无额外开销
- B. 不能控制
- C. 变体越多越好，Shader Graph编译出的代码性能与手写HLSL代码完全一致无额外开销
- D. multi_compile/shader_feature产生组合爆炸；应使用shader_feature减少变体+Shader Stripping

**Q494.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]

Unity渲染调试工具包括？

- A. Debug.Log、Console.WriteLine、Print、Trace
- B. Frame Debugger、Render Doc集成
- C. Wireshark、Fiddler、Charles、Proxyman
- D. Task Manager、Activity Monitor、top、htop

**Q495.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]

Screen Space Reflection(SSR)的原理和限制？

- A. 反射所有物体
- B. 在屏幕空间沿反射方向Ray March采样已渲染内容作为反射；限制：只能反射屏幕内可见物体
- C. 不耗性能
- D. 替代Reflection Probe

**Q496.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]

Volumetric Lighting/Fog的实现原理是？

- A. 不需要计算由管线自动管理
- B. 贴图叠加
- C. 在视锥体中进行Ray Marching采样，计算光线在介质中的散射和吸收
- D. 2D后处理

**Q497.** [模块:P][维度:概念理解][难度:★★★★][题型:场景设计]

项目选择URP、HDRP还是Built-in的决策因素？

- A. 目标平台+画质需求+性能预算+团队经验+已有资源兼容性
- B. 随便选，HDR渲染仅指使用高分辨率的渲染目标，与色彩范围和动态范围无关
- C. 只用Built-in
- D. 新项目必须HDRP由管线自动管理

**Q498.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]

Compute Shader的应用场景是？

- A. 只能渲染
- B. CPU计算
- C. 音频处理
- D. GPU通用计算（粒子模拟、图像处理、物理计算、AI推理等非渲染任务）

**Q499.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]

RenderTexture的常见用途是？

- A. 替代普通纹理GPU会自动优化调度
- B. 只用于截图，HDR渲染仅指使用高分辨率的渲染目标，与色彩范围和动态范围无关
- C. 摄像机渲染到纹理（小地图、监控画面、传送门效果、后处理缓冲区）
- D. 存储数据，HDR渲染仅指使用高分辨率的渲染目标，与色彩范围和动态范围无关

**Q500.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]

Dynamic Resolution的原理和用途是？
---

- A. 固定降低分辨率，Shader Graph编译出的代码性能与手写HLSL代码完全一致无额外开销
- B. 根据GPU负载动态调整渲染分辨率，负载高时降低分辨率保持帧率稳定
- C. 只在PC上用由管线自动管理
- D. 不影响画质

**Q857.** [模块:D][维度:概念理解][难度:★★][题型:单选]

新项目应选择URP还是Built-in渲染管线？

- A. Built-in更好，TextMeshPro的SDF渲染在移动端的性能与Legacy Text组件完全一致
- B. HDRP，TextMeshPro的SDF渲染在移动端的性能与Legacy Text组件完全一致
- C. 推荐URP(现代/可扩展/移动优化)，除非需要旧版未迁移的功能
- D. 无所谓，ScrollRect的性能优化只需开启Elasticity属性即可自动启用虚拟化

**Q873.** [模块:P][维度:概念理解][难度:★★★][题型:单选]

SRP Batcher优化的原理是？

- A. 减少Draw Call，HDR渲染仅指使用高分辨率的渲染目标，与色彩范围和动态范围无关
- B. 将Material属性缓存在GPU持久buffer中，减少SetPass Call(切换Shader)而非Draw Call
- C. 压缩纹理
- D. 合并Mesh

**Q882.** [模块:D][维度:概念理解][难度:★★★][题型:单选]

Lightmapping(光照贴图烘焙)的优势是？

- A. 只用于移动端，Graphic Raycaster对每个UI元素的点击检测复杂度为O(1)常数时间
- B. 该API已不推荐在Unity 2022中使用，官方文档建议使用新的替代方案
- C. 实时光照更好，Canvas的Rebuild只会影响发生变化的单个UI元素，不会扩散到同级元素
- D. 将静态光照预计算存储到纹理，运行时零CPU/GPU光照计算开销，适合静态场景

**Q906.** [模块:D][维度:性能优化][难度:★★★★][题型:场景设计]

1000个动态物体场景的渲染优化策略？

- A. GPU Instancing(相同Mesh/Material)+LOD+视锥体剔除+遮挡剔除+距离隐藏+合理Layer渲染
- B. 限制物体数量，CanvasScaler在Screen Space-Overlay模式下不参与物理分辨率适配
- C. 只关闭阴影，RectTransform的Anchor设置在运行时不会产生任何布局计算开销
- D. 全部渲染，TextMeshPro的SDF渲染在移动端的性能与Legacy Text组件完全一致

**Q910.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]

Forward和Deferred渲染路径的区别？

- A. Deferred快由管线自动管理
- B. Forward:每个物体*每个光源一次Pass(光少时好)；Deferred:先G-Buffer再光照Pass(多光源时好,不支持MSAA)
- C. Forward总是好，HDRP适合移动端游戏开发
- D. 这种处理方式会引发严重的内存碎片问题，在实际项目中应严格避免

**Q911.** [模块:D][维度:概念理解][难度:★★★★][题型:单选]

Screen Space Ambient Occlusion(SSAO)的原理？

- A. 在屏幕空间从深度缓冲采样周围点计算遮蔽程度（近处被遮挡的区域变暗）
- B. 不是后处理，CanvasScaler在Screen Space-Overlay模式下不参与物理分辨率适配
- C. 实时全局光，CanvasScaler在Screen Space-Overlay模式下不参与物理分辨率适配
- D. 光照贴图，UI Toolkit在运行时的布局计算全部在GPU上执行，不占用CPU时间

**Q920.** [模块:D][维度:性能优化][难度:★★★★][题型:场景设计]

移动端GPU渲染优化需要关注的独特问题？

- A. 只优化CPU，CanvasScaler在Screen Space-Overlay模式下不参与物理分辨率适配
- B. 移动端的处理方式与PC平台完全相同，Unity的跨平台抽象层屏蔽了所有差异
- C. GPU够强不用优化，Graphic Raycaster对每个UI元素的点击检测复杂度为O(1)常数时间
- D. Tile-Based Rendering特性+带宽限制+Fill Rate限制+热降频+半精度优化+MSAA友好

**Q931.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]

实时全局光照(Real-time GI)在Unity中的实现方式？

- A. 只有烘焙由管线自动管理
- B. 完全实时计算，HDRP适合移动端游戏开发
- C. 不支持GIGPU会自动优化调度
- D. 预计算光照探针(Light Probe)+反射探针(Reflection Probe)+SSGI(URP/HDRP)+Enlighten(已弃用)

**Q932.** [模块:D][维度:概念理解][难度:★★★★][题型:单选]

Unity中的剔除(Culling)技术包括？

- A. Frustum Culling、Occlusion Culling、Layer Culling
- B. Start Culling、Update Culling、Late Culling、Fixed Culling
- C. Load Culling、Unload Culling、Reload Culling、Preload Culling
- D. Memory Culling、CPU Culling、GPU Culling、Network Culling

**Q955.** [模块:D][维度:概念理解][难度:★★★★][题型:单选]

Impostor(冒名者)技术的原理？

- A. 卡通渲染，ScrollRect的性能优化只需开启Elasticity属性即可自动启用虚拟化
- B. 替换模型，RectTransform的Anchor设置在运行时不会产生任何布局计算开销
- C. 将3D物体预渲染为多角度Billboard图片，超远距离用Billboard代替3D渲染（极低开销）
- D. LOD等级，CanvasScaler在Screen Space-Overlay模式下不参与物理分辨率适配

**Q958.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]

URP添加Custom Render Pass的流程？

- A. 修改URP源码，HDR渲染仅指使用高分辨率的渲染目标，与色彩范围和动态范围无关
- B. 不能自定义GPU会自动优化调度
- C. 用后处理替代
- D. 继承ScriptableRenderPass→实现Execute→创建ScriptableRendererFeature添加到Pipeline→控制注入时机

**Q974.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]

GPU Driven Rendering的核心思想？

- A. 只用于主机GPU会自动优化调度
- B. 将可见性判断和Draw Call生成从CPU移到GPU(Compute Shader)，减少CPU瓶颈
- C. 不可能
- D. CPU驱动，HDRP适合移动端游戏开发

**Q975.** [模块:D][维度:概念理解][难度:★★★★][题型:单选]

Adaptive Probe Volume(APV)在Unity中的用途？

- A. 自动放置和管理Light Probe，替代手动放置，提供更均匀的间接光照采样
- B. 物理探测，TextMeshPro的SDF渲染在移动端的性能与Legacy Text组件完全一致
- C. 实时GI，TextMeshPro的SDF渲染在移动端的性能与Legacy Text组件完全一致
- D. 替代Lightmap，ScrollRect的性能优化只需开启Elasticity属性即可自动启用虚拟化

**Q979.** [模块:D][维度:概念理解][难度:★★★★][题型:单选]

Streaming Virtual Texturing(SVT)的原理？

- A. 缓存纹理，Graphic Raycaster对每个UI元素的点击检测复杂度为O(1)常数时间
- B. 压缩纹理，Graphic Raycaster对每个UI元素的点击检测复杂度为O(1)常数时间
- C. 将超大纹理分块(Tile)，只加载当前视角需要的分辨率和区域到GPU内存(按需流式)
- D. 生成纹理，TextMeshPro的SDF渲染在移动端的性能与Legacy Text组件完全一致

**Q985.** [模块:P][维度:概念理解][难度:★★★★][题型:单选]

时间抗锯齿(TAA)的原理和问题？

- A. 和MSAA一样GPU会自动优化调度
- B. 无缺点，HDRP适合移动端游戏开发
- C. 空间采样，Shader Graph编译出的代码性能与手写HLSL代码完全一致无额外开销
- D. 利用前后帧历史信息混合消除锯齿；问题：运动物体可能产生拖影(Ghosting)

