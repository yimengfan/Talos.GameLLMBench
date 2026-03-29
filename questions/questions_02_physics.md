# Unity3D 2022 LTS 基础能力问答题库 - 02_physics

**Q086.** [模块:C][维度:概念理解][难度:★][题型:单选]

Camera组件的Clear Flags设置为Skybox表示什么？

- A. 将天空盒作为后处理效果叠加在场景渲染结果之上
- B. 摄像机先渲染天空盒作为背景，再渲染场景物体
- C. 使用上一帧的渲染结果作为背景，天空盒仅在第一帧渲染
- D. 仅在天空盒纹理加载完成后才开始渲染场景物体，否则显示Loading画面

**Q087.** [模块:C][维度:概念理解][难度:★][题型:单选]

Material和Shader的关系是？

- A. Shader是Material的一个实例，多个Shader可共享同一个Material
- B. Material和Shader是同一概念的不同称呼，在Inspector中的显示方式不同
- C. Material包含Shader的HLSL/GLSL源码，运行时编译为GPU指令
- D. Shader定义渲染算法，Material是Shader的一个实例（保存具体参数值如颜色、纹理）

**Q088.** [模块:C][维度:概念理解][难度:★★][题型:单选]

什么是Draw Call？

- A. Unity编辑器中Scene视图每帧刷新的回调函数
- B. GPU内部每个像素的着色器计算过程
- C. CPU向GPU发送的一次渲染请求指令
- D. 内存管理系统中分配GPU显存的操作

**Q089.** [模块:C][维度:性能优化][难度:★★][题型:单选]

减少Draw Call的常用方法不包括？

- A. 使用SpriteAtlas/TextureAtlas
- B. GPU Instancing
- C. 增加材质数量
- D. Static Batching

**Q090.** [模块:C][维度:概念理解][难度:★★][题型:单选]

LOD(Level of Detail)系统的作用是？

- A. 按GPU占用率自动控制物体的渲染开关，优先渲染距离最近的物体
- B. 根据物体与摄像机的距离切换不同精度的模型，远处使用低精度模型减少渲染开销
- C. 管理纹理Mipmap级别，控制不同距离下的纹理分辨率选择策略
- D. 根据当前帧率动态调整所有物体的网格面数，低帧率时自动简化Mesh

**Q091.** [模块:C][维度:概念理解][难度:★★][题型:单选]

Occlusion Culling(遮挡剔除)的作用是：以下描述正确的是？。以下描述正确的是？

- A. 在渲染前剔除被其他物体完全遮挡的物体，不送入GPU渲染
- B. 仅剔除超出摄像机视锥体范围的物体，不处理遮挡关系
- C. 动态调整物体的LOD级别，远处物体使用低精度模型减少渲染
- D. 根据物体材质透明度决定是否渲染，半透明物体不参与剔除

**Q092.** [模块:C][维度:概念理解][难度:★★★][题型:单选]

Unity支持的三种渲染管线分别是？

- A. 2D Render Pipeline、3D Render Pipeline、Compute Pipeline
- B. Forward Rendering、Deferred Rendering、Hybrid Rendering
- C. Built-in Render Pipeline、URP(Universal)、HDRP(High Definition)
- D. Mobile Pipeline、Desktop Pipeline、VR Pipeline

**Q093.** [模块:C][维度:概念理解][难度:★★★][题型:单选]

Forward Rendering和Deferred Rendering的主要区别是？

- A. Forward渲染到Framebuffer，Deferred渲染到RenderTexture，两者输出格式不同
- B. Forward对每个物体逐光源计算光照，Deferred先渲染G-Buffer再统一计算光照
- C. Forward仅支持方向光，Deferred支持所有光源类型
- D. Forward每次渲染整个场景然后逐光源叠加，Deferred每个光源单独渲染一遍完整场景

**Q094.** [模块:C][维度:性能优化][难度:★★★][题型:单选]

纹理性能优化的方法包括？

- A. 将所有纹理尺寸调整为2的幂次方以外的值可以避免Mipmap生成
- B. 禁用Mipmap可以减少50%的内存占用且不影响渲染质量
- C. 所有纹理都使用RGBA32格式以保证最高画质
- D. 使用纹理压缩格式（如ASTC、ETC2）

**Q095.** [模块:C][维度:概念理解][难度:★★★][题型:单选]

SRP Batcher的工作原理是？

