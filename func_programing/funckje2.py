print("ok")
def sortowanie(a,b,porownaj):
    def wypisz():
        print("wypisuje")

    if porownaj(a,b):
        print(a,b)
    else:
        print(b,a)
    wypisz()
sortowanie(8,9, lambda a,b: a>b)