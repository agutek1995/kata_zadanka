
with open('kwadratowa.csv', 'w') as f:
    for x in range(10):
        f.write(f"{x};{x*x}\n")


    l1=[x for x in range(10)]
    l2=[x**2 for x in l1]

    print (l1)
    print (l2)
    for x,y in zip(l1, l2):
        print(x, y)
        f.write(f"{x};{y}\n")
    # f.write(f'{}')


