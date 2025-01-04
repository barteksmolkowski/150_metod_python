import itertools
def concat_easy(tablica1, tablica2):
    nowa_tab = []
    for i in range(min(len(tablica1), len(tablica2))):
        nowa_tab.append(tablica1[i] + tablica2[i])
    if len(tablica1) > len(tablica2):
        nowa_tab.extend(tablica1[len(tablica2):])
    elif len(tablica2) > len(tablica1):
        nowa_tab.extend(tablica2[len(tablica1):])
    return nowa_tab

def concat_hard(tablica1, tablica2):
    if len(tablica1) != len(tablica2):
        raise ValueError('The given lists are not of the same length.')
    return [tablica1[i] + tablica2[i] for i in range(len(tablica1))]

def sort_by_row(lista):
    return [sorted(row) for row in lista]

def top3(data):
    result = []
    for row in data:
        result.append(sorted(row, reverse=True)[:3])
    return result

def filter_users(user_data):
    return [user for user in user_data if "level" in user]

def remove_repetitive(numbers):
    def has_repetitive_digits(number):
        digits = str(number)
        return len(digits) != len(set(digits))
    return [num for num in numbers if not has_repetitive_digits(num)]

def calculate_easy(tablica, k=5):
    wynik = []
    for i in range(1, len(tablica) - 1):
        if abs(tablica[i - 1] - tablica[i]) >= k \
            and abs(tablica[i + 1] - tablica[i]) >= k:
            wynik.append(tablica[i])
    return wynik 

def calculate_hard(zdanie):
    slowa = zdanie.split()
    return [' '.join(perm) for perm in itertools.permutations(slowa)]

def create_mask(lista1, lista2):
    return [1 if lista1[i] == lista2[i] else 0 for i in range(len(lista1))]

def distance(lista1, lista2):
    return max(abs(lista1[i] - lista2[i]) for i in range(len(lista1)))

# Testy
def test_concat_easy():
    assert concat_easy([1, 2], [3, 4, 5]) == [4, 6, 5]
    assert concat_easy([1], [2, 3]) == [3, 3]
    assert concat_easy([], [1]) == [1]
    print("test_concat_easy: OK")

def test_concat_hard():
    assert concat_hard([1, 2, 3], [4, 5, 6]) == [5, 7, 9]
    try:
        concat_hard([1, 2], [3])
    except ValueError:
        print("test_concat_hard: OK")
    else:
        raise AssertionError

def test_sort_by_row():
    assert sort_by_row([[3, 1, 2], [4, 6, 5]]) == [[1, 2, 3], [4, 5, 6]]
    assert sort_by_row([[1], [3, 2]]) == [[1], [2, 3]]
    print("test_sort_by_row: OK")

def test_top3():
    assert top3([[10, 5, 7, 8], [1, 3, 2, 4]]) == [[10, 8, 7], [4, 3, 2]]
    assert top3([[1, 2], [3]]) == [[2, 1], [3]]
    print("test_top3: OK")

def test_filter_users():
    assert filter_users([{'name': 'user1'}, {'name': 'user2', 'level': 5}, {'level': 3}]) == [{'name': 'user2', 'level': 5}, {'level': 3}]
    print("test_filter_users: OK")

def test_remove_repetitive():
    assert remove_repetitive([123, 122, 456, 454]) == [123, 456]
    print("test_remove_repetitive: OK")

def test_calculate_easy():
    assert calculate_easy([2, 6, 2, 8, 1, 3, 10, 3]) == [8, 10]
    assert calculate_easy([1, 6, 5, 2, 8, 11, 3, 10, 3], 3) == [2, 8, 11, 3, 10]
    print("test_calculate_easy: OK")

def test_calculate_hard():
    assert calculate_hard("a b c") == ['a b c', 'a c b', 'b a c', 'b c a', 'c a b', 'c b a']
    assert calculate_hard("hello") == ["hello"]
    print("test_calculate_hard: OK")

def test_create_mask():
    assert create_mask([1, 2, 3], [1, 4, 3]) == [1, 0, 1]
    assert create_mask([1], [2]) == [0]
    print("test_create_mask: OK")

def test_distance():
    assert distance([1, 2, 3], [4, 1, 6]) == 3
    assert distance([1, 1, 1], [0, 0, 0]) == 1
    print("test_distance: OK")

# Uruchamianie testów
test_concat_easy()
test_concat_hard()
test_sort_by_row()
test_top3()
test_filter_users()
test_remove_repetitive()
test_calculate_easy()
test_calculate_hard()
test_create_mask()
test_distance()

print("\nWszystkie testy zakończone sukcesem!")