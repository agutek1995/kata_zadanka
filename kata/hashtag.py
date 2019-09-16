def generate_hashtag(s):
    ilosc_znakow=len(s)
    wielkosc_liter=""
    if ilosc_znakow==0 or ilosc_znakow>140:
        return False
    else:
        s=s.lower()
        s=s.split(' ')
        for i in s:
            if len(i)<=1:
                wielkosc_liter=wielkosc_liter+i.upper()
            else:
                wielkosc_liter=wielkosc_liter+i[0].upper()+(i[1:])

        return (f"#{wielkosc_liter}")

print (generate_hashtag("c i n"))