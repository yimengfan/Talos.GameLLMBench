#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

ANSWER_KEY="answer_key.md"
QUESTIONS="questions.md"
LLM_ANSWER="llm_answer.txt"
SCORE_SCRIPT="score_answers.py"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

if [ ! -f "$SCORE_SCRIPT" ]; then
    echo -e "${RED}错误: 评分脚本 $SCORE_SCRIPT 不存在${NC}"
    exit 1
fi

if [ ! -f "$ANSWER_KEY" ]; then
    echo -e "${RED}错误: 答案密钥 $ANSWER_KEY 不存在${NC}"
    exit 1
fi

if [ ! -f "$QUESTIONS" ]; then
    echo -e "${RED}错误: 题库文件 $QUESTIONS 不存在${NC}"
    exit 1
fi

if [ ! -f "$LLM_ANSWER" ]; then
    echo -e "${RED}错误: LLM 答题文件 $LLM_ANSWER 不存在${NC}"
    echo -e "${YELLOW}提示: 请先将 LLM 的答题结果保存为 $LLM_ANSWER${NC}"
    echo -e "${YELLOW}格式: 每行一题，如 Q001. A${NC}"
    exit 1
fi

TOTAL_ANSWERS=$(grep -cE '^Q[0-9]+\.\s*[A-D]' "$LLM_ANSWER" 2>/dev/null || echo 0)
TOTAL_KEY=$(grep -cE '^\*\*Q[0-9]+\.\*\*\s*[A-D]' "$ANSWER_KEY" 2>/dev/null || echo 0)

echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${CYAN}  Unity3D LLM 评测 - 自动评分${NC}"
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "  答案密钥:   $ANSWER_KEY ($TOTAL_KEY 题)"
echo -e "  LLM 答题:  $LLM_ANSWER ($TOTAL_ANSWERS 题)"
echo -e "  题库文件:   $QUESTIONS"
echo ""

if [ "$TOTAL_ANSWERS" -eq 0 ]; then
    echo -e "${RED}错误: $LLM_ANSWER 中未检测到有效答案${NC}"
    echo -e "${YELLOW}期望格式: Q001. A ｜ 分析内容${NC}"
    exit 1
fi

if [ "$TOTAL_ANSWERS" -lt "$TOTAL_KEY" ]; then
    MISSING=$((TOTAL_KEY - TOTAL_ANSWERS))
    echo -e "${YELLOW}警告: LLM 答题数 ($TOTAL_ANSWERS) 少于总题数 ($TOTAL_KEY)，缺少 $MISSING 题${NC}"
    echo ""
fi

echo -e "${GREEN}开始评分...${NC}"
echo ""

python3 "$SCORE_SCRIPT" \
    --answer "$ANSWER_KEY" \
    --llm "$LLM_ANSWER" \
    --questions "$QUESTIONS" \
    --detail

echo ""
echo -e "${GREEN}评分完成。${NC}"
