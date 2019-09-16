
def daj_liczby():
    wynik = []
    for i in range(200):
        if i%7 == 0:
            print(f"dodałem do przetwrzania liczbę {i}")
            wynik.append(i)
    return wynik

def daj_liczby_gen():
    for i in range(20):
        if i%7 == 0:
            print(f"dodałem do przetwrzania liczbę {i}")
            yield i


def wylicz_sume():
    suma = 0
    for liczba in daj_liczby_gen():
        suma += liczba
        if suma > 100:
            break
    print(f"wyliczona suma to {suma}")

wylicz_sume()

print([2*i for i in daj_liczby_gen()])