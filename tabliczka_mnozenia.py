def wiersz_mnozenia(x,y):
    for i in range(x):
        suma=i*y
        print(f'{i}*{y}={suma:2}',end = " ")     # suma zawsze 2 znaki dzięki: {suma:2}
#wiersz_mnozenia(5,5)

def kolumna_mnozaca(a):
    for j in range(a):
        wiersz_mnozenia(a, j)
        print ()
kolumna_mnozaca(5)