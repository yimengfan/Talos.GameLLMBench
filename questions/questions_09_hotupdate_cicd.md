# Unity3D 2022 LTS 基础能力问答题库 - 09_hotupdate_cicd

**Q578.** [模块:Q][维度:概念理解][难度:★★★][题型:单选]

Unity热更新的核心需求是什么？

- A. 让客户端下载完整新包替换旧安装目录，确保代码和资源始终来自同一安装版本
- B. 更新设备上的系统运行库，从而避免重新分发Unity Player和游戏资源
- C. 升级Unity引擎小版本，使旧逻辑在新运行时环境中自动获得修复
- D. 不重新下载/安装游戏的情况下更新代码逻辑和资源（修Bug、加活动、调数值）

**Q579.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]

xLua/toLua热更方案的原理是？

- A. 下载新的C# DLL并直接替换IL2CPP生成的原生代码段来完成逻辑更新
- B. 先把Lua脚本编译成托管DLL，再交给CLR按普通C#程序集方式执行
- C. 通过重新打包AssetBundle把全部脚本逻辑编进资源包，运行时只需换资源包即可
- D. 内嵌Lua虚拟机，C#和Lua互调，下载新Lua脚本替换逻辑；Lua作为解释型语言无需重编译

**Q580.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]

HybridCLR(原huatuo)的原理和优势是？

- A. 只能在Mono后端通过反射替换方法体实现，IL2CPP项目无法使用
- B. 扩展IL2CPP支持动态加载DLL(Interpreter模式)，可直接用C#热更，无需学Lua
- C. 替代IL2CPP
- D. 主要优势是把Lua脚本自动翻译成原生C#代码，从而兼容所有AOT限制

**Q581.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]

ILRuntime的热更原理是？

- A. AOT编译
- B. C#实现的IL解释器，读取DLL的IL字节码在运行时解释执行
- C. 预先把热更DLL转成原生代码并在运行时直接装载，因此执行路径与AOT代码完全一致
- D. 把IL字节码转发到GPU上的Compute Shader执行，从而绕开移动平台的JIT限制

**Q582.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]

主流热更方案各自的特点是？

- A. HybridCLR支持原生C#热更
- B. IL2CPP原生就支持任意托管程序集热加载，HybridCLR和ILRuntime只是封装工具
- C. 所有热更方案都同时覆盖代码、Shader和底层渲染管线更新，不需要区分资源热更
- D. Lua脚本层更适合数值密集和高频循环，因为解释执行通常比原生C#更快

**Q583.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]

为什么IL2CPP模式下不能直接使用System.Reflection.Emit创建新类型？

- A. IL2CPP是AOT编译，将IL转为C++不包含JIT编译器，无法在运行时生成新的原生代码
- B. IL2CPP打包时会移除Emit命名空间，因此运行时根本拿不到这些API
- C. 只要把相关程序集加入link.xml保留列表，Reflection.Emit在IL2CPP下就能正常生成新类型
- D. Unity只是不开放相关权限接口，本质上IL2CPP仍然可以在运行时生成并执行新的机器码

**Q584.** [模块:Q][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

xLua中Lua调用C#的方式：
```lua
local go = CS.UnityEngine.GameObject("NewObj")
local transform = go.transform
transform.position = CS.UnityEngine.Vector3(1, 2, 3)
```
CS.UnityEngine代表什么？

- A. xLua中通过CS表访问C#命名空间和类型
- B. Unity自动生成的场景对象注册表，所有Lua访问的C#类型都会先写入这里
- C. 用于创建场景树的DSL前缀，和C#命名空间映射没有关系
- D. AssetBundle的命名空间前缀，用来根据字符串路径索引资源

**Q585.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]

xLua与C#互调的性能优化方法是？

- A. 频繁通过反射查找成员并在每次调用时动态装箱拆箱，避免生成额外绑定代码
- B. 使用[LuaCallCSharp]生成适配代码减少反射+减少跨语言调用频率+缓存Component引用
- C. 尽量避免任何C#到Lua的调用，只保留Lua单向驱动全部Unity API的模式
- D. 只要开启IL2CPP，C#/Lua互调的反射和封送开销就会被运行时自动优化掉

**Q586.** [模块:Q][维度:概念理解][难度:★★★★][题型:场景设计]

完整的热更新架构应包含什么？

- A. 版本管理+差异检测+下载器(断点续传)+资源解压+代码热更加载器+回退机制
- B. 只更新热更DLL即可，资源永远保持首包版本通常不会引发兼容性问题
- C. 重新安装
- D. 只下载资源清单和资源包即可，失败重试、版本校验和回退链路都可以省略

**Q587.** [模块:Q][维度:Bug诊断][难度:★★★★][题型:单选]

IL2CPP下泛型使用热更时可能遇到的问题是？

- A. 只影响性能
- B. AOT泛型限制：IL2CPP需要泛型实例化代码在编译时生成，新泛型参数组合可能找不到对应代码
- C. 只要补充link.xml保留反射类型，就不会再出现任何AOT泛型缺失问题
- D. 泛型不能用

**Q588.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]

HybridCLR中补充元数据(Supplementary Metadata)的作用是？

- A. 为AOT泛型提供缺失的元数据，使解释器能正确实例化泛型类型
- B. 在构建阶段重新生成缺失的AOT原生代码，让运行时不再需要解释执行
- C. 把所有热更元数据预先转成压缩二进制缓存，以减小DLL和元数据文件的体积
- D. 取代Assembly.Load流程，使热更DLL不再参与类型解析和反射调用

**Q589.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]

热更代码的版本兼容性如何保证？

- A. 每次都做全量包覆盖更新，避免处理接口兼容、数据迁移和灰度发布问题
- B. 只要热更代码能被加载，序列化结构和协议字段变化通常不会影响旧客户端
- C. 接口版本号+数据序列化版本管理+新旧代码兼容设计+灰度发布
- D. 只更新资源

**Q590.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]

iOS平台热更新的限制和绕过方式是？

- A. Apple禁止下载可执行代码；Lua等脚本语言被归类为数据可绕过；HybridCLR通过解释器执行
- B. 只能使用明文Lua文本脚本，任何字节码和解释器方案都会被审核直接拒绝
- C. iOS完全禁止任何形式的热更，包括配置、脚本和资源下发
- D. 只要通过HTTPS下载，Apple对运行时脚本解释和资源更新没有额外审核限制

