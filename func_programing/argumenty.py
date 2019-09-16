
def wypisz_costam1(a):
    print(f"{a}")

def wypisz_costam2(a, b):
    print(f"{a}, {b}")

def wypisz_costam3(a, b, c):
    print(f"{a}, {b}, {c}")

wypisz_costam1(1)
wypisz_costam2(1, 2)
wypisz_costam3(1, 2, 3)

def wypisz(pierwszy, *args):
    print(f"pierwszy = {pierwszy}")
    print(f"mam {len(args)} podanych argumnetow")
    for arg in args:
        print(arg, end=', ')
    print()

wypisz("a", "b", "c", 6, 7, 8, 4, 3, 6, 8)
co_chce_wypisac = ['chce to', 'wypisac']
co_chce_wypisac.append("i")
co_chce_wypisac.append("jeszcze to")
wypisz("P", *co_chce_wypisac)

# print("%s %d %f" % ("ala", 5, 5.6))