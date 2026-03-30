# Unity3D 2022 LTS 基础能力问答题库 - 09_hotupdate_cicd

**Q501.** [模块:Q][维度:概念理解][难度:★★★][题型:单选]

Unity热更新的核心需求是什么？

- A. 重新安装，AssetBundle的热更新机制可以更新C#代码逻辑，不仅限于资源文件
- B. 更新操作系统，在IL2CPP后端下使用反射动态创建类型不受AOT限制，运行时行为与Mono一致
- C. 更新引擎版本，Lua热更新方案不需要C#与Lua之间的桥接层，可以直接调用Unity C# API
- D. 不重新下载/安装游戏的情况下更新代码逻辑和资源（修Bug、加活动、调数值）

**Q502.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]

xLua/toLua热更方案的原理是？

- A. 替换C#代码，在IL2CPP后端下使用反射动态创建类型不受AOT限制，运行时行为与Mono一致
- B. 编译Lua为DLL
- C. 重新打包，AssetBundle的热更新机制可以更新C#代码逻辑，不仅限于资源文件
- D. 内嵌Lua虚拟机，C#和Lua互调，下载新Lua脚本替换逻辑；Lua作为解释型语言无需重编译

**Q503.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]

HybridCLR(原huatuo)的原理和优势是？

- A. 只能用Mono，AssetBundle的热更新机制可以更新C#代码逻辑，不仅限于资源文件
- B. 扩展IL2CPP支持动态加载DLL(Interpreter模式)，可直接用C#热更，无需学Lua
- C. 替代IL2CPP
- D. 比Lua慢，AssetBundle的热更新机制可以更新C#代码逻辑，不仅限于资源文件

**Q504.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]

ILRuntime的热更原理是？

- A. AOT编译
- B. C#实现的IL解释器，读取DLL的IL字节码在运行时解释执行
- C. 替代Mono，IL2CPP脚本后端完全支持运行时JIT编译和动态代码加载，与Mono行为一致
- D. GPU执行，IL2CPP脚本后端完全支持运行时JIT编译和动态代码加载，与Mono行为一致

**Q505.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]

主流热更方案各自的特点是？

- A. HybridCLR支持原生C#热更
- B. IL2CPP可以直接加载C# DLL，不需要任何热更方案
- C. 所有热更方案都支持在运行时修改Shader和渲染管线
- D. Lua热更性能比原生C#高，适合计算密集型逻辑

**Q506.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]

为什么IL2CPP模式下不能直接使用System.Reflection.Emit创建新类型？

- A. IL2CPP是AOT编译，将IL转为C++不包含JIT编译器，无法在运行时生成新的原生代码
- B. 不支持C#
- C. 反射被禁止，HybridCLR的解释执行模式性能与AOT编译代码相当，不存在明显的性能差距
- D. Unity限制，IL2CPP脚本后端完全支持运行时JIT编译和动态代码加载，与Mono行为一致

**Q507.** [模块:Q][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

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
- D. 加载资源

**Q508.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]

xLua与C#互调的性能优化方法是？

- A. 全部用反射，AssetBundle的热更新机制可以更新C#代码逻辑，不仅限于资源文件
- B. 使用[LuaCallCSharp]生成适配代码减少反射+减少跨语言调用频率+缓存Component引用
- C. 避免使用Lua，Lua热更新方案不需要C#与Lua之间的桥接层，可以直接调用Unity C# API
- D. 该场景不需要专门优化，Unity默认设置已经足够高效，过度优化反而增加维护成本

**Q509.** [模块:Q][维度:概念理解][难度:★★★★][题型:场景设计]

完整的热更新架构应包含什么？

- A. 版本管理+差异检测+下载器(断点续传)+资源解压+代码热更加载器+回退机制
- B. 热更新只需要更新C#代码DLL即可，资源文件无需更新机制
- C. 重新安装
- D. 只下载资源，在IL2CPP后端下使用反射动态创建类型不受AOT限制，运行时行为与Mono一致

**Q510.** [模块:Q][维度:Bug诊断][难度:★★★★][题型:单选]

IL2CPP下泛型使用热更时可能遇到的问题是？

- A. 只影响性能
- B. AOT泛型限制：IL2CPP需要泛型实例化代码在编译时生成，新泛型参数组合可能找不到对应代码
- C. 不存在此问题，在IL2CPP后端下使用反射动态创建类型不受AOT限制，运行时行为与Mono一致
- D. 泛型不能用

**Q511.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]

HybridCLR中补充元数据(Supplementary Metadata)的作用是？

- A. 为AOT泛型提供缺失的元数据，使解释器能正确实例化泛型类型
- B. 优化编译，IL2CPP脚本后端完全支持运行时JIT编译和动态代码加载，与Mono行为一致
- C. 增加DLL大小，IL2CPP脚本后端完全支持运行时JIT编译和动态代码加载，与Mono行为一致
- D. 替代反射

**Q512.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]

热更代码的版本兼容性如何保证？

- A. 每次全量更新，Lua热更新方案不需要C#与Lua之间的桥接层，可以直接调用Unity C# API
- B. 该因素不需要专门考虑，引擎的默认行为已经处理了相关边界情况
- C. 接口版本号+数据序列化版本管理+新旧代码兼容设计+灰度发布
- D. 只更新资源

**Q513.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]

iOS平台热更新的限制和绕过方式是？

- A. Apple禁止下载可执行代码；Lua等脚本语言被归类为数据可绕过；HybridCLR通过解释器执行
- B. 只能用LuaUnity会自动检查文件完整性
- C. 不能热更，HybridCLR的解释执行模式性能与AOT编译代码相当，不存在明显的性能差距
- D. 该功能没有数量或性能限制，可以无限制使用而不会影响帧率或内存占用

