#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

SCORE_SCRIPT="score_answers.py"
QUESTIONS_DIR="questions"
ANSWER_KEY_DIR="answer_key"
ANSWERS_DIR="answers"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

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

# Create a temporary file to aggregate all answers and keys
TEMP_DIR=$(mktemp -d)
AGGREGATED_QUESTIONS="$TEMP_DIR/all_questions.md"
AGGREGATED_KEY="$TEMP_DIR/all_keys.md"
AGGREGATED_LLM="$TEMP_DIR/all_llm_answers.txt"

# Clear temporary files if they exist
> "$AGGREGATED_QUESTIONS"
> "$AGGREGATED_KEY"
> "$AGGREGATED_LLM"

# Process all files
has_answers=0

for q_file in "$QUESTIONS_DIR"/questions_*.md; do
    if [ ! -f "$q_file" ]; then continue; fi
    
    # Extract the identifier (e.g., 01_core)
    filename=$(basename "$q_file")
    id=${filename#questions_}
    id=${id%.md}
    
    key_file="$ANSWER_KEY_DIR/answer_key_$id.md"
    llm_file="$ANSWERS_DIR/llm_answer_$id.txt"
    short_id=${id%%_*}
    legacy_llm_file="$ANSWERS_DIR/llm_answer_$short_id.txt"
    
    cat "$q_file" >> "$AGGREGATED_QUESTIONS"
    
    if [ -f "$key_file" ]; then
        cat "$key_file" >> "$AGGREGATED_KEY"
    fi
    
    if [ -f "$llm_file" ]; then
        cat "$llm_file" >> "$AGGREGATED_LLM"
        has_answers=1
    elif [ -f "$legacy_llm_file" ]; then
        cat "$legacy_llm_file" >> "$AGGREGATED_LLM"
        has_answers=1
    fi
done

if [ "$has_answers" -eq 0 ]; then
    echo -e "${RED}错误: 在 $ANSWERS_DIR 目录下未检测到任何有效的答题文件 (llm_answer_*.txt)${NC}"
    echo -e "${YELLOW}推荐命名: llm_answer_01_core.txt；兼容旧命名: llm_answer_01.txt${NC}"
    rm -rf "$TEMP_DIR"
    exit 1
fi

TOTAL_ANSWERS=$(grep -cEi '^Q[0-9]+\.\s*[A-D]' "$AGGREGATED_LLM" 2>/dev/null || echo 0)
TOTAL_KEY=$(grep -cE '^\*\*Q[0-9]+\.\*\*\s*[A-D]' "$AGGREGATED_KEY" 2>/dev/null || echo 0)

echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${CYAN}  Unity3D LLM 评测 - 批量自动评分${NC}"
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "  总题数:      $TOTAL_KEY 题"
echo -e "  LLM 答题总数: $TOTAL_ANSWERS 题"
echo ""

if [ "$TOTAL_ANSWERS" -eq 0 ]; then
    echo -e "${RED}错误: 未检测到有效答案${NC}"
    echo -e "${YELLOW}期望格式: Q001. A  或  Q001. A | 分析内容${NC}"
    rm -rf "$TEMP_DIR"
    exit 1
fi

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

# Cleanup
rm -rf "$TEMP_DIR"

echo ""
echo -e "${GREEN}全部批次评分完成。${NC}"
