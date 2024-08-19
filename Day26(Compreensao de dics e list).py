import pandas as pd
#COMPRENSSAO DE LISTAS
#new_list = [new_value for item in list if test]

# nome = 'Matheus'
# letras = [letra for letra in nome]
# print(letras)

# range_novo = [2*n for n in range(1,5)]
# print(range_novo)

# nomes = ['Alec', 'Matheus', 'Ana', 'Raquel Belchior']
# nomes_curtos = [elemento for elemento in nomes if len(elemento) <= 4]
# print(nomes_curtos)
# nomes_longos_em_caps = [elemento.upper() for elemento in nomes if len(elemento) >= 5]
# print(nomes_longos_em_caps)

with open('arquivos/day26(1).txt') as file1:
    linha1 = file1.readlines()
    lista1 = [n.strip() for n in linha1] #TIRANDO O '\N' DE CADA LINHA DE

with open('arquivos/day26(2).txt') as file2:
    linha2 = file2.readlines()
    lista2 = [n.strip() for n in linha2] #TIRANDO O '\N' DE CADA LINHA

intersecção = [n for n in lista1 if n in lista2]
print(intersecção)




#COMPREENSÃO DE DICS
#new_dict = {new_key: new_value for item in list if test}
#ou
#new_dict = {new_key: new_value for (key,value) in dict.items() if test}


# nomes = ['Alec', 'Matheus', 'Ana', 'Raquel Belchior']
# import random
# pontos_dos_estudantes = {estudante: random.randint(60,100) for estudante in nomes}
# print(pontos_dos_estudantes)
# estudantes_aprovados = {estudante: 'APROVADO' for (estudante,value) in pontos_dos_estudantes.items() if value >= 70}
# print(estudantes_aprovados)


# resposta = input('Digite uma frase: ')
# lista_resposta = resposta.split()
# new_dict = {palavra: len(palavra) for palavra in lista_resposta}
# print(new_dict)

# temp_c = {'Monday': 12, 'Tueday': 20, 'Wednesday':30}
# temp_f = {key: value*1.8 + 32 for (key,value) in temp_c.items()}
# print(temp_f)



# dict_estudantes = {
#     'estudante': ['Matheus', 'Raquel Belchior', 'Morel'],
#     'nota': [89,88,60]
# }
# data_estudantes = pandas.DataFrame(dict_estudantes)
# # for (key,value) in data_estudantes.items():
# #     print(value)
# for (index,row) in data_estudantes.iterrows():
#     if row.estudante == 'Matheus':
#         print(row.nota)

dados = pd.read_csv('arquivos/alfabeto_militar.csv')
resposta = input('Qual o seu nome: ')
dicionario = {row.letter: row.code for (index,row) in dados.iterrows()}
lista_militar = []
for letra in resposta:
    lista_militar.append(dicionario[letra.upper()])
print(lista_militar)