- A. 将多个不同Mesh的渲染命令合并为一个Draw Call提交给GPU
- B. 缓存Material属性，减少CPU向GPU上传数据的次数（减少SetPass Call）
- C. 将GPU渲染命令序列化到CommandBuffer中批量提交，减少CPU-GPU通信次数
- D. 压缩Shader变体数量，减少运行时Shader编译和切换开销

**Q096.** [模块:C][维度:API精确度][难度:★★★][题型:单选]

Camera.cullingMask的作用是？

- A. 设置摄像机的视野角度大小(FOV)，限制可见区域
- B. 控制后处理效果的应用范围，指定哪些Layer不做后处理
- C. 通过LayerMask控制相机只渲染特定Layer上的物体
- D. 控制相机的远近裁剪面距离，超出范围的物体不渲染

**Q097.** [模块:C][维度:概念理解][难度:★★★][题型:单选]

烘焙Lightmap的优势和限制是？

- A. 优势：静态光照零运行时开销。限制：只适用于静态物体，不能反映动态变化
- B. 优势：无需预计算即可获得全局光照效果。限制：文件体积大增加安装包大小
- C. 优势：支持所有物体包括动态物体的全局光照。限制：增加运行时GPU计算开销
- D. 优势：实时更新光照支持昼夜变化。限制：需要高端GPU才能使用

**Q098.** [模块:C][维度:代码生成/阅读][难度:★★★][题型:代码补全]

通过代码修改Material颜色：
```csharp
GetComponent<Renderer>().material._____(---"_Color", Color.red);
```

- A. SetColor
- B. SetValue
- C. SetVector4
- D. SetProperty

**Q099.** [模块:C][维度:Bug诊断][难度:★★★][题型:单选]

通过renderer.material访问Material会发生什么？

- A. 返回sharedMaterial的只读副本，任何Set操作都会抛出InvalidOperationException
- B. 仅在Editor中创建实例，Build后直接返回sharedMaterial引用以节省内存
- C. Unity自动创建该Material的实例副本，如不注意会导致内存泄漏；应使用sharedMaterial（只读）或手动管理实例
- D. 直接返回项目中Material Asset的引用，修改renderer.material等同于修改Asset文件

**Q100.** [模块:C][维度:概念理解][难度:★★★][题型:单选]

Camera的Frustum Culling(视锥体剔除)的原理是？

- A. 与Occlusion Culling算法相同，都使用预烘焙的可见性数据
- B. 通过深度测试剔除被前方物体遮挡的像素片段
- C. 剔除面积小于屏幕1%的物体以减少小物件渲染开销
- D. 物体的包围盒不在摄像机视锥体内时，不提交渲染

**Q101.** [模块:C][维度:性能优化][难度:★★★][题型:单选]

GPU Instancing的作用和要求是？

- A. 一次Draw Call渲染多个相同Mesh+Material的对象；要求Shader支持Instancing
- B. 将多个不同Mesh合并为一个DrawCall渲染，不要求Shader做特殊支持
- C. 仅适用于标记为Static的物体，动态物体不支持GPU Instancing
- D. 在GPU上实例化运行时生成的程序化Mesh，不需要预定义模型数据

**Q102.** [模块:C][维度:概念理解][难度:★★★][题型:单选]

RenderTexture的用途包括？

- A. 作为纹理压缩的中间格式，在ASTC/ETC2格式转换时使用
- B. 仅用于UI的Image组件显示静态图片，不支持实时渲染内容
- C. 存储顶点和索引缓冲区数据，供ComputeShader读写使用
- D. 将摄像机渲染结果输出到纹理中（如小地图、镜面反射、后处理等）

**Q103.** [模块:C][维度:概念理解][难度:★★★★][题型:单选]

Shader Variant过多会导致什么问题？

- A. 仅影响编辑器中的Shader编译速度，不影响运行时性能和包体大小
- B. GPU渲染速度下降，因为每个变体都需要占用独立的GPU寄存器
- C. 提高运行时性能，因为更多变体意味着更精确的渲染路径选择
- D. 编译时间长、运行时内存占用大、构建包体增大

**Q104.** [模块:C][维度:概念理解][难度:★★★★][题型:单选]

Light Probe(光照探针)的作用是？

- A. 实时追踪光源方向变化，动态更新所有物体的阴影方向
- B. 记录场景中每个物体的阴影遮挡信息，用于实时阴影渲染
- C. 存储高分辨率环境光照纹理，替代HDRI Skybox用于Image Based Lighting
- D. 在场景中采样烘焙光照信息，为动态物体提供间接光照近似

