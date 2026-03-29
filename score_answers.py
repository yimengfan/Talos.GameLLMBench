#!/usr/bin/env python3
import argparse
import re
import sys
from collections import defaultdict

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
    has_analysis = {}
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            m = re.match(r"Q(\d+)\.\s*([A-D])\s*\|\s*(.+)", line, re.IGNORECASE)
            if m:
                qnum = int(m.group(1))
                answers[qnum] = m.group(2).upper()
                analysis = m.group(3).strip()
                has_analysis[qnum] = len(analysis) >= 10
            else:
                m2 = re.match(r"Q(\d+)\.\s*([A-D])\s*$", line, re.IGNORECASE)
                if m2:
                    qnum = int(m2.group(1))
                    answers[qnum] = m2.group(2).upper()
                    has_analysis[qnum] = False
    return answers, has_analysis


def parse_question_metadata(filepath):
    metadata = {}
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = re.compile(
        r"\*\*Q(\d+)\.\*\*\s*\[模块:([^\]]+)\]\[维度:([^\]]+)\]\[难度:([^\]]+)\]\[题型:([^\]]+)\]"
    )
    for m in pattern.finditer(content):
        qnum = int(m.group(1))
        metadata[qnum] = {
            "module": m.group(2),
            "dimension": m.group(3),
            "difficulty": m.group(4),
            "qtype": m.group(5),
        }
    return metadata


def score_answers(answer_key, llm_answers, has_analysis, metadata, detail=False):
    total = len(answer_key)
    correct = 0
    wrong_list = []
    unanswered = []
    no_analysis_list = []

    stats = {
        "by_module": defaultdict(lambda: {"correct": 0, "total": 0}),
        "by_dimension": defaultdict(lambda: {"correct": 0, "total": 0}),
        "by_difficulty": defaultdict(lambda: {"correct": 0, "total": 0}),
        "by_qtype": defaultdict(lambda: {"correct": 0, "total": 0}),
    }

    for qnum in sorted(answer_key.keys()):
        correct_answer = answer_key[qnum]
        meta = metadata.get(qnum, {})

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

        llm_answer = llm_answers[qnum]

        if not has_analysis.get(qnum, False):
            no_analysis_list.append((qnum, correct_answer, llm_answer, entry_module))
            wrong_list.append((qnum, correct_answer, llm_answer, entry_module, "无答题分析"))
            continue

        is_correct = llm_answer == correct_answer

        if is_correct:
            correct += 1
            stats["by_module"][entry_module]["correct"] += 1
            stats["by_dimension"][entry_dimension]["correct"] += 1
            stats["by_difficulty"][entry_difficulty]["correct"] += 1
            stats["by_qtype"][mapped_qtype]["correct"] += 1
        else:
            wrong_list.append((qnum, correct_answer, llm_answer, entry_module, "答案错误"))

    return {
        "total": total,
        "correct": correct,
        "wrong_list": wrong_list,
        "unanswered": unanswered,
        "no_analysis_list": no_analysis_list,
        "stats": stats,
    }


def print_report(result, detail=False):
    total = result["total"]
    correct = result["correct"]
    accuracy = correct / total * 100 if total > 0 else 0

    print("=" * 60)
    print(f"  Unity3D LLM 评测报告")
    print("=" * 60)
    print(f"\n  总分: {correct}/{total}  正确率: {accuracy:.1f}%")
    print(f"  答对: {correct}  答错: {len(result['wrong_list'])}  未答: {len(result['unanswered'])}")

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
    difficulty_order = ["★", "★★", "★★★", "★★★★"]
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

    if result["no_analysis_list"]:
        print(f"\n{'─' * 60}")
        print(f"  无答题分析（共 {len(result['no_analysis_list'])} 题，均计为错误）")
        print(f"{'─' * 60}")
        for qnum, correct_ans, llm_ans, module in result["no_analysis_list"][:50]:
            print(f"  Q{qnum:03d}: 回答={llm_ans}  模块={module}")
        if len(result["no_analysis_list"]) > 50:
            print(f"  ... 还有 {len(result['no_analysis_list']) - 50} 题未显示")

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
    args = parser.parse_args()

    answer_key = parse_answer_key(args.answer)
    if not answer_key:
        print(f"错误: 无法从 {args.answer} 解析答案密钥", file=sys.stderr)
        sys.exit(1)

    llm_answers, has_analysis = parse_llm_answers(args.llm)
    if not llm_answers:
        print(f"错误: 无法从 {args.llm} 解析LLM答案", file=sys.stderr)
        sys.exit(1)

    metadata = parse_question_metadata(args.questions)
    if not metadata:
        print(f"警告: 无法从 {args.questions} 解析题目元数据，将跳过分维度统计", file=sys.stderr)

    result = score_answers(answer_key, llm_answers, has_analysis, metadata, detail=args.detail)
    print_report(result, detail=args.detail)


if __name__ == "__main__":
    main()
