import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

from score_answers import validate_analysis


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = REPO_ROOT / "score_answers.py"


class ValidateAnalysisTests(unittest.TestCase):
    def test_scene_design_accepts_constraint_based_analysis_when_keywords_are_sparse(self):
        question_info = {
            "qtype": "场景设计",
            "keywords": set(),
        }

        analysis = (
            "方案要先做架构分层和初始化流程约束，再拆分公共资源分包，"
            "同时保留回滚机制与性能预算，才能保证上线稳定。"
        )

        is_valid, reason = validate_analysis(question_info, analysis)

        self.assertTrue(is_valid)
        self.assertEqual(reason, "")

    def test_scene_design_rejects_generic_filler_analysis(self):
        question_info = {
            "qtype": "场景设计",
            "keywords": set(),
        }

        analysis = "这个方案更合理，性能更好，工程上也更稳妥，所以应该优先选择。"

        is_valid, reason = validate_analysis(question_info, analysis)

        self.assertFalse(is_valid)
        self.assertEqual(reason, "分析未体现方案关键约束")

    def test_code_question_still_requires_api_or_code_anchor(self):
        question_info = {
            "qtype": "代码阅读",
            "keywords": {"getcomponent", "rigidbody"},
        }

        analysis = "这里会因为 GetComponent 没拿到 Rigidbody 而得到 null，后续访问会触发空引用。"

        is_valid, reason = validate_analysis(question_info, analysis)

        self.assertTrue(is_valid)
        self.assertEqual(reason, "")

    def test_code_question_rejects_analysis_without_technical_anchor(self):
        question_info = {
            "qtype": "代码阅读",
            "keywords": {"getcomponent", "rigidbody"},
        }

        analysis = "这个写法看起来不太稳，运行时大概率会出问题，所以不能选。"

        is_valid, reason = validate_analysis(question_info, analysis)

        self.assertFalse(is_valid)
        self.assertEqual(reason, "分析未引用关键API/代码点")


class ScoreAnswersCliTests(unittest.TestCase):
    def _write_fixture_files(self, tmpdir: str):
        tmp_path = Path(tmpdir)

        questions = tmp_path / "questions.md"
        answers = tmp_path / "answer.md"
        llm_good = tmp_path / "llm_good.txt"
        llm_bad = tmp_path / "llm_bad.txt"

        questions.write_text(
            textwrap.dedent(
                """
                **Q001.** [模块:A][维度:概念理解][难度:★★★][题型:场景设计]

                设计一个商业项目客户端启动链路时，更稳妥的方案是？

                - A. 框架初始化→基础配置加载→登录/更新检查→必要资源预热→进入主界面
                - B. 直接进入主界面，其他步骤全部后台补做
                - C. 先全量资源加载，再考虑配置和版本检查
                - D. 完全不需要流程约束，只要最终能进入游戏即可
                """
            ).strip()
            + "\n",
            encoding="utf-8",
        )
        answers.write_text("**Q001.** A\n", encoding="utf-8")
        llm_good.write_text(
            "Q001. A | 需要先完成架构分层下的初始化流程，再做版本检查和资源预热，并保留性能预算与回滚机制。\n",
            encoding="utf-8",
        )
        llm_bad.write_text(
            "Q001. A | 这个方案更合理，性能更好，而且整体上会更稳妥。\n",
            encoding="utf-8",
        )

        return questions, answers, llm_good, llm_bad

    def _run_cli(self, *args: str) -> subprocess.CompletedProcess:
        return subprocess.run(
            [sys.executable, str(SCRIPT_PATH), *args],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

    def test_cli_default_mode_accepts_grounded_analysis(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            questions, answers, llm_good, _ = self._write_fixture_files(tmpdir)

            result = self._run_cli(
                "--answer",
                str(answers),
                "--llm",
                str(llm_good),
                "--questions",
                str(questions),
            )

        self.assertEqual(result.returncode, 0, msg=result.stderr)
        self.assertIn("综合基准分: 1/1", result.stdout)
        self.assertIn("客观选项得分: 1/1", result.stdout)

    def test_cli_choice_only_mode_ignores_low_quality_analysis(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            questions, answers, _, llm_bad = self._write_fixture_files(tmpdir)

            default_result = self._run_cli(
                "--answer",
                str(answers),
                "--llm",
                str(llm_bad),
                "--questions",
                str(questions),
            )
            choice_only_result = self._run_cli(
                "--answer",
                str(answers),
                "--llm",
                str(llm_bad),
                "--questions",
                str(questions),
                "--choice-only",
            )

        self.assertEqual(default_result.returncode, 0, msg=default_result.stderr)
        self.assertIn("综合基准分: 0/1", default_result.stdout)
        self.assertIn("客观选项得分: 1/1", default_result.stdout)

        self.assertEqual(choice_only_result.returncode, 0, msg=choice_only_result.stderr)
        self.assertIn("综合基准分: 1/1", choice_only_result.stdout)
        self.assertIn("客观选项得分: 1/1", choice_only_result.stdout)


if __name__ == "__main__":
    unittest.main()