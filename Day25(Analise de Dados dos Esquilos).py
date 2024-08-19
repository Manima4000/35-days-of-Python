import pandas as pd

#LENDO OS DADOS COM PANDAS
data = pd.read_csv('arquivos/Dados_Esquilos.csv')

#FAZENDO A CONTAGEM DOS ESQUILOS DE ACORDO COM AS CORES
gray = data[data['Primary Fur Color'] == 'Gray']
number_gray = len(gray)

cinnamon = data[data['Primary Fur Color'] == 'Cinnamon']
number_cinnamon = len(cinnamon)

black = data[data['Primary Fur Color'] == 'Black']
number_black = len(black)

#CRIANDO UM ARQUIVO EM CSV 
dados_dict = {
    'cores': ['Gray','Cinnamon','Black'],
    'contagem': [number_gray,number_cinnamon,number_black]
}
dados_dataframe = pd.DataFrame(dados_dict)
dados_dataframe.to_csv('arquivos/dados_esquilos_cores.csv')


