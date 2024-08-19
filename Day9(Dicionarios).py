livro_de_viagens = [
    {
        'pais': 'Estados Unidos',
        'cidades': ['Nova York', 'Orlando'],
        'total': 4
     },
    {
        'pais': 'Brasil',
        'cidades': ['Rio de Janeiro', 'Sao Paulo', 'Florianopolis'],
        'total': 12
    }
]
def atualizar_viagens(pais, cidades, total):
    dicionario = {'pais': pais,
                  'cidades': cidades, 
                  'total': total
                  } 
    livro_de_viagens.append(dicionario)


def leilao():
    dicionario = {}
    name = input('Qual o seu nome?  ')
    lance = int(input('Qual o seu lance? '))
    p = input('Digite sim se havará mais algum lance de alguma pessoa ou não se não haverá: ').lower()
    dicionario[name] = lance
    while p == 'sim':
        name = input('Qual o seu nome?  ')
        lance = int(input('Qual o seu lance? '))
        p = input('Digite sim se havará mais algum lance de alguma pessoa ou não se não haverá: ').lower()
        dicionario[name] = lance
    j = 0
    k = ''
    for key in dicionario:
        if dicionario[key] > j:
            j = dicionario[key]
            k = key
        else: None
    print(f'O Ganhador do leilão é o {k} com um lance de {j}')

leilao()




    