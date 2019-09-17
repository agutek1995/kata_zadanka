def fibonacii(ilosc_elementow=5):
    lista=[0,1]
    if ilosc_elementow<3:
        return (lista[0:ilosc_elementow])

    for i in lista:
        lista.append(lista[-1]+lista[-2])
        if len(lista)>=(ilosc_elementow):
            break
    return (lista)

print (fibonacii(0))
print (fibonacii(1))
print (fibonacii(2))
print (fibonacii(3))
print (fibonacii(4))