**Q591.** [模块:Q][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

HybridCLR加载热更DLL：
```csharp
byte[] dllBytes = await LoadDLLFromServer("HotFix.dll.bytes");
Assembly hotfixAssembly = System.Reflection.Assembly.Load(dllBytes);
Type entryType = hotfixAssembly.GetType("HotFix.GameEntry");
entryType.GetMethod("Start").Invoke(null, null);
```
这段代码做了什么？

- A. 下载到的DLL会在下一次构建时静态链接进主工程，运行时这里只是读取配置入口
- B. 把DLL写入persistentDataPath，等待下次启动由主域自动发现并装载
- C. 重新生成IL2CPP桥接代码并把对应方法体热替换到当前进程中
- D. 从服务器下载DLL→加载到内存→反射获取入口类→调用Start方法启动热更逻辑

**Q592.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]

热更新发布前的测试流程应包含？

- A. 只要编辑器里能跑通热更入口，就可以跳过版本兼容、失败重试和回退演练
- B. 只要开发环境下载成功一次即可，线上包体问题可以通过下一次热更新覆盖解决
- C. 只测业务功能即可，C#/Lua桥接、裁剪配置和AOT兼容性通常不会成为上线风险
- D. 本地热更模拟+灰度测试+回退验证+兼容性测试(新旧版本客户端)

**Q593.** [模块:Q][维度:概念理解][难度:★★★★][题型:场景设计]

xLua项目的代码架构设计原则？

- A. 不需要分层架构，HybridCLR性能与AOT代码等价，所以业务逻辑放哪里都一样
- B. C#做框架和性能敏感逻辑+Lua做业务逻辑+定义清晰的C#/Lua交互接口+减少跨语言调用
- C. 全部C#并通过资源更新驱动逻辑切换，Unity会自动处理脚本版本兼容问题
- D. 全部Lua

**Q594.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]

link.xml在热更中的作用是？

- A. HTML链接
- B. 主要用于把多个热更DLL自动合并成一个程序集，降低Assembly.Load的复杂度
- C. 负责声明远程热更包的下载地址，避免把版本配置硬编码在客户端里
- D. 防止IL2CPP裁剪(strip)掉热更代码需要反射调用的类型和方法

**Q595.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]

Mono和IL2CPP后端的区别和对热更的影响是？

- A. Mono支持JIT可直接加载DLL但性能较低；IL2CPP是AOT性能高但需要HybridCLR/ILRuntime等方案实现热更
- B. IL2CPP支持JIT，在IL2CPP后端下使用反射动态创建类型不受AOT限制，运行时行为与Mono一致
- C. 相关功能仅在旧版Unity中支持，最新版本已将其移除
- D. Mono性能更高

**Q596.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]

热更新的安全考虑包括？

- A. 资源加密和完整性校验
- B. 只要接入CDN，从任意HTTP源下载热更包都天然具备完整性和来源可信性
- C. 热更包不需要版本验证，直接覆盖本地文件是最简单且可靠的策略
- D. 热更包不需要加密，脚本和资源文件在客户端几乎无法被逆向查看

**Q597.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]

热更新的增量更新方案如何实现？

- A. 对比版本文件列表(MD5/CRC)+只下载有差异的文件+本地缓存管理
- B. 不支持增量
- C. 只下载代码文件即可，资源差异通常由Unity运行时自动补齐和修复
- D. 每次全量下载更稳妥，增量更新在客户端几乎无法做版本一致性校验

**Q598.** [模块:Q][维度:概念理解][难度:★★★★][题型:场景设计]

完整的热更新发布流程是？

- A. 开发→构建热更包→上传CDN→更新版本配置→灰度发布→全量发布→监控→回退准备
- B. 重新打包APK
- C. 直接上传到正式环境即可，热更包体积小所以无需灰度、监控和回退预案
- D. 发版后由客户端自行检测新文件，通常不需要CDN配置、版本发布或监控链路

**Q599.** [模块:Q][维度:Bug诊断][难度:★★★★][题型:单选]

HybridCLR热更后运行时报TypeLoadException，可能原因是？

- A. DLL损坏
- B. 内存不足通常会优先表现为TypeLoadException，因为类型元数据无法分配连续空间
- C. 该问题与Unity版本相关，在某些版本中行为不一致，建议查阅版本Release Notes
- D. 热更DLL引用了AOT中被裁剪掉的类型，需要在link.xml中保留或补充元数据

**Q600.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]

热更代码的调试方法是？

- A. 只看日志
- B. 编辑器模式直接运行热更DLL+Lua远程调试(ZeroBrane/VSCode插件)+日志系统+灰度环境
- C. 重新完整构建主包后观察启动日志即可，通常不需要单独的热更调试链路
- D. 不能调试，热更代码一旦脱离主工程编译流程就只能依赖线上日志排查

**Q601.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]

资源热更和代码热更的关系是？

- A. 通常一起做：AssetBundle/Addressables管理资源热更，Lua/HybridCLR/ILRuntime管理代码热更
- B. 完全独立
- C. 只需代码热更，大多数活动、配置和美术修改都能通过脚本自动兼容旧资源
- D. 资源热更天然覆盖脚本逻辑更新，因为业务逻辑最终都会随资源打包一起替换

**Q602.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]

热更新出现严重Bug时的回退策略是？
---

- A. 直接要求玩家重新安装完整客户端，避免维护历史热更包和版本切换逻辑
- B. 等下一次常规发版覆盖即可，线上热更包一旦发布通常不值得维护回退逻辑
- C. 服务器下发版本回退指令+客户端加载上一个正确版本的代码和资源+强制更新机制
- D. 不能回退

**Q603.** [模块:R][维度:概念理解][难度:★★★][题型:单选]

AssetBundle的构建流程是？

- A. 主要靠手动复制目标文件到StreamingAssets目录，Manifest和依赖信息可忽略
- B. 标记资源AB名→BuildPipeline.BuildAssetBundles→输出AB文件+Manifest
- C. 只能用Addressables，原生AssetBundle工作流在Unity 2022里已经不推荐继续使用
- D. 打包流程完全自动，Unity会总是只构建发生变化的Bundle而不需要额外配置

