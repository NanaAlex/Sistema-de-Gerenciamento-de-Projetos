from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# Fluxo Positivo
driver.get("https://practicetestautomation.com/practice-test-login/")

driver.find_element(By.ID, "username").send_keys("student")
driver.find_element(By.ID, "password").send_keys("Password123")
driver.find_element(By.ID, "submit").click()

# Verifica se login foi bem sucedido
sucesso = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.TAG_NAME, "h1"))
)
assert "Logged In Successfully" in sucesso.text
print("Login válido funcionou no Practice Test Automation")

# Faz logout
logout_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Log out"))
)
logout_btn.click()
print("Logout funcionou no Practice Test Automation")

# Fluxo negativo
driver.get("https://practicetestautomation.com/practice-test-login/")

driver.find_element(By.ID, "username").send_keys("usuario_errado")
driver.find_element(By.ID, "password").send_keys("senha_errada")
driver.find_element(By.ID, "submit").click()

# Espera mensagem de erro
erro = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "error"))
)
print("Mensagem de erro capturada:", erro.text)

driver.quit()
