# Unity3D 2022 LTS 基础能力问答题库 - 08_math_input

**Q507.** [模块:N][维度:概念理解][难度:★★][题型:单选]

Unity旧版Input Manager和新版Input System Package的区别是？

- A. 旧版以项目设置中的轴和按键名称为中心，天然支持运行时重绑定和设备热插拔
- B. 打包到移动端后无法正常工作
- C. 旧版基于轮询(GetKey/GetAxis)写死在代码中；新版基于事件和Action映射，支持运行时重绑定
- D. 新版主要面向手柄和触摸设备，键盘鼠标输入仍必须通过旧版Input API单独读取

**Q508.** [模块:N][维度:API精确度][难度:★★][题型:代码补全]

检测用户按下空格键（旧版）：
```csharp
if(Input._____(KeyCode.Space)) { Jump(); }
```

- A. PressKey
- B. KeyDown
- C. GetKeyDown
- D. IsKeyDown

**Q509.** [模块:N][维度:概念理解][难度:★★★][题型:单选]

Input System中Input Action的概念是？

- A. 一个按键
- B. 一个只能绑定单一物理按键的输入槽位，不能跨键盘、手柄和触屏复用
- C. 抽象的操作（如Jump/Move/Fire），可绑定到多种输入设备，实现输入与逻辑的解耦
- D. 一个设备，新Input System不支持多设备同时输入，同一时间只能识别一个活动输入设备

**Q510.** [模块:N][维度:代码生成/阅读][难度:★★★][题型:代码补全]

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

**Q511.** [模块:N][维度:概念理解][难度:★★★][题型:单选]

Input Action Asset中Action Map的作用是？

- A. 定义输入设备的更新频率和轮询顺序，决定键鼠和手柄谁先响应
- B. 将Action按上下文分组（如Gameplay/UI/Vehicle），可以整组启用/禁用
- C. 按平台拆分底层输入后端，运行时不能在不同场景间切换
- D. 只是命名空间

**Q512.** [模块:N][维度:概念理解][难度:★★★][题型:单选]

Input System中Binding和Composite的区别是？

- A. Composite是单个按键的别名，Binding才负责把多个输入合成为一个值
- B. Binding是单个输入映射（如Space→Jump），Composite将多个输入组合成一个值（如WASD→2D Vector）
- C. Composite只支持键盘输入，无法用于手柄方向键或摇杆的组合值
- D. Binding一定直接产出最终值，Composite只用于编辑器里的可视化分组展示

**Q513.** [模块:N][维度:概念理解][难度:★★★★][题型:单选]

实现运行时按键重绑定(Rebinding)的步骤是？

- A. 只能直接修改 Input Actions 资产文件并重新导入工程，运行时无法交互式重绑定
- B. InputAction.PerformInteractiveRebinding()启动→等待用户按键→保存新Binding→序列化到JSON持久化
- C. 修改代码
- D. 重新生成C#包装类并热重载程序集后，新按键才会在运行中生效

**Q514.** [模块:N][维度:概念理解][难度:★★★][题型:单选]

移动端触摸输入的处理方式是？

- A. 只能用第三方
- B. 所有触摸都会被自动折算成一个鼠标左键事件，因此无需区分手指Id和触点阶段
- C. 新Input System只支持单点触控，多点触控通常需要接原生平台接口自己实现
- D. Input System的Touchscreen设备+EnhancedTouch API，或旧版Touch结构体

