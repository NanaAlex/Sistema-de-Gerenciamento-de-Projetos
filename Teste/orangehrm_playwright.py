from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # abre navegador visível
    page = browser.new_page()

    # Fluxo Positivo
    print("Acessando OrangeHRM...")
    page.goto("https://opensource-demo.orangehrmlive.com/")

    page.fill("input[name='username']", "Admin")
    page.fill("input[name='password']", "admin123")
    page.click("button[type='submit']")

    # Verifica se dashboard abriu
    page.wait_for_selector("h6")
    print("Login válido funcionou no OrangeHRM")

    # Logout
    page.click(".oxd-userdropdown-tab")
    page.click("text=Logout")
    print("Logout funcionou no OrangeHRM")

    # Fluxo negativo
    page.fill("input[name='username']", "usuario_errado")
    page.fill("input[name='password']", "senha_errada")
    page.click("button[type='submit']")

    erro = page.inner_text(".oxd-alert-content-text")
    print("Mensagem de erro capturada:", erro)

    browser.close()
