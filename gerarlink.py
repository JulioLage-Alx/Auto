import instaloader

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
        
        # Lista de links de vídeos
        video_links = []

        # Itera sobre os posts do perfil
        for post in profile.get_posts():
            if post.is_video:
                # Coleta o link do post (do formato desejado)
                video_link = f"https://www.instagram.com/reel/{post.shortcode}/"
                video_links.append(video_link)

        # Imprime os links dos vídeos encontrados
        if video_links:
            print(f"Vídeos encontrados para {usuario}:")
            for link in video_links:
                print(link)
                todos_os_links.append(link)  # Adiciona os links à lista

        else:
            print(f"Nenhum vídeo encontrado para {usuario}.")

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"O perfil '{usuario}' não existe.")
    except Exception as e:
        print(f"Erro ao acessar o perfil '{usuario}': {e}")

# Salva todos os links em um arquivo de texto
with open('links.txt', 'w') as arquivo_links:
    for link in todos_os_links:
        arquivo_links.write(link + '\n')  # Escreve cada link em uma nova linha

print(f"Todos os links de vídeo foram salvos em 'links_videos.txt'.")
