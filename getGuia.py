from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import url_guia, chave_consulta


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
# Abre a página da URL fornecida no config.py
driver.get(url_guia)

# Aguarda até que o campo "chaveNota" esteja disponível
campo_chave_nota = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'field_chaveNota'))
)

# Insere a chave de consulta no campo
campo_chave_nota.send_keys(chave_consulta)

# Localiza o botão "Adicionar"
botao_adicionar = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-outline-primary'))
)

# Clica no botão "Adicionar"
botao_adicionar.click()

# Aguarda a página carregar após a ação (ajuste o tempo conforme necessário)
# Você pode usar WebDriverWait para esperar por elementos específicos, se necessário

# Fechar o navegador ao finalizar
driver.quit()
