from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    # Fluxo Positivo
    print("🔹 Acessando site OrangeHRM...")
    driver.get("https://opensource-demo.orangehrmlive.com/")

    print("🔹 Tentando login válido...")
    usuario = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    usuario.send_keys("Admin")

    senha = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    senha.send_keys("admin123")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Verifica se carregou o dashboard
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h6"))
    )
    print("Login válido funcionou no OrangeHRM")

    # Fluxo negativo
    print("Tentando logout...")
    menu_user = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "oxd-userdropdown-tab"))
    )
    menu_user.click()

    logout_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Logout']"))
    )
    logout_btn.click()
    print("Logout funcionou no OrangeHRM")

    # ===== FLUXO NEGATIVO =====
    print("🔹 Tentando login inválido...")
    usuario = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    usuario.send_keys("usuario_errado")

    senha = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    senha.send_keys("senha_errada")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Captura mensagem de erro
    erro = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "oxd-alert-content-text"))
    )
    print("Mensagem de erro capturada:", erro.text)

except Exception as e:
    print("Ocorreu um erro:", str(e))

finally:
    driver.quit()
