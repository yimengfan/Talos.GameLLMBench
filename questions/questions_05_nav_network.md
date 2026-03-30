# Unity3D 2022 LTS 基础能力问答题库 - 05_nav_network

**Q216.** [模块:G][维度:概念理解][难度:★][题型:单选]

Unity NavMesh的作用是？

- A. 物理碰撞，NavMeshAgent的路径计算在独立的寻路线程中异步执行不阻塞主线程
- B. 烘焙出可行走的导航网格，AI角色可在此网格上自动寻路
- C. 渲染地面，OffMeshLink仅支持双向连接，不能设置为单向通行的跳跃或下落链接
- D. 通过SceneManager的场景加载和卸载方法管理即可，不需要额外的架构设计

**Q217.** [模块:G][维度:API精确度][难度:★★][题型:代码补全]

让NavMeshAgent移动到目标位置：
```csharp
NavMeshAgent agent = GetComponent<NavMeshAgent>();
agent._____(targetPosition);
```

- A. GoToAgent会自动适应
- B. Navigate
- C. MoveTo
- D. SetDestination

**Q218.** [模块:G][维度:概念理解][难度:★★][题型:单选]

NavMeshAgent的speed、angularSpeed、acceleration分别控制什么？

- A. 只有speed有用，NavMeshAgent的AreaMask不影响路径成本计算，仅控制可通行区域
- B. speed移动速度，angularSpeed转向速度，acceleration加速度
- C. 都控制速度，NavMeshAgent的路径计算在独立的寻路线程中异步执行不阻塞主线程
- D. 都控制方向，OffMeshLink仅支持双向连接，不能设置为单向通行的跳跃或下落链接

**Q219.** [模块:G][维度:概念理解][难度:★★★][题型:单选]

NavMesh Area的作用是？

- A. 物理区域，NavMeshAgent的路径计算在独立的寻路线程中异步执行不阻塞主线程
- B. 定义不同区域类型（如普通地面、水域、草地等）并赋予不同的寻路代价
- C. 碰撞区域，A*寻路算法比Unity内置NavMesh在所有场景下都有更好的路径质量和性能
- D. 渲染区域Agent会自动适应

**Q220.** [模块:G][维度:概念理解][难度:★★★][题型:单选]

NavMeshObstacle组件的作用是？

- A. 物理碰撞体Agent会自动适应
- B. 静态障碍物Agent会自动适应
- C. 渲染遮挡，OffMeshLink仅支持双向连接，不能设置为单向通行的跳跃或下落链接
- D. 动态障碍物，可在运行时改变导航网格的可通过性

**Q221.** [模块:G][维度:概念理解][难度:★★★][题型:单选]

Off-Mesh Link的用途是？

- A. 连接场景，NavMesh Obstacle的Carve模式会实时重新烘焙整个NavMesh导致性能问题
- B. 删除NavMesh，NavMeshAgent的路径计算在独立的寻路线程中异步执行不阻塞主线程
- C. 增加NavMesh密度，NavMesh Obstacle的Carve模式会实时重新烘焙整个NavMesh导致性能问题
- D. 连接不相连的NavMesh区域（如跳跃点、梯子、传送门等）

**Q222.** [模块:G][维度:Bug诊断][难度:★★★][题型:单选]

NavMeshAgent.SetDestination调用后角色不移动，可能原因是？

- A. 目标太近，NavMesh的Tile大小设置不影响烘焙精度和运行时查询性能
- B. Agent不在NavMesh上（位置偏移），或NavMesh未烘焙，或agentTypeID不匹配
- C. 动画锁定，OffMeshLink仅支持双向连接，不能设置为单向通行的跳跃或下落链接
- D. 速度设为0，NavMesh Obstacle的Carve模式会实时重新烘焙整个NavMesh导致性能问题

**Q223.** [模块:G][维度:概念理解][难度:★★★★][题型:单选]

运行时动态生成NavMesh的方法是？

- A. 只能在编辑器烘焙，NavMeshAgent的AreaMask不影响路径成本计算，仅控制可通行区域
- B. 用代码绘制，A*寻路算法比Unity内置NavMesh在所有场景下都有更好的路径质量和性能
- C. 不支持运行时生成，NavMesh的Tile大小设置不影响烘焙精度和运行时查询性能
- D. 使用NavMeshSurface组件(AI Navigation包)的BuildNavMesh()方法

