import random as rd
from turtle import Turtle, Screen

timmy1 = Turtle('turtle')
timmy1.color('blue')
timmy2 = Turtle(shape="turtle")
timmy2.color('red')
timmy3 = Turtle('turtle')
timmy3.color('yellow')
timmy4 = Turtle(shape="turtle")
timmy4.color('black')
timmy5 = Turtle(shape="turtle")
timmy5.color('pink')
timmy1.speed(5)
timmy2.speed(5)
timmy3.speed(5)
timmy4.speed(5)
timmy5.speed(5)



screen = Screen()
screen.setup(950,500)


def mover_para_frente():
    timmy1.forward()

def mover_para_tras():
    timmy1.backward(10)

def girar_anti():
    timmy1.left(10)

def girar_hor():
    timmy1.right(10)

def limpar_desenho():
    timmy1.clear()
    timmy1.pu()
    timmy1.home()
    timmy1.pd()    

screen.listen()


def desenho():
    screen.onkey(key = 'w', fun = mover_para_frente)
    screen.onkey(key = 's', fun = mover_para_tras)
    screen.onkey(key = 'a', fun = girar_anti)
    screen.onkey(key = 'd', fun = girar_hor)
    screen.onkey(key = 'c', fun = limpar_desenho)


def corrida():
    tartarugas = [timmy1, timmy2, timmy3, timmy4, timmy5]
    aposta = screen.textinput(title = "Faça sua aposta", prompt= 'Qual tartaruga ganhará a corrida? ')
    def teleportar(n,x,y):
        n.pu()
        n.setpos(x,y)
    teleportar(timmy1,-450,200)
    teleportar(timmy2,-450,100)
    teleportar(timmy3,-450,0)
    teleportar(timmy4,-450,-100)
    teleportar(timmy5,-450,-200)
    k = 0
    while k==0:
        for turtle in tartarugas:
            if turtle.xcor() > 400:
                k = turtle
                break
            else:
                turtle.forward(rd.randint(0,15))
    if aposta == k.pencolor():
        print("VOCE GANHOU")
    else:
        print(f'Voce perdeu, o vencedeor é o {k.pencolor()}')
    


     

corrida()

screen.exitonclick()