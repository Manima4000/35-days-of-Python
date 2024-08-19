from tkinter import *


janela = Tk()
janela.title('Conversor de kilometros pra milhas')
janela.minsize(width=250, height=50)
janela.config(padx=20,pady=20)




input = Entry(width=10)
input.grid(column=1, row= 0)



texto1 =  Label(text='km', font=('Arial', 12))
texto1.grid(column=2,row=0)


texto2 =  Label(text= 0, font=('Arial', 12))
texto2.grid(column=1,row=1)
texto2.config(padx=20)

texto3 = Label(text='milhas', font=('Arial', 12))
texto3.grid(column=2,row=1)

texto4 = Label(text='são iguais a', font=('Arial', 12))
texto4.grid(column=0,row=1)

def botao_clicado():
    novo_texto = int(input.get())
    texto2.config(text=novo_texto*0.621)



botao = Button(text='Calcular', command=botao_clicado)
botao.grid(column=1,row=2)













janela.mainloop()