def pintura(b,h,t):
    b = float(input('Qual a base da parade? '))
    h = float(input('Qual a altura da parede? '))
    t = float(input('Quantos metros quadrado seu balde de tinta consegue pintar? '))
    area = b*h
    if area % t ==0:
        print('Voce precisará de {} baldes de tinta'.format(int(area/t)))
    else:
        print('Voce precisará de {} base de tinta'.format(int(area//t + 1)))

def numero_primo(n):
    k = 0
    if n == 2:
        print('O número 2 não é primo')
    else:
        for i in range(2,n):
            v = n%i
            if v == 0:
                k += 1
            else:
                None
        if k == 0:
            print('O número {} é primo !'.format(n))
        else:
            print('O número {} não é primo !'.format(n))


def criptografar(s):
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
    mensagem = input('Digite sua mensagem: ').lower()
    criptografa = []
    mensagem_criptografada = ''
    for letra in mensagem:
        if letra == ' ':
            criptografa.append(' ')
        else:
            for i in range(0,26):
                if letra == alfabeto[i]:
                    criptografa.append(alfabeto[i+s])
                else:
                    None
    for l in criptografa:
        mensagem_criptografada = mensagem_criptografada + l
    print(f'A mensagem criptografada é : {mensagem_criptografada}')

def descriptografar(s):
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
    mensagem = input('Digite sua mensagem criptografa: ').lower()
    descriptografada = []
    mensagem_descriptografada = ''
    for letra in mensagem:
        if letra == ' ':
            descriptografada.append(' ')
        else:
            for i in range (26,52):
                if letra == alfabeto[i]:
                    descriptografada.append(alfabeto[i-s])
                else:
                    None
    for l in descriptografada:
        mensagem_descriptografada = mensagem_descriptografada + l
    print(f'A mensagem criptografada é : {mensagem_descriptografada}')






                    


