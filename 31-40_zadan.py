def preprocess_easy(lista_tupli):
    for i in range(len(lista_tupli) - 1, -1, -1):
        if len(lista_tupli[i]) == 1:
            lista_tupli.pop(i)
    return lista_tupli

def preprocess_hard(lista_krotek):
    for i in range(len(lista_krotek) - 1, -1, -1):
        if all(elementy is None for elementy in lista_krotek[i]):
            lista_krotek.pop(i)
    return lista_krotek

def flatten_easy(lista):
    n_lista = []
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            n_lista.append(lista[i][j])
    return n_lista

def flatten_hard(lista):
    hasztagi_txt = ""
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            hasztagi_txt += "#" + lista[i][j] + " "

    return hasztagi_txt[:-1]

data = {
    'device_id': '3057304985',
    'temp': [23.5, 22.0, 23.1, 25.5, 24.1],
    'city': 'Warsaw',
    'country': 'Poland'
}

def calculate(data):
    temp = []
    for i in range(len(data)):
        if type(data[i][1]) == list:
            for j in range(len(data[i])):
                temp.append(data[i][j])
    return temp

print(calculate(data))