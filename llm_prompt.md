# Unity3D 2022 LTS 基础能力问答 - LLM答题标准提示词

## 提示词模板

```
你是一个Unity3D 2022 LTS的技术专家。请回答以下选择题。
问题列表位于"questions.md"，仅根据questions.md中的内容作答。

【输出格式要求】严格遵守以下格式，每题必须包含答案和答题分析：
1. 每题格式为：
   Q编号. 答案字母 | 分析内容
   例如：Q001. A | Unity中MonoBehaviour的生命周期首先执行Awake，再执行Start...
2. 每题只输出一个字母（A/B/C/D），没有多选题
3. 编号保持题库原编号格式（如Q001, Q002 ... Q999, Q1000）
4. 如果出现选项模糊的单选题请选择你认为概率最高的
5. 每题必须输出答题分析（即 | 后面的内容），分析需要说明选择该答案的理由
6. 答题分析至少包含对相关API/概念的正确描述，不少于10个字
7. 答完一题，将答案输出到 `llm_answer.txt`，若该文档存在则接着该文档进度答题。
如果发现本地有答题完成‘llm_answer.txt’（1000 题）则直接删除，重新开始

【输出示例】
Q001. A | Unity中Awake在脚本实例化时立即调用，早于Start，适合做初始化引用
Q002. D | Rigidbody的isKinematic为true时不受物理引擎力的影响，但仍可通过MovePosition移动
Q003. B | Camera.main在URP中已标记为Obsolete，推荐使用Camera.main或FindAnyObjectByType替代
Q004. C | NavMeshAgent.Warp用于瞬移导航代理到指定位置，而非SetDestination的路径规划
Q005. A | [SerializeField]使private字段在Inspector中可见并可编辑，但不改变其访问级别
---
```
答题后执行 run_score.sh 脚本，