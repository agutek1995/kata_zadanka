napis='jaceka'
napis='ababbbbbccccccccc'
s={}
for literka in napis:
    s[literka]=0
for literka in napis:

    if literka in napis:
        s[literka]+=1
        if s[literka]>=2:
            print(f"{literka} jest {s[literka]}")
#             jednaliterka=literka
#             ilosc=s[literka]
# print (f"{jednaliterka} {ilosc}")

for literka in set(napis):
    if s[literka] >= 2:
        print(f"{literka} jest {s[literka]}")

        # iloscliterek=iloscliterek+1
        # liczonaliterka=literka
        # if iloscliterek>=2:
        #     print(f"{liczonaliterka} wystepuje {iloscliterek}")