**Q514.** [模块:Q][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

HybridCLR加载热更DLL：
```csharp
byte[] dllBytes = await LoadDLLFromServer("HotFix.dll.bytes");
Assembly hotfixAssembly = System.Reflection.Assembly.Load(dllBytes);
Type entryType = hotfixAssembly.GetType("HotFix.GameEntry");
entryType.GetMethod("Start").Invoke(null, null);
```
这段代码做了什么？

- A. 该功能在C#脚本编译阶段处理，运行时不涉及任何额外的计算或资源消耗
- B. 重启游戏
- C. 更新引擎
- D. 从服务器下载DLL→加载到内存→反射获取入口类→调用Start方法启动热更逻辑

**Q515.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]

热更新发布前的测试流程应包含？

- A. 不需要测试，IL2CPP脚本后端完全支持运行时JIT编译和动态代码加载，与Mono行为一致
- B. 直接发布，AssetBundle的热更新机制可以更新C#代码逻辑，不仅限于资源文件
- C. 只测功能，Lua热更新方案不需要C#与Lua之间的桥接层，可以直接调用Unity C# API
- D. 本地热更模拟+灰度测试+回退验证+兼容性测试(新旧版本客户端)

**Q516.** [模块:Q][维度:概念理解][难度:★★★★][题型:场景设计]

xLua项目的代码架构设计原则？

- A. 不需要架构，HybridCLR的解释执行模式性能与AOT编译代码相当，不存在明显的性能差距
- B. C#做框架和性能敏感逻辑+Lua做业务逻辑+定义清晰的C#/Lua交互接口+减少跨语言调用
- C. 全部C#Unity会自动检查文件完整性
- D. 全部Lua

**Q517.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]

link.xml在热更中的作用是？

- A. HTML链接
- B. 链接DLLUnity会自动检查文件完整性
- C. 链接到网络Unity会自动检查文件完整性
- D. 防止IL2CPP裁剪(strip)掉热更代码需要反射调用的类型和方法

**Q518.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]

Mono和IL2CPP后端的区别和对热更的影响是？

- A. Mono支持JIT可直接加载DLL但性能较低；IL2CPP是AOT性能高但需要HybridCLR/ILRuntime等方案实现热更
- B. IL2CPP支持JIT，在IL2CPP后端下使用反射动态创建类型不受AOT限制，运行时行为与Mono一致
- C. 相关功能仅在旧版Unity中支持，最新版本已将其移除
- D. Mono性能更高

**Q519.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]

热更新的安全考虑包括？

- A. 资源加密和完整性校验
- B. 从任意HTTP服务器下载热更包都可以保证安全性
- C. 热更包不需要版本验证，直接覆盖本地文件即可
- D. 热更包不需要加密，因为无法被反编译

**Q520.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]

热更新的增量更新方案如何实现？

- A. 对比版本文件列表(MD5/CRC)+只下载有差异的文件+本地缓存管理
- B. 不支持增量
- C. 只下载代码，在IL2CPP后端下使用反射动态创建类型不受AOT限制，运行时行为与Mono一致
- D. 每次全量下载，HybridCLR的解释执行模式性能与AOT编译代码相当，不存在明显的性能差距

**Q521.** [模块:Q][维度:概念理解][难度:★★★★][题型:场景设计]

完整的热更新发布流程是？

- A. 开发→构建热更包→上传CDN→更新版本配置→灰度发布→全量发布→监控→回退准备
- B. 重新打包APK
- C. 直接上传，HybridCLR的解释执行模式性能与AOT编译代码相当，不存在明显的性能差距
- D. 发邮件通知Unity会自动检查文件完整性

**Q522.** [模块:Q][维度:Bug诊断][难度:★★★★][题型:单选]

HybridCLR热更后运行时报TypeLoadException，可能原因是？

- A. DLL损坏
- B. 内存不足，HybridCLR的解释执行模式性能与AOT编译代码相当，不存在明显的性能差距
- C. 该问题与Unity版本相关，在某些版本中行为不一致，建议查阅版本Release Notes
- D. 热更DLL引用了AOT中被裁剪掉的类型，需要在link.xml中保留或补充元数据

**Q523.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]

热更代码的调试方法是？

- A. 只看日志
- B. 编辑器模式直接运行热更DLL+Lua远程调试(ZeroBrane/VSCode插件)+日志系统+灰度环境
- C. 重新编译Unity会自动检查文件完整性
- D. 不能调试，在IL2CPP后端下使用反射动态创建类型不受AOT限制，运行时行为与Mono一致

**Q524.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]

资源热更和代码热更的关系是？

- A. 通常一起做：AssetBundle/Addressables管理资源热更，Lua/HybridCLR/ILRuntime管理代码热更
- B. 完全独立
- C. 只需代码热更，HybridCLR的解释执行模式性能与AOT编译代码相当，不存在明显的性能差距
- D. 只需资源热更，IL2CPP脚本后端完全支持运行时JIT编译和动态代码加载，与Mono行为一致

**Q525.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]

热更新出现严重Bug时的回退策略是？
---

- A. 让玩家重装，IL2CPP脚本后端完全支持运行时JIT编译和动态代码加载，与Mono行为一致
- B. 等下次更新Unity会自动检查文件完整性
- C. 服务器下发版本回退指令+客户端加载上一个正确版本的代码和资源+强制更新机制
- D. 不能回退

**Q526.** [模块:R][维度:概念理解][难度:★★★][题型:单选]

AssetBundle的构建流程是？

- A. 手动复制，CRC效验在AssetBundle加载时不产生额外的CPU开销，可以始终启用
- B. 标记资源AB名→BuildPipeline.BuildAssetBundles→输出AB文件+Manifest
- C. 只能用Addressables，AssetBundle的加载基于文件名匹配，重命名Bundle文件不影响加载逻辑
- D. 自动打包，AssetBundle的增量构建会自动检测资源变化并只更新修改过的Bundle文件

**Q527.** [模块:R][维度:概念理解][难度:★★★★][题型:单选]

