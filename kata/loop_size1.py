class Node:
    pass

def loop_size(node):
    pass

node1 = Node()
node2 = Node()
node3 = Node()
node4 = Node()

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

slownik = {}
slownik[node1] = 0
slownik[node2] = 3
print(f"slownik[node1] = {slownik[node1]}")
print(f"slownik[node2] = {slownik[node2]}")

if node2.next == node3:
    print("węzeł 2 wskazuje na węzeł 3: node2 -> node3")
else:
    print("węzeł 2 nie wskazuje na węzeł 3: node2 -- node3")

if node2.next == node4:
    print("węzeł 2 wskazuje na węzeł 4: node2 -> node4")
else:
    print("węzeł 2 nie wskazuje na węzeł 4: node2 -- node4")

print("Spacerek")

# Test.assert_equals(loop_size(node1), 3, 'Loop size of 3 expected')
print(f"loop_size(node1) = {loop_size(node1)}")