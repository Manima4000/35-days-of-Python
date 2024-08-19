from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
screen.title('Estados dos EUA')
image = 'arquivos/blank_states_img.gif'
screen.addshape(image)
turtle = Turtle()
turtle.shape(image)

class State(Turtle):
    def __init__(self,x,y,name):
        super().__init__()
        self.pu()
        self.hideturtle()
        self.color('black')
        self.speed('fastest')
        self.goto(x,y)
        self.write(arg = name,move = False,align= 'center', font= ('Arial', 8, 'normal'))


# def obter_coordenadas(x,y):
#     print(x,y)
# screen.onscreenclick(obter_coordenadas)
# screen.mainloop()

game_is_on = True
data = pd.read_csv('arquivos/50_states.csv')
estados = data.state
x_cord = data.x
y_cord = data.y
all_states = estados.to_list()
estados_certos = []
while game_is_on:
    resposta_estado = screen.textinput(title='Adivinhe um Estado', prompt='Digite o nome de um estado')
    if resposta_estado.title() in all_states:
        estados_certos.append(resposta_estado.title())
        posição = all_states.index(resposta_estado.title())
        estado = State(x_cord[posição],y_cord[posição],resposta_estado.title())
    elif resposta_estado.lower() == 'exit':
        game_is_on = False
        estados_restantes = [state for state in all_states if state not in estados_certos]
        print(estados_certos)
        print(estados_restantes)
    

































screen.exitonclick()
