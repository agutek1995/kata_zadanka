with open("liczby.txt") as f:
    lista=[]
    for lines in f:
        lista.append(float(lines))
    print(lista)
    suma=0
    for i in lista:
        suma=suma+i
    print(suma)
with open('liczby.txt', 'a') as f:
    f.write(str(suma))