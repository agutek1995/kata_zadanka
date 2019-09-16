
def chce_elemty(*args):
    for arg in args:
        print(f"moj argumnet = {arg}")
    print()

def chce_elementy(*args, **kwargs):
    for arg in args:
        print(f"moj argumnet = {arg}")
    for k, v in kwargs.items():
        print(f"{k} -> {v}")
    print()

chce_elemty(1, 2)
chce_elemty(1, 2, 4)

chce_elementy(1, 2)
chce_elementy(klucz="wartosc")

