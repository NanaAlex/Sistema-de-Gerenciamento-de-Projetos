from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# Fluxo Positivo
driver.get("https://the-internet.herokuapp.com/login")

# Preenche usuário e senha corretos
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button.radius").click()

# Verifica se entrou na área segura
assert "secure" in driver.current_url
print("Login válido funcionou no Herokuapp")

# Faz logout
logout_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon-2x.icon-signout"))
)
logout_btn.click()
print("Logout funcionou no Herokuapp")

# Fluxo negativo
driver.get("https://the-internet.herokuapp.com/login")

driver.find_element(By.ID, "username").send_keys("usuario_errado")
driver.find_element(By.ID, "password").send_keys("senha_errada")
driver.find_element(By.CSS_SELECTOR, "button.radius").click()

# Espera mensagem de erro aparecer
erro_elemento = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "flash"))
)
print("Mensagem de erro capturada:", erro_elemento.text)

driver.quit()
