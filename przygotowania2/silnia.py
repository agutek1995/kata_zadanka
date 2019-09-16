def silnia(n):
    if n<=1:
        return 1
    else:
        return n*silnia(n-1)
print (silnia(5))

SILNIA=1
for i in range(1,5):
    SILNIA=SILNIA*i
print (SILNIA)

def silnia_iteracyjnie(n):
    silnia = 1
    for i in range(1, n):
        silnia = silnia * i
    return silnia

print(silnia_iteracyjnie(6))
