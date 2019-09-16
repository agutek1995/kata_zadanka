class Node:
    def __init__(self, imie):
        self.moje_imie = imie
        self.next = Node

def loop_size(node):
    pass

node1 = Node("węzeł 1")
node2 = Node("węzeł 2")
node3 = Node("węzeł 3")
node4 = Node("węzeł 4")
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

if node2.next == node3:
    print("węzeł 2 wskazuje na węzeł 3: node2 -> node3")
else:
    print("węzeł 2 nie wskazuje na węzeł 3: node2 -- node3")

if node2.next == node4:
    print("węzeł 2 wskazuje na węzeł 4: node2 -> node4")
else:
    print("węzeł 2 nie wskazuje na węzeł 3: node2 -- node4")

print(f"{node1.moje_imie} -> {node1.next.moje_imie}")
print(f"{node2.moje_imie} -> {node2.next.moje_imie}")
print(f"{node3.moje_imie} -> {node3.next.moje_imie}")
print(f"{node4.moje_imie} -> {node4.next.moje_imie}")

print("spacerek:")
aktualny = node1
for i in range(9):
    print(aktualny.moje_imie)
    aktualny = aktualny.next

# Test.assert_equals(loop_size(node1), 3, 'Loop size of 3 expected')
print(f"loop_size(node1) = {loop_size(node1)}")