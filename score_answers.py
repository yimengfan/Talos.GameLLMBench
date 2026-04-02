#!/usr/bin/env python3
import argparse
import re
import sys
from collections import defaultdict

QUESTION_HEADER_RE = re.compile(
    r"\*\*Q(\d+)\.\*\*\s*\[模块:([^\]]+)\]\[维度:([^\]]+)\]\[难度:([^\]]+)\]\[题型:([^\]]+)\]"
)
OPTION_RE = re.compile(r"-\s*([A-D])\.\s*(.+)")

ASCII_STOPWORDS = {
    "true",
    "false",
    "null",
    "void",
    "int",
    "float",
    "string",
    "bool",
    "var",
    "new",
    "out",
    "ref",
    "get",
    "set",
    "the",
    "and",
    "for",
    "with",
    "from",
    "that",
    "this",
    "only",
    "mode",
    "value",
    "values",
}

SCENARIO_CONSTRAINT_TERMS = [
    "架构",
    "分层",
    "流程",
    "约束",
    "前提",
    "初始化",
    "主界面",
    "模块",
    "系统",
    "事件驱动",
    "树形结构",
    "导航网格",
    "运行时",
    "增量更新",
    "工具链",
    "自动化测试",
    "分包",
    "公共资源",
    "冗余依赖",
    "单元测试",
    "集成测试",
    "端到端",
    "界面栈",
    "资源加载",
    "动画管理",
    "消息解耦",
    "服务器权威",
    "事务一致性",
    "日志审计",
    "回滚机制",
    "性能预算",
    "固定测试场景",
    "录制回放",
    "CI",
    "告警",
    "阻断合入",
]

GLOBAL_TECH_TERMS = [
    "生命周期",
    "Awake",
    "Start",
    "Update",
    "LateUpdate",
    "FixedUpdate",
    "Rigidbody",
    "Collider",
    "CharacterController",
    "LayerMask",
    "NavMesh",
    "Addressables",
    "AssetBundle",
    "ScriptableObject",
    "SerializeReference",
    "Resources",
    "UnloadUnusedAssets",
    "InputAction",
    "Input Debugger",
    "compositionString",
    "Canvas",
    "LayoutGroup",
    "TextMeshPro",
    "AudioMixer",
    "Cinemachine",
    "Timeline",
    "Playable",
    "DOTS",
    "Burst",
    "NativeArray",
    "Job",
    "GC",
    "AOT",
    "IL2CPP",
    "HybridCLR",
    "版本",
    "依赖",
    "引用计数",
    "异步",
    "预加载",
    "碰撞",
    "渲染",
    "输入",
    "热更新",
    "构建",
    "性能",
    "优化",
]

MODULE_MAP = {
    "A": "核心架构",
    "B": "C#与脚本编程",
    "C": "物理系统",
    "D": "渲染基础",
    "E": "动画系统",
    "F": "音频系统",
    "G": "导航寻路",
    "H": "网络系统",
    "I": "粒子系统",
    "J": "ScriptableObject与通用组件",
    "K": "2D系统",
    "L": "编辑器扩展",
    "M": "资源管理",
    "N": "输入系统",
    "O": "数学与几何",
    "P": "渲染管线进阶",
    "Q": "热更新方案",
    "R": "AssetBundle进阶",
    "S": "SDK与平台适配",
    "T": "CI/CD与自动化",
    "U": "UI进阶",
    "V": "游戏逻辑系统",
    "W": "战斗系统",
    "X": "Timeline与Cinemachine",
    "Y": "DOTS/ECS",
    "Z": "Job System与Burst",
    "AA": "性能分析与优化",
    "AB": "序列化与数据管理",
    "AC": "跨平台开发",
    "AD": "Shader编程",
}

DIFFICULTY_LABELS = {
    "★": "入门",
    "★★": "初级",
    "★★★": "中级",
    "★★★★": "高级",
    "★★★★★": "专家",
}

QUESTION_TYPE_MAP = {
    "单选": "单选题",
    "判断": "判断题",
    "代码补全": "代码补全题",
    "代码生成": "代码生成题",
    "代码阅读": "代码阅读题",
    "场景设计": "场景设计题",
    "概念": "概念/配置题",
    "配置": "概念/配置题",
}


def parse_answer_key(filepath):
    answers = {}
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            m = re.match(r"\*\*Q(\d+)\.\*\*\s*([A-D])", line)
            if m:
                answers[int(m.group(1))] = m.group(2)
    return answers


