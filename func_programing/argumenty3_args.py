
def chce_abc(a = -1, b=-1, c=-1):
    print(f"a = {a}, b = {b}, c = {c}")

chce_abc(1, 2, 3)
chce_abc(*[1, 2, 3])
lista = [1, 2, 3]
chce_abc(*lista)

# chce_abc(1, 2, 3, 4)
# chce_abc(*[1, 2,3,4]

chce_abc(1, 2)
# chce_abc(*[1, 2,3,4])
lista = []
lista.append(10)
lista.append(20)
lista.append(30)
chce_abc(*lista)

chce_abc(b=9)
chce_abc(**{'b': 9})
slownik = {}
slownik['b'] = 8
slownik['c'] = 34
chce_abc(**slownik)