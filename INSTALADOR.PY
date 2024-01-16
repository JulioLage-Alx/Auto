from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Defina o caminho para o ChromeDriver
driver_path = r'C:\Users\julio\Downloads\chromedriver-win64 (1)\chromedriver-win64\chromedriver.exe'

# Crie uma pasta para os downloads, se ainda não existir
download_folder = r'C:\Users\julio\Documents\VIDEOS'
os.makedirs(download_folder, exist_ok=True)

# Configurações do Chrome para definir a pasta de download
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    'download.default_directory': download_folder,  # Defina sua pasta de downloads
    'download.prompt_for_download': False,           # Não solicitar confirmação para downloads
    'download.directory_upgrade': True,
    'safebrowsing.enabled': True                      # Habilitar navegação segura
})

service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Lê os links do arquivo
with open('links.txt', 'r') as arquivo_links:
    links = arquivo_links.readlines()

# Loop pelos links e faz o download
for link in links:
    link = link.strip()
    print(f"Baixando vídeo de: {link}")

    # Acesse o site SaveClip
    driver.get('https://saveclip.app/pt')

    # Aguarde até que o campo de entrada esteja visível
    campo_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, 'q'))
    )
    campo_input.clear()
    campo_input.send_keys(link)

    # Aguarde até que o botão de download esteja clicável
    try:
        botao_download = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//button[b[text()="Baixar"]]'))
        )
        botao_download.click()
        print(f"Download iniciado para: {link}")

        # Aguarde o redirecionamento e a nova página carregar
        time.sleep(5)

        # Verifica se a URL mudou
        print("URL atual após clicar no botão de download:", driver.current_url)

        # Aguarde o botão de download final (o href que você mencionou)
        link_download = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@class="abutton is-success is-fullwidth btn-premium mt-3" and contains(@title, "Download Video")]'))
        )
        # Clique no link de download
        driver.execute_script("arguments[0].click();", link_download)
        print(f"Download concluído para: {link}")

        # Aguarde um tempo para o download ser processado
        time.sleep(10)

    except Exception as e:
        print(f"Erro ao baixar {link}: {e}")
        print("URL atual:", driver.current_url)

# Feche o navegador
driver.quit()