**Q604.** [模块:R][维度:概念理解][难度:★★★★][题型:单选]

AssetBundle的Manifest文件包含什么信息？

- A. 主要是每个Bundle内脚本和资源的二进制内容，用于运行时直接恢复对象数据
- B. 只有Bundle文件名和构建时间戳，依赖关系需要运行时通过扫描目录推断
- C. 所有AB的Hash、CRC、依赖关系列表、包含的资源列表
- D. 主要保存已压缩的资源内容副本，便于客户端下载时做差异比较

**Q605.** [模块:R][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

从本地加载AssetBundle：
```csharp
AssetBundle ab = AssetBundle.LoadFromFile(path);
GameObject prefab = ab.LoadAsset<GameObject>("PlayerPrefab");
Instantiate(prefab);
// 使用完毕
ab.Unload(false);
```
LoadFromFile和LoadFromMemory的区别？

- A. LoadFromMemory通常更高效，因为避免了文件IO并且可以直接零拷贝复用底层缓存
- B. LoadFromFile并不会真正访问磁盘数据，更多只是一个逻辑上的Bundle定位接口
- C. LoadFromFile直接从磁盘加载(高效)，LoadFromMemory从byte[]加载(需先读入内存，有额外内存开销)
- D. 两者本质等价，只要最后都得到AssetBundle实例，内存和性能特征没有明显区别

**Q606.** [模块:R][维度:概念理解][难度:★★★★][题型:单选]

AssetBundle.LoadFromFileAsync和同步版本的区别是？

- A. 该API只是在语法上更现代，本质仍是同步加载，无法避免主线程卡顿
- B. 异步通常更慢且更占内存，所以只适合编辑器调试而不适合正式项目
- C. 异步不阻塞主线程（不卡帧），通过回调或await获取结果
- D. 异步接口只有在Awake阶段调用才有效，运行时再调用会退回同步加载

**Q607.** [模块:R][维度:概念理解][难度:★★★★][题型:场景设计]

AssetBundle管理器应具备的功能？

- A. 直接LoadFromFile
- B. 启动时把所有资源全部预加载进内存最简单，后续就不再需要依赖管理和卸载策略
- C. 不需要专门管理器，Unity底层会自动处理所有Bundle依赖、缓存和错误恢复
- D. 依赖自动加载+引用计数+缓存+异步队列+卸载策略+错误处理

**Q608.** [模块:R][维度:Bug诊断][难度:★★★★][题型:单选]

对同一个已加载的AssetBundle再次调用LoadFromFile会怎样？

- A. 抛出异常(The AssetBundle 'X' can't be loaded because another AssetBundle with the same files is already loaded)
- B. 自动覆盖旧实例并替换所有已加载资源引用，等价于一次热重载
- C. 返回当前已加载Bundle的缓存实例，不会产生新的冲突或异常
- D. 是否报错不只看路径，核心还取决于底层Bundle文件标识、已加载状态和运行时缓存中的冲突情况

**Q609.** [模块:R][维度:概念理解][难度:★★★★][题型:单选]

AssetBundle缓存系统(Caching)的作用是？

- A. 不需要做缓存，网络和磁盘都足够快，重复下载和加载Bundle对正式项目影响很小
- B. 通过UnityWebRequestAssetBundle+CachedAssetBundle下载AB时自动缓存到本地，下次优先用缓存
- C. 主要是把所有Bundle永久缓存到内存中，避免任何磁盘访问和版本校验开销
- D. 主要用于替代CDN做分发，只要本地有Caching系统就不再需要远程资源服务

**Q610.** [模块:R][维度:概念理解][难度:★★★★][题型:单选]

AssetBundle Variant的用途是？

- A. 同一AB打包不同品质的资源（如高清/标清纹理），运行时根据设备选择
- B. 主要用于保存同一个Bundle的历史版本，方便客户端在运行时做回滚切换
- C. 专门用于多语言文本资源切换，底层不会改变Bundle的构建和选择逻辑
- D. 主要用于跨平台共享同一套Bundle产物，避免分别为Android和iOS构建资源包

**Q611.** [模块:R][维度:性能优化][难度:★★★★][题型:单选]

AssetBundle性能优化方法？

- A. 使用LZMA压缩格式可以获得最快的加载速度
- B. 在运行时解压所有AssetBundle到内存以获得最佳性能
- C. 每个资源单独打包一个AssetBundle以获得最大的灵活性
- D. 使用LZ4压缩和依赖预加载

**Q612.** [模块:R][维度:概念理解][难度:★★★★][题型:单选]

Scriptable Build Pipeline(SBP)相比传统BuildPipeline的优势是？

- A. 打包到移动端后无法正常工作
- B. 不支持AssetBundle，SBP主要是给Addressables和场景构建使用的内部工具链
- C. 构建速度通常更慢，因为自定义管线会引入更多资源扫描和额外内存拷贝
- D. 更灵活的构建流程+增量构建+更好的缓存+可自定义构建步骤

**Q613.** [模块:R][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

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

- A. Unity已经完全自动处理依赖加载，开发者手动加载依赖只是为了让日志更清晰
- B. 顺序无所谓，主Bundle加载时会自动把所有共享资源递归拉起并绑定完成
- C. 只是调试建议，不先加载依赖通常也不会影响材质、Shader和贴图引用解析
- D. 否则AB中引用的共享资源(Shader/Material/Texture)会丢失(品红色/Missing)

**Q614.** [模块:R][维度:概念理解][难度:★★★★][题型:单选]

AB热更新的完整流程是？

- A. 只下载Manifest即可，客户端拿到最新依赖信息后通常可以直接复用旧Bundle内容
- B. 不需要主动更新，只要下次重启时重新加载本地Bundle，版本差异会被自动修复
- C. 客户端下载远程Manifest→与本地对比→下载差异AB→替换本地AB→重新加载
- D. 每次重新下载所有Bundle最稳妥，差异对比和缓存命中在实际项目里收益很低

**Q615.** [模块:R][维度:Bug诊断][难度:★★★★][题型:单选]

AB文件为什么不能跨平台使用？

- A. 可以跨平台，只要Unity主版本一致，Bundle内容会自动适配目标设备的底层格式
- B. 主要只是Unity版本差异，和平台资源格式、Shader编译结果关系不大
- C. AB包含平台特定的资源格式（如纹理压缩、Shader编译结果），不同平台格式不同
- D. 主要因为不同平台默认Bundle文件名不同，只要手动统一命名即可通用

**Q616.** [模块:R][维度:概念理解][难度:★★★★][题型:单选]

减少AssetBundle包体大小的方法是？

- A. 纹理压缩+音频压缩+去除重复资源+剔除不需要的资源(Editor Only)+使用LZ4/LZMA压缩
- B. 使用更大纹理和更高质量音频能提升压缩比，从而显著减小最终Bundle体积
- C. 增加Bundle数量通常会自然消除重复依赖，因此包体会持续线性下降
- D. 不做压缩通常更省空间，因为运行时无需额外保存解压后的临时数据

**Q617.** [模块:R][维度:概念理解][难度:★★★★][题型:场景设计]

大型项目AB打包策略设计原则？

- A. 按模块/场景分包+公共资源独立包+频繁更新的独立包+控制单个AB大小(5-20MB)+使用分析工具检查冗余
- B. 不需要策略，Bundle划分对更新效率、冗余依赖和内存管理影响很小
- C. 按文件逐个打包最灵活，通常也是依赖最清晰且最便于热更新的做法
- D. 全部打成一个大包最省管理成本，更新时只替换一个文件即可解决所有问题

**Q618.** [模块:R][维度:概念理解][难度:★★★★][题型:单选]

AssetBundle加密的方案是？

- A. Unity内置完整的Bundle加密开关，构建时勾选后运行时LoadFromFile会自动解密
- B. 自定义加密（如AES）打包后加密文件→加载时解密到内存→LoadFromMemory
- C. 只加密Manifest即可，因为真正的资源数据文件默认无法被直接提取和复用
- D. 不能加密，Bundle文件一旦加密就无法再被Unity运行时正确识别和加载

**Q619.** [模块:R][维度:概念理解][难度:★★★★][题型:单选]

AssetBundle.LoadFromStream的优势是？

- A. 该方法执行速度更慢，因为涉及跨线程同步和额外的内存拷贝开销
- B. 该API已不推荐在Unity 2022中使用，官方文档建议使用新的替代方案
- C. 和LoadFromFile一样
- D. 支持自定义Stream（可实现边解密边加载，无需全部解密到内存）

**Q620.** [模块:R][维度:概念理解][难度:★★★★][题型:单选]

AssetBundle引用计数的实现要点？

- A. 加载AB和其资源时增加计数，卸载时减少计数，计数为0时Unload(true)释放
- B. 不需要计数，只要在场景切换时统一UnloadUnusedAssets即可覆盖大多数生命周期问题
- C. Unity会自动管理Bundle和资源依赖的引用关系，业务层通常不必维护独立计数
- D. 引用计数只在编辑器调试阶段有意义，正式包里通常依赖GC和场景卸载回收

**Q621.** [模块:R][维度:概念理解][难度:★★★★][题型:单选]

从AssetBundle迁移到Addressables的步骤和注意事项？

- A. 不需要迁移，AssetBundle工作流和Addressables底层完全不同，混用通常不可行
- B. 添加Addressables Package→标记资源地址→替换加载代码→迁移AB打包逻辑→测试兼容性
- C. Addressables会自动读取现有AssetBundle命名并零修改接管运行时加载逻辑
- D. 当前Unity版本不适合迁移，通常需要降级到更旧的LTS版本才能保持稳定

**Q622.** [模块:R][维度:概念理解][难度:★★★★][题型:单选]

AssetBundle构建缓存的作用是？
---

- A. 不需要做缓存处理，现代设备的IO速度足够快，每次直接读取磁盘即可
- B. 主要是运行时下载缓存，和构建速度、依赖分析以及增量构建命中没有直接关系
- C. 增量构建时只重新打包有变化的资源，大幅减少构建时间
- D. 主要用于保存客户端下载缓存，构建阶段仍然会完整重打所有Bundle

**Q623.** [模块:S][维度:概念理解][难度:★★★][题型:单选]

Unity构建Android APK需要配置什么？

- A. 几乎不需要配置，切到Android平台后大多数签名和SDK选项都会由Unity自动推断
- B. 只需点Build
- C. 只需要SDK
- D. JDK/SDK/NDK路径+Package Name+最低API Level+Target API+KeyStore签名

**Q624.** [模块:S][维度:概念理解][难度:★★★][题型:单选]

Unity构建iOS项目的流程是？

- A. 不需要Xcode，Unity可以直接在macOS上输出可提交App Store的IPA安装包
- B. Unity导出Xcode项目→Xcode配置签名和证书→通过Xcode打包IPA
- C. Unity可以直接输出IPA，导出的Xcode工程通常只用于查看中间文件而不是实际打包
- D. iOS端处理流程与Android几乎完全一致，签名、证书和本地工程差异可以忽略

**Q625.** [模块:S][维度:概念理解][难度:★★★★][题型:单选]

Unity Native Plugin(原生插件)的用途和实现方式是？

- A. 调用平台原生功能(如iOS/Android SDK)；通过DllImport(C/C++)或AndroidJavaObject/UnitySendMessage
- B. 主要面向Android，iOS平台通常不能通过Unity稳定接入原生SDK
- C. 只用于C++插件，而且Android和iOS的调用接口完全统一，通常不需要平台分支代码
- D. 主要用于自动生成浏览器沙箱接口，和移动端原生SDK接入关系不大

**Q626.** [模块:S][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

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

- A. 关闭当前应用并切换回桌面，因为拿到currentActivity后默认会结束Unity宿主Activity
- B. 启动一个新的Android Activity，runOnUiThread主要用于切换到新的页面栈上下文
- C. 获取Android Activity引用，在Android UI线程中执行操作（如显示原生对话框）
- D. 加载原生资源并自动完成SDK初始化，拿到Activity后无需再调用具体Java方法

**Q627.** [模块:S][维度:概念理解][难度:★★★★][题型:单选]

Unity平台条件编译宏的用途是？
```csharp
// Android特定代码
// iOS特定代码
```

- A. 主要用于给不同平台插入调试和日志代码，和正式构建逻辑关系不大
- B. 主要用于运行时判断当前平台，因此代码会在所有平台编译后再决定是否执行
- C. 主要用于平台性能优化开关，本身和代码裁剪、平台编译分支没有直接关系
- D. 根据目标平台编译不同的代码，同一份代码适配多平台

**Q628.** [模块:S][维度:概念理解][难度:★★★★][题型:单选]

Android App Bundle(AAB)相比APK的优势是？

- A. 主要用于浏览器分发，不适合Unity移动项目的正式商店提交流程
- B. 和APK本质完全一样，只是扩展名变化，对分发和安装体积没有实际影响
- C. Google Play按设备提供优化包（按CPU架构/屏幕密度/语言分拆），减少安装包大小
- D. 通常会更大，因为AAB会把所有架构和资源变体都打进统一安装包上传

**Q629.** [模块:S][维度:概念理解][难度:★★★★][题型:场景设计]

接入第三方SDK（支付/广告/统计/推送）的架构设计？

- A. 统一接口层(Interface)+各平台实现(Android/iOS)+工厂模式创建+异步回调机制
- B. 不做抽象最简单，平台差异通常只体现在包格式和证书配置上
- C. 所有地方直接调原生SDK即可，AAB/APK或iOS签名流程不会影响运行时接口设计
- D. 每个业务点单独接一次SDK最灵活，后期平台差异可以交给条件编译自然消化

**Q630.** [模块:S][维度:Bug诊断][难度:★★★★][题型:单选]

Android设备崩溃日志中出现java.lang.UnsatisfiedLinkError，可能原因是？

- A. 内存不足或GC抖动，通常都会先以UnsatisfiedLinkError的形式暴露出来
- B. 这是Unity引擎的已知Bug，在特定版本中存在该问题，升级到最新补丁版本可修复
- C. Java代码逻辑错误最常见，只要JAR/AAR放进Plugins目录，so库一般会自动绑定成功
- D. 原生so库找不到或CPU架构(arm64-v8a/armeabi-v7a)不匹配

**Q631.** [模块:S][维度:概念理解][难度:★★★★][题型:单选]

Android运行时权限(如相机、存储)在Unity中如何处理？

- A. 不需要请求
- B. 使用Android.Permission.RequestUserPermission()在运行时动态请求
- C. 自动授权
- D. 只要在Manifest中声明即可，运行时权限弹窗会由系统在首次调用相关API时自动处理

**Q632.** [模块:S][维度:概念理解][难度:★★★★][题型:单选]

Unity WebGL平台的主要限制包括？

- A. WebGL与移动端和PC几乎没有差异，Unity跨平台层已经屏蔽了线程和网络能力限制
- B. 不能运行复杂Unity项目，主要因为WebGL只适合展示静态内容和简单UI页面
- C. 几乎没有额外限制，线程、内存和浏览器沙箱不会对正式项目造成明显影响
- D. 不支持线程(Thread)+不支持Socket+受浏览器沙箱限制+代码运行在WASM中

**Q633.** [模块:S][维度:概念理解][难度:★★★★][题型:单选]

不同平台内存管理的差异是？

- A. 只有PC平台需要特别关注内存上限，移动端和WebGL通常由Unity自动接管回收策略
- B. 基本不影响开发，只要遵守C#内存管理习惯，平台差异通常不会显著影响崩溃风险
- C. iOS内存限制更严格(被系统杀进程)+Android碎片化严重(不同设备差异大)+WebGL受浏览器限制
- D. 所有平台内存行为基本一致，主要差异只体现在包格式和应用签名流程上

**Q634.** [模块:S][维度:概念理解][难度:★★★★][题型:单选]

多平台适配需要处理的差异包括？

- A. 多平台适配主要只需要改Bundle Identifier和构建输出格式，运行时差异很小
- B. 各平台输入、音频和渲染能力基本相同，条件编译通常只用于第三方SDK集成
- C. 通常只需处理UI分辨率适配，输入、文件系统和渲染差异大多能由Unity自动屏蔽
- D. 输入系统、音频格式、渲染API差异

**Q635.** [模块:S][维度:概念理解][难度:★★★][题型:单选]

PlayerSettings中Company Name和Product Name的影响是？

- A. 只影响应用商店展示信息，对运行时路径和Unity API返回值没有任何影响
- B. 主要用于启动画面和系统设置页显示，和文件路径及运行时标识无关
- C. 只用于商店元数据与签名信息管理，不会影响 `Application.companyName` 等运行时字段
- D. 影响Application.companyName和productName，决定persistentDataPath的路径

**Q636.** [模块:S][维度:概念理解][难度:★★★★][题型:单选]

Unity Android项目的Gradle配置文件(mainTemplate.gradle)的作用是？

- A. 替代Unity Build
- B. 主要用于iOS工程配置共享，Android Gradle依赖和签名通常不通过这里管理
- C. 主要用于资源目录组织和包体裁剪，和Gradle依赖、编译参数关系很弱
- D. 自定义Android构建配置（添加SDK依赖、配置ProGuard、修改编译选项等）

**Q637.** [模块:S][维度:概念理解][难度:★★★★][题型:单选]

移动端性能分级(Quality Tiers)的策略是？

- A. 让玩家手动选择画质通常就足够，不需要根据设备信息自动分层
- B. 统一最高画质最利于保证体验一致性，平台能力差异通常不会显著影响稳定性
- C. 根据设备GPU/内存自动选择画质等级（低中高：调整分辨率/阴影/后处理/LOD/粒子数量）
- D. 统一最低画质最稳妥，可以完全避免做机型分级、动态降级和专项性能调优

**Q638.** [模块:S][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

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

- A. 把UI面板强制拉伸到全屏区域，忽略刘海和圆角带来的可见区域变化
- B. 将UI面板临时移动到屏幕外，用于在切场景时隐藏界面
- C. 只是在做普通分辨率缩放，和安全区域、异形屏遮挡没有直接关系
- D. 将UI面板限制在安全区域内，避免被刘海/圆角遮挡

**Q639.** [模块:S][维度:概念理解][难度:★★★★][题型:场景设计]

Unity项目CI/CD流水线应包含？

- A. 代码拉取→自动编译→单元测试→AB构建→Player构建→自动化测试→部署/上传→通知
- B. 主要还是人工打包和上传，流水线只需要在失败时收集一点日志辅助排查
- C. 只做自动化测试即可，构建、资源打包和部署通常不适合纳入统一流水线
- D. 只做编译产物输出即可，平台差异和部署环节可以完全交给开发者本地处理

**Q640.** [模块:S][维度:Bug诊断][难度:★★★★][题型:单选]

IL2CPP构建时报"Unresolved external symbol"错误，可能原因是？

- A. 普通C#语法错误最常见，IL2CPP阶段的链接错误通常只是编译器表层提示
- B. 代码中使用了平台不支持的API或native方法在目标平台上没有对应实现
- C. 内存不足或优化等级不一致也经常直接导致链接器找不到外部符号实现
- D. 该问题与Unity版本相关，在某些版本中行为不一致，建议查阅版本Release Notes

**Q641.** [模块:S][维度:概念理解][难度:★★★★][题型:单选]

线上崩溃分析工具和流程是？

- A. 不需要专门分析流程，只要用户量足够大，评论区和客服反馈会自然暴露主要崩溃问题
- B. 接入崩溃平台后通常会自动修复大部分常见问题，开发者主要看告警趋势即可
- C. Crashlytics/Bugly收集崩溃→符号化堆栈→分析崩溃模式→定位修复→热更/发版
- D. 看评论

**Q642.** [模块:S][维度:概念理解][难度:★★★★][题型:单选]

减少游戏安装包大小的方法？
---

- A. 只减少资源通常就够了，代码体积和安装结构对正式包大小影响相对有限
- B. 通过降低代码优化等级或禁用部分调试符号，一般就能显著缩小安装包
- C. 该场景不需要专门优化，Unity默认设置已经足够高效，过度优化反而增加维护成本
- D. 纹理压缩+音频压缩+代码裁剪(Managed Stripping)+移除未使用资源+首包最小化+按需下载

**Q643.** [模块:T][维度:概念理解][难度:★★★][题型:单选]

CI/CD在游戏开发中的含义是？

- A. 只是自动测试，Unity Test Framework的[Test]属性用于编写Play Mode异步测试用例
- B. 手动流程
- C. 持续集成(自动编译/测试)+持续交付/部署(自动构建包体/部署)
- D. 只是自动编译，Jenkins/GitHub Actions中运行Unity构建不需要激活License可直接使用

**Q644.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]

Unity命令行构建的方式是？

- A. 用脚本文件打包，Jenkins/GitHub Actions中运行Unity构建不需要激活License可直接使用
- B. 自动检测，Git LFS不适用于Unity项目的大文件管理，推荐直接将asset二进制文件入库
- C. 只能GUI打包
- D. Unity.exe -batchmode -executeMethod ClassName.MethodName -quit，调用静态方法执行BuildPipeline

**Q645.** [模块:T][维度:概念理解][难度:★★★★][题型:场景设计]

Unity + Jenkins CI流水线配置要点？

- A. 不兼容Jenkins，Unity Cloud Build的构建速度与本地构建完全一致，不受网络带宽影响
- B. 不需要配置，Git LFS不适用于Unity项目的大文件管理，推荐直接将asset二进制文件入库
- C. 安装Unity插件+配置Unity路径+构建触发器(Git Push)+构建步骤(命令行)+后处理(归档/通知)
- D. 只能用Unity Cloud Build

**Q646.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]

Unity Test Framework支持哪两种测试模式？

- A. 只有编辑器，Git LFS不适用于Unity项目的大文件管理，推荐直接将asset二进制文件入库
- B. 不支持测试，Jenkins/GitHub Actions中运行Unity构建不需要激活License可直接使用
- C. 只有PlayMode，Git LFS不适用于Unity项目的大文件管理，推荐直接将asset二进制文件入库
- D. EditMode Tests(编辑器同步执行，不需Play) + PlayMode Tests(需进入Play Mode，测试运行时逻辑)

**Q647.** [模块:T][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

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

- A. 该特性目前仍处于实验阶段，官方不建议在生产环境中使用
- B. [UnityTest]不能用yield，[UnityTest]属性标记的测试方法不支持yield return等待异步操作完成
- C. [Test]用于PlayMode
- D. [Test]同步执行不需Unity环境，[UnityTest]返回IEnumerator可等待帧/时间（适合测试协程/物理等）

**Q648.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]

Unity项目CI/CD常用工具包括？

- A. Photoshop、Illustrator、Blender、Maya
- B. Chrome、Firefox、Safari、Edge
- C. Word、Excel、PowerPoint、Outlook
- D. Jenkins、GitHub Actions、GitLab CI

**Q649.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]

Unity构建中Library文件夹缓存的作用是？

- A. 缓存构建产物
- B. 缓存源代码，Git LFS不适用于Unity项目的大文件管理，推荐直接将asset二进制文件入库
- C. 缓存资源导入结果，避免每次构建重新导入所有资源（加速构建）
- D. 不需要缓存

**Q650.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]

游戏版本号管理的规则是？

- A. 不需要版本号
- B. 主版本.次版本.修订号+构建号自动递增；CI自动更新PlayerSettings.bundleVersion
- C. 手动输入
- D. 随机生成

**Q651.** [模块:T][维度:Bug诊断][难度:★★★★][题型:单选]

CI服务器上Unity构建失败但本地成功，常见原因是？

- A. CI环境缺少License激活/Library缓存不一致/SDK路径不同/Git LFS未拉取大文件
- B. CI服务器性能差
- C. 这是Unity引擎的已知Bug，在特定版本中存在该问题，升级到最新补丁版本可修复
- D. 代码问题

**Q652.** [模块:T][维度:概念理解][难度:★★★★][题型:场景设计]

游戏自动化测试金字塔策略？

- A. 只做端到端，Unity Cloud Build的构建速度与本地构建完全一致，不受网络带宽影响
- B. 单元测试(最多，纯逻辑)+集成测试(系统交互)+端到端测试(最少，真实设备)
- C. 不做测试，Unity Cloud Build的构建速度与本地构建完全一致，不受网络带宽影响
- D. 全部手动，Jenkins/GitHub Actions中运行Unity构建不需要激活License可直接使用

**Q653.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]

