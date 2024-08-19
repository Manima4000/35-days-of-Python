from tkinter import *
from tkinter import messagebox
import random
import json

janela = Tk()
janela.title('Gerador de senhas')
janela.minsize(width=500,height=300)
janela.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
imagem = PhotoImage(file='imagens/logo.png')
canvas.create_image(100, 100, image=imagem)
canvas.grid(row=0, column=1)

website = Label(text='Website:', font=('Arial', 10))
website.grid(row=1,column=0)

website2 = Entry(width=35)
website2.grid(row=1,column=1,columnspan=2)
website2.focus()

email_username = Label(text='Email/Username:', font=('Arial', 10))
email_username.grid(row=2,column=0)

email_username2 = Entry(width=35)
email_username2.grid(row=2,column=1,columnspan=2)
email_username2.insert(0, 'matandradefe@gmail.com')


password = Label(text='Password:', font=('Arial', 10))
password.grid(row=3,column=0)

password2 = Entry(width=22)
password2.grid(row=3,column=1)

# ----------------------- Gerando Senha ----------------------- #

def gerar_senha():
    
    password2.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letras = [random.choice(letters) for i in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for i in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for i in range(random.randint(2, 4))]

    password_list = password_letras + password_numbers + password_symbols

    random.shuffle(password_list)

    senha_aleatoria = ''.join(password_list)
    password2.insert(0, senha_aleatoria)
   
# ----------------------- Gerando Senha ----------------------- #

gerador_de_senhas = Button(text='Gerar Senha', command=gerar_senha)
gerador_de_senhas.grid(row=3,column=2)



# ----------------------- Salvando os dados ----------------------- #

def adionacionar_butao():
    texto1 = website2.get()
    texto2 = email_username2.get()
    texto3 = password2.get()
    novo_dado = {
        texto1: {
            'email': texto2,
            'senha': texto3
        }
    }
    if not len(texto1) or not len(texto2) or  not len(texto3):
        messagebox.showinfo(title= 'Oops',message='Por favor, preencha todos os campos')
    else:
        with open('arquivos/senhas.json', 'r') as data_file:
            #lendo os dados antigos
            data = json.load(data_file)
            #atualizando com novo dado
            data.update(novo_dado)

        with open('arquivos/senhas.json', 'w') as data_file:
            #Salvando com novo dado
            json.dump(data, data_file,indent=4)

    website2.delete(0, END)
    password2.delete(0, END)


# ----------------------- Salvando os dados ----------------------- #

# ----------------------- Procurar site ----------------------- #
    
def procurar_website():
    with open('arquivos/senhas.json','r') as data_file:
        data = json.load(data_file)
        try:
            messagebox.showinfo(title=website2.get(), message='Email: {}\nSenha: {}'.format(data[website2.get()]['email'], data[website2.get()]['senha']))
        except:
            messagebox.showinfo(title='Oops', message='Você não possui credenciais em {}'.format(website2.get()))
       






# ----------------------- Procurar site ----------------------- #




adicionar = Button(text='Adicionar',width=36, command=adionacionar_butao)
adicionar.grid(row=4,column=1,columnspan=2)

procurar = Button(text='Procurar',command=procurar_website)
procurar.grid(row=1,column=3)















janela.mainloop()