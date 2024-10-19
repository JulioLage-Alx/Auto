import os

def remove_non_mp4_files(folder_path):
    # Verifica se o caminho fornecido é uma pasta
    if not os.path.isdir(folder_path):
        print(f"O caminho '{folder_path}' não é uma pasta válida.")
        return

    # Itera pelos arquivos na pasta
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Verifica se é um arquivo e se a extensão não é .mp4
        if os.path.isfile(file_path) and not filename.endswith('.mp4'):
            try:
                os.remove(file_path)  # Exclui o arquivo
                print(f"Arquivo removido: {filename}")
            except Exception as e:
                print(f"Erro ao remover {filename}: {e}")

# Exemplo de uso
folder_path = '...\\Auto\\VIDEOS'  # Altere para o caminho desejado
remove_non_mp4_files(folder_path)
