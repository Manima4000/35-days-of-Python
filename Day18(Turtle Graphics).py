from turtle import Turtle, Screen, colormode
import random as rd

timmy = Turtle(shape = 'arrow')

def poligono(n):
    ang_ext = 360/n
    for i in range(0,n):
        timmy.forward(100)
        timmy.right(ang_ext)

def random_color():
    r = rd.randint(0,255)
    g = rd.randint(0,255)
    b = rd.randint(0,255)
    random_color = (r,g,b)
    return random_color

def passeio_aleatorio(n):
    direções = [0,90,180,270]
    i = 0
    while i < n:
        timmy.pencolor(random_color())
        timmy.left(rd.choice(direções))
        timmy.forward(30)
        i += 1

def circulos(ang):
    if 360%ang == 0:
        n = int(360/ang)
        for i in range(0,n):
            timmy.pencolor(random_color())
            timmy.circle(150)
            timmy.left(ang)
    else:
        k = 1
        while k*360 % ang != 0:
            k += 1
        n = int(k*360/ang)
        for i in range(0,n):
            timmy.pencolor(random_color())
            timmy.circle(100)
            timmy.left(ang)

colormode(255)
timmy.pensize(1)
timmy.speed(0)

circulos(32)




















screen = Screen()
screen.exitonclick()