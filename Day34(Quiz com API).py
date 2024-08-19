from tkinter import *
import requests
import random
import html

THEME_COLOR = "#375362"
perguntas_que_ja_foram = []
score = 0
resposta_certa = 'CU'
pergunta = ''


#Funções
def escolher_pergunta():
    global pergunta
    global resposta_certa
    if len(perguntas_que_ja_foram) < 11:
        while pergunta in perguntas_que_ja_foram:
            numero_aleatorio = random.randint(0,9)
            pergunta = data['results'][numero_aleatorio]['question']
            resposta_certa = data['results'][numero_aleatorio]['correct_answer']
        perguntas_que_ja_foram.append(pergunta)
        canvas.itemconfig(pergunta_no_canvas, text= html.unescape(pergunta))
    

def clicar_certo():
    global score
    escolher_pergunta()
    if resposta_certa == 'True':
        score+=1
        score_na_janela['text'] = f'Score: {score}'
    
    

def clicar_errado():
    global score
    escolher_pergunta()
    if resposta_certa == 'False':
        score+=1
        score_na_janela['text'] = f'Score: {score}'




#Banco de perguntas
parametros = {
    'amount': 10,
    'type': 'boolean'
}
resposta = requests.get(url='https://opentdb.com/api.php', params=parametros)
resposta.raise_for_status()
data = resposta.json()




#Janela
janela = Tk()
janela.title('Quiz')
janela.config(padx=50, pady=50, bg= THEME_COLOR, highlightthickness=0)

#Score
score_na_janela = Label(text= f'Score: {score}', fg='white', bg=THEME_COLOR)
score_na_janela.grid(row=0, column=1)



#Canvas
canvas = Canvas(width=300, height=250)
pergunta_no_canvas = canvas.create_text(150,125, text='', font=('Arial',20,'italic'),width=250)
canvas.config(highlightthickness=0)
canvas.grid(row=1, column=0, columnspan=2,pady=50)
escolher_pergunta()
canvas.itemconfig(pergunta_no_canvas, text=pergunta)



#Butao Certo
foto_botao_certo = PhotoImage(file='imagens/Day34/true.png')
butao_certo = Button(image=foto_botao_certo, highlightthickness=0, bg= THEME_COLOR, command=clicar_certo)
butao_certo.config(padx=50, pady=50)
butao_certo.grid(row=2,column=0)

#Butao Errado
foto_botao_errado = PhotoImage(file='imagens/Day34/false.png')
butao_errado = Button(image=foto_botao_errado, highlightthickness=0, bg= THEME_COLOR, command=clicar_errado)
butao_errado.grid(row=2,column=1)





























janela.mainloop()