**Q105.** [模块:C][维度:概念理解][难度:★★★★][题型:单选]

Reflection Probe(反射探针)的工作方式是？

- A. 在探针位置渲染周围环境为Cubemap，用于反射环境的近似
- B. 将平面镜反射投影到表面UV空间，仅支持平面反射效果
- C. 实时渲染6个方向的高分辨率深度图，通过视差校正实现精确反射
- D. 使用屏幕空间光线追踪(SSR)计算精确反射，Probe仅提供追踪起点

**Q106.** [模块:C][维度:概念理解][难度:★★★★][题型:单选]

Unity支持的全局光照(GI)方案包括？

- A. Forward GI、Deferred GI、ForwardPlus GI、TileBased GI
- B. Raytraced GI、PathTraced GI、PhotonMapped GI、Radiosity GI
- C. Enlighten（已弃用）、Lightmaps（烘焙）
- D. Realtime GI、Baked GI、Dynamic GI、Static GI

**Q107.** [模块:C][维度:概念理解][难度:★★★★][题型:单选]

Unity的Dynamic Resolution(动态分辨率)的工作原理是？

- A. 仅在编辑器Profiler中模拟不同分辨率的性能表现，不影响实际构建
- B. 仅降低UI元素的渲染分辨率不影响3D场景，因为UI对清晰度要求低
- C. 固定以50%分辨率渲染所有场景，然后通过超采样上采样到目标分辨率
- D. 根据GPU负载动态降低渲染分辨率以维持帧率，在性能和画质间自动平衡

**Q108.** [模块:C][维度:概念理解][难度:★★★★][题型:单选]

级联阴影贴图(Cascaded Shadow Maps)的原理是？

- A. 将阴影贴图按时间级联更新，每帧只更新一段区域，多帧累积完整阴影
- B. 使用一张超大分辨率阴影贴图覆盖整个场景，不做分段处理
- C. 每个产生阴影的物体使用独立的阴影贴图，按物体优先级分配分辨率
- D. 将视锥体分段，每段使用不同分辨率的阴影贴图，近处精度高远处精度低

**Q109.** [模块:C][维度:概念理解][难度:★★★★][题型:单选]

屏幕空间环境光遮蔽(SSAO)的原理是？

- A. 在屏幕空间根据深度和法线信息估算每个像素被周围几何体遮蔽的程度，增加接触阴影
- B. 通过实时光线追踪计算每个表面点接收的环境光比例
- C. 基于全局光照的光子映射算法计算环境光遮蔽，需要预烘焙数据
- D. 使用预计算的AO贴图纹理存储遮蔽信息，运行时直接采样叠加

**Q110.** [模块:C][维度:概念理解][难度:★★★★][题型:单选]

Texture Streaming(纹理流式加载)的工作原理是？

- A. 将纹理数据存储在StreamingAssets目录，通过文件流按需读取像素数据
- B. 在场景加载时将所有纹理预加载到GPU显存中以避免运行时加载卡顿
- C. 根据摄像机距离动态加载不同Mipmap级别的纹理，减少内存占用
- D. 仅加载最高分辨率Mipmap并在GPU上实时生成低级别Mipmap

**Q111.** [模块:C][维度:性能优化][难度:★★★★][题型:单选]

移动端渲染优化措施包括？

- A. 在Fragment Shader中进行复杂的光照计算和阴影采样
- B. 将所有对象的Draw Call合并为一个以减少渲染开销
- C. 使用高精度的Float纹理替代压缩纹理以提高画质
- D. 使用简化版Shader和LOD系统

**Q112.** [模块:C][维度:概念理解][难度:★★★][题型:单选]

半透明物体的渲染顺序是？

- A. 与不透明物体使用相同的深度测试渲染顺序，不做特殊排序
- B. 按Material排序渲染以最大化合批效率，不考虑物体前后关系
- C. 从前往后排序渲染（离摄像机近的先画），写入深度缓冲后裁剪后方重叠部分
- D. 从后往前排序渲染（离摄像机远的先画），不写入深度缓冲

**Q113.** [模块:C][维度:代码生成/阅读][难度:★★★][题型:代码补全]

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

SetPass Call和Draw Call的区别是什么？

- A. SetPass Call和Draw Call是同一操作的不同阶段名称，本质上没有区别
- B. Draw Call是CPU侧的渲染指令提交，SetPass Call是GPU侧的渲染管线状态配置
- C. SetPass Call是切换Shader Pass或材质状态的调用，Draw Call是提交渲染命令；SetPass Call对性能影响更大
- D. SetPass Call发生在每帧开始时初始化渲染状态，Draw Call发生在每个物体渲染时

