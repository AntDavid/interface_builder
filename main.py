from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from selenium.common.exceptions import WebDriverException, NoSuchElementException, TimeoutException

CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'  # Ajuste conforme seu ambiente

BASE_URL = "http://dpainel.desenvolve.com.br"
LOGIN_URL = f"{BASE_URL}/intra/login/"
HARDWARE_URL = f"{BASE_URL}/intra/dc/hardware/?nome=RS1866"


# Credenciais de login
# Atenção: Nunca compartilhe credenciais sensíveis em código público!
# As credenciais abaixo são fictícias e devem ser substituídas por valores reais.
USERNAME = "Pedro"
PASSWORD = "Cabral123"

def create_chrome_driver():
    service = Service(CHROMEDRIVER_PATH)
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    # options.add_argument("--headless=new")  # descomente para rodar oculto
    driver = webdriver.Chrome(service=service, options=options)
    driver.set_page_load_timeout(30)
    return driver

def login(driver):
    print("Realizando login...")
    driver.get(LOGIN_URL)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "form-signin")))

    driver.find_element(By.NAME, "user").clear()
    driver.find_element(By.NAME, "user").send_keys(USERNAME)
    time.sleep(0.5)

    driver.find_element(By.ID, "temp-pass").clear()
    driver.find_element(By.ID, "temp-pass").send_keys(PASSWORD)
    time.sleep(0.5)

    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/intra/logout/')]")))
    print("Login realizado com sucesso!")
    time.sleep(0.5)

def add_interface(driver, interface_name):
    print(f"\nAdicionando interface {interface_name}...")

    driver.get(HARDWARE_URL)
    time.sleep(0.5)  # aguarda carregar página

    # Clica no botão "Adicionar interface"
    add_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.add-button-interface"))
    )
    add_button.click()
    time.sleep(0.5)  # espera modal/form abrir

    # Espera o formulário ficar visível
    form = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "form.add.add-interface"))
    )

    # Preenche o campo Nome
    nome_input = driver.find_element(By.ID, "id_interface_nome")
    nome_input.clear()
    time.sleep(0.5)
    nome_input.send_keys(interface_name)
    time.sleep(0.5)

    # Preenche o campo MAC com mais tempo entre as ações
    mac_input = driver.find_element(By.ID, "id_interface_mac")
    mac_input.clear()
    time.sleep(1)  # Espera mais tempo após limpar
    
    # Digita o MAC lentamente
    mac_address = "00:00:00:00:00:00"
    for char in mac_address:
        mac_input.send_keys(char)
        time.sleep(0.3)  # 300ms entre cada caractere
    time.sleep(1)  # Espera adicional após terminar de digitar

    # Seleciona o tipo Ethernet "10 Gbit/s com cabo de cobre" (value="10GBASE-T")
    select_ethernet = Select(driver.find_element(By.ID, "id_ethernet_tipo"))
    select_ethernet.select_by_value("10GBASE-SR")
    time.sleep(0.5)

    # Clica no botão "Adicionar" (submit)
    submit_button = driver.find_element(By.CSS_SELECTOR, "form.add.add-interface button[type='submit']")
    submit_button.click()
    print("Botão Adicionar clicado. Aguardando resposta...")
    time.sleep(1)  # aguarda processamento do envio

    # Verifica feedback
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.success"))
        )
        print(f"✅ Interface {interface_name} adicionada com sucesso!")
        return True
    except TimeoutException:
        try:
            error_msg = driver.find_element(By.CSS_SELECTOR, "div.error").text
            print(f"❌ Erro ao adicionar interface {interface_name}: {error_msg}")
        except NoSuchElementException:
            print(f"⚠️ Sem confirmação de sucesso ou erro para interface {interface_name}.")
        return False

def main():
    driver = None
    try:
        if not os.path.exists(CHROMEDRIVER_PATH):
            raise FileNotFoundError(f"Chromedriver não encontrado em {CHROMEDRIVER_PATH}")

        driver = create_chrome_driver()
        login(driver)
       
        
        for i in range(48):
            interface_name = f"0/{i:02d}"
            success = add_interface(driver, interface_name)
            time.sleep(1)

    except Exception as e:
        print(f"Erro: {e}")
    finally:
        if driver:
            driver.quit()
            print("Navegador fechado.")

if __name__ == "__main__":
    main()