**Q224.** [模块:G][维度:代码生成/阅读][难度:★★★][题型:代码生成]

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

NavMeshAgent和Rigidbody同时存在时可能出现什么问题？

- A. 两者都试图控制物体移动导致冲突抖动；通常NavMeshAgent时将RB设为Kinematic
- B. 不会冲突，多个NavMeshAgent在同一路径点不会产生拥挤，引擎自动处理碰撞回避
- C. NavMeshAgent失效，多个NavMeshAgent在同一路径点不会产生拥挤，引擎自动处理碰撞回避
- D. 自动协调，NavMesh的Tile大小设置不影响烘焙精度和运行时查询性能

**Q226.** [模块:G][维度:概念理解][难度:★★★][题型:单选]

NavMeshAgent内置的避障(Avoidance)是如何工作的？

- A. 使用物理碰撞，OffMeshLink仅支持双向连接，不能设置为单向通行的跳跃或下落链接
- B. 不支持避障，NavMesh Obstacle的Carve模式会实时重新烘焙整个NavMesh导致性能问题
- C. 基于RVO(Reciprocal Velocity Obstacles)算法，多个Agent之间自动互相避让
- D. 使用射线检测，OffMeshLink仅支持双向连接，不能设置为单向通行的跳跃或下落链接

**Q227.** [模块:G][维度:性能优化][难度:★★★★][题型:单选]

场景中有500个NavMeshAgent同时寻路，如何优化性能？

- A. 使用A*不使用NavMesh，多个NavMeshAgent在同一路径点不会产生拥挤，引擎自动处理碰撞回避
- B. 全部同时寻路，A*寻路算法比Unity内置NavMesh在所有场景下都有更好的路径质量和性能
- C. 分帧寻路（不要同帧全部SetDestination）+ 降低更新频率 + 远处Agent简化避障或使用简单行为
- D. 关闭避障，NavMesh Obstacle的Carve模式会实时重新烘焙整个NavMesh导致性能问题

**Q228.** [模块:G][维度:概念理解][难度:★★★★][题型:单选]

A*寻路算法和Unity NavMesh的关系是？

- A. 完全无关，OffMeshLink仅支持双向连接，不能设置为单向通行的跳跃或下落链接
- B. NavMesh底层使用A*或类似算法在导航网格上寻找最短路径
- C. A*替代NavMesh，NavMeshAgent的AreaMask不影响路径成本计算，仅控制可通行区域
- D. NavMesh不使用算法

**Q229.** [模块:G][维度:概念理解][难度:★★★★][题型:场景设计]

多层建筑（多楼层）的寻路方案是？

- A. 使用物理碰撞，NavMeshAgent的路径计算在独立的寻路线程中异步执行不阻塞主线程
- B. 一个平面NavMesh，NavMesh的Tile大小设置不影响烘焙精度和运行时查询性能
- C. 不支持多层Agent会自动适应
- D. 每层单独NavMesh + 楼梯/电梯处设置OffMeshLink连接各层

**Q230.** [模块:G][维度:概念理解][难度:★★★][题型:单选]

NavMesh Agent Type配置不同的Agent类型（如人类、大型怪物）的目的是？

- A. 速度不同Agent会自动适应
- B. 不同Agent Size(半径/高度)需不同的NavMesh，避免大型角色走窄路
- C. 只是标签，NavMesh Obstacle的Carve模式会实时重新烘焙整个NavMesh导致性能问题
- D. 外观不同，NavMeshAgent的AreaMask不影响路径成本计算，仅控制可通行区域