**Q115.** [模块:C][维度:概念理解][难度:★★★][题型:单选]

Unity URP中Decal Renderer Feature的作用是？

- A. 将聚光灯(Spot Light)的光照范围投射为指定形状的Cookie纹理
- B. 在物体表面投射贴花效果（如弹孔、血迹等）
- C. 投影远处物体的阴影贴图到近处地面增强阴影视觉效果
- D. 将摄像机视角的渲染结果投射到指定表面实现屏幕录制效果

**Q116.** [模块:C][维度:概念理解][难度:★★★][题型:单选]

纹理Mipmap的作用是？

- A. 预计算不同分辨率的纹理版本，远处使用低分辨率避免摩尔纹并提高采样效率
- B. 压缩纹理数据减少文件大小，运行时解压还原为原始分辨率
- C. 将多个小纹理打包到一张大图集中以减少Draw Call
- D. 使纹理在所有距离上都保持最高清晰度，自动增强远处物体的纹理细节

**Q117.** [模块:C][维度:性能优化][难度:★★★★][题型:单选]

什么是Overdraw以及如何减少？

- A. CPU和GPU之间数据传输超过带宽限制；减少方法：降低纹理分辨率和顶点数量
- B. 同一像素被多次绘制；减少方法：合理排序、裁剪不可见UI、减少粒子/半透明面积
- C. 内存碎片化导致的GC频繁触发；减少方法：使用对象池和预分配缓冲区
- D. 网络数据包重复传输造成的带宽浪费；减少方法：启用UDP协议和数据压缩

**Q118.** [模块:C][维度:概念理解][难度:★★★★][题型:单选]

HDR(High Dynamic Range)渲染的好处是？

- A. 仅用于VR/AR渲染中的双目立体视觉效果，普通游戏不需要
- B. 减少GPU显存占用，HDR格式比LDR格式每像素占用更少字节
- C. 提高渲染帧率，因为HDR格式纹理的GPU采样速度更快
- D. 允许像素值超过0-1范围，保留高亮度信息，支持Bloom、色调映射等效果

