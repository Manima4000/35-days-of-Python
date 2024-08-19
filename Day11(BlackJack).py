import random


minhas_cartas = []
cartas_do_computador = []
game_over = False



def deal_card():
    cartas = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    carta = random.choice(cartas)
    return carta



def calculate_score(list):
    if sum(list) == 21 and len(list) == 2:
        return 0
    if sum(list) > 21 and 11 in list:
        list.remove(11)
        list.append(1)
    if sum(list) == 21:
        return 0
    return sum(list)



def comparar(minha_soma, soma_computador):
    if minha_soma > 21 and soma_computador > 21:
        return 'EMPATE'
    
    if minha_soma == soma_computador:
        return 'EMPATE'
    
    if minha_soma > 21 and soma_computador < 21:
        return 'VOCE PERDEU'
    
    if minha_soma <21 and soma_computador >21:
        return 'VOCE GANHOU'
    
    if minha_soma < 21 and soma_computador <21:

        if minha_soma != 0 and soma_computador != 0 and minha_soma > soma_computador:
            return 'VOCE GANHOU'
        
        if minha_soma != 0 and soma_computador != 0 and minha_soma < soma_computador:
            return "VOCE PERDEU"
        
        if minha_soma == 0:
            return 'VOCE GANHOU'
        
        if soma_computador == 0:
            'VOCE PERDEU'




#adicionando cartas nos decks:
for i in range(2):
    minhas_cartas.append(deal_card())
    cartas_do_computador.append(deal_card())


while not game_over:
    #SOMANDO AS CARTAS:
    minha_soma = calculate_score(minhas_cartas)
    soma_computador = calculate_score(cartas_do_computador)

    print(f'Suas cartas: {minhas_cartas}, Soma: {minha_soma}')
    print(f"Primeira carta do Computador: {cartas_do_computador[0]}")

    if minha_soma == 0 or soma_computador == 0 or minha_soma > 21:
        game_over = True

    p = input('Você deseja comprar uma carta? Digite s ou n: ')

    if p.lower() == 'n':
        game_over = True

    if p.lower() == 's':
        minhas_cartas.append(deal_card())
        
while soma_computador != 0 and soma_computador < 17:
    cartas_do_computador.append(deal_card())
    soma_computador = calculate_score(cartas_do_computador)

print(f"Suas Cartas: {minhas_cartas}, Soma: {minha_soma}")
print(f'Cartas do computador: {cartas_do_computador}, Soma: {soma_computador}')
print(comparar(minha_soma,soma_computador))
   

