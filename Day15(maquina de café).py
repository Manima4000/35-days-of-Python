menu = {
    'espresso':{
        'water': 50,
        'coffe': 18,
        'milk': 0,
        'custo': 1.5
    },
    'latte':{
        'water': 200,
        'coffe': 24,
        'milk': 150,
        'custo': 2.5
    },
    'capucciono':{
        'water': 250,
        'coffe': 24,
        'milk': 100,
        'custo': 3
    }
}

recurso_da_maquina = {
    'water': 500,
    'coffe': 150,
    'milk': 400
}

def espresso():
    if escolha == 'espresso':
        if menu['espresso']['water'] > recurso_da_maquina['water']:
            print("Desculpa, não temos mais água")
        elif menu['espresso']['coffe'] > recurso_da_maquina['coffe']:
            print("Desculpa, não temos café")
        elif menu['espresso']['milk'] > recurso_da_maquina['milk']:
            print("Desculpa, não temos leite")
        else:
            m1 = int(input('Você irá inserir quantas moedas de 1 real? '))
            m2 = int(input('Você irá inserir quantas moedas de 50 centavos? '))
            m3 = int(input('Você irá inserir quantas moedas de 25 centavos? '))
            m4 = int(input('Você irá inserir quantas moedas de 10 centavos? '))
            m2 = 0.5*m2
            m3 = 0.25*m3
            m4 = 0.1*m4
            soma = m1 + m2 + m3 + m4
            if soma < menu['espresso']['custo']:
                print("Você inseriu um valor menor que o valor do produto. Você terá seu dinheiro de volta.")
            else:
                print(f"Você insiriu {soma} reais e recebrá {float(soma - menu['espresso']['custo'])} de troco")
                for key in recurso_da_maquina:
                    recurso_da_maquina[key] = recurso_da_maquina[key] - menu['espresso'][key]

def latte():
    if escolha == 'latte':
        if menu['latte']['water'] > recurso_da_maquina['water']:
            print("Desculpa, não temos mais água")
        elif menu['latte']['coffe'] > recurso_da_maquina['coffe']:
            print("Desculpa, não temos café")
        elif menu['latte']['milk'] > recurso_da_maquina['milk']:
            print("Desculpa, não temos leite")
        else:
            m1 = int(input('Você irá inserir quantas moedas de 1 real? '))
            m2 = int(input('Você irá inserir quantas moedas de 50 centavos? '))
            m3 = int(input('Você irá inserir quantas moedas de 25 centavos? '))
            m4 = int(input('Você irá inserir quantas moedas de 10 centavos? '))
            m2 = 0.5*m2
            m3 = 0.25*m3
            m4 = 0.1*m4
            soma = m1 + m2 + m3 + m4
            if soma < menu['latte']['custo']:
                print("Você inseriu um valor menor que o valor do produto. Você terá seu dinheiro de volta.")
            else:
                print(f"Você insiriu {soma} reais e recebrá {float(soma - menu['latte']['custo'])} de troco")
                for key in recurso_da_maquina:
                    recurso_da_maquina[key] = recurso_da_maquina[key] - menu['latte'][key]

def capucciono():
    if escolha == 'capucciono':
        if menu['capucciono']['water'] > recurso_da_maquina['water']:
            print("Desculpa, não temos mais água")
        elif menu['capucciono']['coffe'] > recurso_da_maquina['coffe']:
            print("Desculpa, não temos café")
        elif menu['capucciono']['milk'] > recurso_da_maquina['milk']:
            print("Desculpa, não temos leite")
        else:
            m1 = int(input('Você irá inserir quantas moedas de 1 real? '))
            m2 = int(input('Você irá inserir quantas moedas de 50 centavos? '))
            m3 = int(input('Você irá inserir quantas moedas de 25 centavos? '))
            m4 = int(input('Você irá inserir quantas moedas de 10 centavos? '))
            m2 = 0.5*m2
            m3 = 0.25*m3
            m4 = 0.1*m4
            soma = m1 + m2 + m3 + m4
            if soma < menu['capucciono']['custo']:
                print("Você inseriu um valor menor que o valor do produto. Você terá seu dinheiro de volta.")
            else:
                print(f"Você insiriu {soma} reais e recebrá {float(soma - menu['capucciono']['custo'])} de troco")
                for key in recurso_da_maquina:
                    recurso_da_maquina[key] = recurso_da_maquina[key] - menu['capucciono'][key]


escolha = input('O que você deseja? (espresso/latte/capucciono): ')
if escolha == 'off':
    print('A maquina encerrou.')

while escolha != 'off':

    if escolha == 'report':
        print(f"Water: {recurso_da_maquina['water']}\nCoffe: {recurso_da_maquina['coffe']}\nMilk: {recurso_da_maquina['milk']}")

    elif escolha ==  'espresso':
        espresso()

    elif escolha == 'latte':
        latte()

    elif escolha == 'capucciono':
        capucciono()
    escolha = input("Deseja pedir mais alguma coisa? (espresso/latte/capucciono): ")

if escolha == 'off':
    print("A Maquina encerrou")
