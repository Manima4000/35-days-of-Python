import random as rd
from turtle import Turtle, Screen
import time
POSICOES_INICIAIS = (0,-20,-40)
DISTANCIA_DO_MOVIMENTO = 20


screen = Screen()
screen.setup(width= 600, height=600)
screen.bgcolor('black')
screen.title('Jogo da Cobrinha')
screen.tracer(0)
class Cobra:
    def __init__(self):
        self.segmentos = []
        self.create()
        self.cabeça = self.segmentos[0]
    
    def create(self):
        for segmento in POSICOES_INICIAIS:
            novo_segmento = Turtle('square')
            novo_segmento.pu()
            novo_segmento.color('white')
            novo_segmento.setx(segmento)
            self.segmentos.append(novo_segmento)
    
    def move(self):
        for seg in range(len(self.segmentos)-1,0,-1):
            new_x = self.segmentos[seg-1].xcor()
            new_y = self.segmentos[seg-1].ycor()
            self.segmentos[seg].goto(new_x,new_y)
        self.cabeça.forward(DISTANCIA_DO_MOVIMENTO)
    
    def crescer(self):
        novo_segmento = Turtle('square')
        novo_segmento.speed('fastest')
        novo_segmento.pu()
        novo_segmento.color('black')
        new_x = self.segmentos[-1].xcor()
        new_y = self.segmentos[-1].ycor()
        novo_segmento.goto(new_x,new_y)
        self.segmentos.append(novo_segmento)
        novo_segmento.color('white')

    
    def up(self):
        if self.cabeça.heading() == 270:
            None
        else:
            self.cabeça.setheading(90)

    def down(self):
        if self.cabeça.heading() == 90:
            None
        else:
            self.cabeça.setheading(270)

    def left(self):
        if self.cabeça.heading() == 0:
            None
        else:
            self.cabeça.setheading(180)

    def right(self):
        if self.cabeça.heading() == 180:
            None
        else:
            self.cabeça.setheading(0)

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) #diminuir as dimensões pela metade
        self.color('blue')
        self.speed('fastest')
        self.goto(rd.randint(-280,280),rd.randint(-280,280))
    
    def gerar_pos(self):
        self.goto(rd.randint(-280,280),rd.randint(-280,280))

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.placar = 0
        with open('arquivos/highscore(Cobrinha).txt', 'r') as file:
            self.highscore = int(file.read())
        self.pu()
        self.color('white')
        self.speed('fastest')
        self.hideturtle()
        self.goto(0,260)

    
    def aumentar_score(self):
        self.clear()
        self.placar = self.placar + 1
        

food = Food()
score = Score()
game_ove = Score()
game_ove.goto(0,0)

c = Cobra()
screen.listen()
screen.onkey(key = 'Up', fun = c.up)
screen.onkey(key = 'Down', fun = c.down)
screen.onkey(key = 'Left', fun = c.left)
screen.onkey(key = 'Right', fun = c.right)



games_is_on = True

while games_is_on:
    screen.update()
    time.sleep(0.1)
    score.write(f'Score: {score.placar} / Highscore: {score.highscore}',align='center',font = ('Arial', 16, 'normal'))
    c.move()
    if c.cabeça.distance(food) < 20:
        food.gerar_pos()
        score.aumentar_score()
        c.crescer()
    if c.cabeça.xcor() > 290 or c.cabeça.xcor() <-290 or c.cabeça.ycor() > 290 or c.cabeça.ycor() < -290:
        games_is_on = False
        if score.placar > score.highscore:
            score.highscore = score.placar
            with open('arquivos/highscore(Cobrinha).txt', 'w') as file:
                file.write(str(score.highscore))
        game_ove.write(arg = 'GAME OVER',move = False,align= 'center', font= ('Arial', 32, 'normal'))
    for segmento in c.segmentos[1:]:
        if c.cabeça.distance(segmento) < 10:
            if score.placar > score.highscore:
                score.highscore = score.placar
                with open('arquivos/highscore(Cobrinha).txt', 'w') as file:
                    file.write(str(score.highscore))
            games_is_on = False
            game_ove.write(arg = 'GAME OVER',move = False,align= 'center', font= ('Arial', 32, 'normal'))
        
        





































screen.exitonclick()