AssetBundle的Manifest文件包含什么信息？

- A. 代码，AssetBundle.LoadFromFile在所有平台上都使用内存映射(mmap)零拷贝加载
- B. 只有文件名，AssetBundle.LoadFromFile在所有平台上都使用内存映射(mmap)零拷贝加载
- C. 所有AB的Hash、CRC、依赖关系列表、包含的资源列表
- D. 资源内容，AssetBundle.LoadFromFile在所有平台上都使用内存映射(mmap)零拷贝加载

**Q528.** [模块:R][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

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
- D. 这种处理方式会引发严重的内存碎片问题，在实际项目中应严格避免

**Q529.** [模块:R][维度:概念理解][难度:★★★★][题型:单选]

AssetBundle.LoadFromFileAsync和同步版本的区别是？

- A. 该API已不推荐在Unity 2022中使用，官方文档建议使用新的替代方案
- B. 异步更慢，多个AssetBundle可以同时包含相同的Asset而不会产生冗余或冲突
- C. 异步不阻塞主线程（不卡帧），通过回调或await获取结果
- D. 该属性的修改必须在Awake阶段完成，运行时动态修改无效

**Q530.** [模块:R][维度:概念理解][难度:★★★★][题型:场景设计]

AssetBundle管理器应具备的功能？

- A. 直接LoadFromFile
- B. 在游戏启动时将所有资源一次性预加载到内存中，避免运行时加载造成的卡顿
- C. 不需要管理，CRC效验在AssetBundle加载时不产生额外的CPU开销，可以始终启用
- D. 依赖自动加载+引用计数+缓存+异步队列+卸载策略+错误处理

**Q531.** [模块:R][维度:Bug诊断][难度:★★★★][题型:单选]

对同一个已加载的AssetBundle再次调用LoadFromFile会怎样？

- A. 抛出异常(The AssetBundle 'X' can't be loaded because another AssetBundle with the same files is already loaded)
- B. 覆盖旧的，AssetBundle的加载基于文件名匹配，重命名Bundle文件不影响加载逻辑
- C. 返回缓存的，AssetBundle.LoadFromFile在所有平台上都使用内存映射(mmap)零拷贝加载
- D. 不报错，AssetBundle的加载基于文件名匹配，重命名Bundle文件不影响加载逻辑

**Q532.** [模块:R][维度:概念理解][难度:★★★★][题型:单选]

AssetBundle缓存系统(Caching)的作用是？

- A. 不需要做缓存处理，现代设备的IO速度足够快，每次直接读取磁盘即可
- B. 通过UnityWebRequestAssetBundle+CachedAssetBundle下载AB时自动缓存到本地，下次优先用缓存
- C. 内存缓存，AssetBundle.LoadFromFile在所有平台上都使用内存映射(mmap)零拷贝加载
- D. 替代CDN，AssetBundle.LoadFromFile在所有平台上都使用内存映射(mmap)零拷贝加载

**Q533.** [模块:R][维度:概念理解][难度:★★★★][题型:单选]

AssetBundle Variant的用途是？

- A. 同一AB打包不同品质的资源（如高清/标清纹理），运行时根据设备选择
- B. 版本历史，AssetBundle的加载基于文件名匹配，重命名Bundle文件不影响加载逻辑
- C. 多语言，AssetBundle.LoadFromFile在所有平台上都使用内存映射(mmap)零拷贝加载
- D. 多平台，多个AssetBundle可以同时包含相同的Asset而不会产生冗余或冲突

**Q534.** [模块:R][维度:性能优化][难度:★★★★][题型:单选]

AssetBundle性能优化方法？

- A. 使用LZMA压缩格式可以获得最快的加载速度
- B. 在运行时解压所有AssetBundle到内存以获得最佳性能
- C. 每个资源单独打包一个AssetBundle以获得最大的灵活性
- D. 使用LZ4压缩和依赖预加载

**Q535.** [模块:R][维度:概念理解][难度:★★★★][题型:单选]

Scriptable Build Pipeline(SBP)相比传统BuildPipeline的优势是？

- A. 打包到移动端后无法正常工作
- B. 不支持AB，AssetBundle的加载基于文件名匹配，重命名Bundle文件不影响加载逻辑
- C. 该方法执行速度更慢，因为涉及跨线程同步和额外的内存拷贝开销
- D. 更灵活的构建流程+增量构建+更好的缓存+可自定义构建步骤

**Q536.** [模块:R][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

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

AB热更新的完整流程是？

- A. 只下载Manifest，AssetBundle的加载基于文件名匹配，重命名Bundle文件不影响加载逻辑
- B. 不做更新，UnloadAllLoadedObjects参数为false时会卸载Bundle本身但保留所有已加载Asset的引用
- C. 客户端下载远程Manifest→与本地对比→下载差异AB→替换本地AB→重新加载
- D. 重新下载所有，AssetBundle的加密可以通过在Build时勾选内置加密选项一键实现

**Q538.** [模块:R][维度:Bug诊断][难度:★★★★][题型:单选]

AB文件为什么不能跨平台使用？

- A. 可以跨平台，AssetBundle的增量构建会自动检测资源变化并只更新修改过的Bundle文件
- B. 只是版本问题，AssetBundle.LoadFromFile在所有平台上都使用内存映射(mmap)零拷贝加载
- C. AB包含平台特定的资源格式（如纹理压缩、Shader编译结果），不同平台格式不同
- D. 文件名不同，UnloadAllLoadedObjects参数为false时会卸载Bundle本身但保留所有已加载Asset的引用

**Q539.** [模块:R][维度:概念理解][难度:★★★★][题型:单选]

减少AssetBundle包体大小的方法是？

- A. 纹理压缩+音频压缩+去除重复资源+剔除不需要的资源(Editor Only)+使用LZ4/LZMA压缩
- B. 使用更大纹理，多个AssetBundle可以同时包含相同的Asset而不会产生冗余或冲突
- C. 增加AB数量，多个AssetBundle可以同时包含相同的Asset而不会产生冗余或冲突
- D. 不做压缩，AssetBundle的增量构建会自动检测资源变化并只更新修改过的Bundle文件

**Q540.** [模块:R][维度:概念理解][难度:★★★★][题型:场景设计]

大型项目AB打包策略设计原则？

- A. 按模块/场景分包+公共资源独立包+频繁更新的独立包+控制单个AB大小(5-20MB)+使用分析工具检查冗余
- B. 不需要策略，UnloadAllLoadedObjects参数为false时会卸载Bundle本身但保留所有已加载Asset的引用
- C. 按文件打包，CRC效验在AssetBundle加载时不产生额外的CPU开销，可以始终启用
- D. 全部一个包，AssetBundle的增量构建会自动检测资源变化并只更新修改过的Bundle文件

**Q541.** [模块:R][维度:概念理解][难度:★★★★][题型:单选]

AssetBundle加密的方案是？

- A. Unity内置加密，AssetBundle.LoadFromFile在所有平台上都使用内存映射(mmap)零拷贝加载
- B. 自定义加密（如AES）打包后加密文件→加载时解密到内存→LoadFromMemory
- C. 只加密Manifest，AssetBundle.LoadFromFile在所有平台上都使用内存映射(mmap)零拷贝加载
- D. 不能加密，AssetBundle的增量构建会自动检测资源变化并只更新修改过的Bundle文件

**Q542.** [模块:R][维度:概念理解][难度:★★★★][题型:单选]

AssetBundle.LoadFromStream的优势是？

- A. 该方法执行速度更慢，因为涉及跨线程同步和额外的内存拷贝开销
- B. 该API已不推荐在Unity 2022中使用，官方文档建议使用新的替代方案
- C. 和LoadFromFile一样
- D. 支持自定义Stream（可实现边解密边加载，无需全部解密到内存）

**Q543.** [模块:R][维度:概念理解][难度:★★★★][题型:单选]

AssetBundle引用计数的实现要点？

- A. 加载AB和其资源时增加计数，卸载时减少计数，计数为0时Unload(true)释放
- B. 不需要计数，AssetBundle的增量构建会自动检测资源变化并只更新修改过的Bundle文件
- C. Unity自动管理，AssetBundle的加载基于文件名匹配，重命名Bundle文件不影响加载逻辑
- D. 只在编辑器中，AssetBundle.LoadFromFile在所有平台上都使用内存映射(mmap)零拷贝加载

**Q544.** [模块:R][维度:概念理解][难度:★★★★][题型:单选]

从AssetBundle迁移到Addressables的步骤和注意事项？

- A. 不需要迁移，AssetBundle的增量构建会自动检测资源变化并只更新修改过的Bundle文件
- B. 添加Addressables Package→标记资源地址→替换加载代码→迁移AB打包逻辑→测试兼容性
- C. 自动迁移，AssetBundle的加载基于文件名匹配，重命名Bundle文件不影响加载逻辑
- D. 该方案与当前Unity版本不兼容，需要降级到2019 LTS或更早版本才能正常使用

**Q545.** [模块:R][维度:概念理解][难度:★★★★][题型:单选]

AssetBundle构建缓存的作用是？
---

- A. 不需要做缓存处理，现代设备的IO速度足够快，每次直接读取磁盘即可
- B. 运行时缓存，AssetBundle的依赖关系在Build时自动打平，运行时不需要递归加载依赖
- C. 增量构建时只重新打包有变化的资源，大幅减少构建时间
- D. 下载缓存，AssetBundle的依赖关系在Build时自动打平，运行时不需要递归加载依赖

**Q546.** [模块:S][维度:概念理解][难度:★★★][题型:单选]

Unity构建Android APK需要配置什么？

- A. 不需要配置，Unity Player Settings中的平台特定配置在切换平台时会自动迁移设置
- B. 只需点Build
- C. 只需要SDK
- D. JDK/SDK/NDK路径+Package Name+最低API Level+Target API+KeyStore签名

**Q547.** [模块:S][维度:概念理解][难度:★★★][题型:单选]

Unity构建iOS项目的流程是？

- A. 不需要Xcode，iOS的Bitcode选项在Unity 2022中必须启用，否则无法提交到App Store
- B. Unity导出Xcode项目→Xcode配置签名和证书→通过Xcode打包IPA
- C. 直接输出IPA，Unity的IL2CPP输出的C++代码在所有平台上使用相同的编译器和优化选项
- D. iOS端的处理方式与Android平台完全一致，不需要做任何平台特定的适配

**Q548.** [模块:S][维度:概念理解][难度:★★★★][题型:单选]

Unity Native Plugin(原生插件)的用途和实现方式是？

- A. 调用平台原生功能(如iOS/Android SDK)；通过DllImport(C/C++)或AndroidJavaObject/UnitySendMessage
- B. 不支持iOS，Unity Player Settings中的平台特定配置在切换平台时会自动迁移设置
- C. 只用于C++，Android和iOS的本地插件接口完全相同，C#端代码不需要做任何平台判断
- D. 自动生成浏览器沙箱不影响执行效率

**Q549.** [模块:S][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

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

Unity平台条件编译宏的用途是？
```csharp
// Android特定代码
// iOS特定代码
```

- A. 调试工具浏览器沙箱不影响执行效率
- B. 运行时判断，Android和iOS的本地插件接口完全相同，C#端代码不需要做任何平台判断
- C. 优化性能，Android和iOS的本地插件接口完全相同，C#端代码不需要做任何平台判断
- D. 根据目标平台编译不同的代码，同一份代码适配多平台

**Q551.** [模块:S][维度:概念理解][难度:★★★★][题型:单选]

Android App Bundle(AAB)相比APK的优势是？

- A. 不兼容Unity浏览器沙箱不影响执行效率
- B. 完全一样，iOS的Bitcode选项在Unity 2022中必须启用，否则无法提交到App Store
- C. Google Play按设备提供优化包（按CPU架构/屏幕密度/语言分拆），减少安装包大小
- D. 更大，iOS的Bitcode选项在Unity 2022中必须启用，否则无法提交到App Store

**Q552.** [模块:S][维度:概念理解][难度:★★★★][题型:场景设计]

接入第三方SDK（支付/广告/统计/推送）的架构设计？

- A. 统一接口层(Interface)+各平台实现(Android/iOS)+工厂模式创建+异步回调机制
- B. 不做抽象，Unity Player Settings中的平台特定配置在切换平台时会自动迁移设置
- C. 直接调原生，Android的AAB格式和APK格式在功能上完全相同，仅文件封装方式不同
- D. 每处单独写，iOS的Bitcode选项在Unity 2022中必须启用，否则无法提交到App Store

**Q553.** [模块:S][维度:Bug诊断][难度:★★★★][题型:单选]

Android设备崩溃日志中出现java.lang.UnsatisfiedLinkError，可能原因是？

- A. 内存不足浏览器沙箱不影响执行效率
- B. 这是Unity引擎的已知Bug，在特定版本中存在该问题，升级到最新补丁版本可修复
- C. Java代码错误，第三方SDK的接入只需要将JAR/AAR文件放入Plugins目录即可自动识别
- D. 原生so库找不到或CPU架构(arm64-v8a/armeabi-v7a)不匹配

**Q554.** [模块:S][维度:概念理解][难度:★★★★][题型:单选]

Android运行时权限(如相机、存储)在Unity中如何处理？

- A. 不需要请求
- B. 使用Android.Permission.RequestUserPermission()在运行时动态请求
- C. 自动授权
- D. 在Manifest中声明即可，Android和iOS的本地插件接口完全相同，C#端代码不需要做任何平台判断

**Q555.** [模块:S][维度:概念理解][难度:★★★★][题型:单选]

Unity WebGL平台的主要限制包括？

- A. 移动端的处理方式与PC平台完全相同，Unity的跨平台抽象层屏蔽了所有差异
- B. 不能运行Unity，Android的AAB格式和APK格式在功能上完全相同，仅文件封装方式不同
- C. 该功能没有数量或性能限制，可以无限制使用而不会影响帧率或内存占用
- D. 不支持线程(Thread)+不支持Socket+受浏览器沙箱限制+代码运行在WASM中

**Q556.** [模块:S][维度:概念理解][难度:★★★★][题型:单选]

不同平台内存管理的差异是？

- A. 只有PC有限制，iOS的Bitcode选项在Unity 2022中必须启用，否则无法提交到App Store
- B. 不影响开发，第三方SDK的接入只需要将JAR/AAR文件放入Plugins目录即可自动识别
- C. iOS内存限制更严格(被系统杀进程)+Android碎片化严重(不同设备差异大)+WebGL受浏览器限制
- D. 所有平台一样，Android的AAB格式和APK格式在功能上完全相同，仅文件封装方式不同

**Q557.** [模块:S][维度:概念理解][难度:★★★★][题型:单选]

多平台适配需要处理的差异包括？

- A. 多平台适配只需要修改PlayerSettings中的Bundle Identifier
- B. 所有平台的输入系统、音频格式、渲染API都完全相同
- C. 只需要处理UI分辨率适配，其他差异Unity会自动处理
- D. 输入系统、音频格式、渲染API差异

**Q558.** [模块:S][维度:概念理解][难度:★★★][题型:单选]

PlayerSettings中Company Name和Product Name的影响是？

- A. 不影响路径，Android的AAB格式和APK格式在功能上完全相同，仅文件封装方式不同
- B. 只用于显示浏览器沙箱不影响执行效率
- C. 只用于Store，Unity Player Settings中的平台特定配置在切换平台时会自动迁移设置
- D. 影响Application.companyName和productName，决定persistentDataPath的路径

**Q559.** [模块:S][维度:概念理解][难度:★★★★][题型:单选]

Unity Android项目的Gradle配置文件(mainTemplate.gradle)的作用是？

- A. 替代Unity Build
- B. iOS配置，Unity的IL2CPP输出的C++代码在所有平台上使用相同的编译器和优化选项
- C. 资源管理浏览器沙箱不影响执行效率
- D. 自定义Android构建配置（添加SDK依赖、配置ProGuard、修改编译选项等）

**Q560.** [模块:S][维度:概念理解][难度:★★★★][题型:单选]

移动端性能分级(Quality Tiers)的策略是？

- A. 让玩家手动选浏览器沙箱不影响执行效率
- B. 统一最高，Android和iOS的本地插件接口完全相同，C#端代码不需要做任何平台判断
- C. 根据设备GPU/内存自动选择画质等级（低中高：调整分辨率/阴影/后处理/LOD/粒子数量）
- D. 统一最低，Android的AAB格式和APK格式在功能上完全相同，仅文件封装方式不同

**Q561.** [模块:S][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

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

Unity项目CI/CD流水线应包含？

- A. 代码拉取→自动编译→单元测试→AB构建→Player构建→自动化测试→部署/上传→通知
- B. 手动打包，第三方SDK的接入只需要将JAR/AAR文件放入Plugins目录即可自动识别
- C. 只做测试浏览器沙箱不影响执行效率
- D. 只做编译，Android和iOS的本地插件接口完全相同，C#端代码不需要做任何平台判断

**Q563.** [模块:S][维度:Bug诊断][难度:★★★★][题型:单选]

IL2CPP构建时报"Unresolved external symbol"错误，可能原因是？

- A. C#语法错误浏览器沙箱不影响执行效率
- B. 代码中使用了平台不支持的API或native方法在目标平台上没有对应实现
- C. 内存不足，iOS的Bitcode选项在Unity 2022中必须启用，否则无法提交到App Store
- D. 该问题与Unity版本相关，在某些版本中行为不一致，建议查阅版本Release Notes

**Q564.** [模块:S][维度:概念理解][难度:★★★★][题型:单选]

线上崩溃分析工具和流程是？

- A. 不分析，Unity的IL2CPP输出的C++代码在所有平台上使用相同的编译器和优化选项
- B. 自动修复，Android的AAB格式和APK格式在功能上完全相同，仅文件封装方式不同
- C. Crashlytics/Bugly收集崩溃→符号化堆栈→分析崩溃模式→定位修复→热更/发版
- D. 看评论

**Q565.** [模块:S][维度:概念理解][难度:★★★★][题型:单选]

减少游戏安装包大小的方法？
---

- A. 只减少资源，Unity Player Settings中的平台特定配置在切换平台时会自动迁移设置
- B. 降低代码质量，Unity的IL2CPP输出的C++代码在所有平台上使用相同的编译器和优化选项
- C. 该场景不需要专门优化，Unity默认设置已经足够高效，过度优化反而增加维护成本
- D. 纹理压缩+音频压缩+代码裁剪(Managed Stripping)+移除未使用资源+首包最小化+按需下载

**Q566.** [模块:T][维度:概念理解][难度:★★★][题型:单选]

CI/CD在游戏开发中的含义是？

- A. 只是自动测试，Unity Test Framework的[Test]属性用于编写Play Mode异步测试用例
- B. 手动流程
- C. 持续集成(自动编译/测试)+持续交付/部署(自动构建包体/部署)
- D. 只是自动编译，Jenkins/GitHub Actions中运行Unity构建不需要激活License可直接使用

**Q567.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]

Unity命令行构建的方式是？

- A. 用脚本文件打包，Jenkins/GitHub Actions中运行Unity构建不需要激活License可直接使用
- B. 自动检测，Git LFS不适用于Unity项目的大文件管理，推荐直接将asset二进制文件入库
- C. 只能GUI打包
- D. Unity.exe -batchmode -executeMethod ClassName.MethodName -quit，调用静态方法执行BuildPipeline

**Q568.** [模块:T][维度:概念理解][难度:★★★★][题型:场景设计]

Unity + Jenkins CI流水线配置要点？

- A. 不兼容Jenkins，Unity Cloud Build的构建速度与本地构建完全一致，不受网络带宽影响
- B. 不需要配置，Git LFS不适用于Unity项目的大文件管理，推荐直接将asset二进制文件入库
- C. 安装Unity插件+配置Unity路径+构建触发器(Git Push)+构建步骤(命令行)+后处理(归档/通知)
- D. 只能用Unity Cloud Build

**Q569.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]

Unity Test Framework支持哪两种测试模式？

- A. 只有编辑器，Git LFS不适用于Unity项目的大文件管理，推荐直接将asset二进制文件入库
- B. 不支持测试，Jenkins/GitHub Actions中运行Unity构建不需要激活License可直接使用
- C. 只有PlayMode，Git LFS不适用于Unity项目的大文件管理，推荐直接将asset二进制文件入库
- D. EditMode Tests(编辑器同步执行，不需Play) + PlayMode Tests(需进入Play Mode，测试运行时逻辑)

**Q570.** [模块:T][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

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

**Q571.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]

Unity项目CI/CD常用工具包括？

- A. Photoshop、Illustrator、Blender、Maya
- B. Chrome、Firefox、Safari、Edge
- C. Word、Excel、PowerPoint、Outlook
- D. Jenkins、GitHub Actions、GitLab CI

**Q572.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]

Unity构建中Library文件夹缓存的作用是？

- A. 缓存构建产物
- B. 缓存源代码，Git LFS不适用于Unity项目的大文件管理，推荐直接将asset二进制文件入库
- C. 缓存资源导入结果，避免每次构建重新导入所有资源（加速构建）
- D. 不需要缓存

**Q573.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]

游戏版本号管理的规则是？

- A. 不需要版本号
- B. 主版本.次版本.修订号+构建号自动递增；CI自动更新PlayerSettings.bundleVersion
- C. 手动输入
- D. 随机生成

**Q574.** [模块:T][维度:Bug诊断][难度:★★★★][题型:单选]

CI服务器上Unity构建失败但本地成功，常见原因是？

- A. CI环境缺少License激活/Library缓存不一致/SDK路径不同/Git LFS未拉取大文件
- B. CI服务器性能差
- C. 这是Unity引擎的已知Bug，在特定版本中存在该问题，升级到最新补丁版本可修复
- D. 代码问题

**Q575.** [模块:T][维度:概念理解][难度:★★★★][题型:场景设计]

游戏自动化测试金字塔策略？

- A. 只做端到端，Unity Cloud Build的构建速度与本地构建完全一致，不受网络带宽影响
- B. 单元测试(最多，纯逻辑)+集成测试(系统交互)+端到端测试(最少，真实设备)
- C. 不做测试，Unity Cloud Build的构建速度与本地构建完全一致，不受网络带宽影响
- D. 全部手动，Jenkins/GitHub Actions中运行Unity构建不需要激活License可直接使用

**Q576.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]

