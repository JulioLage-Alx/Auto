import os

def juntar_descricoes(pasta_origem, arquivo_saida):
    with open(arquivo_saida, 'w', encoding='utf-8') as outfile:
        for filename in os.listdir(pasta_origem):
            if filename.endswith('.txt'):  # Verifica se o arquivo é um .txt
                caminho_arquivo = os.path.join(pasta_origem, filename)
                with open(caminho_arquivo, 'r', encoding='utf-8') as infile:
                    # Lê o conteúdo do arquivo e remove quebras de linha desnecessárias
                    conteudo = infile.read().strip().replace('\n', ' ')
                    outfile.write(conteudo + '\n')  # Adiciona uma nova linha após cada descrição

# Exemplo de uso
pasta = r'VIDEOS'  # Caminho da pasta onde estão os arquivos
arquivo_saida = r'DESCRIÇAO\descricao.txt'  # Caminho do arquivo de saída

juntar_descricoes(pasta, arquivo_saida)
print(f"Descrições salvas em: {arquivo_saida}")