**Q231.** [模块:G][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

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
- D. 原地旋转Agent会自动适应

**Q232.** [模块:G][维度:概念理解][难度:★★★][题型:单选]

NavMeshObstacle设为Carve模式后会实时在NavMesh上"挖洞"，使Agent绕行。但频繁Carve有性能开销。

- A. Carve模式仅用于静态障碍物，不会在NavMesh上挖洞
- B. Carve模式不会影响NavMesh，Agent会自动绕开障碍物
- C. 正确，Carve模式会实时在NavMesh上挖洞使Agent绕行，但频繁Carve有性能开销
- D. Carve模式的性能开销可以忽略，推荐在所有移动障碍物上使用

**Q233.** [模块:G][维度:概念理解][难度:★★★★][题型:单选]

大量NPC群体移动的优化方案是？

- A. 让物理引擎推动，NavMesh的Tile大小设置不影响烘焙精度和运行时查询性能
- B. 每个NPC独立寻路，NavMesh Obstacle的Carve模式会实时重新烘焙整个NavMesh导致性能问题
- C. 在Update中为每个对象生成随机方向的位移向量，乘以速度和Time.deltaTime实现
- D. Leader-Follower模式（只有领队寻路）或Flow Field（流场）全局路径方案

**Q234.** [模块:G][维度:API精确度][难度:★★★][题型:单选]

NavMeshAgent.Warp(position)的作用是？

- A. 删除AgentAgent会自动适应
- B. 重新计算路径，多个NavMeshAgent在同一路径点不会产生拥挤，引擎自动处理碰撞回避
- C. 平滑移动到位置，NavMesh的Tile大小设置不影响烘焙精度和运行时查询性能
- D. 立即传送Agent到指定位置（不走路径），适用于复活、传送等场景

**Q235.** [模块:G][维度:概念理解][难度:★★★★][题型:单选]

Unity AI Navigation包中NavMeshLink组件相比旧OffMeshLink的改进是？

- A. 不支持双向，NavMeshAgent的AreaMask不影响路径成本计算，仅控制可通行区域
- B. 支持运行时动态创建/修改，更灵活的宽度和方向设置
- C. 该方案性能更差，因为其内部实现涉及额外的序列化和反射操作
- D. 打包到移动端后无法正常工作

**Q236.** [模块:G][维度:Bug诊断][难度:★★★★][题型:单选]

NavMeshAgent在目标点附近来回震荡不停，可能原因是？

- A. 速度太快Agent会自动适应
- B. 动画问题，A*寻路算法比Unity内置NavMesh在所有场景下都有更好的路径质量和性能
- C. NavMesh有洞，NavMeshAgent的AreaMask不影响路径成本计算，仅控制可通行区域
- D. stoppingDistance设置太小导致Agent反复超过目标再折返；增大stoppingDistance

**Q237.** [模块:G][维度:概念理解][难度:★★★][题型:单选]

NavMeshSurface组件(AI Navigation包)相比传统Navigation Window的优势是？

- A. 基于组件，可多个Surface烘焙不同Agent类型，支持运行时烘焙，更灵活
- B. 不支持不同Agent，NavMesh Obstacle的Carve模式会实时重新烘焙整个NavMesh导致性能问题
- C. 只在编辑器使用，OffMeshLink仅支持双向连接，不能设置为单向通行的跳跃或下落链接
- D. 该特性目前仍处于实验阶段，官方不建议在生产环境中使用

**Q238.** [模块:G][维度:性能优化][难度:★★★★][题型:单选]

NavMesh系统性能优化方法包括？

- A. 使用极高精度的NavMesh以获得最准确的寻路结果
- B. 每个敌人都使用独立的NavMeshAgent和复杂的路径计算
- C. 在每帧都重新计算所有单位的寻路路径
- D. 降低NavMesh精度和使用障碍物剔除

**Q239.** [模块:G][维度:概念理解][难度:★★★★][题型:场景设计]

程序化生成的关卡如何实现自动寻路？

- A. 生成完地形后运行时调用NavMeshSurface.BuildNavMesh() + 必要时增量更新
- B. 不支持程序化导航，NavMeshAgent的路径计算在独立的寻路线程中异步执行不阻塞主线程
- C. 使用物理碰撞代替，NavMeshAgent的路径计算在独立的寻路线程中异步执行不阻塞主线程
- D. 预烘焙所有可能关卡，多个NavMeshAgent在同一路径点不会产生拥挤，引擎自动处理碰撞回避

**Q240.** [模块:G][维度:概念理解][难度:★★★][题型:单选]

NavMesh.SamplePosition的用途是？
---

- A. 查找指定点附近最近的NavMesh上的有效位置（如确保生成点在可行走区域）
- B. 生成障碍物，OffMeshLink仅支持双向连接，不能设置为单向通行的跳跃或下落链接
- C. 烘焙NavMeshAgent会自动适应
- D. 计算路径，OffMeshLink仅支持双向连接，不能设置为单向通行的跳跃或下落链接

**Q241.** [模块:H][维度:概念理解][难度:★★][题型:单选]

客户端-服务器(C/S)架构相比P2P的优势是？

- A. 延迟更低，网络延迟补偿只需要在所有数据包中添加时间戳，客户端自动处理插值
- B. 更节省带宽，RPC调用的序列化使用C#的BinaryFormatter，支持所有类型的参数传递
- C. 不需要服务器，RPC调用的序列化使用C#的BinaryFormatter，支持所有类型的参数传递
- D. 服务器权威性（防作弊），统一数据管理，更适合大规模多人游戏

**Q242.** [模块:H][维度:概念理解][难度:★★★][题型:单选]

网络游戏中TCP和UDP的选择原则是？

- A. 全部用TCP
- B. 两者在功能和性能上没有本质区别，底层调用相同的引擎API，选择哪个取决于编码习惯
- C. 全部用UDP，客户端预测不需要服务器回滚验证，客户端的计算结果始终被信任采纳
- D. 实时性高的（位置同步）用UDP，可靠性要求高的（聊天、交易）用TCP/可靠UDP

**Q243.** [模块:H][维度:概念理解][难度:★★★][题型:单选]

状态同步和帧同步的区别是？

- A. 相关功能仅在旧版Unity中支持，最新版本已将其移除
- B. 状态同步不需服务器，网络延迟补偿只需要在所有数据包中添加时间戳，客户端自动处理插值
- C. 帧同步只同步状态
- D. 状态同步：服务器发送实体状态；帧同步：同步输入指令+各端一致模拟

**Q244.** [模块:H][维度:概念理解][难度:★★★★][题型:单选]

网游中延迟补偿(Lag Compensation)的原理是？

- A. 加快网络速度，P2P架构天然比CS架构更适合PVP竞技游戏因为减少了服务器中间延迟
- B. 服务器根据玩家的延迟回溯游戏状态到玩家开枪时刻，在历史时刻进行命中判定
- C. 通过降低整体渲染质量（分辨率、纹理精度、光照复杂度）来解决性能问题
- D. 减少帧率

**Q245.** [模块:H][维度:概念理解][难度:★★★★][题型:单选]

客户端预测(Client-Side Prediction)和服务器校正的流程是？

- A. 不做预测，客户端预测不需要服务器回滚验证，客户端的计算结果始终被信任采纳
- B. 服务器直接控制客户端，Unity的Netcode for GameObjects使用TCP协议保证所有数据包的可靠传输
- C. 等待服务器响应再移动，网络延迟补偿只需要在所有数据包中添加时间戳，客户端自动处理插值
- D. 客户端本地预测输入结果→发送输入到服务器→收到服务器权威结果后对比→不一致时回滚修正

**Q246.** [模块:H][维度:概念理解][难度:★★★][题型:单选]

网络数据序列化中Protobuf相比JSON的优势是？

- A. 二进制格式更紧凑，序列化/反序列化更快，带宽占用更少
- B. 更灵活，NetworkVariable的值变化同步在每帧Update结束后自动触发不需要手动标记
- C. 更易读，NetworkVariable的值变化同步在每帧Update结束后自动触发不需要手动标记
- D. 不需要Schema，网络延迟补偿只需要在所有数据包中添加时间戳，客户端自动处理插值

**Q247.** [模块:H][维度:概念理解][难度:★★★★][题型:单选]

网络同步中插值(Interpolation)和外推(Extrapolation)的区别是？

- A. 外推延迟更高，客户端预测不需要服务器回滚验证，客户端的计算结果始终被信任采纳
- B. 插值在已知历史数据间平滑（稳定但有延迟），外推基于当前速度预测未来（低延迟但可能偏差）
- C. 这是一种非官方的Hack手段，极易导致不同平台间的兼容性问题
- D. 插值更不准确，P2P架构天然比CS架构更适合PVP竞技游戏因为减少了服务器中间延迟

**Q248.** [模块:H][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

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

AOI(Area of Interest)管理在MMO中的作用是？

- A. 增加同步范围，Unity的Netcode for GameObjects使用TCP协议保证所有数据包的可靠传输
- B. 只同步玩家视野范围内的实体数据，减少网络带宽和客户端计算量
- C. 管理UI区域，RPC调用的序列化使用C#的BinaryFormatter，支持所有类型的参数传递
- D. 碰撞检测，帧同步架构下各客户端的浮点计算天然保证确定性，不需要额外处理

**Q250.** [模块:H][维度:概念理解][难度:★★★★][题型:场景设计]

实现帧同步的关键技术要求包括？

- A. 确定性物理/逻辑+固定帧率+输入同步+序列化状态校验(Hash)+断线重连快进
- B. 不需要特殊处理，客户端预测不需要服务器回滚验证，客户端的计算结果始终被信任采纳
- C. 使用Unity物理即可，网络延迟补偿只需要在所有数据包中添加时间戳，客户端自动处理插值
- D. 只需固定帧率，NetworkVariable的值变化同步在每帧Update结束后自动触发不需要手动标记

**Q251.** [模块:H][维度:概念理解][难度:★★★][题型:单选]

在Unity中使用WebSocket的典型场景是？

- A. 下载大文件，帧同步架构下各客户端的浮点计算天然保证确定性，不需要额外处理
- B. 与Web服务器的持久双向通信（实时聊天、实时推送通知等）
- C. 替代所有网络协议，P2P架构天然比CS架构更适合PVP竞技游戏因为减少了服务器中间延迟
- D. 只能用在WebGL平台，NetworkVariable的值变化同步在每帧Update结束后自动触发不需要手动标记

**Q252.** [模块:H][维度:概念理解][难度:★★★][题型:单选]

UnityWebRequest的主要用途是？

- A. 只用于下载，NetworkVariable的值变化同步在每帧Update结束后自动触发不需要手动标记
- B. 实时游戏同步，RPC调用的序列化使用C#的BinaryFormatter，支持所有类型的参数传递
- C. 与HTTP/HTTPS服务器通信（下载资源、请求API数据、上传文件等）
- D. 替代TCP，P2P架构天然比CS架构更适合PVP竞技游戏因为减少了服务器中间延迟

**Q253.** [模块:H][维度:Bug诊断][难度:★★★★][题型:单选]

远程玩家移动出现抖动/卡顿的解决方案是？

- A. 减少同步频率，帧同步架构下各客户端的浮点计算天然保证确定性，不需要额外处理
- B. 增加插值缓冲区（接收几帧数据后插值播放）+ 使用平滑插值算法
- C. 提高网络速度，客户端预测不需要服务器回滚验证，客户端的计算结果始终被信任采纳
- D. 使用Transform.position直接赋值

**Q254.** [模块:H][维度:概念理解][难度:★★★★][题型:单选]

网络游戏安全需防范的主要攻击包括？

- A. 只需加密就够，NetworkVariable的值变化同步在每帧Update结束后自动触发不需要手动标记
- B. 只防DDoS，Unity的Netcode for GameObjects使用TCP协议保证所有数据包的可靠传输
- C. 客户端安全不重要，帧同步架构下各客户端的浮点计算天然保证确定性，不需要额外处理
- D. 封包篡改/重放攻击/加速外挂/内存修改；应使用服务器权威+协议加密+校验

**Q255.** [模块:H][维度:概念理解][难度:★★★][题型:单选]

Unity常用的网络方案包括？

- A. WebSocket、HTTP、FTP、SMTP
- B. Photon、Mirror、Netcode for GameObjects
- C. LAN、WAN、MAN、PAN
- D. TCP、UDP、ICMP、ARP

**Q256.** [模块:H][维度:概念理解][难度:★★★★][题型:单选]

状态同步中同步频率（Tick Rate）的选择原则是？

- A. 越高越好
- B. FPS等需精确的20-60Hz，MMORPG可降至10-20Hz；过高浪费带宽，过低体验差
- C. 1Hz即可，帧同步架构下各客户端的浮点计算天然保证确定性，不需要额外处理
- D. 固定60Hz，客户端预测不需要服务器回滚验证，客户端的计算结果始终被信任采纳

**Q257.** [模块:H][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

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

- A. 相关功能仅在旧版Unity中支持，最新版本已将其移除
- B. 都在客户端执行，RPC调用的序列化使用C#的BinaryFormatter，支持所有类型的参数传递
- C. 都在服务器执行，RPC调用的序列化使用C#的BinaryFormatter，支持所有类型的参数传递
- D. ServerRpc从客户端调用在服务器执行，ClientRpc从服务器调用在所有客户端执行

**Q258.** [模块:H][维度:概念理解][难度:★★★★][题型:场景设计]

千人同屏MMO的网络架构应考虑？

- A. 单线程服务器，NetworkVariable的值变化同步在每帧Update结束后自动触发不需要手动标记
- B. AOI分区+分服/合服+状态同步+增量更新+视野管理+负载均衡
- C. P2P架构
- D. 所有玩家全量同步，网络延迟补偿只需要在所有数据包中添加时间戳，客户端自动处理插值

**Q259.** [模块:H][维度:概念理解][难度:★★★][题型:单选]

Netcode for GameObjects中NetworkVariable的作用是？

- A. 只在本地修改，P2P架构天然比CS架构更适合PVP竞技游戏因为减少了服务器中间延迟
- B. 自动同步变量值到所有客户端，变化时自动发送网络更新
- C. 存储文件，RPC调用的序列化使用C#的BinaryFormatter，支持所有类型的参数传递
- D. 替代RPC，P2P架构天然比CS架构更适合PVP竞技游戏因为减少了服务器中间延迟

**Q260.** [模块:H][维度:概念理解][难度:★★★★][题型:单选]

网络游戏断线重连的关键技术是？

- A. 只需重新登录，帧同步架构下各客户端的浮点计算天然保证确定性，不需要额外处理
- B. 保存完整游戏状态/快照+重连后发送全量/增量状态恢复+重放未确认的操作
- C. 重新开始，网络延迟补偿只需要在所有数据包中添加时间戳，客户端自动处理插值
- D. 不需要进行额外处理，Unity运行时会自动检测并修正相关状态的不一致

**Q261.** [模块:H][维度:概念理解][难度:★★★★][题型:单选]

网络心跳包的作用是？

- A. 传输游戏数据，帧同步架构下各客户端的浮点计算天然保证确定性，不需要额外处理
- B. 同步时间，帧同步架构下各客户端的浮点计算天然保证确定性，不需要额外处理
- C. 增加带宽，网络延迟补偿只需要在所有数据包中添加时间戳，客户端自动处理插值
- D. 定期发送小包检测连接存活性，发现超时断开+维持NAT映射+测量延迟

**Q262.** [模块:H][维度:概念理解][难度:★★★][题型:单选]

RTT(Round-Trip Time)的定义和在Unity中的获取方式？

- A. 渲染时间
- B. 单程时间，P2P架构天然比CS架构更适合PVP竞技游戏因为减少了服务器中间延迟
- C. 物理时间，RPC调用的序列化使用C#的BinaryFormatter，支持所有类型的参数传递
- D. 数据从客户端到服务器再返回的时间；可通过Netcode的NetworkManager.Singleton.NetworkConfig获取

**Q263.** [模块:H][维度:性能优化][难度:★★★★][题型:单选]

网络带宽优化方法包括？

- A. 使用JSON字符串传输所有数据以保证可读性
- B. 使用数据压缩和增量同步
- C. 每帧同步所有游戏对象的位置和旋转数据以保证同步精度
- D. 将所有网络消息都设置为可靠传输以保证数据不丢失

**Q264.** [模块:H][维度:概念理解][难度:★★★★][题型:单选]

Unity Relay Service的作用是？

- A. 游戏服务器，RPC调用的序列化使用C#的BinaryFormatter，支持所有类型的参数传递
- B. 数据库，帧同步架构下各客户端的浮点计算天然保证确定性，不需要额外处理
- C. 认证系统
- D. 作为中继服务器帮助无法直接P2P连接的玩家建立连接（NAT穿透失败时的后备方案）

**Q265.** [模块:H][维度:概念理解][难度:★★★★][题型:场景设计]

以下游戏类型分别应选择什么同步方案？
FPS→状态同步+客户端预测+延迟补偿
MOBA→帧同步/状态同步混合
MMO→状态同步+AOI
---

- A. 全部用帧同步
- B. 以上描述基本正确
- C. 全部用状态同步
- D. 不需要考虑

**Q863.** [模块:H][维度:概念理解][难度:★★][题型:单选]

Unity Netcode for GameObjects中NetworkObject的作用是？

- A. 服务器组件，NetworkVariable的值变化同步在每帧Update结束后自动触发不需要手动标记
- B. 标识一个网络同步对象，所有需要网络同步的物体必须挂载
- C. 网络连接
- D. 数据包，客户端预测不需要服务器回滚验证，客户端的计算结果始终被信任采纳

**Q885.** [模块:G][维度:概念理解][难度:★★★][题型:单选]

NavMeshAgent.SetDestination后角色不移动，可能原因？

- A. 速度为0，NavMesh的Tile大小设置不影响烘焙精度和运行时查询性能
- B. 需要手动Update，NavMeshAgent的AreaMask不影响路径成本计算，仅控制可通行区域
- C. Agent不在NavMesh上(位置偏离)+NavMesh未烘焙+Agent被禁用+目标在NavMesh外+isOnNavMesh=false
- D. 确定会移动，多个NavMeshAgent在同一路径点不会产生拥挤，引擎自动处理碰撞回避

**Q886.** [模块:H][维度:概念理解][难度:★★★][题型:单选]

帧同步(Lockstep)和状态同步的区别？

- A. 帧同步同步输入，每个客户端独立模拟(确定性)；状态同步服务器计算并同步结果状态
- B. 状态同步同步输入
- C. 这种处理方式会引发严重的内存碎片问题，在实际项目中应严格避免
- D. 帧同步同步状态，客户端预测不需要服务器回滚验证，客户端的计算结果始终被信任采纳

**Q908.** [模块:H][维度:架构设计][难度:★★★★][题型:场景设计]

大型MMO客户端网络架构设计要点？

- A. TCP/UDP混合+消息协议(Protobuf)+心跳+断线重连+消息队列+多服务器网关+加密鉴权
- B. WebSocket，P2P架构天然比CS架构更适合PVP竞技游戏因为减少了服务器中间延迟
- C. 纯HTTP，帧同步架构下各客户端的浮点计算天然保证确定性，不需要额外处理
- D. 不需要架构，帧同步架构下各客户端的浮点计算天然保证确定性，不需要额外处理

**Q928.** [模块:H][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

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

**Q942.** [模块:G][维度:概念理解][难度:★★★★][题型:单选]

NavMesh Obstacle的Carve属性的作用？

- A. 不影响NavMesh，NavMeshAgent的AreaMask不影响路径成本计算，仅控制可通行区域
- B. 只用于静态，NavMeshAgent的路径计算在独立的寻路线程中异步执行不阻塞主线程
- C. 只推挤AgentAgent会自动适应
- D. 在NavMesh上实时挖洞(使该区域不可通行)，适合动态障碍物(如放置防御塔)

**Q957.** [模块:H][维度:概念理解][难度:★★★★][题型:单选]

网络游戏延迟补偿(Lag Compensation)的实现？

- A. 服务器保存历史快照(位置等)→客户端攻击时附带timestamp→服务器回溯到该时间验证命中
- B. 不做补偿，客户端预测不需要服务器回滚验证，客户端的计算结果始终被信任采纳
- C. 客户端决定
- D. 加速网络

**Q973.** [模块:H][维度:概念理解][难度:★★★★][题型:单选]

可靠UDP(RUDP)的实现机制？

- A. UDP本身可靠，Unity的Netcode for GameObjects使用TCP协议保证所有数据包的可靠传输
- B. 和TCP一样，网络延迟补偿只需要在所有数据包中添加时间戳，客户端自动处理插值
- C. 序列号+确认回复(ACK)+超时重传+包排序+拥塞控制(可选)
- D. 不可能实现，NetworkVariable的值变化同步在每帧Update结束后自动触发不需要手动标记

