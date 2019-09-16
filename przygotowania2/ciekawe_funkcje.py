lista=[5,5,588,8,10,15,1]
lista.append(5)
print('; '.join([str(x) for x in lista]))
print(lista)
print(len(lista))


s={'ogorek':'zielony','pomidor':'czerwony'}
for k,v in s.items():
    print (k)
# s.clear()
for i in (s.values()):
    print (i+',', end='  ')
    print ()
print(', '.join(s))

class Punkt:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def wypisz_wsp(self):
        print(f'moje wspolrzedne to {self.x}, {self.y}')
Punkt(5,4).wypisz_wsp()