def parse_llm_answers(filepath):
    answers = {}
    analyses = {}
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            m = re.match(r"Q(\d+)\.\s*([A-D])\s*[|｜]\s*(.+)", line, re.IGNORECASE)
            if m:
                qnum = int(m.group(1))
                answers[qnum] = m.group(2).upper()
                analyses[qnum] = m.group(3).strip()
            else:
                m2 = re.match(r"Q(\d+)\.\s*([A-D])\s*$", line, re.IGNORECASE)
                if m2:
                    qnum = int(m2.group(1))
                    answers[qnum] = m2.group(2).upper()
                    analyses[qnum] = ""
    return answers, analyses


def extract_keywords(text):
    ascii_tokens = {
        token.lower()
        for token in re.findall(r"[A-Za-z_][A-Za-z0-9_<>.]{2,}", text)
        if token.lower() not in ASCII_STOPWORDS
    }
    phrase_tokens = {term for term in GLOBAL_TECH_TERMS if term in text}
    chinese_phrases = {
        phrase
        for phrase in re.findall(r"[\u4e00-\u9fff]{3,}", text)
        if len(phrase) >= 3
    }
    return ascii_tokens | phrase_tokens | chinese_phrases


def parse_question_bank(filepath, answer_key):
    question_bank = {}

    def flush_question(current_qnum, current_meta, block_lines):
        if current_qnum is None:
            return

        options = {}
        stem_lines = []
        options_started = False

        for raw_line in block_lines:
            stripped = raw_line.strip()
            option_match = OPTION_RE.match(stripped)
            if option_match:
                options_started = True
                options[option_match.group(1)] = option_match.group(2).strip()
                continue
            if not options_started:
                stem_lines.append(stripped)

        correct_option = answer_key.get(current_qnum, "")
        correct_option_text = options.get(correct_option, "")
        keyword_source = "\n".join(stem_lines + [correct_option_text])

        question_bank[current_qnum] = {
            **current_meta,
            "stem": "\n".join(stem_lines).strip(),
            "options": options,
            "correct_option_text": correct_option_text,
            "keywords": extract_keywords(keyword_source),
        }

    with open(filepath, "r", encoding="utf-8") as f:
        current_qnum = None
        current_meta = None
        block_lines = []

        for line in f:
            match = QUESTION_HEADER_RE.match(line.strip())
            if match:
                flush_question(current_qnum, current_meta, block_lines)
                current_qnum = int(match.group(1))
                current_meta = {
                    "module": match.group(2),
                    "dimension": match.group(3),
                    "difficulty": match.group(4),
                    "qtype": match.group(5),
                }
                block_lines = []
            elif current_qnum is not None:
                block_lines.append(line.rstrip("\n"))

        flush_question(current_qnum, current_meta, block_lines)

    return question_bank


def validate_analysis(question_info, analysis):
    analysis = analysis.strip()
    if len(analysis) < 20:
        return False, "缺少分析或分析过短"

    analysis_lower = analysis.lower()
    keyword_hits = 0
    for keyword in question_info.get("keywords", set()):
        if any("a" <= ch.lower() <= "z" or ch.isdigit() for ch in keyword):
            if keyword in analysis_lower:
                keyword_hits += 1
        elif keyword in analysis:
            keyword_hits += 1

    global_hits = sum(1 for term in GLOBAL_TECH_TERMS if term in analysis)
    scenario_constraint_hits = sum(1 for term in SCENARIO_CONSTRAINT_TERMS if term in analysis)
    has_code_signal = bool(re.search(r"[A-Za-z_][A-Za-z0-9_<>.()]{2,}", analysis))
    qtype = question_info.get("qtype", "")
    has_question_keywords = bool(question_info.get("keywords"))

    if qtype in {"代码补全", "代码生成", "代码阅读"}:
        if keyword_hits >= 1 or (has_code_signal and has_question_keywords):
            return True, ""
        return False, "分析未引用关键API/代码点"

    if qtype == "场景设计":
        if keyword_hits >= 2:
            return True, ""
        if not has_question_keywords and (global_hits >= 2 or scenario_constraint_hits >= 2):
            return True, ""
        if keyword_hits >= 1 and scenario_constraint_hits >= 1:
            return True, ""
        if scenario_constraint_hits >= 3:
            return True, ""
        return False, "分析未体现方案关键约束"

    if keyword_hits >= 1 or (not has_question_keywords and (global_hits >= 1 or has_code_signal)):
        return True, ""

    return False, "分析未引用关键技术点"


