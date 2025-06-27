#Meu projeto
import customtkinter as ctk
from tkinter import messagebox #Colocar essa Linha!!!

#Configuração Inicial
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# Criar a janela principal
janela = ctk.CTk() #Função de criar a tela
janela.title("Seletor de Cor")
janela.geometry("400X200")

# Código em si
def verificar_habilitacao():
 
    nome = entrada_nome.get()
    idade = entrada_idade.get()

    if not nome or not idade:
        messagebox.showwarning("Campos Vazios", "Preencha todos os campos.")
        return

    try:
        idade = int(idade)
    except ValueError:
        messagebox.showwarning("Erro", "A idade precisa ser um número inteiro.")
        return

    if idade >= 18:
        resultado.configure(text=f"{nome}, você está apto(a) a dirigir!", text_color="green")
    else:
        resultado.configure(text=f"{nome}, você NÃO está apto(a) a dirigir.", text_color="red")

# Label de Digite seu Nome
label_nome = ctk.CTkLabel(janela, text="Digite o seu nome: ")
label_nome.pack(pady=(20, 5))

entrada_nome = ctk.CTkEntry(janela, width=250)
entrada_nome.pack()
# Label de Digite sua Idade
label_idade = ctk.CTkLabel(janela, text="Digite a sua idade: ")
label_idade.pack(pady=(20, 5))

entrada_idade = ctk.CTkEntry(janela, width=250)
entrada_idade.pack()



# Botão de Verificar




# Label do Resultado (O Texto falando sobre se Pode ou Não Dirigir)
resultado = ctk.CTkLabel(janela, text="")
resultado.pack(pady=10)

# Loop principal da janela
janela.mainloop()