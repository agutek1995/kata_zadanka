def tribonacci(signature, n):
    #your code here
    if n<3:
        signature=signature[:n]
        return signature
    else:
        for i in range(n-3):
            signature.append(signature[-1]+signature[-2]+signature[-3])
        return signature
print (tribonacci([1,1,1],10))