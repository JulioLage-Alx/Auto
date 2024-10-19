import os
import logging
import time
import subprocess
from random import choice
import emoji

def posta():
    logging.basicConfig(level=logging.INFO, filename='upload_log.txt', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

    pasta_videos = '...\\Auto\\VIDEOS'
    descricao_path = '...\\Auto\\DESCRIÇAO\\descricao.txt'  # Caminho completo
    linha_contador_path = '...\\BOOT-TIKTPK\\Auto\\CONTADOR\\LINHA_CONTADOR.TXT'
    cookies_path = '...\\TiktokAutoUploader\\CookiesDir\\tiktok_session-contaone.cookie'
    TEMPO_ESPERA = 5

    os.makedirs(os.path.dirname(linha_contador_path), exist_ok=True)

    def carregar_descricoes(caminho):
        if os.path.exists(caminho):
            with open(caminho, 'r', encoding='utf-8') as descri:
                return [linha.strip() for linha in descri.readlines() if linha.strip()]
        return []

    linha_inicio = 0
    if os.path.exists(linha_contador_path):
        with open(linha_contador_path, 'r') as file:
            linha_inicio = int(file.read().strip())

    videos = [f for f in os.listdir(pasta_videos) if f.endswith('.mp4')] 
    descricoes = carregar_descricoes(descricao_path)

    for i, video in enumerate(videos[linha_inicio:], start=linha_inicio):
        if i >= linha_inicio + 10:
            break

        video_path = os.path.join(pasta_videos, video)
        logging.info(f"Fazendo upload de: {video_path}")
        print(f"Fazendo upload de: {video_path}")

        video_size = os.path.getsize(video_path)
        if video_size == 0 or video_size < 1024:
            logging.warning(f"O vídeo {video} está vazio ou muito pequeno e será ignorado.")
            continue

        if i < len(descricoes) and descricoes[i].strip():
            descricao = descricoes[i]
        else:
            descricoes_padrao = [
                "link na bio\n #Produto #Achado #presente #achado",
                "Confira o link na bio!\n #Novidade #Promoção",
                "Não perca essa oferta incrível! Link na bio!\n #Desconto #Imperdível"
            ]
            descricao = choice(descricoes_padrao)

        descricao = emoji.emojize(descricao)
        logging.info(f"Iniciando upload do vídeo: {video_path} com descrição: {descricao}")

        try:
            subprocess.run([
                'python', 
                r'C:\Users\julio\OneDrive\Documentos\GitHub\TiktokAutoUploader\cli.py', 
                'upload', 
                '-u', 
                'contaone', 
                '-v', 
                video_path,
                '-t', 
                descricao  # Usando a descrição correta
            ], check=True)  # Adicionando check=True para levantar erro se falhar

            logging.info(f"Upload concluído para: {video}")
            print(f"Upload concluído para: {video}")

            with open(linha_contador_path, 'w') as file:
                file.write(str(i + 1))

            time.sleep(TEMPO_ESPERA)

        except Exception as e:
            logging.error(f"Erro ao fazer upload de {video}: {e}")
            print(f"Erro ao fazer upload de {video}: {e}")
            continue

if __name__ == "__main__":
    posta()
