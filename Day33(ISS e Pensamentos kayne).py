import requests
from tkinter import *

# resposta = requests.get(url='http://api.open-notify.org/iss-now.json')
# print(resposta) #reposta foi 200, logo foi bem sucedido

# #Tipos de resposta
# #1XX => algo esta a acontecer, isso não é definitivo
# #2XX => você conseguiu oq querida, está td certo
# #3XX => Geralmente vc não tem permissão pra acessar esses dados, vá embora
# #4XX ou 404=> Voce fez merda
# #5XX => servidor/website caiu

# data = resposta.json()
# longitude = data['iss_position']['longitude']
# latitude = data['iss_position']['latitude']
# iss_position = (longitude, latitude)
# print(iss_position)

# ---------------------------------------------------------------- Projeto 2 ---------------------------------------------------------------- #

# def obter_pensamento():
#     resposta_kayne = requests.get(url='https://api.kanye.rest')
#     resposta_kayne.raise_for_status()
#     data_kayne = resposta_kayne.json()
#     quote = data_kayne['quote']
#     canvas.itemconfig(pensamento, text=quote)

# janela = Tk()
# janela.title('Gerador de fala do Kayne')
# janela.config(padx=50, pady=50)

# canvas = Canvas(width=300, height=414)
# imagem_balao = PhotoImage(file='imagens/Day33/background.png')
# canvas.create_image(150, 207, image=imagem_balao)
# pensamento = canvas.create_text(150,207,text='Vamos começar os pensamentos', fill='white', font=("Arial",20,'bold'), width=250)
# canvas.pack()

# foto_kayne = PhotoImage(file='imagens/Day33/kanye.png')
# butao_kayne = Button(image=foto_kayne, highlightthickness=0, command=obter_pensamento)
# butao_kayne.pack()

# janela.mainloop()

# ---------------------------------------------------------------- Projeto 2 ---------------------------------------------------------------- #

# ---------------------------------------------------------------- Projeto 3 ---------------------------------------------------------------- #
#API COM PARAMETROS

MINHA_LAT = -22.996389
MINHA_LNG = -43.400200

parametros = {
    'lat': MINHA_LAT,
    'lng': MINHA_LNG,
    'formatted': 0
}


resposta = requests.get(url='https://api.sunrise-sunset.org/json', params=parametros)
resposta.raise_for_status()
data = resposta.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']
print(sunrise.split('T')[1].split('+')[0]) #pegando o horario do nascer do sol
print(sunset.split('T')[1].split('+')[0]) #pegando o horario do por do sol














# ---------------------------------------------------------------- Projeto 3 ---------------------------------------------------------------- #