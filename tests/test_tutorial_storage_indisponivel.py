"""EVO-USO-01 / TUT-STORAGE: ensaio de navegador independente.

Executar com SIRE_TEST_URL apontando para servidor LOCAL com dados sintéticos:
  SIRE_TEST_URL=http://127.0.0.1:8000 python -m unittest tests.test_tutorial_storage_indisponivel -v
Requer playwright e Chromium instalados. Não executa reservas nem autenticação.
"""
import os
import unittest


@unittest.skipUnless(os.environ.get("SIRE_TEST_URL"), "Defina SIRE_TEST_URL para ambiente isolado")
class TutorialSemStorageTest(unittest.TestCase):
    def test_guia_funciona_quando_local_storage_falha(self):
        from playwright.sync_api import sync_playwright

        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            try:
                page = browser.new_page(viewport={"width": 375, "height": 812})
                page.add_init_script("""
                    Object.defineProperty(window, 'localStorage', {
                      configurable: true,
                      get() { throw new DOMException('Bloqueado para ensaio', 'SecurityError'); }
                    });
                """)
                page.goto(os.environ["SIRE_TEST_URL"], wait_until="domcontentloaded")
                help_button = page.get_by_role("button", name="Como usar")
                self.assertTrue(help_button.is_visible())
                help_button.click()
                dialog = page.get_by_role("dialog", name="Tutorial de uso do SIRE")
                self.assertTrue(dialog.is_visible())
                self.assertIn("Etapa 1", dialog.inner_text())
                page.keyboard.press("Escape")
                self.assertFalse(dialog.is_visible())
                self.assertTrue(help_button.is_visible())
            finally:
                browser.close()


if __name__ == "__main__":
    unittest.main()
