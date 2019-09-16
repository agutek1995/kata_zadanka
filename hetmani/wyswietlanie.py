
def wyswietl_hetmanow(lista_pozycji):

    for pozycja_hetmana in lista_pozycji:
        print((' '*pozycja_hetmana)+'H')

# wyswietl_hetmanow([1,2,5,8,7,8,7,2])

def wyswietl_hetmanow_poz(*args):
    print(f"args = {args}")
    lista=[]
    for i in args:
        lista.append(i)
    wyswietl_hetmanow(lista)
    wyswietl_hetmanow(args)


# wyswietl_hetmanow([1, 2])
wyswietl_hetmanow_poz(1, 2)