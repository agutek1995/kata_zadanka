def isValidWalk(walk):
    #determine if walk is valid
    suman=0
    sumaw=0
    sumae=0
    sumas=0
    for i in walk:
        if i=='s':
            sumas+=1
        elif i == 'n':
            suman+=1
        elif i=='e':
            sumae+=1
        elif i=='w':
            sumaw+=1
    if len(walk)!=10:
        return False
    else:
        if suman==sumas and sumaw==sumae:
            return True
        else:
            return False
isValidWalk()


