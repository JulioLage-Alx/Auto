
# Instagram Video Downloader and Auto-Poster

Este projeto permite baixar vídeos de qualquer perfil do Instagram e postá-los automaticamente em sua conta. É uma ferramenta útil para quem deseja compartilhar conteúdo de forma prática e rápida, ideal para criadores de conteúdo e marketers digitais.

## Estrutura do Projeto

O projeto possui a seguinte estrutura de diretórios:


Auto/
├── CONTADOR/
├── COOKIES/
├── DESCRIÇAO/
├── PERFIS/
├── PRONPT/
│   ├── __pycache__/
│   ├── Baixar.py
│   ├── Descricoes.py
│   ├── limp.py
│   └── posti.py
├── VIDEOS/
└── .gitattributes


### Diretórios

- **CONTADOR/**: Armazena contagens ou estatísticas relacionadas aos vídeos.
- **COOKIES/**: Contém arquivos de cookies necessários para autenticação no Instagram.
- **DESCRIÇAO/**: Armazena descrições ou informações sobre os vídeos.
- **PERFIS/**: Contém uma lista de perfis de Instagram dos quais os vídeos serão baixados.
- **PRONPT/**: Contém os scripts principais do projeto:
  - `Baixar.py`: Script responsável por baixar vídeos de perfis do Instagram.
  - `Descricoes.py`: Script para manipulação e gerenciamento das descrições dos vídeos.
  - `limp.py`: Script para limpeza e organização dos arquivos indesejados.
  - `posti.py`: Script que automatiza a postagem dos vídeos baixados.
- **VIDEOS/**: Diretório onde os vídeos baixados são armazenados.

## Pré-requisitos

Certifique-se de ter o seguinte instalado em seu ambiente:

- [Python 3.x](https://www.python.org/downloads/)
- Bibliotecas necessárias:
  - `instaloader`
  - `tiktok_uploader`
  - `emoji`
  - Qualquer outra biblioteca que você utilizar nos scripts (verifique nos scripts e instale-as com `pip install -r requirements.txt`)

## Como Usar

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu_usuario/Auto.git
   cd Auto
   ```

2. Adicione os perfis de Instagram no diretório `PERFIS/` em um arquivo `usuarios.txt`.

3. Configure o arquivo de cookies no diretório `COOKIES/` para autenticação (consulte a documentação do Instaloader para mais informações sobre como gerar o arquivo de cookies).

4. Execute o script para baixar vídeos:

   ```bash
   python PRONPT/Baixar.py
   ```

5. Após o download, execute o script para postar automaticamente:

   ```bash
   python PRONPT/posti.py
   ```

## Contribuições

Sinta-se à vontade para contribuir com melhorias ou novas funcionalidades. Faça um fork do repositório, crie uma nova branch e envie um pull request. Toda contribuição é bem-vinda!

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

Para mais informações ou sugestões, entre em contato com [juliolage.alx@gmail.com](mailto:juliolage.alx@gmail.com).
