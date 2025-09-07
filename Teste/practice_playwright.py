from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # abre navegador visível
    page = browser.new_page()

     # Fluxo Positivo
    print("Acessando Practice Test Automation...")
    page.goto("https://practicetestautomation.com/practice-test-login/")

    page.fill("#username", "student")
    page.fill("#password", "Password123")
    page.click("#submit")

    assert "Logged In Successfully" in page.inner_text("h1")
    print("Login válido funcionou no Practice Test Automation")

    # Logout
    page.click("text=Log out")
    print("Logout funcionou no Practice Test Automation")

    # Fluxo negativo
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.fill("#username", "usuario_errado")
    page.fill("#password", "senha_errada")
    page.click("#submit")

    erro = page.inner_text("#error")
    print("Mensagem de erro capturada:", erro)

    browser.close()
