
suma=0
lista=[]
for i in range(4):
    suma=[i-1]+[i-2]
    print(suma)

#-------------------------------


lista=[0,1]
for _ in range(19):
    lista.append(lista[-1]+lista[-2])
print(lista)

#--------------------------------

lista=[0]*4
lista[0]=0
lista[1]=1
for i in range(2,4):
    lista[i] = lista[i-1] + lista[i-2]
    print(lista)

#----------------------------

a, b = 0, 1
print(a)
for _ in range(4):
    print(a)
    a, b = b, a+b