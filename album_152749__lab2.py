# 1. Zaimplementować wyszukiwania największej liczby w nieposortowanej liście liczb.
#    Przetestować jego działanie i oszacować złożoność obliczeniową tego algorytmu.
########################################################
def max_search(arr):
    max = arr[0]
    for i in range(len(arr)):
        if arr[i] > max:
            maxi = arr[i]
    return max

# Summary: To jest typ O(N), gdzie N to długość listy,
# co oznacza, że czas wykonania algorytmu zależy tylko od długości listy.


max_search([1, 5, 9, 2, 11, 6, 3])

########################################################
# 2. Zaimplementować algorytm sortowania przez wstawianie (insertion sort).
#    Przetestować jego działanie i oszacować złożoność obliczeniową tego algorytmu.
########################################################


def insert_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i-1
        while temp < arr[j] and j >= 0:
            arr[j+1], arr[j] = arr[j], arr[j+1]
            j -= 1
        arr[j+1] = temp

# Summary: To jest typ O(N^2), gdzie pierwsze N oznacza iteracje po całej liście,
# a drugie N to liczba porównań potrzebna do znalezienia odpowiedniego miejsca
# dla elementa w już posortowanej części.


insert_sort(([1, 5, 9, 2, 11, 6, 3]))

########################################################
# 3. Zaimplementować opisany poniżej algorytm i oszacować jego złożoność obliczeniową.
########################################################


def val_counter(arr1, arr2):
    counter = 0
    for i in arr1:
        if i in arr2:
            counter += 1
    return counter

# Summary: To jest typ O(N^2), gdzie pierwsze N oznacza iteracje po całej liście arr1,
# a drugie N to ilość iteracji po liście arr2.


val_counter('ala ma kota', 'aeiouy')

########################################################
# Zaimplementować algorytm obliczający sumę cyfr wprowadzanej przez użytkownika liczby.
########################################################


def sum_arr(val):
    sum = 0
    for i in range(len(val)):
        sum += int(val[i])
    return sum


val = input('Input a number: \n')
sum_arr(val)

# Summary: To jest typ O(N), gdzie N to ilość cyfr w wejściowej liczbe.
# Czas wykonania funkcji rośnie liniowo wraz ze wzrostem ilości cyfr.

