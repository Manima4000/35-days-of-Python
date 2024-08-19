def calculadora():
    numero1 = int(input('Qual o primeiro numero? '))
    operacao = input('+\n-\n*\n/\nQual a operação? ')
    numero2 = int(input('Qual o segundo numero? '))
    variavel = 'y'
    resultado = 0
    while variavel == 'y':
        if operacao == '+':
            resultado = numero1 + numero2
            print(f'O resultado dessa operação é {resultado}.')
            variavel = input(f'Você ainda quer fazer operação com {resultado}? Digite y para continuar: ')
            if variavel != 'y':
                break
            else:
                numero1 = resultado 
                operacao = input('Digite a operação: ')
                numero2 =int(input('Digite o segundo numero: '))
        elif operacao == '-':
            resultado = numero1 - numero2
            print(f'O resultado dessa operação é {resultado}.')
            variavel = input(f'Você ainda quer fazer operação com {resultado}? Digite y para continuar: ')
            if variavel != 'y':
                break
            else:
                numero1 = resultado 
                operacao = input('Digite a operação: ')
                numero2 =int(input('Digite o segundo numero: '))
        elif operacao == '*':
            resultado = numero1 * numero2
            print(f'O resultado dessa operação é {resultado}.')
            variavel = input(f'Você ainda quer fazer operação com {resultado}? Digite y para continuar: ')
            if variavel != 'y':
                break
            else:
                numero1 = resultado 
                operacao = input('Digite a operação: ')
                numero2 =int(input('Digite o segundo numero: '))
        elif operacao == '/':
            resultado = numero1 / numero2
            print(f'O resultado dessa operação é {resultado}.')
            variavel = input(f'Você ainda quer fazer operação com {resultado}? Digite y para continuar: ')
            if variavel != 'y':
                break
            else:
                numero1 = resultado 
                operacao = input('Digite a operação: ')
                numero2 =int(input('Digite o segundo numero: '))
    return resultado

calculadora()

