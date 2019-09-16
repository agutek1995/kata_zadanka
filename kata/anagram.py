def anagrams(word, words):
    #your code here
    lista_anagramow=[]

    for i in words:
        if len(i)==len(word):
            anagram=i
            for j in word:
                n=word.count(j)
                anagram=anagram.replace(j, '',n)
                if  anagram=='':
                    lista_anagramow.append(i)
                if len(anagram)==0:
                    break
    return (lista_anagramow)

anagrams('abba', ['bbaa','kkaa','aaabb','abba'])