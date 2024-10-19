import tkinter as tk
from tkinter import messagebox
import Baixar as bx
import sys
import os
import posti as ps


def escrever_no_txt(caminho_arquivo, texto):
    try:
        with open(caminho_arquivo, 'a', encoding='utf-8') as file:
            file.write(texto + '\n')
        print(f"Texto adicionado ao arquivo: {caminho_arquivo}")
    except Exception as e:
        print(f"Ocorreu um erro ao escrever no arquivo: {e}")
def escreveusuario():
    def salvar_usuario(event=None):  # Adicionando 'event' como argumento
        texto_usuario = entry_usuario.get().strip()
        if texto_usuario:
            caminho = '...\Auto\PERFIS\usuarios.txt'
            escrever_no_txt(caminho, texto_usuario)
            messagebox.showinfo("Sucesso", f"Usuário '{texto_usuario}' adicionado com sucesso!")
            entrada_janela.destroy()
        else:
            messagebox.showwarning("Aviso", "Por favor, insira um nome de usuário.")

    # Criar a janela para inserir o usuário
    entrada_janela = tk.Toplevel(root)
    entrada_janela.geometry("300x150")
    entrada_janela.config(bg="black")
    
    label_titulo = tk.Label(entrada_janela, text="INSERIR USUÁRIO", font=("Arial", 14, "bold"), bg="black", fg="white")
    label_titulo.pack(pady=(30, 0))  # Espaçamento vertical acima e nenhum abaixo do label

    # Estilização da janela
    label_instrucao = tk.Label(entrada_janela, text="Digite o nome do perfil:", font=("Arial", 12), bg="black", fg="white")
    label_instrucao.pack(pady=10)

    entry_usuario = tk.Entry(entrada_janela, font=("Arial", 12), width=25)
    entry_usuario.pack(pady=5)
    
    # Adiciona o evento para o Enter
    entry_usuario.bind("<Return>", salvar_usuario)  # Liga o evento Enter à função salvar_usuario

    btn_salvar = tk.Button(entrada_janela, text="Salvar", command=salvar_usuario, font=("Arial", 12), bg="blue", fg="white")
    btn_salvar.pack(pady=10)


def baixar_videos():
    try:
        mensagem = bx.baixa()  # Assume que bx.baixa() retorna uma string com a mensagem
        messagebox.showinfo("Sucesso", mensagem)
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao baixar os vídeos: {e}")

def postar_videos():
    try:
        mensagem = ps.posta()  # Assume que ps.posta() retorna uma string com a mensagem
        messagebox.showinfo("Sucesso", mensagem)
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao postar os vídeos: {e}")

# Criar a janela principal
root = tk.Tk()
root.title("Instagram Video Manager")
root.geometry("300x300")
root.config(bg="black")

# Adicionar um label com a frase acima
label_titulo = tk.Label(root, text="BOOT POST", font=("Arial", 14,"bold"), bg="black", fg="white")
label_titulo.pack(pady=(30,0))  # Espaçamento vertical acima e abaixo do label

# Estilização dos botões
button_style = {
    'font': ("Arial", 12,"bold"),
    'bg': "green",
    'fg': "white",
    'width': 15
}
frame_botoes = tk.Frame(root)
frame_botoes.config(bg="black")
frame_botoes.pack(expand=True)  # Centraliza o frame na janela

# Criar botões para as ações
btn_baixar = tk.Button(frame_botoes, text="Baixar Vídeos", command=baixar_videos, **button_style)
btn_baixar.pack(pady=5)  # Usando pack para centralizar

btn_postar = tk.Button(frame_botoes, text="Postar Vídeos", command=postar_videos, **button_style)
btn_postar.pack(pady=5)  # Usando pack para centralizar

btn_inserir = tk.Button(frame_botoes, text="Inserir Usuário", command=escreveusuario, **button_style)
btn_inserir.pack(pady=5)  # Usando pack para centralizar
root.mainloop()
