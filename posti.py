from tiktok_uploader.upload import upload_video 
import os 
import Baixar as bd
import Geralink as ger

# Caminhos para os arquivos e pastas
caminho_perfis = r'PERFIS/perfis.txt'
pasta_videos = r'C:\Users\Betânia Rodrigues\Documents\VIDEOS' 
link_path = r'C:\Users\Betânia Rodrigues\Documents\Nova pasta\LINK\link.txt'
descricao_path = r'C:\Users\Betânia Rodrigues\Documents\Nova pasta\DESCRICAO\descricoes.txt'

# Coleta os links dos vídeos
ger.Geralink(caminho_perfis)

# Lê os links do arquivo
with open(link_path, 'r', encoding='utf-8') as arquivo_links:
    links = arquivo_links.readlines()

# Baixa os vídeos para a pasta especificada
for link in links:
    link = link.strip()  # Remove espaços em branco
    bd.baixar_videos(link, pasta_videos)

# Obtém a lista de arquivos na pasta de vídeos 
videos = [f for f in os.listdir(pasta_videos) if f.endswith('.mp4')] 

# Lê as descrições do arquivo
with open(descricao_path, 'r', encoding='utf-8') as descri:
    descricoes = [linha.strip() for linha in descri.readlines()]

# Faz upload de cada vídeo
for i, video in enumerate(videos):
    video_path = os.path.join(pasta_videos, video)  # Cria o caminho completo do vídeo
    print(f"Fazendo upload de: {video_path}")  # Exibe o vídeo que está sendo enviado
    
    # Usa a descrição correspondente, se existir
    if i < len(descricoes):
        descricao = descricoes[i]
    else:
        descricao = "Descrição padrão"  # Define uma descrição padrão caso não haja

    upload_video(video_path,  
                 description=descricao,  
                 cookies=r'C:\Users\Betânia Rodrigues\Documents\Nova pasta\COOKIES\www.tiktok.com_15-10-2024.json')
    
    print(f"Upload concluído para: {video}")
