# with open('arquivos/weather_data.csv','r') as data_file:
#     data = data_file.readlines()
#     print(data)


# import csv
# with open('arquivos/weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperaturas = []
#     for row in data:
#         if row[1] != 'temp':
#             temperaturas.append(int(row[1]))
#     print(temperaturas)


import pandas as pd

data = pd.read_csv('arquivos/weather_data.csv')
print(data)
print('\n')
print(data['temp'])

data_in_dic = data.to_dict() #TRANSFORMANDO UMA TABELA (DATA FRAME) EM DICIONARIO
print(data_in_dic)

temp_list = data['temp'].to_list() #TRANSFORMANDO UM ´SERIE' (COLUNA) EM LISTA
print(temp_list)
print(data['temp'].mean()) #CALCULA A MEDIA DE UMA SERIE, tem como calcular mediana/moda/outra coisas...
print(data['temp'].max()) #CALCULA O VALOR MAXIMO
print(data['temp'].mode()) #CALCULA A MODA

#OUTRA MANEIRA DE ESCREVER data['condition'] (COLUNA)
print(data.condition)

#DADOS EM UMA LINHA
print(data[data.day == 'Monday']) #RETORNA A LINHA QUE COMEÇA POR MONDAY (SE TIVESSE MAIS DE 1, IA PRINTAR TODAS)
print('\n')

#PRINTANDO A LINHA NO QUAL A TEMPERATURA É MAXIMA
print(data[data.temp == data.temp.max()])
print('\n')

#Acessando dados de um determinada linha
terça = data[data.day == 'Tuesday']
print(terça.condition)
print('\n')
temp_in_faren = int(terça.temp[1])*1.8 + 32
print(f'Temperatura da terça em farenheit: {temp_in_faren}°F')
print('\n')

#CRIANDO UM QUADRO DE DADOS DO 0
data_dict = {
    'students': ['Matheus','Raquel','Luiz'],
    'Age': [20,21,24]
}
data_frame = pd.DataFrame(data_dict)
print(data_frame)
# data_frame.to_csv('arquivos/criando_dataframe.csv')   #TAL LINHA É PRA CRIAR UM ARQUIVO DATA_FRAME (JÁ ESTÁ CRIANDO)