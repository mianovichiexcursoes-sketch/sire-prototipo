"""EVO-USO-01: ensaio adicional de viewports; requer servidor Django sintético em 8765.
Executar: python scripts/teste_tutorial_viewports.py
Não acessa produção, não submete formulários e não usa dados pessoais.
"""
import json
import os
from pathlib import Path
from playwright.sync_api import sync_playwright

BASE = os.environ.get("SIRE_TEST_BASE_URL", "http://127.0.0.1:8765")
OUT = Path(__file__).resolve().parents[1] / "evidencias/2026-11-23_tutorial_viewports"
OUT.mkdir(parents=True, exist_ok=True)
checks = []

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(
        headless=True,
        args=["--no-sandbox"],
        **({"executable_path": os.environ["SIRE_CHROMIUM_BINARY"]}
           if os.environ.get("SIRE_CHROMIUM_BINARY") else {}),
    )
    for width, height in [(320, 568), (375, 812)]:
        page = browser.new_page(viewport={"width": width, "height": height})
        posts = []
        page.on("request", lambda req: posts.append(req.url) if req.method == "POST" else None)
        page.goto(BASE, wait_until="domcontentloaded")
        page.get_by_role("button", name="Como usar", exact=True).click()
        dialog = page.get_by_role("dialog")
        assert dialog.is_visible(), f"{width}: diálogo ausente"
        assert page.locator(".sire-guia-alvo").count() == 1, f"{width}: alvo ausente"
        rect = dialog.bounding_box()
        assert rect is not None and rect["x"] >= 0 and rect["x"] + rect["width"] <= width + 1, f"{width}: painel fora da tela"
        page.screenshot(path=str(OUT / f"tutorial-{width}.png"), full_page=True)
        page.get_by_role("button", name="Fechar", exact=True).click()
        assert not dialog.is_visible(), f"{width}: Fechar não ocultou painel"
        assert page.get_by_role("button", name="Como usar").evaluate("(e) => e === document.activeElement"), f"{width}: foco não retornou"
        assert not posts, f"{width}: tutorial gerou POST inesperado"
        checks.append({"viewport": f"{width}x{height}", "dialogo": "ok", "fechar_foco": "ok", "post": 0})
        page.close()
    browser.close()
(OUT / "resultados.json").write_text(json.dumps(checks, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(checks, ensure_ascii=False))
