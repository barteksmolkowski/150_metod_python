def is_nested(listy):
    if not listy:
        return False
    for i in range(len(listy)):
        if type(listy[i]) != list:
            return False
    return True

def is_all_equal(lista):
    zmienna = lista[0]
    for i in range(len(lista)):
        if lista[i] != zmienna:
            return False
    return True

def is_valid_array(macierz):
    if macierz == None:
        return True
    else:
        for i in range(len(macierz)):
            if type(macierz[i]) != list:
                return False
        dlugosc_wiersza = len(macierz[0])
        for i in range(len(macierz)):
            if len(macierz[i]) != dlugosc_wiersza:
                return False
        return True

def swap_elements_easy(lista):
    ostatnia = lista[len(lista) - 1]
    lista.remove(ostatnia)
    lista.append(lista[0])
    lista[0] = ostatnia
    return lista

def swap_elements_hard(lista, index1, index2):
    zmiana = lista[index1]
    lista[index1] = lista[index2]
    lista[index2] = zmiana
    return lista

def reverse_words(tekst):
    tablica = []
    slowo = ""
    for i in range(len(tekst)):
        if tekst[i] == " ":
            tablica.append(slowo)
            slowo = ""
        else:
            slowo += tekst[i]
        if i == len(tekst) - 1:
            tablica.append(slowo)

    n_tablica = []
    i = len(tablica) - 1
    while i >= 0:
        n_tablica.append(tablica[i])
        i -= 1

    return " ".join(n_tablica)

def remove_common_elements(tablica1, tablica2):
    if len(tablica1) > len(tablica2):
        tablica1, tablica2 = tablica2, tablica1

    for element in tablica2:
        while element in tablica1:
            tablica1.remove(element)
    return tablica1, tablica2

def convert(data):
    slownik = {"user":[], "main_technology":[]}
    for i in range(len(data)):
        slownik["user"].append(data[i]["user"])
        slownik["main_technology"].append(data[i]["main_technology"])

    return slownik

def get_indices_easy(tablica, element):
    indeksy = []
    for i in range(len(tablica)):
        if tablica[i] == element:
            indeksy.append((i))
    return indeksy

def get_indices_hard(tablica):
    indeksy = []
    for i in range(len(tablica)):
        if type(tablica[i]) == str:
            indeksy.append(i)
    return indeksy