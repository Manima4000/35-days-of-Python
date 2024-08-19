frutas = ['maça','limao','melancia']
def fazer_torta(index):
    try: #Tenta o try
        fruta = frutas[index]
        print('Torta de', fruta)
    except IndexError: #Caso de merda no try, o except é executado
        print('Torta de fruta')
    #else: é executado caso de bom
    #finally: é executado sempre


