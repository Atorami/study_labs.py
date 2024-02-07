########################################################
# Zadanie 1
# Pobrać plik tekstowy zawierający tekst książki „Alice’s Adventures in Wonderland” ().
# Następnie, należy wczytać ten plik do programu oraz zliczyć liczbę występowań poszczególnych słów w pliku.
# Na końcu program powinien wyświetlić top 10 słów występujących w tekście. Zadanie należy wykonać bez
# użycia klasy Counter.
########################################################
import requests
import re
import random
import string


def text_top_counter():
    url = "https://www.gutenberg.org/cache/epub/11/pg11.txt"
    response = requests.get(url)
    words = re.findall(r'\b\w+\b', response.text.lower())

    if response.status_code == 200:
        word_dict = {}
        for line in words:
            words = line.split()

            for word in words:
                word = word.strip('.,!?"()[]{}:;')
                word = word.lower()

                word_dict[word] = word_dict.get(word, 0) + 1

        sorted_dict = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)

        print("Top 10 words:")
        for i in range(min(10, len(sorted_dict))):
            print(f"{sorted_dict[i][0]}: {sorted_dict[i][1]}")

########################################################
# Zadanie 2:
# Zadanie jest tłumaczeniem Problemu 14 ze strony Project Euler https://projecteuler.net/problem=14.
# Dla zbioru dodatnich liczb całkowitych zdefiniowano następującą sekwencję iteracyjną:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Używając tych reguł i zaczynając od 13, wygenerujemy następujący ciąg:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# Widać, że uzyskany ciąg (zaczynający się od 13 i kończący się na 1) zawiera 10 wartości. Mimo że nie istnieje
# formalnego dowodu na to, uważa się że niezależnie od liczby początkowej ciąg ten zakończy się na 1.
# Która liczba poniżej 1 miliona generuje najdłuższy ciąg?
# UWAGA: W trakcie obliczeń wyrazy ciągu mogą przekraczać jeden milion.
# Komentarz do zadania: Należy napisać kod, odpowiadający na postawione w problemie pytanie. Po założeniu konta na wyżej wspomnianej stronie można sprawdzić czy obliczona przez nasz kod odpowiedź jest dobra
# czy nie. Podejście do rozwiązania „wprost” będzie liczyło odpowiedź przez jakiś czas. Można jednak zastosować
# sprytniejszego podejścia, dodając słownik który będzie pamiętał długości ciągów które są generowane przez te
# lub inne liczby. W ten sposób nie będziemy musieli po raz kolejny obliczać ciągów długości których były już
# przez nas zliczane.
########################################################


def collatz_finder():
    max_len = 0
    start_num = 0
    memo = {}
    limit = 1000000

    def collatz_len(n):
        if n in memo:
            return memo[n]

        if n == 1:
            return 1
        elif n % 2 == 0:
            length = 1 + collatz_len(n // 2)
        else:
            length = 1 + collatz_len(3 * n + 1)

        memo[n] = length
        return length

    for i in range(1, limit):
        curr_len = collatz_len(i)
        if curr_len > max_len:
            max_len = curr_len
            start_num = i

    return start_num


########################################################
# Zadanie 3
# Napisz funkcję która znajdzie kolizję dla podanego jako argument hash. Jako funkcja hash należy użyć funkcję
# używaną w zadaniach do zrobienia na zajęciach (h = djb2(key) % 997).
# Funkcja powinna działać mniej-więcej zgodnie z następującym algorytmem:
# • Wygeneruje losową kombinacje liter alfabetu angielskiego o zadanej długości.
# • Oblicza hash z wygenerowanej kombinacji.
# • Powtarzaj poprzednie dwa kroki dopóki nie zostanie znaleziona kombinacja z której uzyskujemy taki sam
# hash jak podany jako argument.
# • Zwróć znalezioną kombinacje liter.
########################################################
def find_collision():
    target_hash = 42

    def djb2(key):
        hash_value = 5381
        for char in key:
            hash_value = (hash_value * 33) ^ ord(char)
        return hash_value % 997

    while True:
        candidate = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
        if djb2(candidate) == target_hash:
            print(f"The collision for hash {target_hash}: '{candidate}'")
            break

########################################################
# Zadanie 4:
# Zaimplementować funkcję, która sprawdzi czy w liście pełniącej rolę tablicy mieszającej istnieje wartość przypisana to danego klucza. Funkcja ma przyjmować jako argumenty listę oraz klucz, wartość dla którego należy
# znaleźć zgodnie z algorytmem:
# Funkcja pobierz(T, key)
# • Oblicz idx jako idx = H(key) mod len(T)
# • Jeżeli T[idx] nie jest puste i T[idx][0] = key
# – Zakończ działanie funkcji i zwróć T[idx][1], będące value przypisanym do klucza key
# • Komentarz: Rozwiązywanie kolizji
# • Dla wartości idx w przedziale [0, len(T) − 1] wykonaj
# – Jeżeli T[idx] jest puste
# ∗ Zakończ działanie funkcji i zwróć None
# – Jeżeli T[idx] nie jest puste i T[idx][0] = key
# ∗ Zakończ działanie funkcji i zwróć T[idx][1], będące value przypisanym do klucza key
# • Wyświetl komunikat o błędzie.
# • Zakończ działanie funkcji
########################################################
########################################################


def key_ex_checker(T, key):
    idx = hash(key) % len(T)

    if T[idx] and T[idx][0] == key:
        return T[idx][1]

    # collision

    for idx in range(0, len(T)-1):
        if not T[idx]:
            return None
        elif T[idx] and T[idx][0] == key:
            return T[idx][1]

    print("Value not found")
    return None