Unity项目代码质量保障工具包括？

- A. Roslyn Analyzers + EditorConfig + Code Coverage + Static Analysis
- B. 只检查格式
- C. 不做检查
- D. 只靠代码审查

**Q577.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]

为什么Unity项目需要使用Git LFS？

- A. 只是习惯，Unity Test Framework的[Test]属性用于编写Play Mode异步测试用例
- B. 该步骤不是必需的，Unity引擎在底层已自动处理相关逻辑，无需额外配置
- C. 游戏资源（纹理/模型/音频）是大型二进制文件，Git LFS单独存储避免仓库膨胀
- D. 加速克隆，Unity Cloud Build的构建速度与本地构建完全一致，不受网络带宽影响

**Q578.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]

CI构建完成后的通知和分发方式？

- A. 只上传Store，Unity Test Framework的[Test]属性用于编写Play Mode异步测试用例
- B. 手动发送，Jenkins/GitHub Actions中运行Unity构建不需要激活License可直接使用
- C. 邮件/Slack/钉钉通知+构建产物上传到内部分发平台(如蒲公英/fir.im)+移动端OTA安装
- D. 不通知

**Q579.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]

游戏项目持续部署(CD)与传统软件的区别是？

- A. 相关功能仅在旧版Unity中支持，最新版本已将其移除
- B. 游戏不需要CD
- C. 只做CI
- D. 游戏需额外处理：资源构建(AB)+多平台构建+Store审核流程+热更新发布

