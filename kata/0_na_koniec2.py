def move_zeros(array):
    #your code here
    koniec = []
    for index in range(len(array)):
        if index >= len(array):
            break
        i = array[index]
        if i==0 and (str(i) == "0" or str(i) == "0.0"):
            # print(f"before remove {i}: {array}")
            del array[index]
            # print(f"after remove   : {array}")
            koniec.append(0)
    array += koniec
    return array

# Test.assert_equals(move_zeros([0,1,None,2,False,1,0]),[1,None,2,False,1,0,0])

# print (move_zeros([['a', 'b', None, 'c', 'd', 1, 1, 3, [], 1, 9, {}, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]))
print (move_zeros([0,1,None,2,False,1,0]))
print (move_zeros([9, 0.0, 9, 1, 2, 1, 1, 0.0, 3, 1, 9, 0, 0, 9, 0, 0, 0, 0, 0, 0]))