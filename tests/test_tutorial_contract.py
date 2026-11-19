"""Static safety contract for EVO-USO-01; NOT a browser/usability test.

Run: python -m unittest discover -s tests -p 'test_tutorial_contract.py'
This only checks the source file, not Django, CSS rendering or actual interactions.
"""
from pathlib import Path
import unittest

SOURCE = Path(__file__).resolve().parents[1] / "sire/static/sire/js/tutorial-uso.js"


class TutorialContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.script = SOURCE.read_text(encoding="utf-8")

    def test_controls_are_explicitly_non_submit(self):
        self.assertIn("help.type = 'button'", self.script)
        for action in ("anterior", "proximo", "pular", "fechar"):
            self.assertIn('type="button"', self.script)
            self.assertIn(f'data-action="{action}"', self.script)
        self.assertNotIn(".submit(", self.script)
        self.assertNotIn(".requestSubmit(", self.script)

    def test_role_specific_steps(self):
        for role in ("visitante", "passageiro", "agente"):
            self.assertIn(f"role === '{role}'", self.script)
        self.assertIn("document.body.dataset.sireRole", self.script)

    def test_keyboard_and_missing_target_handling(self):
        self.assertIn("event.key !== 'Escape'", self.script)
        self.assertIn("if (visible(el)) steps.push", self.script)
        self.assertIn("if (!steps.length)", self.script)
        self.assertIn("heading.focus(", self.script)

    def test_storage_errors_are_caught_and_key_is_versioned(self):
        self.assertIn("sire-tutorial-v2-", self.script)
        self.assertIn("catch (_) { return null; }", self.script)
        self.assertIn("catch (_) {}", self.script)

    def test_no_personal_data_is_written_by_literal_storage_calls(self):
        for value in ("'seen'", "'yes'", "'no'"):
            self.assertIn(value, self.script)
        self.assertNotIn("localStorage.setItem('cpf'", self.script)


if __name__ == "__main__":
    unittest.main()
