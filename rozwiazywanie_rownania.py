
def rozwiazanie_rownania(x, y=30, podzelnik=17):
    """
    znajdz pary liczb całkowitych (x, y), takich, że
    istnieje jakieś całkowiete k takie, że:
    x^2 + y^3 = 17*k

    :param x: liczba całkowita
    :param y: liczba całkowita
    :param podzelnik: liczba całkowita przez, która szukamy podzielności
    :return:
    """
    for i in range(x):
        for j in range(y):
            suma=((i)**2)+((j)**3)
            podzielnosc_prze_podzielnik=suma%podzelnik
            if podzielnosc_prze_podzielnik==0:
                print (f"{i}^2+{j}^3={suma} jest podzielna przez {podzelnik}")

rozwiazanie_rownania(30, y=3, podzelnik=3)


# rozwiazanie_rownania(30, 30, podzelnik=123)
# rozwiazanie_rownania(30, y, podzelnik=123)