def valid_parentheses(string):
    #your code he
    liczba_otw=0
    liczba_zam=0
    ostatni=" "
    pierwszy="none"
    for i in string:
        if i=="(":
            liczba_otw+=1
        if i == ")":
            liczba_zam += 1
        if i=="(" or i==")":
            ostatni=i
            if pierwszy=="none":
                pierwszy=i
        print (f"otwarte={liczba_otw}    zamkniete={liczba_zam}")
        if liczba_zam>liczba_otw:
            return False
    if liczba_otw==liczba_zam and ostatni!="(" and pierwszy!=")":
        return True
    else:
        return False

print(valid_parentheses('()()(())'))
# print(valid_parentheses('sdds(gedgr'))
# print(valid_parentheses("qgczie)k(tbjdioegthki(e(pmgg)xxbqnft)lvw"))
print(valid_parentheses('())(( )'))
