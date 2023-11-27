# Zadanie 1:
    # Zaimplementować funkcję obliczającą silnię podanej jako argument funkcji liczby n.
    # Funkcja powinna używać rekurencji do obliczenia silni.
######################################################

def sil(x):
    if x == 1:
        return x
    else:
        return x*sil(x-1)

######################################################
# Zadanie 2:
    # Zaimplementować funkcje który obliczy i wypisze kolejne elementy sekwencji Collatza (wzór poniżej) używając
    # rekurencji. Algorytm ma wystartować od podawanej jako argument funkcji liczby cn i działać do momentu aż
    # osiągniemy wartości cn+1 = 1.
######################################################


def sekw(x):
    arr = []

    def rec(x, arr):
        if x == 1:
            return arr.append(x)
        elif x % 2 == 0:
            arr.append(x)
            return rec(x / 2, arr)
        else:
            arr.append(x)
            return rec(3 * x + 1, arr)

    rec(x, arr)
    return arr

######################################################
# Zadanie 3:
    # Zaimplementuj funkcje obliczającą największy wspólny dzielnik dwóch liczb a i b za pomocą rekurencji.
    # Liczby a i b powinny być argumentami funkcji.
######################################################


def dziel(a, b):
    if b == 0:
        return a
    else:
        return dziel(b, a % b)

######################################################
# Zadanie 4:
    # Zaimplementować rekurencyjny algorytm szybkiego sortowania (quicksort) i przetestować jego działanie.
######################################################


def q_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        smaller = [i for i in arr[1:] if i <= pivot]
        bigger = [i for i in arr[1:] if i > pivot]
        return q_sort(smaller) + [pivot] + q_sort(bigger)
