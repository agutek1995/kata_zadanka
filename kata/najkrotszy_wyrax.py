def find_short(s):
    # your code here
    # return l # l: shortest word length
    world=s.split(' ')
    l=530
    for i in world:
        if l>len(i):
            l=len(i)
    print (l)

find_short("basic tests fgh jjhj hjjjjjjjjjjjjjjjjjjjjjjjjj jjjjjjjjjjjjjjjjjjjjjj")

