import random

words = ['melancia','rato','teclado','fone','camelo']
palavra = random.choice(words)
letras = len(palavra)
vidas = 6
x = letras
traços = []


while x > 0:
    traços.append('_')
    x = x -1

print(''.join(traços))
while vidas > 0 and letras > 0:
    v = input('Escolha uma letra: ').lower()
    for i,k in enumerate(palavra):
        if k == v:
            traços[i] = k
            letras = letras - 1
        else:
            None
    if v not in palavra:
        print('Não tem essa letra')
        vidas = vidas - 1
        print('Você ainda tem {} vidas'.format(vidas))
    print(''.join(traços))

if letras == 0:
     print('PARABENS, VOCE GANHOU !!!')
if vidas == 0:
     print('QUE PENA, VOCE PERDEU :(')
            
