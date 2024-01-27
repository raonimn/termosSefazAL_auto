import sys
import time
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from config import username, password, url_login, url_pagina_apos_login, termo_apreensao


# Configuração do navegador
driver_path = 'chromedriver.exe'

# Opções do Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-extensions')
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')

# Criação do driver do Chrome
chrome_service = webdriver.chrome.service.Service(driver_path)
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Abre o site
driver.get(url_login)

# Aguarda até que o campo de usuário esteja disponível
campo_usuario = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, 'username'))
)

# Insere o login e a senha
campo_usuario.send_keys(username)
campo_senha = driver.find_element(By.NAME, 'password')
campo_senha.send_keys(password)

# Clica no botão de login
campo_senha.send_keys(Keys.RETURN)

# Aguarda a página carregar após o login
# Você pode usar WebDriverWait para esperar por elementos específicos, se necessário

# Navega até a página após o login
driver.get(url_pagina_apos_login)

# Aguarda até que o campo numTade esteja disponível
campo_num_tade = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'numTade'))
)

# Insere a string no campo numTade
campo_num_tade.send_keys(termo_apreensao)

# Atraso de 2 segundos
time.sleep(2)

# Localiza o botão "Consultar" usando o seletor CSS fornecido pelo Selenium IDE
botao_consultar = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-info > span > span'))
)

# Clica no botão "Consultar"
try:
    botao_consultar.click()
except ElementClickInterceptedException:
    print('Erro: O clique no botão "Consultar" foi interceptado. Possível elemento sobreposto.')
    driver.quit()
    sys.exit(1)
# Aguarda a página carregar após a consulta (ajuste o tempo conforme necessário)
# Você pode usar WebDriverWait para esperar por elementos específicos, se necessário

# Aguarda até que a tabela esteja presente
tabela_presente = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'jh-table'))
)

# Localiza o elemento na coluna "Situação" usando o novo seletor CSS
situacao_element = driver.find_element(By.CSS_SELECTOR, 'tbody .text-center:nth-child(3) > span')

# Obtém o texto da coluna "Situação"
situacao_texto = situacao_element.text

# Imprime o texto
print('Situação:', situacao_texto)

# Fechar o navegador ao finalizar
driver.quit()