# Zadanie 1:
    # Napisz funkcję, sprawdzającą czy wszystkie otwarte nawiasy w napisie zostały zamknięte prawidłowo.
    # Funkcja ma wykorzystywać do tego celu stos i obsługiwać dwa typy nawiasów: okrągłe i kwadratowe.
######################################################

def brackets_validator(arr):
    stack = []

    for i in arr:
        if i in '([':
            stack.append(i)
        elif stack and ((i == ']' and stack[-1] == '[') or (i == ')' and stack[-1] == '(')):
            stack.pop()
    if not stack:
        print('Brackets closed correct')
    else:
        print('Brackets closed incorrect')
    return stack


######################################################
# Zadanie 2:
    # Napisać funkcje, symulującą działanie placówki „Poczta Polska”. Funkcja ta ma otrzymać na wejściu listę krotek,
    # zawierających po kolei imię klienta oraz zmienną True/False która oznacza czy klient będzie musiał wrócić do okienka po raz drugi.
    # Na końcu działania funkcja powinna zwrócić listę osób wychodzących z poczty w tej kolejności w której one będą wychodzić.
    # Funkcja powinna używać kolejki. Kolejka powinna być obsługiwana następująco:
    # (a) Pobierz osobę na początku kolejki.
    # (b) Sprawdź czy osoba musi coś wysłać.
    # (c) Jeżeli tak to dopisz na koniec kolejki.
    # (d) Jeżeli nie to dopisz do listy osób wychodzących z poczty.
######################################################

from collections import deque


def post_line(arr):
    que = deque()
    que_arr = []

    for i in arr:
        que.append([i, False])

    while que:
        person = que.popleft()
        if person[0][1] and not person[1]:
            que.append([person[0], True])
        else:
            que_arr.append(person[0][0])
    return que_arr

######################################################
# Zadanie 3:
    # Zaimplementuj algorytm porządkowania stosu za pomocą stosu pomocniczego zgodnie z
    # pseudokodem przedstawionym na wykładzie.
######################################################


def double_stack(arr):
    left_stack = [min(arr)]
    right_stack = [max(arr)]

    arr.remove(min(arr))
    arr.remove(max(arr))

    for i in arr:

        while left_stack[-1] >= i:
            right_stack.append(left_stack.pop())
        while right_stack[-1] < i:
            left_stack.append(right_stack.pop())
        left_stack.append(i)

    return left_stack + right_stack[::-1]
