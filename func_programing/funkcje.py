
def print_a():
    print("A")

def print_b():
    print("B")

# print_a()
# print_b()

x = 5
x = 6
y = x

y = lambda: print("C")
y()

(lambda: print("D")) ()

f = lambda x: 2*x
print(f(5))

g = lambda x, y: 2*x + y
print(g(5, 1))

def jackowe_sortowanie(a, b):
    if a < b:
        print(f"{a} {b}")
    else:
        print(f"{b} {a}")

def jackowe_sortowanie_lambda(a, b, prownaj):
    if prownaj(a, b):
        print(f"{a} {b}")
    else:
        print(f"{b} {a}")

jackowe_sortowanie_lambda(1, 2, lambda x, y: x < y)
jackowe_sortowanie_lambda(1, 2, lambda x, y: x > y)


txt = "abcd"
print(txt[1] < 'a')

jackowe_sortowanie_lambda("ala", "bob", lambda x, y: x[0] < y[0])

jackowe_sortowanie_lambda((5, 6), (7, 8), lambda p1, p2: p1[0]**2 + p1[1]**2 < p2[0]**2 + p2[1] ** 2)
jackowe_sortowanie_lambda((9, 6), (7, 8), lambda p1, p2: p1[0]**2 + p1[1]**2 < p2[0]**2 + p2[1] ** 2)
