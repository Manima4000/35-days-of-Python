from turtle import Turtle, Screen
import random as rd
import time

MOVE_DISTANCE = 20
CARS_MOVE = 2
DIFICULDADE = 2


screen = Screen()
screen.setup(width= 600, height=600)
screen.bgcolor('white')
screen.title('Atravessar a rua')
screen.tracer(0)
cars = []
colors = ['red','blue','purple','green','yellow','pink','orange']


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.color('black')
        self.shape('turtle')
        self.goto(0,-280)
        self.left(90)
    
    def up(self):
        self.forward(MOVE_DISTANCE  )

class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.color(rd.choice(colors))
        self.shape('square')
        self.left(180)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(rd.randint(250,300),rd.randint(-260,300))
    
    
    def move(self):
        self.forward(CARS_MOVE)
    
class Score(Turtle):
    def __init__(self,x_cord,y_cord):
        super().__init__()
        self.placar = 0
        self.pu()
        self.color('black')
        self.speed('fastest')
        self.hideturtle()
        self.goto(x_cord,y_cord)

    
    def aumentar_score(self):
        self.clear()
        self.placar = self.placar + 1
    

level = Score(-230,250)

player = Player()

GAME_OVER = Score(0,0)



screen.listen()
screen.onkey(key = 'Up', fun=player.up)

games_is_on = True
while games_is_on:
    screen.update()
    time.sleep(0.01)
    level.write(f'Level: {level.placar}',align='center',font = ('Arial', 16, 'normal'))
    k = rd.randint(1,6)
    if k == 1:
        carro = Cars()
        cars.append(carro)
    for i in range(0,len(cars)-1):
        cars[i].move()
    for car in cars:
        if abs(player.xcor() - car.xcor()) <= 20 and abs(player.ycor() - car.ycor()) <= 15:
            GAME_OVER.write(arg = 'GAME OVER',move = False,align= 'center', font= ('Arial', 32, 'normal'))
            games_is_on = False
    if player.ycor() >= 280:
        level.clear()
        level.placar += 1
        player.goto(0,-280)
        CARS_MOVE += 1.5
    






































screen.exitonclick()