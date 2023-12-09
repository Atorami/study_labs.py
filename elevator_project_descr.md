# Ogólny opis projektu

    Należy zbadać 3 algorytmy poruszania się windy w 3 różnych sytuacjach. Za pomocą symulacji (szczegółowy opis
    poniżej) należy zbadać który z tych algorytmów poruszania się windy będzie najlepszy pod kątem pokonywanej
    przez windę odległości.

# Szczegółowy opis

    Chcemy zbadać jaki z 3 algorytmów będzie najlepszy pod kątem pokonywanej w budynku odległości (im mniej
    pokonuje tym lepiej, bo dłużej się zużywa).
    Założenia ogólne:
    • Blok mieszkalny ma 10 piętr, czyli 11 kondygnacji (liczymy od 0, wtedy 0 będzie parterem + 10 kolejnych
    kondygnacji).
    • Wysokość jednej kondygnacji to 2.8m, czyli jeżeli winda wjechała z parteru (0) na 1 piętro, to pokonała ona
    2.8m.
    • Dla każdego z 9 przypadków (3 algorytmy razy 3 scenariusze) wykonujemy 1000 powtórzeń, czyli 1000 losowań
    piętro początkowe - piętro końcowe.
    Należy przebadać 3 algorytmy poruszania się windy w 3 scenariuszach (oznaczona zwykłymi liczbami):
    1. Całkowicie losowe podanie piętra początkowego i piętra końcowego. Przykładowo, można to zaimplementować
    w ten sposób (należy odpowiednio wcześniej zaimportować bibliotekę random):
    
    ```python
    def script1():
    start = random.randint(0, 10)
    finish = random.randint(0, 10)
    
    while start == finish:
    finish = random.randint(0, 10)
    
    return start, finish
    
    start, finish = script1()

    ```

    2. Symulujemy przypadek kiedy ludzie jadą do pracy: 70% ludzi zjeżdża z piętr powyżej 4 na parter.
    W pozostałych 30% wypadków stosujemy scenariusz 1. Przykładowa implementacja:

    ```python
    def script2():
    if random.random() < 0.7:
    start = random.randint(4, 10)
    finish = 0
    
        return start, finish
    return script1()
    
    start, finish = script2()

    ```

    3. Symulujemy przypadek kiedy ludzie wracają z pracy/zakupów: 70% ludzi jedzie z parteru (0) na dowolne inne
    piętro. W pozostałych 30% wypadków stosujemy scenariusz 1. Przykładowa implementacja:

    ```python
    def script3():
    if random.random() < 0.7:
    start = 0
    finish = random.randint(1, 10)
    
        return start, finish
    return script1()
    
    start, finish = script3()

    ```

    W kolejnych sekcjach są przedstawione 3 algorytmy (oznaczone liczbami rzymskimi) poruszania się windy
    które należy przebadać. Każdy algorytm należy przebadać w każdym z 3 scenariuszy.
    (I) Winda zostaje na tym piętrze na którym skończyła swój ruch.
    Rozpatrzymy przykład dla 3 przejazdów windy, w tabeli poniżej podane piętra początkowe oraz końcowe:

    | Start | Finish |
    | :----:| :----: |
    | 0     |  7     |
    | 2     |  5     |
    | 6     |  1     |

    Przy takim losowaniu w tym algorytmie winda będzie zatrzymywać się na następujących piętrach:

    0 → 7 → 2 → 5 → 6 → 1

    Przebytą odległość liczymy jako różnice bezwzględną pomiędzy kolejnymi piętrami razy wysokość kondygnacji, czyli:

    (|0 − 7| + |7 − 2| + |2 − 5| + |5 − 6| + |6 − 1|) × 2.8 = (7 + 5 + 3 + 1 + 5) × 2.8 = 58.8

    Czyli korzystając z tego algorytmu winda pokonała odległość 58.8 m.
    (II) Winda po przejeździe zawsze wraca na parter (piętro 0), a dopiero potem jedzie na kolejne piętro.
    Rozpatrzymy ten sam przykład co dla poprzedniego algorytmu:
    Przy takim losowaniu w tym algorytmie winda będzie zatrzymywać się na następujących piętrach:

    0 → 7 → 0 → 2 → 5 → 0 → 6 → 1 → 0

    Czyli pokonana odległość będzie wynosić:

    (7 + 7 + 2 + 3 + 5 + 6 + 5 + 1) × 2.8 = 100.8

    Czyli korzystając z tego algorytmu winda pokona odległość 100.8m.
    (III) Algorytm autorski - należy opracować własny algorytm poruszania się windy oraz opisać go za pomocą schematu blokowego oraz słownie.
    W wyniku takiego badania ma powstać tabela z wynikami, przykład takiej tabeli poniżej. Poszczególne pola
    tej tabelki muszą zawierać odległość którą przebyła winda po symulacji przejazdu windą 1000 ludzi przy użyciu
    wybranego scenariusz i wybranego algorytmu. Proszę skonwertować te wartości w kilometry i zaokrąglić do dwóch
    wartości po przycinku. Wartości podane w tabeli są przykładowe i nie należy na nie się wzorować.
    
    | Scenariusz    | Algorytm I | Algorytm II | Algorytm III |
    |    :----:     |    :----:  |    :----:   |     :----:   |
    | Scenariusz 1  |  10.21 km  |   8.78 km   |    7.38 km   |
    | Scenariusz 2  |     ...    |      ...    |     ...      |
    | Scenariusz 3  |     ...    |      ...    |     ...      |
    | Wartość średnia  |  ...    |      ...    |     ...      |

    Na podstawie powyższej tabeli z wynikami należy wyciągnąć odpowiednie wnioski. Należy wskazać który z
    algorytmów pasuje do którego scenariusza oraz który z nich jest lepszy jeżeli uwzględniać tylko średnią odległość.