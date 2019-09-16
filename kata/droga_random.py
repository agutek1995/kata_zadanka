def isValidWalk(walk):
    #determine if walk is valid

    import random
    from random import choices
    walk=random.choices(['n','w','e','s'],k=4)
    print(walk)
    zbior=set(walk)
    print (zbior)
    if len(zbior)==len(walk):
        return True
    else:
        return False
wynik = isValidWalk(['e', 's', 'n', 'e', 's'])
print(f" wynik")