Unity项目代码质量保障工具包括？

- A. Roslyn Analyzers + EditorConfig + Code Coverage + Static Analysis
- B. 只检查格式
- C. 不做检查
- D. 只靠代码审查

**Q654.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]

为什么Unity项目需要使用Git LFS？

- A. 只是习惯，Unity Test Framework的[Test]属性用于编写Play Mode异步测试用例
- B. 该步骤不是必需的，Unity引擎在底层已自动处理相关逻辑，无需额外配置
- C. 游戏资源（纹理/模型/音频）是大型二进制文件，Git LFS单独存储避免仓库膨胀
- D. 加速克隆，Unity Cloud Build的构建速度与本地构建完全一致，不受网络带宽影响

**Q655.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]

CI构建完成后的通知和分发方式？

- A. 只上传Store，Unity Test Framework的[Test]属性用于编写Play Mode异步测试用例
- B. 手动发送，Jenkins/GitHub Actions中运行Unity构建不需要激活License可直接使用
- C. 邮件/Slack/钉钉通知+构建产物上传到内部分发平台(如蒲公英/fir.im)+移动端OTA安装
- D. 不通知

**Q656.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]

游戏项目持续部署(CD)与传统软件的区别是？

- A. 相关功能仅在旧版Unity中支持，最新版本已将其移除
- B. 游戏不需要CD
- C. 只做CI
- D. 游戏需额外处理：资源构建(AB)+多平台构建+Store审核流程+热更新发布