def score_answers(answer_key, llm_answers, analyses, question_bank, strict_analysis=True):
    total = len(answer_key)
    answered = 0
    choice_correct = 0
    analysis_valid = 0
    benchmark_correct = 0
    wrong_list = []
    unanswered = []
    low_quality_analysis_list = []

    stats = {
        "by_module": defaultdict(lambda: {"correct": 0, "total": 0}),
        "by_dimension": defaultdict(lambda: {"correct": 0, "total": 0}),
        "by_difficulty": defaultdict(lambda: {"correct": 0, "total": 0}),
        "by_qtype": defaultdict(lambda: {"correct": 0, "total": 0}),
    }

    for qnum in sorted(answer_key.keys()):
        correct_answer = answer_key[qnum]
        meta = question_bank.get(qnum, {})

        entry_module = MODULE_MAP.get(meta.get("module", ""), meta.get("module", "未知"))
        entry_dimension = meta.get("dimension", "未知")
        entry_difficulty = meta.get("difficulty", "未知")
        entry_qtype = meta.get("qtype", "未知")

        stats["by_module"][entry_module]["total"] += 1
        stats["by_dimension"][entry_dimension]["total"] += 1
        stats["by_difficulty"][entry_difficulty]["total"] += 1

        mapped_qtype = QUESTION_TYPE_MAP.get(entry_qtype, entry_qtype)
        stats["by_qtype"][mapped_qtype]["total"] += 1

        if qnum not in llm_answers:
            unanswered.append(qnum)
            continue

        answered += 1
        llm_answer = llm_answers[qnum]
        analysis = analyses.get(qnum, "")
        analysis_ok, analysis_reason = validate_analysis(meta, analysis) if strict_analysis else (True, "")

        is_correct = llm_answer == correct_answer
        if is_correct:
            choice_correct += 1
        if analysis_ok:
            analysis_valid += 1

        if is_correct and analysis_ok:
            benchmark_correct += 1
            stats["by_module"][entry_module]["correct"] += 1
            stats["by_dimension"][entry_dimension]["correct"] += 1
            stats["by_difficulty"][entry_difficulty]["correct"] += 1
            stats["by_qtype"][mapped_qtype]["correct"] += 1
        else:
            reasons = []
            if not is_correct:
                reasons.append("答案错误")
            if not analysis_ok:
                reasons.append(analysis_reason)
                low_quality_analysis_list.append((qnum, llm_answer, entry_module, analysis_reason))
            wrong_list.append((qnum, correct_answer, llm_answer, entry_module, "；".join(reasons)))

    return {
        "total": total,
        "answered": answered,
        "choice_correct": choice_correct,
        "analysis_valid": analysis_valid,
        "benchmark_correct": benchmark_correct,
        "wrong_list": wrong_list,
        "unanswered": unanswered,
        "low_quality_analysis_list": low_quality_analysis_list,
        "stats": stats,
    }


