from __future__ import annotations

from pathlib import Path
import sys
import unittest

TOOL_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOL_DIR))
import rule_discovery as rd  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[3]


class HumanReviewCapabilityTests(unittest.TestCase):
    def read(self, relative: str) -> str:
        return (REPO_ROOT / relative).read_text(encoding="utf-8")

    def test_human_review_architecture_is_canonical_and_consumer_bounded(self):
        path = REPO_ROOT / "docs/architecture/human-review-architecture.md"
        self.assertTrue(path.is_file())
        parsed = rd.parse_front_matter_file(path)
        self.assertEqual("architecture:human-review", parsed.metadata.get("id"))
        self.assertEqual("architecture", parsed.metadata.get("type"))
        self.assertEqual("active", parsed.metadata.get("status"))

        text = path.read_text(encoding="utf-8")
        self.assertIn("本架构定义普通 Consumer 软件项目中", text)
        self.assertIn("不用于规范 `agentic-dev` 自身", text)
        self.assertIn("结构化 Markdown 评审草稿", text)
        self.assertIn("delivery_target = none", text)
        self.assertIn("不得因为需要端到端理解就建立新的持久业务模型层", text)
        self.assertIn("人工评审与 `skill:review-change` 不是同一责任", text)

    def test_human_review_skill_contract_and_navigation(self):
        path = REPO_ROOT / "skills/human-review/SKILL.md"
        self.assertTrue(path.is_file())
        parsed = rd.parse_front_matter_file(path)
        self.assertEqual("human-review", parsed.metadata.get("name"))
        self.assertEqual("skill:human-review", parsed.metadata["metadata"].get("agentic-dev-id"))
        self.assertEqual("skill", parsed.metadata["metadata"].get("agentic-dev-type"))
        self.assertEqual("active", parsed.metadata["metadata"].get("agentic-dev-status"))

        text = path.read_text(encoding="utf-8")
        for heading in ["## 触发条件", "## 输入", "## 流程", "## 输出", "## 退出条件", "## 升级"]:
            self.assertIn(heading, text)
        self.assertIn("delivery_target = none", text)
        self.assertIn("不建立持久 BPMN、UML 或业务模型中间层", text)
        self.assertIn("当前请求实际是独立仓库变更复核", text)

        skills_readme = self.read("skills/README.md")
        architecture_readme = self.read("docs/architecture/README.md")
        self.assertIn("`human-review`", skills_readme)
        self.assertIn("human-review-architecture.md", architecture_readme)

    def test_methods_integrate_human_review_without_new_stage(self):
        requirement = self.read("docs/methods/requirement-baseline-establishment.md")
        ai_development = self.read("docs/methods/ai-development.md")
        architecture = self.read("docs/methods/architecture-clarification.md")

        for text in [requirement, ai_development, architecture]:
            self.assertIn("architecture:human-review", text)
            self.assertIn("skill:human-review", text)

        self.assertIn("Consumer 未采用 `skill:human-review` 时", requirement)
        self.assertIn("不要求固定人工审批", ai_development)
        self.assertIn("不因为存在人工评审能力而自动升级", architecture)

        self.assertNotIn("Human Review →", ai_development)
        self.assertNotIn("Human Review →", architecture)

    def test_authority_writeback_is_required_for_review_completion(self):
        architecture = self.read("docs/architecture/human-review-architecture.md")
        skill = self.read("skills/human-review/SKILL.md")
        eval_text = self.read("evals/behavior/human-review.json")

        self.assertIn("待权威回写 / 未完成", architecture)
        self.assertIn("不得把“已经列出待执行回写动作”解释为“评审完成”", architecture)
        self.assertIn("重新读取并确认真实 owner 已持久化该决定", architecture)
        self.assertIn("待权威回写 / 评审未完成", skill)
        self.assertIn("缺少写权限时允许当前执行返回，但不得声称人工评审已经完成", skill)
        self.assertIn("后续执行必须先完成并重新读取验证权威回写", skill)

        self.assertIn('"id": "B-HR-04"', eval_text)
        self.assertIn("明确本次人工评审当前是否已经完成", eval_text)
        self.assertIn("待权威回写 / 评审未完成", eval_text)
        self.assertIn("不把列出待执行回写动作等同于人工评审完成", eval_text)
        self.assertIn("实际回写并重新读取验证 Architecture 后才可判定评审完成", eval_text)

    def test_explicit_delivery_contract_is_bounded(self):
        architecture = self.read("docs/architecture/human-review-architecture.md")
        skill = self.read("skills/human-review/SKILL.md")

        self.assertIn("`delivery_target = html`", architecture)
        self.assertIn("`delivery_target = docx`", architecture)
        self.assertIn("静态、轻量、无需后端服务", architecture)
        self.assertIn("客户、合同、法规明确提供的正式模板或格式要求", architecture)
        for font_key in ["`eastAsia`", "`ascii`", "`hAnsi`", "`cs`"]:
            self.assertIn(font_key, architecture)
        self.assertIn("WPS / Word", architecture)
        self.assertIn("无法实际生成或验证目标文件时", architecture)

        self.assertIn("生成 HTML 交互评审视图", skill)
        self.assertIn("生成 DOCX 正式文档", skill)
        self.assertIn("只有真实生成并实际完成相应验证后", skill)
        self.assertIn("不为每种格式建立独立 Skill", skill)
        self.assertIn("正式 DOCX 只能使用已经实际回写并重新读取确认的收敛内容", skill)

    def test_behavior_eval_exists_and_covers_discriminating_cases(self):
        eval_path = REPO_ROOT / "evals/behavior/human-review.json"
        self.assertTrue(eval_path.is_file())
        text = eval_path.read_text(encoding="utf-8")
        for case_id in [
            "B-HR-01",
            "B-HR-02",
            "B-HR-03",
            "B-HR-04",
            "B-HR-05",
            "B-HR-06",
            "B-HR-07",
            "B-HR-08",
        ]:
            self.assertIn(case_id, text)
        self.assertIn("结构化 Markdown", text)
        self.assertIn("review-change", text)
        self.assertIn("不建立持久 BPMN", text)
        self.assertIn("delivery_target = html", text)
        self.assertIn("delivery_target = docx", text)
        self.assertIn("eastAsia", text)
        self.assertIn("WPS / Word", text)
        self.assertIn("待权威回写 / 评审未完成", text)


if __name__ == "__main__":
    unittest.main()
