import os
import time
import requests
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

def baixar_video_instagram(post_url, pasta_destino):
    os.makedirs(pasta_destino, exist_ok=True)
    shortcode = post_url.split('/')[-2]

    options = uc.ChromeOptions()
    driver = uc.Chrome(options=options)

    try:
        driver.get(post_url)
        print("Aguardando o carregamento da página...")
        time.sleep(5)

        # Procura o elemento de vídeo
        video_elements = driver.find_elements(By.TAG_NAME, 'video')

        if video_elements:
            # Tenta pegar o src do vídeo
            video_url = video_elements[0].get_attribute('src')
        else:
            # Procura por elementos <source>
            source_elements = driver.find_elements(By.TAG_NAME, 'source')
            if source_elements:
                video_url = source_elements[0].get_attribute('src')
            else:
                print("Não foi possível encontrar o elemento de vídeo ou fonte.")
                return

        if video_url and not video_url.startswith("blob:"):
            video_path = os.path.join(pasta_destino, f"{shortcode}.mp4")
            if not os.path.exists(video_path):
                # Usando requests para baixar o vídeo
                response = requests.get(video_url, stream=True)
                if response.status_code == 200:
                    with open(video_path, 'wb') as f:
                        for chunk in response.iter_content(chunk_size=1024):
                            f.write(chunk)
                    print(f"Vídeo baixado e salvo em: {video_path}")
                else:
                    print(f"Erro ao baixar o vídeo: {response.status_code}")
            else:
                print(f"O vídeo já foi baixado: {video_path}")
        else:
            print("O post não contém um vídeo acessível.")

    except Exception as e:
        print(f"Erro ao baixar o vídeo: {e}")

    finally:
        driver.quit()

# Exemplo de uso
links_path = r'C:\Users\Betânia Rodrigues\Documents\Nova pasta\LINK\link.txt'
pasta_destino = r'C:\Users\Betânia Rodrigues\Documents\Nova pasta\VIDEO'

with open(links_path, 'r', encoding='utf-8') as file:
    for line in file:
        post_url = line.strip()
        if post_url:
            baixar_video_instagram(post_url, pasta_destino)
            time.sleep(60)  # Pausa entre downloads
