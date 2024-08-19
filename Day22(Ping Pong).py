from turtle import Turtle, Screen
import time
import random as rd

SPEED_BALL = 0

class Paddle(Turtle):
    def __init__(self,x_cor):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('white')
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(x_cor,0)
    
    def up(self):
        new_y = self.ycor() + 20
        x = self.xcor()
        self.goto(x,new_y)
    
    def down(self):
        new_y = self.ycor() - 20
        x = self.xcor()
        self.goto(x,new_y)
    
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.shape('circle')
        self.color('white')
        self.x_move = 4
        self.y_move = 4
        
        
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)
    
    def bounce(self):
        self.y_move *= -1
    
    def colision(self):
        self.x_move *= -1

class Score(Turtle):
    def __init__(self,x_cord,y_cord):
        super().__init__()
        self.placar = 0
        self.pu()
        self.color('white')
        self.speed('fastest')
        self.hideturtle()
        self.goto(x_cord,y_cord)

    
    def aumentar_score(self):
        self.clear()
        self.placar = self.placar + 1
    


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Ping Pong')
screen.tracer(0)

linha_central = Turtle()
linha_central.pu()
linha_central.left(90)
linha_central.color('white')
linha_central.goto(0,-410)
for i in range(0,13):
    linha_central.pd()
    linha_central.forward(30)
    linha_central.pu()
    linha_central.forward(30)


paddle1 = Paddle(350)
paddle2 = Paddle(-350)
ball = Ball()
score1 = Score(100,200)
score2 = Score(-100,200)
game_ove = Score(0,0)
winner = Score(0,-50)


screen.listen()
screen.onkey(key= "Up", fun = paddle1.up)
screen.onkey(key= "Down", fun = paddle1.down)
screen.onkey(key= "w", fun = paddle2.up)
screen.onkey(key= "s", fun = paddle2.down)
paddles = [paddle1, paddle2]
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.01)
    score1.write(f'{score1.placar}',align='center',font = ('Arial', 64, 'normal'))
    score2.write(f'{score2.placar}',align='center',font = ('Arial', 64, 'normal'))
    ball.move()
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce()
    if ball.xcor() == paddle1.xcor()-10 and ball.distance(paddle1) <= 50:
        ball.colision()
    if ball.xcor() == paddle2.xcor()+10 and ball.distance(paddle2) <= 50:
        ball.colision()
    if ball.xcor() >= 400:
        score2.clear()
        score2.placar += 1
        ball.goto(0,0)
    if ball.xcor() <= -400:
        score1.clear()
        score1.placar += 1
        ball.goto(0,0)
    if score1.placar == 5 or score2.placar == 5:
        game_is_on = False
        game_ove.write(arg = 'GAME OVER',move = False,align= 'center', font= ('Arial', 32, 'normal'))
        if score1.placar == 5:
            winner.write(arg = 'JOGADOR 1 VENCEU',move = False,align= 'center', font= ('Arial', 24, 'normal'))
        else:
            winner.write(arg = 'JOGADOR 2 VENCEU',move = False,align= 'center', font= ('Arial', 24, 'normal'))

        
    



































screen.exitonclick()