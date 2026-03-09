"""Auto-grading: Lab 8 deliverable structure."""
import pytest, json, os, ast

BASE = os.path.join(os.path.dirname(__file__), "..")


class TestCoreFiles:
    def test_notebook(self):
        assert os.path.exists(os.path.join(BASE, "lab8_ship_it.ipynb"))

    def test_devassist_cli(self):
        path = os.path.join(BASE, "devassist.py")
        assert os.path.exists(path)
        with open(path) as f:
            ast.parse(f.read())

    def test_test_suite(self):
        path = os.path.join(BASE, "evaluation", "test_suite.py")
        assert os.path.exists(path)
        with open(path) as f:
            ast.parse(f.read())

    def test_test_cases(self):
        path = os.path.join(BASE, "evaluation", "test_cases.json")
        with open(path) as f:
            cases = json.load(f)
        assert len(cases) >= 12, f"Only {len(cases)} test cases (need ≥12)"


class TestPromptVersioning:
    def test_v1_0(self):
        assert os.path.exists(os.path.join(BASE, "prompt_templates", "system_prompt_v1.0.md"))

    def test_v1_1(self):
        assert os.path.exists(os.path.join(BASE, "prompt_templates", "system_prompt_v1.1.md"))

    def test_changelog(self):
        path = os.path.join(BASE, "prompt_templates", "CHANGELOG.md")
        assert os.path.exists(path)
        with open(path) as f:
            content = f.read()
        assert "v1.1" in content and "v1.0" in content


class TestEvaluation:
    def test_evaluation_md(self):
        assert os.path.exists(os.path.join(BASE, "evaluation", "evaluation.md"))

    def test_rubric(self):
        assert os.path.exists(os.path.join(BASE, "evaluation", "rubric.md"))

    def test_results(self):
        assert os.path.exists(os.path.join(BASE, "evaluation", "results.md"))


class TestDocs:
    def test_final_report(self):
        assert os.path.exists(os.path.join(BASE, "docs", "final_report.md"))

    def test_risk_register(self):
        path = os.path.join(BASE, "docs", "risk_register.md")
        assert os.path.exists(path)
        with open(path) as f:
            content = f.read()
        # Should have at least 5 numbered risk rows
        import re
        rows = re.findall(r'\|\s*\d+\s*\|', content)
        assert len(rows) >= 5, f"Only {len(rows)} risk entries (need ≥5)"

    def test_usage_policy(self):
        path = os.path.join(BASE, "docs", "usage_policy.md")
        assert os.path.exists(path)
        with open(path) as f:
            content = f.read().lower()
        assert "intended use" in content
        assert "limitation" in content

    def test_demo_script(self):
        assert os.path.exists(os.path.join(BASE, "docs", "demo_script.md"))

    def test_portfolio_reflection(self):
        assert os.path.exists(os.path.join(BASE, "docs", "portfolio_reflection.md"))


class TestNotebook:
    def test_valid(self):
        with open(os.path.join(BASE, "lab8_ship_it.ipynb")) as f:
            nb = json.load(f)
        assert len(nb["cells"]) >= 15

    def test_executed(self):
        with open(os.path.join(BASE, "lab8_ship_it.ipynb")) as f:
            nb = json.load(f)
        n = sum(1 for c in nb["cells"] if c.get("cell_type") == "code" and c.get("outputs"))
        assert n >= 5, f"Only {n} cells executed"


class TestSecurityUtils:
    def test_imports(self):
        import sys
        sys.path.insert(0, BASE)
        from utils.security_utils import sanitize_input, validate_output
        assert sanitize_input("hello")["blocked"] is False
        assert validate_output("Normal response.")["passed"] is True
