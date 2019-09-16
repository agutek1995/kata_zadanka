def duplicate_count(text):
    text=text.lower()
    # Your code goes here
    wystapienie = 0
    ilosczdublowanych = 0
    lista=[]
    for i in text:
        if text.count(i)>1:
            lista.append(i)
            print(lista)
    for j in set(lista):
            # set usuwa powtórzenie
        ilosczdublowanych = ilosczdublowanych + 1



    return (ilosczdublowanych)

print(duplicate_count('aAAbBccdr'))