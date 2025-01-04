# Funkcje
def calculate(lista):
    for i in range(len(lista)):
        if lista[i] % 2 != 0:
            lista[i] = lista[i] * 2
    return lista

def sort_tuple(lista_tupli):
    return sorted(lista_tupli, key=lambda x: x[1])

def replace_neg(lista):
    for i in range(len(lista)):
        if lista[i] < 0:
            lista[i] = 0
    return lista

def count(lista):
    dodatnie, ujemne = 0, 0
    for liczba in lista:
        if liczba >= 0:
            dodatnie += 1
        else:
            ujemne += 1
    return (dodatnie, ujemne)

def preprocess_text(znaki):
    liczba = 0
    for i in znaki:
        try:
            liczba = liczba * 10 + int(i)
        except:
            continue
    return liczba

def preprocess_files(lista):
    wynik = []
    for i in range(len(lista)):
        if lista[i].endswith("png"):
            wynik.append(lista[i])
    return wynik

def make_hashtags(lista):
    znaki = ""
    for word in lista:
        znaki += f"#{word} "
    return znaki.strip()

def convert_numbers(text):
    slownik = {'2': 'two', '3': 'three'}
    slowa = text.split()
    for i in range(len(slowa)):
        if slowa[i] in slownik:
            slowa[i] = slownik[slowa[i]]
    return ' '.join(slowa)

def convert_text(text):
    tablica = text.split("_")
    for i in range(len(tablica)):
        tablica[i] = tablica[i][0].upper() + tablica[i][1:]
    wynik = "".join(tablica)
    return wynik

def convert_text_first(text):
    tablica = text.split("_")
    for i in range(1, len(tablica)):
        tablica[i] = tablica[i][0].upper() + tablica[i][1:]
    wynik = "".join(tablica)
    return wynik

# Uruchamianie testów
def test_calculate():
    assert calculate([1, 2, 3, 4]) == [2, 2, 6, 4]
    assert calculate([5, 6, 7, 8]) == [10, 6, 14, 8]
    assert calculate([1, 3, 5]) == [2, 6, 10]
    print("test_calculate: OK")

def test_sort_tuple():
    assert sort_tuple([(1, 3), (4, 2), (5, 1)]) == [(5, 1), (4, 2), (1, 3)]
    assert sort_tuple([(1, 7), (2, 5), (3, 2)]) == [(3, 2), (2, 5), (1, 7)]
    assert sort_tuple([(2, 2), (4, 4), (6, 1)]) == [(6, 1), (2, 2), (4, 4)]
    print("test_sort_tuple: OK")

def test_replace_neg():
    assert replace_neg([1, -2, 3, -4, 5]) == [1, 0, 3, 0, 5]
    assert replace_neg([10, -1, 6]) == [10, 0, 6]
    assert replace_neg([-9, -8]) == [0, 0]
    assert replace_neg([0, 3, 4]) == [0, 3, 4]
    print("test_replace_neg: OK")

def test_count():
    assert count([10, -1, 6]) == (2, 1)
    assert count([-9, -8]) == (0, 2)
    assert count([0, 3, 4]) == (3, 0)
    print("test_count: OK")

def test_preprocess_text():
    assert preprocess_text('hello123') == 123
    assert preprocess_text('456abc') == 456
    assert preprocess_text('a1b2c3') == 123
    assert preprocess_text('test!@#') == 0
    print("test_preprocess_text: OK")

def test_preprocess_files():
    assert preprocess_files(['image1.png', 'image2.jpg', 'image3.png']) == ['image1.png', 'image3.png']
    assert preprocess_files(['file1.txt', 'file2.png']) == ['file2.png']
    assert preprocess_files(['photo.png', 'video.mp4']) == ['photo.png']
    assert preprocess_files(['picture.jpeg']) == []
    print("test_preprocess_files: OK")

def test_make_hashtags():
    assert make_hashtags(['hello', 'world']) == "#hello #world"
    assert make_hashtags(['python', 'is', 'fun']) == "#python #is #fun"
    assert make_hashtags(['good', 'morning']) == "#good #morning"
    assert make_hashtags(['code']) == "#code"
    print("test_make_hashtags: OK")

def test_convert_numbers():
    assert convert_numbers('I have 2 apples and 3 oranges') == "I have two apples and three oranges"
    assert convert_numbers('123') == "123"
    assert convert_numbers('4') == "4"
    assert convert_numbers('2 and 3') == "two and three"
    print("test_convert_numbers: OK")

def test_convert_text():
    assert convert_text('this_is_a_test') == "ThisIsATest"
    assert convert_text('hello_world_python') == "HelloWorldPython"
    assert convert_text('goodbye_earth') == "GoodbyeEarth"
    assert convert_text('python_is_great') == "PythonIsGreat"
    print("test_convert_text: OK")

def test_convert_text_first():
    assert convert_text_first('this_is_a_test') == "thisIsATest"
    assert convert_text_first('hello_world_python') == "helloWorldPython"
    assert convert_text_first('goodbye_earth') == "goodbyeEarth"
    assert convert_text_first('python_is_great') == "pythonIsGreat"
    print("test_convert_text_first: OK")

# Uruchamianie testów
test_calculate()
test_sort_tuple()
test_replace_neg()
test_count()
test_preprocess_text()
test_preprocess_files()
test_make_hashtags()
test_convert_numbers()
test_convert_text()
test_convert_text_first()

print("\nWszystkie testy zakończone sukcesem!")