import random

numero = random.randint(0,101)

def verificar(a,b,vidas):
    if a > b:
        return print(f"Muito grande\nVocê ainda tem {vidas} chutes")
    if a < b: 
        return print(f"Muito pequeno\nVocê ainda tem {vidas} chutes")
    if a == b: return print(f"Parabens!! Você acertou i número com {vidas+1} vidas")

def easy():
    vidas = 10
    print(f"Você tem {vidas} para acertar o numero")
    chute = int(input("Faça um chute: "))
    if chute == numero:
        return print(f"Parabens!! Você acertou o número com {vidas} vidas")
    else:
        while chute != numero and vidas > 1:
            vidas = vidas - 1
            verificar(chute,numero,vidas)
            chute = int(input('Faça outro chute: '))
        if chute == numero and vidas !=0: return  print(f"Parabens!! Você acertou i número com {vidas} vidas")
        if vidas == 1: return print("Você perdeu :(")

def hard():
    vidas = 5
    print(f"Você tem {vidas} para acertar o numero")
    chute = int(input("Faça um chute: "))
    if chute == numero:
        return print(f"Parabens!! Você acertou o número com {vidas} vidas")
    else:
        while chute != numero and vidas > 1:
            vidas = vidas - 1
            verificar(chute,numero,vidas)
            chute = int(input('Faça outro chute: '))
        if chute == numero and vidas !=0: return  print(f"Parabens!! Você acertou i número com {vidas} vidas")
        if vidas == 1: return print("Você perdeu :(")   
    


choose = input("Bem vendo ao jogo de adivinhar numeros !\nEu estou pensando em um número entre 1 e 100.\nEscolha a dificuldade. Escrve 'facil' ou 'dificil': ")
if choose == "facil":
    easy()
if choose == "dificil":
    hard()


