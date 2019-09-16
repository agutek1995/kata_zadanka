
# wypisz_sume = {pracuj....}
def wypisz_sume(a, b):
    print(a + b)

def wypisz_sume_log(*args):
    print(f"dostałem argumenty: {args}")
    wypisz_sume(*args)

wypisz_sume_log(2, 3)

def log(f):
    print("ktos robi dekorator")
    def wewnetrzna(*args, **kwargs):
        print(f"dostałem argumenty: {args}")
        f(*args, **kwargs)
    return wewnetrzna

# wypisz_sume2 = log( {pracuj....} )
@log
def wypisz_sume2(a, b):
    print(a + b)
wypisz_sume2 = log(wypisz_sume2)

wypisz_sume2(2, 6)
wypisz_sume2(1, 4)