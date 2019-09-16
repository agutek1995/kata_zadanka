l1=[2,4,8,15,1257,751]
# klucz:liczba, wartosc+liczba do kwadratu
s={i:i**2 for i in l1}
print (s)

l=[]
for i in s.items():
    l.append(str(i[1]))
print (l)

l=[str(i[1]) for i in s.items() ]
l=[str(v) for k, v in s.items() ]
print (l)