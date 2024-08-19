from tkinter import *

janela = Tk()
janela.title('Meu Primeiro Programa GUI')
janela.minsize(width=500, height=300)

#Label
my_label = Label(text='Eu sou o label', font=('Arial', 24, 'bold'))
my_label.grid(column=0, row=0)
my_label['text'] = 'Novo texto'
my_label.config(padx= 20, pady=20) #adicionando um espaço em tornp

#Botao

def botao_clicado():
    print('Clicaram no botao')
    novo_texto = input.get()
    my_label.config(text=novo_texto)

botao = Button(text='Clique aqui', command=botao_clicado)
botao.grid(column=1,row=1)


#Entry

input = Entry(width=10)
input.grid(column=2, row= 2)
















janela.mainloop()