def print_report(result, detail=False):
    total = result["total"]
    benchmark_correct = result["benchmark_correct"]
    choice_correct = result["choice_correct"]
    answered = result["answered"]
    analysis_valid = result["analysis_valid"]
    benchmark_accuracy = benchmark_correct / total * 100 if total > 0 else 0
    choice_accuracy = choice_correct / total * 100 if total > 0 else 0
    analysis_rate = analysis_valid / answered * 100 if answered > 0 else 0

    print("=" * 60)
    print(f"  Unity3D LLM 评测报告")
    print("=" * 60)
    print(f"\n  综合基准分: {benchmark_correct}/{total}  综合正确率: {benchmark_accuracy:.1f}%")
    print(f"  客观选项得分: {choice_correct}/{total}  选项正确率: {choice_accuracy:.1f}%")
    print(f"  分析合格数: {analysis_valid}/{answered}  分析合格率: {analysis_rate:.1f}%")
    print(f"  综合答对: {benchmark_correct}  综合答错: {len(result['wrong_list'])}  未答: {len(result['unanswered'])}")

    stats = result["stats"]

    print(f"\n{'─' * 60}")
    print(f"  按模块统计")
    print(f"{'─' * 60}")
    print(f"  {'模块':<20} {'正确/总数':<12} {'正确率':<10}")
    print(f"  {'─' * 42}")
    for module in sorted(stats["by_module"].keys()):
        s = stats["by_module"][module]
        rate = s["correct"] / s["total"] * 100 if s["total"] > 0 else 0
        bar = "█" * int(rate / 5) + "░" * (20 - int(rate / 5))
        print(f"  {module:<20} {s['correct']:>3}/{s['total']:<5} {rate:>5.1f}%  {bar}")

    print(f"\n{'─' * 60}")
    print(f"  按能力维度统计")
    print(f"{'─' * 60}")
    for dim in sorted(stats["by_dimension"].keys()):
        s = stats["by_dimension"][dim]
        rate = s["correct"] / s["total"] * 100 if s["total"] > 0 else 0
        bar = "█" * int(rate / 5) + "░" * (20 - int(rate / 5))
        print(f"  {dim:<20} {s['correct']:>3}/{s['total']:<5} {rate:>5.1f}%  {bar}")

    print(f"\n{'─' * 60}")
    print(f"  按难度统计")
    print(f"{'─' * 60}")
    difficulty_order = ["★", "★★", "★★★", "★★★★", "★★★★★"]
    for diff in difficulty_order:
        if diff in stats["by_difficulty"]:
            s = stats["by_difficulty"][diff]
            rate = s["correct"] / s["total"] * 100 if s["total"] > 0 else 0
            label = DIFFICULTY_LABELS.get(diff, diff)
            bar = "█" * int(rate / 5) + "░" * (20 - int(rate / 5))
            print(f"  {diff} {label:<12} {s['correct']:>3}/{s['total']:<5} {rate:>5.1f}%  {bar}")

    print(f"\n{'─' * 60}")
    print(f"  按题型统计")
    print(f"{'─' * 60}")
    for qt in sorted(stats["by_qtype"].keys()):
        s = stats["by_qtype"][qt]
        rate = s["correct"] / s["total"] * 100 if s["total"] > 0 else 0
        bar = "█" * int(rate / 5) + "░" * (20 - int(rate / 5))
        print(f"  {qt:<16} {s['correct']:>3}/{s['total']:<5} {rate:>5.1f}%  {bar}")

    if detail and result["wrong_list"]:
        print(f"\n{'─' * 60}")
        print(f"  错误详情（共 {len(result['wrong_list'])} 题）")
        print(f"{'─' * 60}")
        for qnum, correct_ans, llm_ans, module, reason in result["wrong_list"][:50]:
            print(f"  Q{qnum:03d}: 正确={correct_ans}  回答={llm_ans}  模块={module}  原因={reason}")
        if len(result["wrong_list"]) > 50:
            print(f"  ... 还有 {len(result['wrong_list']) - 50} 题未显示")

    if result["low_quality_analysis_list"]:
        print(f"\n{'─' * 60}")
        print(f"  分析不合格（共 {len(result['low_quality_analysis_list'])} 题，算作综合评分错误）")
        print(f"{'─' * 60}")
        for qnum, llm_ans, module, reason in result["low_quality_analysis_list"][:50]:
            print(f"  Q{qnum:03d}: 回答={llm_ans}  模块={module}  原因={reason}")
        if len(result["low_quality_analysis_list"]) > 50:
            print(f"  ... 还有 {len(result['low_quality_analysis_list']) - 50} 题未显示")

    if result["unanswered"]:
        print(f"\n{'─' * 60}")
        print(f"  未答题（共 {len(result['unanswered'])} 题）")
        print(f"{'─' * 60}")
        for qnum in result["unanswered"][:20]:
            print(f"  Q{qnum:03d}")
        if len(result["unanswered"]) > 20:
            print(f"  ... 还有 {len(result['unanswered']) - 20} 题未显示")

    print(f"\n{'=' * 60}")


def main():
    parser = argparse.ArgumentParser(description="Unity3D LLM 评测评分脚本")
    parser.add_argument("--answer", required=True, help="答案密钥文件路径 (answer_key.md)")
    parser.add_argument("--llm", required=True, help="LLM 答题文件路径 (llm_answer.txt)")
    parser.add_argument("--questions", default="questions.md", help="题库文件路径 (用于提取元数据)")
    parser.add_argument("--detail", action="store_true", help="显示错误详情")
    parser.add_argument("--choice-only", action="store_true", help="兼容旧版，仅按选项字母评分")
    args = parser.parse_args()

    answer_key = parse_answer_key(args.answer)
    if not answer_key:
        print(f"错误: 无法从 {args.answer} 解析答案密钥", file=sys.stderr)
        sys.exit(1)

    llm_answers, analyses = parse_llm_answers(args.llm)
    if not llm_answers:
        print(f"错误: 无法从 {args.llm} 解析LLM答案", file=sys.stderr)
        sys.exit(1)

    question_bank = parse_question_bank(args.questions, answer_key)
    if not question_bank:
        print(f"警告: 无法从 {args.questions} 解析题目元数据，将跳过分维度统计", file=sys.stderr)

    result = score_answers(
        answer_key,
        llm_answers,
        analyses,
        question_bank,
        strict_analysis=not args.choice_only,
    )
    print_report(result, detail=args.detail)


if __name__ == "__main__":
    main()
