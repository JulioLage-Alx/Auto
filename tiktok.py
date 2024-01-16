from tiktok_uploader.upload import upload_video 
import os 
 
# Define o caminho para a pasta de vídeos 
pasta_videos = r'C:\Users\julio\Documents\VIDEOS' 
 
# Obtém a lista de arquivos na pasta de vídeos 
videos = [f for f in os.listdir(pasta_videos) if f.endswith('.mp4')] 

# Faz upload de cada vídeo
for video in videos:
    video_path = os.path.join(pasta_videos, video)  # Cria o caminho completo do vídeo
    print(f"Fazendo upload de: {video_path}")  # Exibe o vídeo que está sendo enviado
    upload_video(video_path,  
                 description='Link na Descriçao \n #produtos #conteudo #bombando',  
                 cookies='C:/Users/julio/Documents/cook/cookies.txt')
    print(f"Upload concluído para: {video}")
