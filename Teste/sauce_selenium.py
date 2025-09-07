from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

# Fluxo Positivo
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Verifica se logou
assert "inventory" in driver.current_url
print("Login válido funcionou no SauceDemo")

# Faz logout
driver.find_element(By.ID, "react-burger-menu-btn").click()
time.sleep(1)
driver.find_element(By.ID, "logout_sidebar_link").click()
print("Logout funcionou no SauceDemo")

# Fluxo negativo
driver.get("https://www.saucedemo.com/")  # volta para tela de login

# Espera e preenche usuário inválido
usuario = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "user-name"))
)
usuario.clear()
usuario.send_keys("usuario_errado")

# Espera e preenche senha inválida
senha = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "password"))
)
senha.clear()
senha.send_keys("senha_errada")

# Clica no botão de login
login_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "login-button"))
)
login_btn.click()

# Agora espera a mensagem de erro ficar visível
erro_elemento = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))
)

print("Mensagem de erro capturada:", erro_elemento.text)