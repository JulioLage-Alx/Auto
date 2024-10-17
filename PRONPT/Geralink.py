import instaloader
import time
from concurrent.futures import ThreadPoolExecutor

# Inicializa o Instaloader
L = instaloader.Instaloader()

def coletar_reels(usuario):
    todos_os_links = []
    print(f"Coletando vídeos do usuário: {usuario}")
    
    try:
        profile = instaloader.Profile.from_username(L.context, usuario)
        count = 0

        for post in profile.get_posts():
            if post.is_video:
                video_link = f"https://www.instagram.com/reel/{post.shortcode}/"
                todos_os_links.append(video_link)
                count += 1
                
                if count >= 1000:  # Limite de 1000 links
                    break

        print(f"Vídeos encontrados para {usuario}: {count} links coletados.")
    except instaloader.exceptions.ProfileNotExistsException:
        print(f"O perfil '{usuario}' não existe.")
    except Exception as e:
        print(f"Erro ao acessar o perfil '{usuario}': {e}")

    return todos_os_links

def Geralink(usuarios_path):
    with open(usuarios_path, 'r', encoding='utf-8') as arquivo:
        usuarios = [linha.strip() for linha in arquivo.readlines()]

    todos_os_links = []

    with ThreadPoolExecutor(max_workers=5) as executor:
        results = executor.map(coletar_reels, usuarios)

    # Agrega todos os links coletados
    for links in results:
        todos_os_links.extend(links)

    # Salva todos os links em um arquivo de texto
    link_path = r'C:\Users\julio\OneDrive\Documentos\GitHub\Auto\LINKS\links.txt'
    with open(link_path, 'w', encoding='utf-8') as arquivo_links:
        for link in todos_os_links:
            arquivo_links.write(link + '\n')

    print(f"Todos os links de vídeo foram salvos em '{link_path}'.")

# Caminho para o arquivo com os nomes de usuários
caminho_perfis = r'C:\Users\julio\OneDrive\Documentos\GitHub\Auto\PERFIS\usuarios.txt'
Geralink(caminho_perfis)
