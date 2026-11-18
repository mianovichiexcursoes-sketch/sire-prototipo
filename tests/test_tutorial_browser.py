"""EVO-USO-01: testes de navegador isolados, somente dados sintéticos.

Executar a partir da raiz: python -m unittest discover -s tests -p 'test_tutorial_browser.py' -v
Requer playwright e navegador Chromium instalados. Não conecta ao Render/Drive.
"""
from pathlib import Path
import unittest

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "sire/static/sire/js/tutorial-uso.js"
HTML = """<!doctype html><html lang="pt-BR"><head></head>
<body data-sire-role="{role}"><header><nav><a href="#catalogo">Catálogo</a>
<a href="#reservas">Minhas reservas</a><a href="#agente">Excursões da agência</a></nav></header>
<main><h1>Catálogo</h1><button type="submit" form="reserva">Confirmar reserva de uma vaga</button>
<form id="reserva"><input name="synthetic" value="TESTE"></form></main></body></html>"""


class TutorialBrowserTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.chromium.launch(headless=True)

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.playwright.stop()

    def page_for(self, role="visitante", block_storage=False):
        context = self.browser.new_context()
        page = context.new_page()
        page.set_content(HTML.format(role=role))
        if block_storage:
            page.evaluate("""() => {
                Object.defineProperty(window, 'localStorage', {
                    configurable: true, get() { throw new DOMException('Denied', 'SecurityError'); }
                });
            }""")
        page.add_script_tag(path=str(SCRIPT))
        self.addCleanup(context.close)
        return page

    def test_tut01_offer_and_permanent_help(self):
        page = self.page_for()
        self.assertEqual(page.get_by_text("Quer conhecer o SIRE?").count(), 1)
        page.get_by_role("button", name="Agora não").click()
        self.assertEqual(page.get_by_role("button", name="Como usar").count(), 1)
        page.get_by_role("button", name="Como usar").click()
        self.assertTrue(page.get_by_role("dialog").is_visible())

    def test_tut02_passenger_no_signup_instruction(self):
        page = self.page_for("passageiro")
        page.get_by_role("button", name="Começar").click()
        dialog = page.get_by_role("dialog")
        titles = []
        for _ in range(5):
            titles.append(dialog.locator(".sire-guia-titulo").inner_text())
            dialog.get_by_role("button", name="Próximo").click() if _ < 4 else None
        self.assertNotIn("Criar conta", titles)
        self.assertIn("Minhas reservas", titles)

    def test_tut03_agent_only_agency_steps(self):
        page = self.page_for("agente")
        page.get_by_role("button", name="Começar").click()
        self.assertEqual(page.locator(".sire-guia-titulo").inner_text(), "Excursões da agência")

    def test_tut04_escape_returns_focus(self):
        page = self.page_for()
        page.get_by_role("button", name="Agora não").click()
        help_button = page.get_by_role("button", name="Como usar")
        help_button.click()
        page.keyboard.press("Escape")
        self.assertFalse(page.get_by_role("dialog").is_visible())
        self.assertTrue(help_button.evaluate("(el) => document.activeElement === el"))

    def test_tut05_storage_unavailable(self):
        page = self.page_for(block_storage=True)
        page.get_by_role("button", name="Começar").click()
        self.assertTrue(page.get_by_role("dialog").is_visible())
        page.get_by_role("button", name="Pular / Fechar").click()
        self.assertFalse(page.get_by_role("dialog").is_visible())

    def test_tut06_never_submits_form(self):
        page = self.page_for("passageiro")
        page.evaluate("""() => { window.__submitted = 0;
            document.querySelector('form').addEventListener('submit', e => {
                e.preventDefault(); window.__submitted += 1;
            }); }""")
        page.get_by_role("button", name="Começar").click()
        for _ in range(4):
            page.get_by_role("button", name="Próximo").click()
        page.get_by_role("button", name="Concluir").click()
        self.assertEqual(page.evaluate("window.__submitted"), 0)


if __name__ == "__main__":
    unittest.main()
