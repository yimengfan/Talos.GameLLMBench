#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

SCORE_SCRIPT="score_answers.py"
QUESTIONS_DIR="questions"
ANSWER_KEY_DIR="answer_key"
ANSWERS_DIR="answers"
SCORE_HISTORY_DIR="score_history"
ARCHIVED_ANSWERS_DIR="$SCORE_HISTORY_DIR/archived_answers"
REPORTS_DIR="$SCORE_HISTORY_DIR/reports"
LATEST_REPORT="$SCORE_HISTORY_DIR/latest_score.txt"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

REUSE_LAST_ANSWERS=0

usage() {
    cat <<'EOF'
Usage: bash run_score.sh [--reuse-last-answers]

默认行为:
  1. 只读取 answers/ 目录下当前存在的 llm_answer_*.txt
  2. 评分完成后自动把本次答案归档到 score_history/archived_answers/
  3. 下次未检测到新答案时，不会重复读取已归档答案，而是直接显示上次得分

Options:
  --reuse-last-answers   显式复用最近一次归档的答案重新评分
  -h, --help             显示帮助
EOF
}

while [ $# -gt 0 ]; do
    case "$1" in
        --reuse-last-answers)
            REUSE_LAST_ANSWERS=1
            ;;
        -h|--help)
            usage
            exit 0
            ;;
        *)
            echo -e "${RED}错误: 未知参数 $1${NC}"
            usage
            exit 1
            ;;
    esac
    shift
done

if [ ! -f "$SCORE_SCRIPT" ]; then
    echo -e "${RED}错误: 评分脚本 $SCORE_SCRIPT 不存在${NC}"
    exit 1
fi

if [ ! -d "$QUESTIONS_DIR" ]; then
    echo -e "${RED}错误: 题库目录 $QUESTIONS_DIR 不存在${NC}"
    exit 1
fi

if [ ! -d "$ANSWER_KEY_DIR" ]; then
    echo -e "${RED}错误: 答案密钥目录 $ANSWER_KEY_DIR 不存在${NC}"
    exit 1
fi

if [ ! -d "$ANSWERS_DIR" ]; then
    echo -e "${RED}错误: LLM 答题目录 $ANSWERS_DIR 不存在${NC}"
    echo -e "${YELLOW}提示: 请先将 LLM 的答题结果按批次保存到 $ANSWERS_DIR 目录下 (如 llm_answer_01.txt)${NC}"
    exit 1
fi

mkdir -p "$ARCHIVED_ANSWERS_DIR" "$REPORTS_DIR"

# Create a temporary file to aggregate all answers and keys
TEMP_DIR=$(mktemp -d)
AGGREGATED_QUESTIONS="$TEMP_DIR/all_questions.md"
AGGREGATED_KEY="$TEMP_DIR/all_keys.md"
AGGREGATED_LLM="$TEMP_DIR/all_llm_answers.txt"

cleanup() {
    rm -rf "$TEMP_DIR"
}