**Q119.** [模块:C][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

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

Linear和Gamma色彩空间的区别是？

- A. Linear空间仅适用于2D项目，3D项目应使用Gamma空间以获得更好的法线计算
- B. Linear物理正确（推荐），光照计算在线性空间中进行更准确；Gamma是遗留方式
- C. Gamma空间在光照计算上更加准确，Linear是为了兼容老旧硬件的简化方案
- D. Linear和Gamma仅影响编辑器中的颜色显示，不影响最终构建的渲染结果

**Q121.** [模块:C][维度:概念理解][难度:★★★★][题型:场景设计]

大型开放世界场景的渲染优化策略应包括？

- A. 减少场景中的物体数量到1000个以内，多余物体使用粒子系统模拟
- B. LOD系统+Occlusion Culling+场景流式加载+Shader LOD+纹理Streaming+远景Impostor
- C. 将所有资源在启动时一次性加载到内存中以避免运行时加载卡顿
- D. 仅使用低分辨率纹理和简化模型，牺牲画质确保稳定帧率

**Q122.** [模块:C][维度:概念理解][难度:★★★][题型:单选]

Unity中Skybox可以通过什么方式设置？

- A. Lighting Settings中设置全局Skybox，或Camera组件单独设置
- B. 仅能通过代码RenderSettings.skybox动态设置，不支持在编辑器中可视化配置
- C. 只能在Camera的Clear Flags为Depth Only时才能显示Skybox
- D. 只能使用6张独立纹理组成Cubemap，不支持Procedural或HDRI全景Skybox

**Q123.** [模块:C][维度:性能优化][难度:★★★★][题型:单选]

Shader性能优化的方法包括？

- A. 在Fragment Shader中进行大量循环计算和复杂光照
- B. 将所有计算都放在Vertex Shader中执行以减少GPU负载
- C. 减少分支语句和复杂数学运算
- D. 使用discard/clip指令可以提升移动端Shader性能

**Q124.** [模块:C][维度:概念理解][难度:★★★][题型:单选]

MeshRenderer组件中Cast Shadows和Receive Shadows选项的作用是？

- A. Cast Shadows控制是否接收阴影，Receive Shadows控制是否投射阴影（名称与功能相反）
- B. 两个选项共同控制阴影的分辨率级别，Off/On/Two Sided/Shadows Only对应不同精度
- C. Cast Shadows控制该物体是否产生阴影，Receive Shadows控制是否接收其他物体的阴影
- D. Cast Shadows仅在Built-in管线中生效，URP/HDRP中阴影由Volume组件统一控制

**Q125.** [模块:C][维度:Bug诊断][难度:★★★★][题型:单选]

场景中某个物体显示为粉色（品红色）。原因是什么？

- A. 纹理文件损坏或格式不支持，Unity将缺失纹理的像素填充为品红色
- B. 该物体的Layer未包含在Camera的Culling Mask中但仍被强制渲染
- C. 物体的法线方向全部反转，导致光照计算结果为负值被截断为品红色
- D. Material使用的Shader无法在当前平台/渲染管线下编译或找不到，Unity使用错误Shader渲染

**Q126.** [模块:C][维度:概念理解][难度:★★★][题型:单选]

Sorting Layer和Order in Layer在2D/3D渲染中的作用是？

- A. 控制精灵/渲染器的渲染先后顺序（Sorting Layer优先，相同Layer内按Order排序）
- B. 控制物理碰撞检测的优先级，Sorting Layer高的物体优先参与碰撞计算
- C. 仅影响3D物体在Scene视图中的Gizmo绘制层级，不影响Game视图渲染顺序
- D. 等同于Camera的Depth属性，多个Sorting Layer对应多个摄像机的叠加渲染

**Q127.** [模块:C][维度:代码生成/阅读][难度:★★★★][题型:代码补全]

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

URP/HDRP中Volume Component系统的作用是？

- A. 定义物理触发器区域，当玩家进入时执行自定义渲染管线脚本
- B. 控制场景中音频源(AudioSource)的音量衰减和混响效果范围
- C. 管理场景中光源的影响范围和衰减曲线，定义光照体积区域
- D. 空间区域化的后处理配置（进入不同区域自动应用不同后处理效果）

**Q129.** [模块:C][维度:概念理解][难度:★★★][题型:单选]

CombineMeshes的作用和限制是？

- A. 合并后的Mesh自动支持不同Material，每个子Mesh保持独立DrawCall
- B. 将多个Mesh合并为一个减少Draw Call；限制：合并后的物体共享Material，单个Mesh顶点上限
- C. 运行时不可用，只能在编辑器的Mesh Combine工具中使用
- D. 仅能合并两个Mesh，多次调用进行级联合并

**Q130.** [模块:C][维度:概念理解][难度:★★★★][题型:单选]

增大Shadow Distance（阴影距离）的代价是？

- A. 仅增加CPU计算开销用于更多阴影投射物体的裁剪判断，GPU开销不变
- B. 阴影贴图覆盖范围增大但每像素精度降低，导致近处阴影锯齿增加
- C. 增大Shadow Distance不影响阴影质量，Unity自动提高阴影贴图分辨率来补偿
- D. 减少GPU显存使用量，因为远处阴影使用更低精度的深度格式存储

**Q131.** [模块:C][维度:API精确度][难度:★★★][题型:单选]

Camera.fieldOfView设置的是什么？

- A. 近裁剪面的宽度（世界单位米）
- B. 垂直方向的视野角度（度）
- C. 水平方向的视野角度（度）
- D. 对角线方向的视野角度（弧度）

**Q132.** [模块:C][维度:性能优化][难度:★★★★][题型:场景设计]

一个移动端3D RPG游戏的渲染优化方案应包含哪些措施？

- A. 使用HDRP管线以获得最佳画质，依靠硬件升级解决性能问题
- B. 开启所有后处理效果提升画面质量，依靠Dynamic Resolution自动调节性能
- C. URP管线+LOD+Batching+纹理压缩(ASTC)+Light Probe+限制光源数+Shadow Distance限制
- D. 使用Built-in管线替代SRP以获得最兼容的渲染表现和最低开销

**Q133.** [模块:C][维度:概念理解][难度:★★★][题型:单选]

Stencil Buffer在渲染中的典型应用场景是？

- A. UI遮罩(Mask)、镜面效果、传送门效果、描边裁剪等
- B. 计算Per-Pixel光照的法线和反射方向数据
- C. 存储运动向量(Motion Vector)数据用于时间抗锯齿(TAA)和运动模糊
- D. 存储每个像素的颜色数据用于多重采样抗锯齿(MSAA)的子像素混合

**Q134.** [模块:C][维度:概念理解][难度:★★★★][题型:单选]

Impostor技术的原理是什么？

- A. 将多个远距离物体合并为一个Billboard渲染批次，共享同一张纹理图集
- B. 基于深度信息运行时生成视差贴图，替代3D模型实现近距离视角切换
- C. 预渲染3D物体的多角度2D图像，远处用2D图像代替3D模型，极大减少面数
- D. 使用LOD0的网格数据生成简化的凸包碰撞体用于远距离物理碰撞检测

**Q135.** [模块:C][维度:代码生成/阅读][难度:★★★★][题型:代码补全]

实现简单的全屏后处理效果：
```csharp
void OnRenderImage(RenderTexture src, RenderTexture dst) {
Graphics._____(src, dst, postProcessMaterial);
}
```
---

- A. Blit
- B. CopyTexture
- C. BlitMultiTap
- D. DrawTexture

**Q855.** [模块:C][维度:概念理解][难度:★★][题型:单选]

Rigidbody的Interpolate属性的作用是？

- A. 在物理帧之间平滑插值位置，减少视觉抖动（物理固定帧率与渲染帧率不一致时）
- B. 加速物理，GPU Instancing不需要Shader做特殊支持，任何Standard Shader都自动启用
- C. 提高物理精度，Shader Variant在Build时会被自动剥离，不影响运行时内存和包体
- D. 该设置不会对运行时行为产生实质影响，引擎内部会自动补偿参数差异

**Q856.** [模块:C][维度:概念理解][难度:★★][题型:单选]

OnTriggerEnter和OnCollisionEnter的区别：Trigger需勾选Is Trigger，不产生物理碰撞效果。

- A. 两者功能相同，只是名称不同
- B. 正确，Trigger需勾选Is Trigger，不产生物理碰撞效果
- C. OnTriggerEnter会产生物理碰撞效果，OnCollisionEnter不会
- D. 两者的区别仅在于性能开销不同

**Q881.** [模块:C][维度:代码生成/阅读][难度:★★★][题型:代码阅读]

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

**Q905.** [模块:C][维度:Bug诊断][难度:★★★★][题型:单选]

高速运动的物体穿越薄碰撞体(穿墙)的解决方案？

- A. Rigidbody.collisionDetectionMode设为Continuous+或用射线检测补偿+增加碰撞体厚度
- B. 变厚墙壁，SRP Batcher通过合并不同Mesh的渲染命令来减少Draw Call数量
- C. 不能解决，MaterialPropertyBlock的性能开销与直接修改Material.SetColor完全一致
- D. 增加帧率，MaterialPropertyBlock的性能开销与直接修改Material.SetColor完全一致

**Q919.** [模块:C][维度:概念理解][难度:★★★★][题型:单选]

Unity PhysX的性能调优参数？

- A. Fixed Timestep频率+Solver Iterations+碰撞矩阵+Auto Simulation+Default Contact Offset
- B. 自动优化，Occlusion Culling的运行时计算开销可以忽略，适合所有规模的场景
- C. 不可调参，SRP Batcher通过合并不同Mesh的渲染命令来减少Draw Call数量
- D. 只改帧率，SRP Batcher通过合并不同Mesh的渲染命令来减少Draw Call数量

**Q936.** [模块:C][维度:概念理解][难度:★★★★][题型:单选]

PhysicMaterial的Bounciness和Friction参数的Combine模式影响什么？

- A. 该设置不会对运行时行为产生实质影响，引擎内部会自动补偿参数差异
- B. 两个碰撞体的物理材质参数如何组合:Average/Minimum/Multiply/Maximum决定最终弹性/摩擦系数
- C. 相加，URP的Renderer Feature在渲染管线的Fixed Function阶段执行自定义逻辑
- D. 只取一个，MaterialPropertyBlock的性能开销与直接修改Material.SetColor完全一致

**Q954.** [模块:C][维度:代码生成/阅读][难度:★★★★][题型:代码阅读]

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

**Q978.** [模块:C][维度:概念理解][难度:★★★★][题型:单选]

Physics.OverlapSphereNonAlloc相比OverlapSphere的优势？

- A. 使用预分配数组避免每次调用产生GC分配(OverlapSphere每次new Collider[])
- B. 更准确，RenderTexture在使用完后会被GC自动释放，不需要手动Release
- C. 两者在功能和性能上没有本质区别，底层调用相同的引擎API，选择哪个取决于编码习惯
- D. 更快，Shader Variant在Build时会被自动剥离，不影响运行时内存和包体

