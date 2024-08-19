from tkinter import *
import time

janela = Tk()
janela.title('Pomodoro')
janela.config(padx=100, pady=100, bg= "#f7f5dd")

canvas = Canvas(width=200, height=224, bg= "#f7f5dd", highlightthickness=0)
tomate = PhotoImage(file='imagens/tomato.png')
canvas.create_image(100, 112, image=tomate)
canvas.create_text(100,130,text='00:00', fill='white', font=("Courier",35,'bold'))
canvas.grid(row=1, column=1)

my_label = Label(text='Timer', font=('Courier', 40, 'bold'), bg="#f7f5dd",fg="#9bdeac")
my_label.grid(row=0, column=1)

start = Button(text='Começar', highlightthickness=0)
start.grid(row=2,column=0)

reset = Button(text='Resetar', highlightthickness=0)
reset.grid(row=2,column=2)

check = Label(text = "✔",highlightthickness=0, bg="#f7f5dd", fg="#9bdeac")
check.grid(row=3,column=1)

##VER DEPOIS... MT CHATO
    




























janela.mainloop()