**Q515.** [模块:N][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

PlayerInput组件有哪些通知模式？
```csharp
// 通过SendMessages方式：
void OnMove(InputValue value) {
Vector2 moveInput = value.Get<Vector2>();
}
void OnJump(InputValue value) { /* 跳跃 */ }
```
其他模式包括？

- A. 只有C# Events一种，其他写法都只是旧版示例代码的封装形式
- B. 只有SendMessages和BroadcastMessages两种，UnityEvents和C# Events需要手写桥接
- C. 只有UnityEvents和C# Events两种，SendMessages在新系统中已经被废弃
- D. SendMessages、BroadcastMessages、UnityEvents、C# Events四种

**Q516.** [模块:N][维度:概念理解][难度:★★★][题型:单选]

Input System中Interaction（如Hold/Tap/SlowTap）的作用是？

- A. 把输入限制到某类设备上，只有匹配设备时Action才会进入performed
- B. 定义输入的交互行为模式（长按、点击、双击等），在满足条件时触发
- C. 为UI输入声明优先级，避免游戏输入和UI输入在同一帧同时触发
- D. 在运行时动态改写Binding路径，并立即覆盖原有的按键配置

**Q517.** [模块:N][维度:概念理解][难度:★★★★][题型:单选]

Input System中Processor（如Invert/Normalize/DeadZone）的作用是？

- A. 对输入值进行后处理变换（反转、归一化、死区过滤等）
- B. 管理Action Map
- C. 切换当前生效的Control Scheme，并决定由哪个设备接管后续输入
- D. 在Action触发前拦截输入事件，并改写其started/performed/canceled生命周期

**Q518.** [模块:N][维度:Bug诊断][难度:★★★][题型:单选]

使用新Input System后输入无响应，常见原因是？

- A. PlayerInput只能用于UI输入，游戏逻辑输入必须全部手写轮询才能生效
- B. 只要项目同时启用了旧版Input和新版Input，所有新系统输入都会默认失效
- C. InputAction只能在FixedUpdate中读取，在Update中读取一定得不到输入值
- D. 未在Player Settings中设置Active Input Handling为"Input System Package"或"Both"

**Q519.** [模块:N][维度:概念理解][难度:★★★★][题型:场景设计]

支持键鼠+手柄+触屏的统一输入方案应如何设计？

- A. 继续用旧版Input统一读取键鼠和手柄，触屏单独写一层适配即可保证维护成本最低
- B. 为每个设备写独立控制器脚本，通过平台宏在构建时裁剪不需要的实现
- C. 只保留一个Action Map，在运行时手动改Binding字符串比Control Scheme更稳定
- D. 使用Input System的Control Scheme + 每个Scheme定义不同设备Binding + 自动设备切换 + UI提示动态更新

**Q520.** [模块:N][维度:概念理解][难度:★★★][题型:单选]

旧版Input.GetAxis("Horizontal")返回什么？

- A. true或false
- B. -1到1之间的float值，有平滑过渡
- C. 0或1
- D. 未归一化的屏幕坐标增量，需要手动除以Time.deltaTime后才能作为轴值使用

**Q521.** [模块:N][维度:概念理解][难度:★★★★][题型:单选]

实现手柄震动(Haptic)的方式？

- A. 通过AudioMixer输出低频音效即可直接驱动手柄左右震动马达
- B. Input System的Gamepad.current.SetMotorSpeeds(low, high)控制左右马达
- C. 只要设备支持手柄输入，Unity会在按键触发时自动开启默认震动反馈，无需代码控制
- D. 必须通过原生平台SDK单独实现，Input System本身不提供任何通用手柄震动接口

**Q522.** [模块:N][维度:概念理解][难度:★★★★][题型:单选]

游戏中输入缓冲(Input Buffer)的作用是？

- A. 把所有输入延迟到当前动画播完后再统一执行，避免状态切换期间的误触
- B. 过滤高频重复按键，只保留最后一次按下的结果来减少输入噪声
- C. 在网络同步里对输入做插值平滑，以降低高延迟环境下的操作抖动
- D. 在短时间窗口内记录输入，即使当前不能执行也在窗口期内有效（如格斗游戏的连招输入）

**Q523.** [模块:N][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

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

- A. 把输入向量转换到局部坐标系，使摇杆方向始终跟随UI父节点旋转
- B. 根据`maxRadius`对输入方向做平滑插值，避免拖动时出现突变
- C. 限制向量长度不超过maxRadius（摇杆不超出底盘范围）
- D. 把任意非零向量都拉伸到半径边界，使摇杆始终保持最大输入强度

**Q524.** [模块:N][维度:概念理解][难度:★★★][题型:单选]

在FixedUpdate中检测Input.GetKeyDown可能丢失输入，因为FixedUpdate和Update调用频率不同。

- A. 正确，在FixedUpdate中检测Input.GetKeyDown可能丢失输入，因为调用频率不同
- B. Unity会自动处理输入缓冲，不会丢失任何输入
- C. FixedUpdate和Update的调用频率相同，不会丢失输入
- D. Input.GetKeyDown在FixedUpdate中更准确

**Q525.** [模块:N][维度:概念理解][难度:★★★★][题型:单选]

Input System的On-Screen Button/Stick的原理是？

- A. 替代所有输入
- B. 独立于Input System，新Input System不支持多设备同时输入，同一时间只能识别一个活动输入设备
- C. 只用于调试，新Input System不支持多设备同时输入，同一时间只能识别一个活动输入设备
- D. 将UI交互事件模拟为对应设备的输入（如触摸屏幕按钮模拟为键盘按键或手柄按钮）

**Q526.** [模块:N][维度:概念理解][难度:★★★★][题型:单选]

Input System使用的最佳实践包括？

- A. 使用Input Action和Input Action Map
- B. 在Update中每帧检测Input.GetKey以保证响应及时
- C. 将所有输入检测都放在FixedUpdate中以获得稳定的响应
- D. 使用旧的Input Manager和新Input System混合可以提高兼容性

**Q527.** [模块:N][维度:概念理解][难度:★★★][题型:单选]

识别滑动手势(Swipe)通常需要检测什么？

- A. 只检测起点，PlayerInput组件的Invoke Unity Events模式性能优于C# Generate Class方式
- B. 只要手指离开屏幕就可视为一次滑动，不需要判断方向、距离和持续时间
- C. 只检测时间
- D. 触摸起点和终点的距离、方向、时间差，满足阈值则判定为对应方向的滑动

**Q528.** [模块:N][维度:概念理解][难度:★★★★][题型:单选]

Input System Debugger(Window→Analysis→Input Debugger)可以查看什么？

- A. 主要看设备树和状态事件流，便于确认某个按键、摇杆或触摸输入是否真的被系统识别到
- B. 在多线程环境下直接调用该接口会导致主线程阻塞或程序崩溃
- C. 只看日志
- D. 当前连接的所有输入设备、每个设备的实时输入状态、Action触发历史

**Q529.** [模块:N][维度:性能优化][难度:★★★★][题型:单选]

Input System事件驱动相比旧版每帧轮询的性能优势是？

- A. 两者都要维护输入状态，但事件驱动更偏向按变化分发，轮询则需要业务层主动查询当前值
- B. 旧版每帧轮询更快，因为省掉了事件分发和回调注册带来的额外开销
- C. 该技术方案没有明显优势，在小型项目中反而增加不必要的架构复杂度
- D. 事件驱动只在输入变化时触发回调，减少无效的每帧检查

**Q530.** [模块:N][维度:概念理解][难度:★★★★][题型:场景设计]

本地多人游戏(Local Co-op)的输入处理方案是？

- A. 每个玩家分配独立的PlayerInput组件+不同的Control Scheme+设备自动分配
- B. 需要网络，InputAction的canceled回调只在长按操作释放时触发，短按不会触发该回调
- C. 如果设备数量很少会比较麻烦，但本地多人仍可通过设备配对和独立Action Map实现
- D. 也可以共用一套输入资源，但通常仍需要在运行时为不同玩家拆分设备和动作上下文

**Q531.** [模块:N][维度:概念理解][难度:★★★][题型:单选]

Unity中处理中文/日文等IME输入需要注意什么？

- A. 不支持中文，PlayerInput组件的Invoke Unity Events模式性能优于C# Generate Class方式
- B. Input Field组件自动处理IME，但自定义文本输入需要处理Input.compositionString
- C. 不一定非要第三方插件，但如果自定义输入框较复杂，通常仍要自己处理组合串、候选词和提交时机
- D. 所有IME输入最终都会自动转换成普通KeyDown事件，因此不需要处理组合中的候选字符串

**Q532.** [模块:N][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

Input System中InputAction.CallbackContext的phases是什么？
```csharp
moveAction.performed += ctx => { /* 输入执行中 */ };
moveAction.canceled += ctx => { /* 输入取消/释放 */ };
moveAction.started += ctx => { /* 输入开始 */ };
```
三个回调的触发时机区别？

- A. started、performed、canceled只是不同命名的同一个回调阶段，触发时机完全一致
- B. canceled只在设备断开时触发，普通按键松开和交互中断不会进入该阶段
- C. started=输入刚开始，performed=交互完成/值变化，canceled=输入停止/Interaction未完成
- D. 只有performed有用，PlayerInput组件的Invoke Unity Events模式性能优于C# Generate Class方式

**Q533.** [模块:N][维度:概念理解][难度:★★★★][题型:单选]

移动端陀螺仪和加速度计输入在Unity中如何获取？

- A. 只能通过各平台原生SDK桥接，Unity的输入层不暴露这些传感器数据
- B. Input.gyro(旧版)或Input System的GravitySensor/Gyroscope设备
- C. Unity 2022 LTS不支持该功能，需要等待后续版本更新或使用第三方插件替代
- D. 只能用第三方，PlayerInput组件的Invoke Unity Events模式性能优于C# Generate Class方式

**Q534.** [模块:N][维度:Bug诊断][难度:★★★★][题型:单选]

UI按钮点击时同时触发了游戏内的射击操作（输入穿透），解决方法是？

- A. 不能解决，新Input System不支持多设备同时输入，同一时间只能识别一个活动输入设备
- B. 把UI按钮移到单独场景中渲染，这样游戏输入系统就不会再收到同一帧点击
- C. 在点击UI期间临时禁用整个输入资源，再在下一帧全部重新启用
- D. 使用EventSystem.current.IsPointerOverGameObject()判断是否在UI上，是则不处理游戏输入

**Q535.** [模块:N][维度:概念理解][难度:★★★★][题型:单选]

Input System的架构分为哪几层？

- A. 只有设备层和Action层两层，中间不存在独立的状态抽象和玩家封装
- B. Action层当然最常用，但完整系统还会围绕设备状态、绑定解析和玩家输入上下文组织能力
- C. 没有明确分层，所有输入都会直接从设备对象同步推到业务代码
- D. 设备层(Device)→状态层(State)→Action层(Action)→用户层(PlayerInput)

**Q536.** [模块:N][维度:概念理解][难度:★★★★][题型:场景设计]

Input System实现输入录制和回放(用于回放系统/Bug复现)的方案？
---

- A. 录屏
- B. InputEventTrace记录所有输入事件→序列化到文件→回放时重放事件流
- C. 只记录最终角色位置和行为结果，回放时由AI推测原始输入即可
- D. Unity 2022 LTS不支持该功能，需要等待后续版本更新或使用第三方插件替代

**Q537.** [模块:O][维度:概念理解][难度:★★][题型:单选]

Vector3.forward在Unity中表示什么？

- A. (0, 0, -1)
- B. (0, 1, 0)
- C. (0, 0, 1)，即世界坐标系的Z轴正方向
- D. (1, 0, 0)

**Q538.** [模块:O][维度:概念理解][难度:★★★][题型:单选]

Vector3.Dot(a, b)的几何意义是？

- A. 两向量夹角
- B. |a|*|b|*cos(θ)，可判断两向量的方向关系（>0同侧、=0垂直、<0异侧）
- C. 两向量相加，Random.Range(0, 10)在int重载下返回0-10的整数（包含10）
- D. 两向量距离长度等于两向量长度之积

**Q539.** [模块:O][维度:概念理解][难度:★★★][题型:单选]

Vector3.Cross(a, b)的几何意义和应用是？

- A. 两向量距离TRS变换的顺序可以任意排列
- B. 结果是垂直于a和b的向量，大小为|a|*|b|*sin(θ)；用于求法线、判断左右方向
- C. 点积，Mathf.InverseLerp的返回值总是在0-1之间，超出范围自动Clamp
- D. 两向量角度始终返回最近的碰撞点

**Q540.** [模块:O][维度:API精确度][难度:★★][题型:代码补全]

在两点间线性插值移动：
```csharp
transform.position = Vector3._____(startPos, endPos, t);
```

- A. Lerp
- B. Smooth
- C. Move
- D. Blend

**Q541.** [模块:O][维度:概念理解][难度:★★★][题型:单选]

Quaternion相比欧拉角(Euler Angles)的优势是？

- A. 该技术方案没有明显优势，在小型项目中反而增加不必要的架构复杂度
- B. 无万向锁(Gimbal Lock)+可平滑插值(Slerp)+更少的存储(4个float)
- C. 更直观，Mathf.InverseLerp的返回值总是在0-1之间，超出范围自动Clamp
- D. 更好理解

**Q542.** [模块:O][维度:API精确度][难度:★★★][题型:代码补全]

让物体朝向目标：
```csharp
Vector3 dir = target.position - transform.position;
transform.rotation = Quaternion._____(dir);
```

- A. FromDirection
- B. LookRotation
- C. LookAt
- D. RotateTowards

**Q543.** [模块:O][维度:概念理解][难度:★★★★][题型:单选]

万向锁(Gimbal Lock)的问题是什么？

- A. 锁定物体，Quaternion欧拉角转换始终是无损的，任意欧拉角和Quaternion可以双向精确转换
- B. 渲染错误TRS变换的顺序可以任意排列
- C. 性能问题，Random.Range(0, 10)在int重载下返回0-10的整数（包含10）
- D. 当一个旋转轴旋转90度时，另两个轴重合导致失去一个自由度，无法正确表示某些旋转

**Q544.** [模块:O][维度:概念理解][难度:★★★][题型:单选]

Quaternion.Slerp和Quaternion.Lerp的区别是？

- A. 这是一种非官方的Hack手段，极易导致不同平台间的兼容性问题
- B. Lerp更精确TRS变换的顺序可以任意排列
- C. Slerp球面插值（恒速、弧线路径），Lerp线性插值（非恒速但性能更好、差异小时可替代）
- D. Slerp不能用于旋转始终返回最近的碰撞点

**Q545.** [模块:O][维度:代码生成/阅读][难度:★★★][题型:代码生成]

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
- B. 相关功能仅在旧版Unity中支持，最新版本已将其移除
- C. Slerp匀速，Random.Range(0, 10)在int重载下返回0-10的整数（包含10）
- D. RotateTowards按比例长度等于两向量长度之积

**Q546.** [模块:O][维度:概念理解][难度:★★★★][题型:单选]

4x4变换矩阵(Matrix4x4)包含哪些信息？

- A. 旋转(3x3) + 平移(最后一列) + 缩放(编码在旋转部分中)，可以组合多次变换
- B. 只有缩放，Mathf.InverseLerp的返回值总是在0-1之间，超出范围自动Clamp
- C. 只有旋转，Quaternion欧拉角转换始终是无损的，任意欧拉角和Quaternion可以双向精确转换
- D. 只有位置

**Q547.** [模块:O][维度:概念理解][难度:★★★][题型:单选]

Transform.TransformPoint和Transform.InverseTransformPoint的作用是？

- A. 旋转物体
- B. 移动物体，Quaternion欧拉角转换始终是无损的，任意欧拉角和Quaternion可以双向精确转换
- C. 两者都基于同一组变换关系，但一个做正向坐标变换，一个做逆向坐标变换，语义并不相同
- D. TransformPoint将本地坐标转世界坐标，InverseTransformPoint将世界坐标转本地坐标

**Q548.** [模块:O][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

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

- A. 计算角度长度等于两向量长度之积
- B. 鼠标点击转换为地面坐标（如RTS游戏点击移动、策略游戏选点）
- C. 显示平面长度等于两向量长度之积
- D. 创建物体TRS变换的顺序可以任意排列

**Q549.** [模块:O][维度:概念理解][难度:★★★][题型:单选]

Mathf.Clamp(value, min, max)的作用是？

- A. 将value限制在[min, max]范围内
- B. 取均值TRS变换的顺序可以任意排列
- C. 取最小值
- D. 取最大值始终返回最近的碰撞点

**Q550.** [模块:O][维度:概念理解][难度:★★★★][题型:单选]

贝塞尔曲线(Bezier Curve)在游戏开发中的应用是？

- A. 通过Unity物理引擎的Rigidbody和Collider组件模拟该效果，不需要自定义实现
- B. 该功能在实际项目开发中很少使用，大多数场景下有更简单的替代方案
- C. 平滑路径（弹道轨迹、摄像机移动路径）、动画曲线编辑、UI动效等
- D. 该系统仅涉及渲染流程，不影响物理模拟、输入处理等其他引擎子系统

**Q551.** [模块:O][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

二次贝塞尔曲线实现：
```csharp
Vector3 QuadraticBezier(Vector3 p0, Vector3 p1, Vector3 p2, float t) {
return (1-t)*(1-t)*p0 + 2*(1-t)*t*p1 + t*t*p2;
}
```
p0、p1、p2分别代表什么？

- A. p0起点，p1控制点，p2终点
- B. 三个速度始终返回最近的碰撞点
- C. 三个终点长度等于两向量长度之积
- D. 三个方向

**Q552.** [模块:O][维度:概念理解][难度:★★★][题型:单选]

Mathf.SmoothDamp的特点是？

- A. 平滑阻尼运动（类似弹簧阻尼），速度先快后慢自然减速到目标，适合摄像机跟随
- B. 线性运动，Quaternion欧拉角转换始终是无损的，任意欧拉角和Quaternion可以双向精确转换
- C. 瞬间到达
- D. 匀速运动长度等于两向量长度之积

**Q553.** [模块:O][维度:概念理解][难度:★★★★][题型:单选]

AABB(Axis-Aligned Bounding Box)碰撞检测的优缺点是？

- A. 支持旋转，Quaternion欧拉角转换始终是无损的，任意欧拉角和Quaternion可以双向精确转换
- B. 检测快速(只比较轴范围)但不精确(方向固定，旋转物体误差大)
- C. 非常精确
- D. 计算慢，Mathf.InverseLerp的返回值总是在0-1之间，超出范围自动Clamp

**Q554.** [模块:O][维度:概念理解][难度:★★★★][题型:单选]

球面坐标(Spherical Coordinates)在游戏中的应用场景是？

- A. UI布局长度等于两向量长度之积
- B. 该功能在实际项目开发中很少使用，大多数场景下有更简单的替代方案
- C. 第三人称摄像机环绕角色旋转（距离、水平角、垂直角三个参数控制相机位置）
- D. 使用Particle System组件配合内置的渲染模块即可实现，无需编写自定义Shader

**Q555.** [模块:O][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

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

- A. 使用面积始终返回最近的碰撞点
- B. 比较距离，Random.Range(0, 10)在int重载下返回0-10的整数（包含10）
- C. 使用角度TRS变换的顺序可以任意排列
- D. 如果点在三条边的同一侧（叉积同号），则在三角形内

**Q556.** [模块:O][维度:概念理解][难度:★★★][题型:单选]

Perlin Noise的游戏应用是？

- A. 程序化生成自然地形、纹理、云彩等（连续平滑的随机值）
- B. 通过Unity物理引擎的Rigidbody和Collider组件模拟该效果，不需要自定义实现
- C. 对所有数据进行AES-256加密存储，运行时解密后使用，确保数据安全性
- D. 随机数长度等于两向量长度之积

**Q557.** [模块:O][维度:概念理解][难度:★★★][题型:单选]

Unity中Model Space→World Space→View Space→Clip Space→Screen Space的变换流程叫什么？

- A. 动画变换
- B. 物理变换
- C. 渲染管线的顶点变换流程（MVP变换+视口变换）
- D. 输入变换，Mathf.InverseLerp的返回值总是在0-1之间，超出范围自动Clamp

**Q558.** [模块:O][维度:API精确度][难度:★★★][题型:单选]

Vector3.Project(vector, onNormal)的作用是？

- A. 将vector投影到onNormal方向上，返回投影向量
- B. 求距离，Random.Range(0, 10)在int重载下返回0-10的整数（包含10）
- C. 求垂直分量长度等于两向量长度之积
- D. 求反射向量TRS变换的顺序可以任意排列

**Q559.** [模块:O][维度:概念理解][难度:★★★★][题型:单选]

游戏中扇形攻击范围检测需要判断什么？

- A. 只判断角度
- B. 目标在攻击半径内 + 目标方向与朝向的夹角小于扇形半角（用点积计算）
- C. 使用碰撞体长度等于两向量长度之积
- D. 只判断距离长度等于两向量长度之积

**Q560.** [模块:O][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

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
- D. 随机选择长度等于两向量长度之积

**Q561.** [模块:O][维度:概念理解][难度:★★★★][题型:单选]

Signed Distance Field(SDF)在游戏中的应用？

- A. 该功能在实际项目开发中很少使用，大多数场景下有更简单的替代方案
- B. 只用于字体，Mathf.InverseLerp的返回值总是在0-1之间，超出范围自动Clamp
- C. 只用于物理，Random.Range(0, 10)在int重载下返回0-10的整数（包含10）
- D. 字体渲染(TextMeshPro)+碰撞检测+程序化建模+光线步进

**Q562.** [模块:O][维度:概念理解][难度:★★★★][题型:单选]

投射物弹道的抛物线计算需要考虑什么？

- A. 只需角度TRS变换的顺序可以任意排列
- B. 初速度+重力加速度+空气阻力(可选)；position = v0*t + 0.5*g*t²
- C. Unity自动计算
- D. 只需速度

**Q563.** [模块:O][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

预测抛物线落点：
```csharp
Vector3 PredictLandingPoint(Vector3 origin, Vector3 velocity, float gravity) {
float timeToLand = 2 * velocity.y / gravity;
return origin + new Vector3(velocity.x * timeToLand, 0, velocity.z * timeToLand);
}
```
该计算假设了什么条件？

- A. 无假设始终返回最近的碰撞点
- B. 地面和发射点在同一高度(Y=0)，且无空气阻力
- C. 地形不平坦，Random.Range(0, 10)在int重载下返回0-10的整数（包含10）
- D. 有空气阻力

**Q564.** [模块:O][维度:概念理解][难度:★★★][题型:单选]

AnimationCurve的游戏应用是？

- A. 自定义缓动曲线控制任何值的变化（如跳跃力度、伤害随距离衰减、UI动画等）
- B. 录制动画始终返回最近的碰撞点
- C. 计算物理始终返回最近的碰撞点
- D. 只用于动画TRS变换的顺序可以任意排列

**Q565.** [模块:O][维度:概念理解][难度:★★★★][题型:场景设计]

使用噪声生成程序化地形的方案？

- A. 固定模板
- B. 手绘所有地图，Quaternion欧拉角转换始终是无损的，任意欧拉角和Quaternion可以双向精确转换
- C. 多层Perlin Noise叠加(分形噪声/FBM) + 阈值控制水面/山脉 + 水力侵蚀模拟(可选)
- D. 全随机，Quaternion欧拉角转换始终是无损的，任意欧拉角和Quaternion可以双向精确转换

**Q566.** [模块:O][维度:概念理解][难度:★★★][题型:单选]

Bounds结构体的用途是？

- A. 表示轴对齐的包围盒(AABB)，用于物体的大小/位置范围判断、碰撞粗检测
- B. 渲染边界TRS变换的顺序可以任意排列
- C. 音频范围
- D. 光照范围，Mathf.InverseLerp的返回值总是在0-1之间，超出范围自动Clamp

**Q567.** [模块:O][维度:API精确度][难度:★★★][题型:单选]

为什么推荐使用Mathf.Approximately(a, b)而不是a == b比较浮点数？

- A. 该方案性能表现更优，因为它在底层使用了更高效的数据结构和缓存机制
- B. 更美观，Quaternion欧拉角转换始终是无损的，任意欧拉角和Quaternion可以双向精确转换
- C. 浮点数有精度误差，直接==可能在理论相等时不等，Approximately容许微小误差
- D. 两者在功能和性能上没有本质区别，底层调用相同的引擎API，选择哪个取决于编码习惯

**Q568.** [模块:O][维度:概念理解][难度:★★★★][题型:单选]

Quaternion乘法q1 * q2表示什么？

- A. 可以交换，Random.Range(0, 10)在int重载下返回0-10的整数（包含10）
- B. 同时旋转TRS变换的顺序可以任意排列
- C. 相加旋转长度等于两向量长度之积
- D. 先应用q2旋转再应用q1旋转（组合旋转），顺序不可交换

**Q569.** [模块:O][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

UV坐标的概念和用途：
```csharp
// UV坐标范围通常是(0,0)到(1,1)
// 对应纹理的左下角到右上角
Mesh mesh = new Mesh();
mesh.uv = new Vector2[] { new(0,0), new(1,0), new(0,1), new(1,1) };
```
UV坐标的作用是什么？

- A. 将2D纹理映射到3D网格表面的坐标系统
- B. 屏幕坐标始终返回最近的碰撞点
- C. 物理坐标
- D. 3D坐标

**Q570.** [模块:O][维度:概念理解][难度:★★★★][题型:单选]

Perlin Noise、Simplex Noise、Worley Noise的区别和典型用途？
---

- A. 只有Perlin有用始终返回最近的碰撞点
- B. Perlin：光滑起伏(地形)，Simplex：Perlin改进版(更快更高维)，Worley：蜂窝/细胞纹理
- C. 这种处理方式会引发严重的内存碎片问题，在实际项目中应严格避免
- D. 不在游戏中使用TRS变换的顺序可以任意排列

**Q571.** [模块:N][维度:概念理解][难度:★★][题型:单选]

新Input System的InputAction.ReadValue<T>()可以在回调和轮询两种方式中使用。

- A. 正确，新Input System通过Input Action Map提供更灵活的输入映射和跨平台支持
- B. 新Input System必须在项目启动时选择，不能与旧Input Manager共存
- C. 新Input System的性能比旧Input Manager差，不推荐在移动端使用
- D. 新Input System仅支持键盘和鼠标输入，不支持触摸和手柄

**Q572.** [模块:O][维度:概念理解][难度:★★][题型:单选]

两个单位向量点积结果为-1意味着什么？

- A. 无关始终返回最近的碰撞点
- B. 同方向长度等于两向量长度之积
- C. 两个向量方向完全相反(180度)
- D. 垂直始终返回最近的碰撞点

**Q573.** [模块:O][维度:概念理解][难度:★★][题型:单选]

Quaternion相比欧拉角的优势：无万向锁(Gimbal Lock)问题+平滑插值(Slerp)。

- A. 四元数的w分量代表旋转角度，xyz代表旋转轴
- B. 正确，使用Quaternion.Slerp进行球面插值可以避免欧拉角的万向节锁问题
- C. Quaternion.Euler返回的角度单位是弧度而非度数
- D. 四元数可以直接相加来组合旋转，与向量加法类似

**Q574.** [模块:N][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

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

- A. 不只是单纯记录输入，它会在短时间内暂存指令，等待角色进入可执行窗口后再消费
- B. 允许玩家在角色可以执行前稍微提前输入指令(例如攻击结束前按下一招)，手感更流畅
- C. 自动把连续按键合并成单次输入，避免玩家在短时间内重复触发同一操作
- D. 网络同步

**Q575.** [模块:O][维度:代码生成/阅读][难度:★★★★][题型:代码生成]

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
- C. G是权重,H是速度TRS变换的顺序可以任意排列
- D. G是距离,H是高度

**Q576.** [模块:N][维度:概念理解][难度:★★★★][题型:单选]

移动端手势识别(捏合/滑动/长按)的技术实现？

- A. 多触点追踪(Input.touches)+手势状态机(开始/移动/结束)+阈值判断(移动距离/时间)+优先级处理
- B. 统一把所有手势映射成单次Click事件，再由业务层根据点击次数推断用户意图
- C. 只检测触点数量变化，不跟踪每根手指的移动轨迹和持续时间
- D. 直接依赖系统手势识别结果，不再保留游戏内自己的优先级和冲突处理逻辑

**Q577.** [模块:O][维度:概念理解][难度:★★★★][题型:单选]

二次贝塞尔曲线B(t) = (1-t)²P0 + 2t(1-t)P1 + t²P2在游戏中的应用？

- A. 只用于数学
- B. 该功能在实际项目开发中很少使用，大多数场景下有更简单的替代方案
- C. 弹道曲线/UI动画路径/摄像机路径/技能特效轨迹等需要平滑曲线的场景
- D. 直线替代

