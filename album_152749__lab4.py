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

def post_line(arr):
    out = []
    out2 = []

    for i in range(len(arr)):
        if not arr[i][1]:
            out.append(arr[i][0])
        else:
            out2.append(arr[i][0])

    print(out+out2)


line = [
    ('Grazyna', True),
    ('Laura', False),
    ('Bartek', False),
    ('Andrzej', True),
    ('Wiesiek', False)
]
post_line(line)
