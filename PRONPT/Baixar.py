import os
import instaloader
import Descricoes as dc
import limp as lp
            
pasta ='...\\Auto\\VIDEOS'   # Caminho da pasta onde estão os arquivos
arquivo_saida = '...\\Auto\\DESCRIÇAO\\descricao.txt'  # Caminho do arquivo de saída

def baixar_apenas_videos_perfil(nome_perfil, pasta_destino):
    os.makedirs(pasta_destino, exist_ok=True)

    loader = instaloader.Instaloader()

    # Faz login se necessário (opcional)
    # loader.login("seu_usuario", "sua_senha")  # Descomente e insira suas credenciais

    try:
        profile = instaloader.Profile.from_username(loader.context, nome_perfil)
    except Exception as e:
        print(f"Erro ao acessar o perfil {nome_perfil}: {e}")
        return []

    video_salvos = []  # Lista para armazenar os vídeos salvos

    for post in profile.get_posts():
        if post.is_video:
            print(f"Baixando vídeo do perfil {nome_perfil}: {post.date_utc.strftime('%Y-%m-%d_%H-%M-%S')}.mp4")
            try:
                # Baixa o post, salvando os arquivos no diretório de destino
                loader.download_post(post, target=pasta_destino)

                # Renomeia o arquivo após o download
                for file in os.listdir(pasta_destino):
                    video_file_path = os.path.join(pasta_destino, file)
                    if post.date_utc.strftime('%Y-%m-%d') in file and file.endswith('.mp4'):
                        new_video_name = f"{post.date_utc.strftime('%Y-%m-%d_%H-%M-%S')}.mp4"
                        new_video_path = os.path.join(pasta_destino, new_video_name)

                        # Adiciona um sufixo se o novo nome já existir
                        counter = 1
                        while os.path.exists(new_video_path):
                            new_video_path = os.path.join(pasta_destino, f"{post.date_utc.strftime('%Y-%m-%d_%H-%M-%S')}_{counter}.mp4")
                            counter += 1

                        os.rename(video_file_path, new_video_path)
                        video_salvos.append(new_video_path)

            except Exception as e:
                print(f"Erro ao baixar o vídeo: {e}")


    

    return video_salvos if video_salvos else "Nenhum vídeo foi salvo."


def baixa():
# Caminhos para os arquivos e pastas
    caminho_perfis = '...\Auto\PERFIS\usuarios.txt'


# Lê os nomes dos perfis do arquivo
    with open(caminho_perfis, 'r', encoding='utf-8') as perfis_file:
        perfis = [linha.strip() for linha in perfis_file.readlines()]

# Baixa vídeos de todos os perfis listados
    todos_videos = []
    for perfil in perfis:
     videos = baixar_apenas_videos_perfil(perfil, pasta)
     if isinstance(videos, list):
          todos_videos.extend(videos)

    print("Todos os vídeos baixados:", todos_videos)

    dc.juntar_descricoes(pasta, arquivo_saida)
    print(f"Descrições salvas em: {arquivo_saida}")
    lp.remove_non_mp4_files(pasta)