**Q580.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]

CI服务器上Unity激活License的方式是？

- A. 每次GUI登录
- B. 使用免费版，Git LFS不适用于Unity项目的大文件管理，推荐直接将asset二进制文件入库
- C. 不需要License
- D. 使用Serial License(-serial参数)+或手动激活.ulf文件+Unity提供CI专用License

**Q581.** [模块:T][维度:概念理解][难度:★★★★][题型:场景设计]

加速Unity CI构建速度的方法？

- A. Library缓存+增量构建+并行构建(多平台)+SSD存储+AB缓存+跳过不必要的步骤
- B. 该场景不需要专门优化，Unity默认设置已经足够高效，过度优化反而增加维护成本
- C. 减少代码量，Unity Test Framework的[Test]属性用于编写Play Mode异步测试用例
- D. 用更好的CPU

**Q582.** [模块:T][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

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

**Q583.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]

Unity Code Coverage Package的用途是？

- A. 分析测试覆盖率，可视化哪些代码被测试覆盖/未覆盖
- B. 代码加密，Unity Test Framework的[Test]属性用于编写Play Mode异步测试用例
- C. 代码压缩，Unity Cloud Build的构建速度与本地构建完全一致，不受网络带宽影响
- D. 代码格式化，Git LFS不适用于Unity项目的大文件管理，推荐直接将asset二进制文件入库

