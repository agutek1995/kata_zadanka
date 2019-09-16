with open('dane.txt') as f:
    with open('dane2.txt', 'w') as f2:
        lista=[]
        for line in f:
            if 'jacek' in line:
                print(line.rstrip())
                a=line.split(' ')
                print (a)

                poprzednie_slowo = ""
                print(line)
                for i in a:
                    # print (i)
                    if 'jacek' in i:
                        print(poprzednie_slowo)
                        lista.append(poprzednie_slowo)
                        break
                        print (line)
                    else:
                        poprzednie_slowo = i
                f2.write(poprzednie_slowo)
        print(','.join(lista))

