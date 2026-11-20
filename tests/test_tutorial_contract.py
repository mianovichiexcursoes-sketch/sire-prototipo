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

    def test_mobile_layout_has_bounded_panel_and_touch_targets(self):
        # Static guard only: does not prove visibility at 320px or 375x812.
        self.assertIn("@media(max-width:500px)", self.script)
        self.assertIn("width:calc(100vw - 1rem)", self.script)
        self.assertIn("max-height:min(45dvh,22rem)", self.script)
        self.assertIn("overflow:auto", self.script)
        self.assertIn("min-height:44px", self.script)

    def test_tutorial_does_not_claim_modal_or_trigger_navigation(self):
        self.assertIn("panel.setAttribute('aria-modal', 'false')", self.script)
        self.assertIn("help.setAttribute('aria-haspopup', 'dialog')", self.script)
        self.assertNotIn("window.location =", self.script)
        self.assertNotIn("location.href =", self.script)
        self.assertNotIn(".click()", self.script)


if __name__ == "__main__":
    unittest.main()
