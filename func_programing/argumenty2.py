
def co_maja(co_ma_ala, co_ma_bob):
    print(f"Ala ma {co_ma_ala}. Bob ma {co_ma_bob}.")

co_maja(co_ma_bob="psa", co_ma_ala="kota")


def co_maja2(**kwargs):
    if 'co_ma_ala' in kwargs:
        a = kwargs['co_ma_ala']
    elif 'ala' in kwargs:
        a = kwargs['ala']
    b = kwargs['co_ma_bob']
    print(f"Ala ma {a}. Bob ma {b}.")

# co_maja2(co_ma_bob="psa", co_ma_ala="kota")
# co_maja2(co_ma_bob="psa", ala="kota")

def co_maja_hitoria(*args, **kwargs):
    print("Dawno dawno temu...")
    co_maja2(*args, **kwargs)

co_maja2(co_ma_bob="psa", co_ma_ala="kota")
co_maja_hitoria(co_ma_bob="psa", co_ma_ala="kota")

slownik = {"co_ma_ala": "kota", "co_ma_bob": "nietoperza"}
co_maja2(**slownik)
