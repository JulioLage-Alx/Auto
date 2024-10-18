import os
from tiktok_uploader.upload import upload_video 
import logging
import time
from random import choice
import emoji  # Importa a biblioteca emoji

BROWSERS = [
    'edge'  
]

# Configuração do logging
logging.basicConfig(level=logging.INFO, filename='upload_log.txt', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

# Caminhos para os arquivos e pastas
pasta_videos = r'VIDEOS' 
descricao_path = r'DESCRIÇAO\descricao.txt'
linha_contador_path = r'CONTADOR\LINHA_CONTADOR.TXT'
descricao_contador_path = r'CONTADOR\DESCRICAO_CONTADOR.TXT'
cookies_path = r'COOKIES\cookies.txt'
TEMPO_ESPERA = 5  # Tempo de espera em segundos

# Garante que o diretório do contador exista
os.makedirs(os.path.dirname(linha_contador_path), exist_ok=True)

# Função para carregar descrições
def carregar_descricoes(caminho):
    if os.path.exists(caminho):
        with open(caminho, 'r', encoding='utf-8') as descri:
            return [linha.strip() for linha in descri.readlines() if linha.strip()]
    return []

# Lê a linha onde parou
linha_inicio = 0
if os.path.exists(linha_contador_path):
    with open(linha_contador_path, 'r') as file:
        linha_inicio = int(file.read().strip())

# Obtém a lista de arquivos na pasta de vídeos 
videos = [f for f in os.listdir(pasta_videos) if f.endswith('.mp4')] 

# Lê as descrições do arquivo
descricoes = carregar_descricoes(descricao_path)

# Faz upload de até 10 vídeos
for i, video in enumerate(videos[linha_inicio:], start=linha_inicio):  # Começa a partir da linha onde parou
    if i >= linha_inicio + 10:  # Limita a 10 uploads por execução
        break

    video_path = os.path.join(pasta_videos, video)  # Cria o caminho completo do vídeo
    logging.info(f"Fazendo upload de: {video_path}")  # Registra o vídeo que está sendo enviado
    print(f"Fazendo upload de: {video_path}")  # Exibe no console
    
    # Verifica se o vídeo está vazio ou muito pequeno
    video_size = os.path.getsize(video_path)
    if video_size == 0 or video_size < 1024:  # Verifica se o vídeo é vazio ou muito pequeno (menor que 1 KB)
        logging.warning(f"O vídeo {video} está vazio ou muito pequeno e será ignorado.")
        continue

    # Usa a descrição correspondente, se existir
    if i < len(descricoes) and descricoes[i].strip():
        descricao = descricoes[i]
    else:
        # Descrições padrão
        descricoes_padrao = [
            "link na bio\n #Produto #Achado #presente #achado",
            "Confira o link na bio!\n #Novidade #Promoção",
            "Não perca essa oferta incrível! Link na bio!\n #Desconto #Imperdível"
        ]
        descricao = choice(descricoes_padrao)  # Escolhe uma descrição padrão aleatoriamente

    # Substitui os códigos de emoji na descrição
    descricao = emoji.emojize(descricao)  # Converte os códigos de emoji para emojis reais

    # Verifica se o arquivo de cookies existe
    if not os.path.exists(cookies_path):
        logging.error(f"O caminho do arquivo de cookies não existe: {cookies_path}")
        print(f"O caminho do arquivo de cookies não existe: {cookies_path}")
        continue  # Ignora o upload se o arquivo de cookies não existir

    try:
        logging.info(f"Iniciando upload do vídeo: {video_path} com descrição: {descricao}")
        start_time = time.time()  # Marca o tempo de início
        
        upload_video(video_path,  
                     description=descricao,  
                     cookies=cookies_path, 
                     browser=choice(BROWSERS))
        
        elapsed_time = time.time() - start_time  # Calcula o tempo de upload
        logging.info(f"Upload concluído para: {video} em {elapsed_time:.2f} segundos")
        print(f"Upload concluído para: {video}")

        # Salva a última linha e descrição onde parou
        with open(linha_contador_path, 'w') as file:
            file.write(str(i + 1))  # Salva a próxima linha a ser postada
        with open(descricao_contador_path, 'w') as file:
            file.write(descricao)  # Salva a descrição do último vídeo postado

        # Adiciona um tempo de espera após cada upload
        time.sleep(TEMPO_ESPERA)  # Espera 5 segundos antes do próximo upload

    except Exception as e:
        logging.error(f"Erro ao fazer upload de {video}: {e}")
        print(f"Erro ao fazer upload de {video}: {e}")  # Exibe no console
        continue  # Continua para o próximo vídeo em caso de erro
