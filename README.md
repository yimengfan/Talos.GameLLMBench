# Talos.GameLLMBench
A benchmark framework for evaluating LLM capabilities in game development.

当前正式题库为连续编号的 1000 道单选题，范围为 Q001-Q1000，覆盖 Unity3D 2022 LTS 常见核心模块、工程实践与高级专题。

## 这个库的作用

Talos.GameLLMBench 用来评估一个 LLM 在游戏开发，尤其是 Unity3D 场景下的真实答题能力。它不只看选项是否选对，还会检查分析是否真的锚定到题目的关键技术点。

这个库主要解决三类问题：

1. 判断模型是否真的理解 Unity API、生命周期、资源管理、渲染、热更新、CI/CD 等知识，而不是只会猜选项。
2. 区分“字母答对但分析空泛”和“真正有工程依据的正确回答”。
3. 用统一题库、统一答案格式、统一评分方式，对不同模型或不同版本做横向对比。

## 仓库结构

核心目录和文件如下：

- `questions/`
  存放题库分片，当前共有 10 个文件，题号连续覆盖 Q001-Q1000。
- `answer_key/`
  存放标准答案密钥。该目录不能暴露给被测模型。
- `answers/`
  存放当前待评分的 LLM 答题结果。
- `score_answers.py`
  核心评分脚本。
- `run_score.sh`
  一键评分入口，会自动聚合题目、答案键和当前答案，并在评分后归档答案。
- `llm_prompt.md`
  给被测模型的执行提示词模板。
- `gen_questions_rule.md`
  题库生成规范、答题格式规范和评分语义说明。
- `score_history/`
  存放历史评分报告和归档后的答案文件。

## 如何让 LLM 答题

### 1. 准备题目

把 `questions/` 目录下的题目分片喂给 LLM。推荐按分片执行，例如：

- `questions/questions_01_core.md`
- `questions/questions_02_physics.md`
- `questions/questions_03_render.md`

如果你要让 Agent 自动跑完整题库，建议配合 [llm_prompt.md](llm_prompt.md) 中的流程执行。

### 2. 答案输出格式

每个答案文件建议先输出两行模型元数据，方便后续做按模型和版本的评分统计：

```text
MODEL_NAME: GPT-5.4
MODEL_VERSION: 2026-04-01
```

之后再逐题输出答案，格式必须严格为：

```text
Q001. A | 分析内容
Q002. D | 分析内容
Q003. B | 分析内容
```

要求如下：

- 每题只能有一个大写字母选项 `A-D`
- `|` 后必须带分析
- 分析建议不少于 20 字
- 分析必须引用题目相关的 API、类名、机制、生命周期、约束条件或工程方案依据
- 场景设计题不能只写“更合理”“性能更好”这类泛化空话，必须体现架构分层、初始化顺序、资源拆分、测试层级、回滚机制、性能预算等可核验约束

### 3. 答案文件命名

推荐命名：

```text
answers/llm_answer_01_core.txt
answers/llm_answer_02_physics.txt
```

也兼容旧命名：

```text
answers/llm_answer_01.txt
answers/llm_answer_02.txt
```

## 如何评分

### 一键评分

在仓库根目录直接运行：

```bash
bash run_score.sh
```

这个脚本会自动做以下事情：

1. 聚合 `questions/` 下全部题目分片
2. 聚合 `answer_key/` 下全部答案密钥
3. 读取 `answers/` 下当前存在的 `llm_answer_*.txt`
4. 调用 [score_answers.py](score_answers.py) 输出总成绩和分维度统计
5. 评分完成后，把本次消费过的答案移动到 `score_history/archived_answers/时间戳/`
6. 把最新评分报告写入 `score_history/latest_score.txt`

### 无新答案时的行为

如果 `answers/` 目录里没有新的答案文件：

- 默认不会重复读取已经归档的旧答案
- 会直接显示上一次得分

如果你明确要复用最近一次归档答案重新评分，执行：

```bash
bash run_score.sh --reuse-last-answers
```

### 直接调用评分脚本

如果你不想走一键脚本，也可以直接运行：

```bash
python3 score_answers.py --answer answer_key.md --llm llm_answer.txt --questions questions.md --detail
```

如果只想按旧版“字母是否正确”统计，不检查分析质量：

```bash
python3 score_answers.py --answer answer_key.md --llm llm_answer.txt --questions questions.md --detail --choice-only
```

## 评分规则说明

### 默认评分

默认报告包含三组核心指标：

- **综合基准分**
  选项正确，且分析有效锚定题目关键技术点。
- **客观选项分**
  只统计字母是否选对，便于和旧版结果做横向对比。
- **分析合格数**
  统计分析是否满足技术锚点要求。

### 场景设计题的特殊判定

对场景设计题，评分器除了匹配 API 和术语，还允许通过命中明确的工程约束词来判定分析有效，例如：

- 架构分层
- 流程顺序
- 初始化顺序
- 资源拆分
- 回滚机制
- 测试分层
- 性能预算
- 审计和告警

这样可以减少“题面 API 关键词较少，但回答其实很专业”时的误杀。

### 兼容旧版评分

`--choice-only` 模式下，会退回到旧版逻辑，只按字母正确率统计，不再要求分析锚点。

## 成绩如何解读

默认可按下面区间粗略理解：

- `> 85%`：专家级
- `70% - 85%`：高级
- `50% - 70%`：初中级
- `< 50%`：入门级

同时建议结合以下统计一起看：

- 按模块统计：看模型在哪些 Unity 模块上明显短板
- 按能力维度统计：看是 API 精确度、代码阅读还是 Bug 诊断问题
- 按题型统计：看模型是单选题稳定，还是场景设计题更强

## 推荐使用流程

如果你第一次使用这个库，推荐按下面顺序：

1. 阅读 [llm_prompt.md](llm_prompt.md)，确定答题格式和执行方式
2. 将 `questions/` 分片喂给目标 LLM
3. 把答案保存到 `answers/llm_answer_*.txt`
4. 运行 `bash run_score.sh`
5. 查看终端输出和 [score_history/latest_score.txt](score_history/latest_score.txt)
6. 如需重复统计同一批归档答案，使用 `bash run_score.sh --reuse-last-answers`

## 相关文档

- [llm_prompt.md](llm_prompt.md): LLM 自动答题提示词模板
- [gen_questions_rule.md](gen_questions_rule.md): 题库生成与答题输出规范
- [score_answers.py](score_answers.py): 核心评分脚本
- [run_score.sh](run_score.sh): 一键评分入口
