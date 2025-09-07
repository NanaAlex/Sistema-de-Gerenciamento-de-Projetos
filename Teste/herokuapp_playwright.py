from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # abre navegador visível
    page = browser.new_page()

    # Fluxo Positivo
    print("Acessando Herokuapp...")
    page.goto("https://the-internet.herokuapp.com/login")

    page.fill("#username", "tomsmith")
    page.fill("#password", "SuperSecretPassword!")
    page.click("button.radius")

    assert "secure" in page.url
    print("Login válido funcionou no Herokuapp")

    # Logout
    page.click(".icon-2x.icon-signout")
    print("Logout funcionou no Herokuapp")

    # Fluxo negativo
    page.goto("https://the-internet.herokuapp.com/login")  # volta pra tela de login
    page.fill("#username", "usuario_errado")
    page.fill("#password", "senha_errada")
    page.click("button.radius")

    erro = page.inner_text("#flash")
    print("Mensagem de erro capturada:", erro)

    browser.close()
