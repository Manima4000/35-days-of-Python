from tkinter import *
import pandas as pd
import random
import time

BACKGROUND_COLOR = "#B1DDC6"

#Lendo os dados
data = pd.read_csv('arquivos/Day31/french_words.csv')
data_in_list = data.to_dict(orient='records')
escolha = {}

# ------------------------------------------------- Funções ------------------------------------------------- #

def next_card():
    global escolha
    escolha = random.choice(data_in_list)
    canvas.itemconfig(palavra_da_carta, text=escolha['French'])
    canvas.itemconfig(imagem, image=imagem_front)
    canvas.itemconfig(palavra_da_carta, fill= 'black')
    canvas.itemconfig(titulo_da_carta, text='French')
    janela.after(3000, func=trocar_imagem)
    

def trocar_imagem():
    global escolha
    canvas.itemconfig(imagem, image=imagem_back)
    canvas.itemconfig(palavra_da_carta, fill= 'white', text=escolha['English'])
    canvas.itemconfig(titulo_da_carta, text='English')

def conheço_a_palavra():
    data_in_list.remove(escolha)
    next_card()
    print(len(data_in_list))


# ------------------------------------------------- Funções ------------------------------------------------- #



#Janela
janela = Tk()
janela.title('Jogo de cartas')
janela.config(padx=50, pady=50, bg= BACKGROUND_COLOR, highlightthickness=0)

#Imagem da frente
canvas = Canvas(width=800, height=526)
imagem_front = PhotoImage(file='imagens/Day31/card_front.png')
imagem_back = PhotoImage(file='imagens/Day31/card_back.png')
imagem = canvas.create_image(400, 263, image=imagem_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0,columnspan=2)


#Butao Certo
foto_botao_certo = PhotoImage(file='imagens/Day31/right.png')
butao_certo = Button(image=foto_botao_certo, highlightthickness=0, bg= BACKGROUND_COLOR,command=conheço_a_palavra)
butao_certo.grid(row=1,column=0)

#Butao Errado
foto_botao_errado = PhotoImage(file='imagens/Day31/wrong.png')
butao_errado = Button(image=foto_botao_errado, highlightthickness=0, bg= BACKGROUND_COLOR,command=next_card)
butao_errado.grid(row=1,column=1)

#Palavra 'French'
titulo_da_carta = canvas.create_text(400,150,text='French', font=("Arial",40,'italic'))

#Palavra francesa no canvas
palavra_da_carta = canvas.create_text(400,253, text='Palavra francesa', font=('Arial',60,'bold'))
next_card()


















janela.mainloop()