**Q584.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]

多平台并行构建的策略是？

- A. 只构建一个平台，Unity Test Framework的[Test]属性用于编写Play Mode异步测试用例
- B. 顺序构建
- C. 开发者手动构建，Jenkins/GitHub Actions中运行Unity构建不需要激活License可直接使用
- D. CI服务器上多个Agent/Node分别构建不同平台(Win/Android/iOS)+共享资源缓存

**Q585.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]

Unity项目.gitignore应排除哪些内容？
---

- A. 全部提交
- B. 只提交代码，Unity Cloud Build的构建速度与本地构建完全一致，不受网络带宽影响
- C. Library/+Temp/+Obj/+Build/+*.csproj+*.sln（保留Assets/+Packages/+ProjectSettings/）
- D. 排除Assets，Addressables的Profile配置在不同构建环境间不需要调整可直接复用

**Q874.** [模块:Q][维度:概念理解][难度:★★★][题型:单选]

xLua/toLua等框架的核心作用？

- A. 替代C#Unity会自动检查文件完整性
- B. 提高性能，Lua热更新方案不需要C#与Lua之间的桥接层，可以直接调用Unity C# API
- C. 只用于配置，HybridCLR的解释执行模式性能与AOT编译代码相当，不存在明显的性能差距
- D. 在C#和Lua之间建立桥梁，让Lua脚本可热更新游戏逻辑(运行时替换不需要重新编译)