**Q657.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]

CI服务器上Unity激活License的方式是？

- A. 每次GUI登录
- B. 使用免费版，Git LFS不适用于Unity项目的大文件管理，推荐直接将asset二进制文件入库
- C. 不需要License
- D. 使用Serial License(-serial参数)+或手动激活.ulf文件+Unity提供CI专用License

**Q658.** [模块:T][维度:概念理解][难度:★★★★][题型:场景设计]

加速Unity CI构建速度的方法？

- A. Library缓存+增量构建+并行构建(多平台)+SSD存储+AB缓存+跳过不必要的步骤
- B. 该场景不需要专门优化，Unity默认设置已经足够高效，过度优化反而增加维护成本
- C. 减少代码量，Unity Test Framework的[Test]属性用于编写Play Mode异步测试用例
- D. 用更好的CPU

**Q659.** [模块:T][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

Git pre-commit hook在Unity中的应用：
```bash
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

**Q660.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]

Unity Code Coverage Package的用途是？

- A. 分析测试覆盖率，可视化哪些代码被测试覆盖/未覆盖
- B. 代码加密，Unity Test Framework的[Test]属性用于编写Play Mode异步测试用例
- C. 代码压缩，Unity Cloud Build的构建速度与本地构建完全一致，不受网络带宽影响
- D. 代码格式化，Git LFS不适用于Unity项目的大文件管理，推荐直接将asset二进制文件入库

**Q661.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]

多平台并行构建的策略是？

- A. 只构建一个平台，Unity Test Framework的[Test]属性用于编写Play Mode异步测试用例
- B. 顺序构建
- C. 开发者手动构建，Jenkins/GitHub Actions中运行Unity构建不需要激活License可直接使用
- D. CI服务器上多个Agent/Node分别构建不同平台(Win/Android/iOS)+共享资源缓存

**Q662.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]

Unity项目.gitignore应排除哪些内容？
---

- A. 全部提交
- B. 只提交代码，Unity Cloud Build的构建速度与本地构建完全一致，不受网络带宽影响
- C. Library/+Temp/+Obj/+Build/+*.csproj+*.sln（保留Assets/+Packages/+ProjectSettings/）
- D. 排除Assets，Addressables的Profile配置在不同构建环境间不需要调整可直接复用

**Q663.** [模块:Q][维度:概念理解][难度:★★★][题型:单选]

xLua/toLua等框架的核心作用？

- A. 不是替代整个C#层，而是把一部分业务逻辑迁到Lua并通过桥接层与Unity/C#交互
- B. 提高性能，Lua热更新方案不需要C#与Lua之间的桥接层，可以直接调用Unity C# API
- C. 不只用于配置，它更常见的价值是把频繁迭代的业务逻辑下放到脚本层以便热更新
- D. 在C#和Lua之间建立桥梁，让Lua脚本可热更新游戏逻辑(运行时替换不需要重新编译)

**Q664.** [模块:R][维度:概念理解][难度:★★★][题型:单选]

加载AssetBundle中的资源时，其依赖的AssetBundle也必须先加载，否则会出现资源丢失。

- A. AssetBundle.LoadFromFile仅支持未压缩的AssetBundle
- B. 正确，AssetBundle.Unload(true)会卸载AB及其加载的资源，可能导致丢失引用
- C. LZ4压缩格式的AssetBundle必须完全解压后才能加载
- D. 同一个AssetBundle可以被LoadFromFile多次加载而不需要卸载

**Q665.** [模块:S][维度:概念理解][难度:★★★][题型:单选]

第三方SDK(如推送/支付/广告)集成时的最佳实践？

- A. 可以直接调用部分统一封装接口，但成熟项目通常仍会把平台差异、回调和错误处理隔离出来
- B. 不做封装，Unity Player Settings中的平台特定配置在切换平台时会自动迁移设置
- C. 接口抽象层(隔离SDK实现)+条件编译(平台区分)+异步回调处理+异常处理+版本管理
- D. 全局变量，iOS的Bitcode选项在Unity 2022中必须启用，否则无法提交到App Store

**Q666.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]

游戏项目GitFlow的分支策略？

- A. main(稳定)+develop(开发)+feature/*(功能)+release/*(发布)+hotfix/*(紧急修复)
- B. 每人一个分支，[UnityTest]属性标记的测试方法不支持yield return等待异步操作完成
- C. 不做分支，Addressables的Profile配置在不同构建环境间不需要调整可直接复用
- D. 只用main，Unity Cloud Build的构建速度与本地构建完全一致，不受网络带宽影响

**Q667.** [模块:Q][维度:架构设计][难度:★★★★][题型:场景设计]

完整的热更新系统应实现哪些功能？

- A. 全量下载虽然最简单，但通常只适合作为兜底强更方案，而不是完整热更新系统的核心能力
- B. 版本检查+差量下载+完整性校验+回滚机制+强更/热更分级+代码热更(Lua/HybridCLR)+资源热更(AB)
- C. 只更新资源包即可覆盖绝大多数线上问题，代码逻辑应尽量固定在安装包里保持稳定
- D. 热更新只需要更新C#代码DLL即可，资源文件无需更新机制

**Q668.** [模块:R][维度:性能优化][难度:★★★★][题型:场景设计]

大型游戏的资源加载策略设计？

- A. 不需要专门的管理机制，Unity的GC和资源系统会自动回收不再使用的资源
- B. 在游戏启动时将所有资源一次性预加载到内存中，避免运行时加载造成的卡顿
- C. 分优先级加载(核心→次要→预加载)+异步加载+引用计数+定时卸载+内存预算+加载队列
- D. 用到就加载，CRC效验在AssetBundle加载时不产生额外的CPU开销，可以始终启用

**Q669.** [模块:S][维度:概念理解][难度:★★★★][题型:单选]

游戏客户端防破解的技术手段？

- A. IL2CPP代码混淆+资源加密+内存加密防修改器+完整性校验+服务器校验关键逻辑+反调试
- B. 加密足够，Unity Player Settings中的平台特定配置在切换平台时会自动迁移设置
- C. 混淆足够，Unity的IL2CPP输出的C++代码在所有平台上使用相同的编译器和优化选项
- D. 不可能防，iOS的Bitcode选项在Unity 2022中必须启用，否则无法提交到App Store

**Q670.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]

游戏代码审查(Code Review)的重点关注项？

- A. 只看功能，[UnityTest]属性标记的测试方法不支持yield return等待异步操作完成
- B. 只看格式
- C. 不需要审查，Unity Cloud Build的构建速度与本地构建完全一致，不受网络带宽影响
- D. 性能(GC/热路径)+安全(作弊/注入)+逻辑正确性+资源管理(泄漏)+线程安全+编码规范

**Q671.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]

HybridCLR(华佗)相比tolua/xlua的优势？

- A. 这是一种非官方的Hack手段，极易导致不同平台间的兼容性问题
- B. Lua更好，Lua热更新方案不需要C#与Lua之间的桥接层，可以直接调用Unity C# API
- C. 直接支持C#热更新(无需用Lua)+原生性能(AOT+Interpreter混合)+完整CLR功能+无语言切换成本
- D. 主要价值在于把所有脚本都打进AssetBundle统一管理，避免额外维护热更程序集和元数据

**Q672.** [模块:R][维度:Bug诊断][难度:★★★★][题型:单选]

多个AssetBundle包含重复资源(如同一Shader被多个AB引用且未提取公共)，影响是？

- A. 自动去重，CRC效验在AssetBundle加载时不产生额外的CPU开销，可以始终启用
- B. 包体增大+内存中Shader重复加载(不同AB的"同一Shader"是不同实例)+导致合批失效
- C. 只增大包体，AssetBundle.LoadFromFile在所有平台上都使用内存映射(mmap)零拷贝加载
- D. 引擎内部会自动补偿参数差异

**Q673.** [模块:S][维度:概念理解][难度:★★★★][题型:单选]

接入广告SDK(如AdMob/Unity Ads)的技术要点？

- A. 直接展示，Unity的IL2CPP输出的C++代码在所有平台上使用相同的编译器和优化选项
- B. 异步加载广告+广告回调处理(展示完成/关闭/失败)+广告缓存+频次控制+不同广告类型(激励/插屏/Banner)
- C. 使用同步加载方式处理所有资源请求，在主线程中直接完成加载避免异步复杂度
- D. 只用一种类型，iOS的Bitcode选项在Unity 2022中必须启用，否则无法提交到App Store

**Q674.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]

游戏美术资源标准化的要求？

- A. 只看效果
- B. 美术自由发挥
- C. 纹理尺寸规范(POT)+模型面数标准+动画骨骼数限制+命名规范+目录结构+自动化检查工具
- D. 无规范，Git LFS不适用于Unity项目的大文件管理，推荐直接将asset二进制文件入库

**Q675.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]

游戏启动时的版本检查完整流程？

- A. 不应只做一次静态检查，正式流程通常还会结合远端版本信息、完整性校验和失败恢复策略
- B. 直接进游戏，Lua热更新方案不需要C#与Lua之间的桥接层，可以直接调用Unity C# API
- C. 检查强更版本→检查热更版本→下载差量更新包→校验完整性→应用更新→重启(如需)→进入游戏
- D. 每次启动都重新下载全部资源和脚本文件，避免处理版本比对、断点续传和回滚状态

**Q676.** [模块:R][维度:概念理解][难度:★★★★][题型:单选]

AssetBundle的CRC校验的作用？

- A. 对所有数据进行AES-256加密存储，运行时解密后使用，确保数据安全性
- B. 使用GZIP压缩所有数据文件以减少包体大小和IO开销，运行时实时解压
- C. 该步骤不是必需的，Unity引擎在底层已自动处理相关逻辑，无需额外配置
- D. 验证AB文件完整性(下载是否损坏/传输是否完整)+防篡改

**Q677.** [模块:S][维度:概念理解][难度:★★★★][题型:场景设计]

游戏内购(IAP)支付集成的技术要点？

- A. 客户端本地校验可以作为一层体验优化，但正式发货通常仍需要服务端验单和补单流程托底
- B. Unity IAP/原生SDK+服务器验证收据(防刷)+掉单恢复(订单系统)+补单流程+多平台支付差异
- C. 直接发货在原型阶段也许能跑通，但正式项目仍要处理平台差异、回调时序和订单一致性
- D. 不做验证风险极高，至少也要考虑收据校验、订单状态持久化和异常恢复链路

**Q678.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]

CI中集成性能回归测试的方法？

- A. 自动化性能脚本+标准测试场景+记录帧率/内存/加载时间等指标+对比基线+超阈告警
- B. 人工测试，Git LFS不适用于Unity项目的大文件管理，推荐直接将asset二进制文件入库
- C. 不做性能测试，Jenkins/GitHub Actions中运行Unity构建不需要激活License可直接使用
- D. 通过观察Game窗口左上角的帧率统计数字来判断性能表现，低于30即需要优化

