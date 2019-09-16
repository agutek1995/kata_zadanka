lista1 = [1, 2, 7, 8, 10]

lista2 = []
for i in lista1:
    lista2.append(2*i)
print(lista2)

lista3 = [2*i for i in lista1]
print(lista3)

print([2*i for i in lista1])

#[1, 3] -> {"ala 1": 2, "ala 3": 6}
l = [1, 3]
s = {}
for i in l:
 s[f"ala{i}" ]=i*2
print (s)
s = {f"ala{i}": i*2 for i in l}
print (s)

lista58=[]
for k,v in s.items():
    lista58.append(f"{k}=>{v}")
print(lista58)

lista59=[(f"{k}=>{v}") for k,v in s.items()]
print(lista59)

print([i*2 for i in range(10) if i%3 == 0])