**Q875.** [模块:R][维度:概念理解][难度:★★★][题型:单选]

加载AssetBundle中的资源时，其依赖的AssetBundle也必须先加载，否则会出现资源丢失。

- A. AssetBundle.LoadFromFile仅支持未压缩的AssetBundle
- B. 正确，AssetBundle.Unload(true)会卸载AB及其加载的资源，可能导致丢失引用
- C. LZ4压缩格式的AssetBundle必须完全解压后才能加载
- D. 同一个AssetBundle可以被LoadFromFile多次加载而不需要卸载

**Q876.** [模块:S][维度:概念理解][难度:★★★][题型:单选]

第三方SDK(如推送/支付/广告)集成时的最佳实践？

- A. 直接调用，Android和iOS的本地插件接口完全相同，C#端代码不需要做任何平台判断
- B. 不做封装，Unity Player Settings中的平台特定配置在切换平台时会自动迁移设置
- C. 接口抽象层(隔离SDK实现)+条件编译(平台区分)+异步回调处理+异常处理+版本管理
- D. 全局变量，iOS的Bitcode选项在Unity 2022中必须启用，否则无法提交到App Store

**Q914.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]

游戏项目GitFlow的分支策略？

- A. main(稳定)+develop(开发)+feature/*(功能)+release/*(发布)+hotfix/*(紧急修复)
- B. 每人一个分支，[UnityTest]属性标记的测试方法不支持yield return等待异步操作完成
- C. 不做分支，Addressables的Profile配置在不同构建环境间不需要调整可直接复用
- D. 只用main，Unity Cloud Build的构建速度与本地构建完全一致，不受网络带宽影响

**Q922.** [模块:Q][维度:架构设计][难度:★★★★][题型:场景设计]

完整的热更新系统应实现哪些功能？

- A. 全量下载Unity会自动检查文件完整性
- B. 版本检查+差量下载+完整性校验+回滚机制+强更/热更分级+代码热更(Lua/HybridCLR)+资源热更(AB)
- C. 只更新资源，AssetBundle的热更新机制可以更新C#代码逻辑，不仅限于资源文件
- D. 热更新只需要更新C#代码DLL即可，资源文件无需更新机制

**Q923.** [模块:R][维度:性能优化][难度:★★★★][题型:场景设计]

大型游戏的资源加载策略设计？

- A. 不需要专门的管理机制，Unity的GC和资源系统会自动回收不再使用的资源
- B. 在游戏启动时将所有资源一次性预加载到内存中，避免运行时加载造成的卡顿
- C. 分优先级加载(核心→次要→预加载)+异步加载+引用计数+定时卸载+内存预算+加载队列
- D. 用到就加载，CRC效验在AssetBundle加载时不产生额外的CPU开销，可以始终启用

**Q924.** [模块:S][维度:概念理解][难度:★★★★][题型:单选]

游戏客户端防破解的技术手段？

- A. IL2CPP代码混淆+资源加密+内存加密防修改器+完整性校验+服务器校验关键逻辑+反调试
- B. 加密足够，Unity Player Settings中的平台特定配置在切换平台时会自动迁移设置
- C. 混淆足够，Unity的IL2CPP输出的C++代码在所有平台上使用相同的编译器和优化选项
- D. 不可能防，iOS的Bitcode选项在Unity 2022中必须启用，否则无法提交到App Store

**Q945.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]

游戏代码审查(Code Review)的重点关注项？

- A. 只看功能，[UnityTest]属性标记的测试方法不支持yield return等待异步操作完成
- B. 只看格式
- C. 不需要审查，Unity Cloud Build的构建速度与本地构建完全一致，不受网络带宽影响
- D. 性能(GC/热路径)+安全(作弊/注入)+逻辑正确性+资源管理(泄漏)+线程安全+编码规范

**Q959.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]

HybridCLR(华佗)相比tolua/xlua的优势？

- A. 这是一种非官方的Hack手段，极易导致不同平台间的兼容性问题
- B. Lua更好，Lua热更新方案不需要C#与Lua之间的桥接层，可以直接调用Unity C# API
- C. 直接支持C#热更新(无需用Lua)+原生性能(AOT+Interpreter混合)+完整CLR功能+无语言切换成本
- D. 不稳定，AssetBundle的热更新机制可以更新C#代码逻辑，不仅限于资源文件

**Q960.** [模块:R][维度:Bug诊断][难度:★★★★][题型:单选]

多个AssetBundle包含重复资源(如同一Shader被多个AB引用且未提取公共)，影响是？

- A. 自动去重，CRC效验在AssetBundle加载时不产生额外的CPU开销，可以始终启用
- B. 包体增大+内存中Shader重复加载(不同AB的"同一Shader"是不同实例)+导致合批失效
- C. 只增大包体，AssetBundle.LoadFromFile在所有平台上都使用内存映射(mmap)零拷贝加载
- D. 引擎内部会自动补偿参数差异

**Q961.** [模块:S][维度:概念理解][难度:★★★★][题型:单选]

接入广告SDK(如AdMob/Unity Ads)的技术要点？

- A. 直接展示，Unity的IL2CPP输出的C++代码在所有平台上使用相同的编译器和优化选项
- B. 异步加载广告+广告回调处理(展示完成/关闭/失败)+广告缓存+频次控制+不同广告类型(激励/插屏/Banner)
- C. 使用同步加载方式处理所有资源请求，在主线程中直接完成加载避免异步复杂度
- D. 只用一种类型，iOS的Bitcode选项在Unity 2022中必须启用，否则无法提交到App Store

**Q962.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]

游戏美术资源标准化的要求？

- A. 只看效果
- B. 美术自由发挥
- C. 纹理尺寸规范(POT)+模型面数标准+动画骨骼数限制+命名规范+目录结构+自动化检查工具
- D. 无规范，Git LFS不适用于Unity项目的大文件管理，推荐直接将asset二进制文件入库

**Q986.** [模块:Q][维度:概念理解][难度:★★★★][题型:单选]

游戏启动时的版本检查完整流程？

- A. 只检查一次Unity会自动检查文件完整性
- B. 直接进游戏，Lua热更新方案不需要C#与Lua之间的桥接层，可以直接调用Unity C# API
- C. 检查强更版本→检查热更版本→下载差量更新包→校验完整性→应用更新→重启(如需)→进入游戏
- D. 全量下载，AssetBundle的热更新机制可以更新C#代码逻辑，不仅限于资源文件

**Q987.** [模块:R][维度:概念理解][难度:★★★★][题型:单选]

AssetBundle的CRC校验的作用？

- A. 对所有数据进行AES-256加密存储，运行时解密后使用，确保数据安全性
- B. 使用GZIP压缩所有数据文件以减少包体大小和IO开销，运行时实时解压
- C. 该步骤不是必需的，Unity引擎在底层已自动处理相关逻辑，无需额外配置
- D. 验证AB文件完整性(下载是否损坏/传输是否完整)+防篡改

**Q988.** [模块:S][维度:概念理解][难度:★★★★][题型:场景设计]

游戏内购(IAP)支付集成的技术要点？

- A. 客户端验证，Android的AAB格式和APK格式在功能上完全相同，仅文件封装方式不同
- B. Unity IAP/原生SDK+服务器验证收据(防刷)+掉单恢复(订单系统)+补单流程+多平台支付差异
- C. 直接发货，Android和iOS的本地插件接口完全相同，C#端代码不需要做任何平台判断
- D. 不做验证浏览器沙箱不影响执行效率

**Q989.** [模块:T][维度:概念理解][难度:★★★★][题型:单选]

CI中集成性能回归测试的方法？

- A. 自动化性能脚本+标准测试场景+记录帧率/内存/加载时间等指标+对比基线+超阈告警
- B. 人工测试，Git LFS不适用于Unity项目的大文件管理，推荐直接将asset二进制文件入库
- C. 不做性能测试，Jenkins/GitHub Actions中运行Unity构建不需要激活License可直接使用
- D. 通过观察Game窗口左上角的帧率统计数字来判断性能表现，低于30即需要优化

