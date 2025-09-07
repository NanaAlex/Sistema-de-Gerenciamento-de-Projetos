from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # abre navegador visível
    page = browser.new_page()

    # Fluxo Positivo
    print("Acessando SauceDemo...")
    page.goto("https://www.saucedemo.com")

    page.fill("input[data-test='username']", "standard_user")
    page.fill("input[data-test='password']", "secret_sauce")
    page.click("input[data-test='login-button']")

    assert "inventory" in page.url
    print("Login válido funcionou no SauceDemo")

    # Logout
    page.click("#react-burger-menu-btn")
    page.click("#logout_sidebar_link")
    print("Logout funcionou no SauceDemo")

    # Fluxo negativo
    page.fill("input[data-test='username']", "usuario_errado")
    page.fill("input[data-test='password']", "senha_errada")
    page.click("input[data-test='login-button']")

    erro = page.inner_text("h3[data-test='error']")
    print("Mensagem de erro capturada:", erro)

    browser.close()