cleanup_eval_state_files() {
    local removed_files=()
    local state_file

    for state_file in \
        "$SCRIPT_DIR/.eval_progress.json" \
        "$SCRIPT_DIR/.eval_spec.json" \
        "$SCRIPT_DIR/.eval_spec_state.json" \
        "$SCRIPT_DIR/.spec_state.json"
    do
        if [ -f "$state_file" ]; then
            rm -f "$state_file"
            removed_files+=("$(basename "$state_file")")
        fi
    done

    if [ ${#removed_files[@]} -gt 0 ]; then
        echo ""
        echo -e "${GREEN}已清理评测状态文件: ${removed_files[*]}${NC}"
    fi
}

trap cleanup EXIT

AGGREGATED_HAS_ANSWERS=0
ANSWER_SOURCE_LABEL=""
declare -a CONSUMED_FILES=()

aggregate_from_dir() {
    local source_dir="$1"

    AGGREGATED_HAS_ANSWERS=0
    CONSUMED_FILES=()

    > "$AGGREGATED_QUESTIONS"
    > "$AGGREGATED_KEY"
    > "$AGGREGATED_LLM"

    for q_file in "$QUESTIONS_DIR"/questions_*.md; do
        if [ ! -f "$q_file" ]; then continue; fi

        local filename id key_file llm_file short_id legacy_llm_file
        filename=$(basename "$q_file")
        id=${filename#questions_}
        id=${id%.md}

        key_file="$ANSWER_KEY_DIR/answer_key_$id.md"
        llm_file="$source_dir/llm_answer_$id.txt"
        short_id=${id%%_*}
        legacy_llm_file="$source_dir/llm_answer_$short_id.txt"

        cat "$q_file" >> "$AGGREGATED_QUESTIONS"

        if [ -f "$key_file" ]; then
            cat "$key_file" >> "$AGGREGATED_KEY"
        fi

        if [ -f "$llm_file" ]; then
            cat "$llm_file" >> "$AGGREGATED_LLM"
            AGGREGATED_HAS_ANSWERS=1
            CONSUMED_FILES+=("$llm_file")
        elif [ -f "$legacy_llm_file" ]; then
            cat "$legacy_llm_file" >> "$AGGREGATED_LLM"
            AGGREGATED_HAS_ANSWERS=1
            CONSUMED_FILES+=("$legacy_llm_file")
        fi
    done
}

show_last_score_and_exit() {
    if [ -f "$LATEST_REPORT" ]; then
        echo -e "${YELLOW}未检测到新的答案文件，默认不会重复读取已归档答案。${NC}"
        echo -e "${CYAN}以下为上次得分:${NC}"
        echo ""
        cat "$LATEST_REPORT"
        exit 0
    fi

    echo -e "${RED}错误: 在 $ANSWERS_DIR 目录下未检测到任何有效的答题文件 (llm_answer_*.txt)${NC}"
    echo -e "${YELLOW}推荐命名: llm_answer_01_core.txt；兼容旧命名: llm_answer_01.txt${NC}"
    exit 1
}

aggregate_from_dir "$ANSWERS_DIR"
ANSWER_SOURCE_LABEL="$ANSWERS_DIR"

if [ "$AGGREGATED_HAS_ANSWERS" -eq 0 ]; then
    if [ "$REUSE_LAST_ANSWERS" -eq 1 ]; then
        LATEST_ARCHIVE_DIR=$(find "$ARCHIVED_ANSWERS_DIR" -mindepth 1 -maxdepth 1 -type d | sort | tail -n 1)
        if [ -n "${LATEST_ARCHIVE_DIR:-}" ]; then
            aggregate_from_dir "$LATEST_ARCHIVE_DIR"
            ANSWER_SOURCE_LABEL="$LATEST_ARCHIVE_DIR"
        fi
    fi
fi

if [ "$AGGREGATED_HAS_ANSWERS" -eq 0 ]; then
    show_last_score_and_exit
fi

TOTAL_ANSWERS=$(grep -cEi '^Q[0-9]+\.\s*[A-D]' "$AGGREGATED_LLM" 2>/dev/null || echo 0)
TOTAL_KEY=$(grep -cE '^\*\*Q[0-9]+\.\*\*\s*[A-D]' "$AGGREGATED_KEY" 2>/dev/null || echo 0)
RUN_TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
CURRENT_REPORT="$REPORTS_DIR/score_${RUN_TIMESTAMP}.txt"

if [ "$TOTAL_ANSWERS" -eq 0 ]; then
    echo -e "${RED}错误: 未检测到有效答案${NC}"
    echo -e "${YELLOW}期望格式: Q001. A  或  Q001. A | 分析内容${NC}"
    exit 1
fi

{
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${CYAN}  Unity3D LLM 评测 - 批量自动评分${NC}"
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "  总题数:      $TOTAL_KEY 题"
    echo -e "  LLM 答题总数: $TOTAL_ANSWERS 题"
    echo -e "  本次答案来源: $ANSWER_SOURCE_LABEL"
    echo ""

    if [ "$TOTAL_ANSWERS" -lt "$TOTAL_KEY" ]; then
        MISSING=$((TOTAL_KEY - TOTAL_ANSWERS))
        echo -e "${YELLOW}警告: LLM 答题总数 ($TOTAL_ANSWERS) 少于总题数 ($TOTAL_KEY)，缺少 $MISSING 题${NC}"
        echo ""
    fi

    echo -e "${GREEN}开始综合评分...${NC}"
    echo ""

    python3 "$SCORE_SCRIPT" \
        --answer "$AGGREGATED_KEY" \
        --llm "$AGGREGATED_LLM" \
        --questions "$AGGREGATED_QUESTIONS" \
        --detail

    echo ""
    echo -e "${GREEN}全部批次评分完成。${NC}"
} | tee "$CURRENT_REPORT"

cp "$CURRENT_REPORT" "$LATEST_REPORT"

cleanup_eval_state_files

if [ "$ANSWER_SOURCE_LABEL" = "$ANSWERS_DIR" ]; then
    ARCHIVE_RUN_DIR="$ARCHIVED_ANSWERS_DIR/$RUN_TIMESTAMP"
    mkdir -p "$ARCHIVE_RUN_DIR"
    for answer_file in "${CONSUMED_FILES[@]}"; do
        mv "$answer_file" "$ARCHIVE_RUN_DIR/"
    done

    echo ""
    echo -e "${GREEN}本次答案已归档到 $ARCHIVE_RUN_DIR${NC}"
    echo -e "${YELLOW}后续若未显式指定 --reuse-last-answers，将不会重复读取这些已归档答案。${NC}"
else
    echo ""
    echo -e "${YELLOW}本次使用的是已归档答案，未移动任何文件。${NC}"
fi
