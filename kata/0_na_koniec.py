def move_zeros(array):
    #your code here
    for i in array:
        if i==0 and i is not False:
            # print(f"before remove {i}: {array}")
            array.remove(i)
            # print(f"after remove   : {array}")
            array.append(0)
    return array

# Test.assert_equals(move_zeros([0,1,None,2,False,1,0]),[1,None,2,False,1,0,0])

# print (move_zeros([['a', 'b', None, 'c', 'd', 1, 1, 3, [], 1, 9, {}, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]))
print (move_zeros([0,1,None,2,False,1,0]))