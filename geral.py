import instaloader
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from tiktok_uploader.upload import upload_video

# Inicializa o Instaloader
L = instaloader.Instaloader()

# Lê os nomes dos usuários do arquivo
with open('usuarios.txt', 'r') as arquivo:
    usuarios = [linha.strip() for linha in arquivo.readlines()]

# Lista para armazenar todos os links de vídeo
todos_os_links = []

# Itera sobre cada usuário no arquivo
for usuario in usuarios:
    print(f"Coletando vídeos do usuário: {usuario}")

    try:
        profile = instaloader.Profile.from_username(L.context, usuario)

        # Itera sobre os posts do perfil
        for post in profile.get_posts():
            if post.is_video:
                # Coleta o link do post (do formato desejado)
                video_link = f"https://www.instagram.com/reel/{post.shortcode}/"
                todos_os_links.append(video_link)  # Adiciona os links à lista

        # Imprime os links dos vídeos encontrados
        print(f"Vídeos encontrados para {usuario}: {len(todos_os_links)} links coletados.")

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"O perfil '{usuario}' não existe.")
    except Exception as e:
        print(f"Erro ao acessar o perfil '{usuario}': {e}")

# Salva todos os links em um arquivo de texto
with open('links.txt', 'w') as arquivo_links:
    for link in todos_os_links:
        arquivo_links.write(link + '\n')  # Escreve cada link em uma nova linha

print(f"Todos os links de vídeo foram salvos em 'links.txt'.")

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

        # Aguarde o botão de download final
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

# Feche o navegador após o download
driver.quit() 

# Faz upload de cada vídeo que foi baixado
videos = [f for f in os.listdir(download_folder) if f.endswith('.mp4')]

for video in videos:
    video_path = os.path.join(download_folder, video)  # Cria o caminho completo do vídeo
    print(f"Fazendo upload de: {video_path}")  # Exibe o vídeo que está sendo enviado
    upload_video(video_path,  
                 description='Link na Descrição \n #produtos #conteudo #bombando',  
                 cookies='C:/Users/julio/Documents/cook/cookies.txt')
    print(f"Upload concluído para: {video}")
    
    # Exclui o vídeo após o upload
    os.remove(video_path)  # Remove o vídeo do diretório
    print(f"Vídeo excluído: {video_path}")
