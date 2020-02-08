def PermCheck(A):
    # return 1 if array A is a permutation, 0 otherwise
    correctXor = 0
    for i in range(1, len(A)+1):
        correctXor ^= i #XOR if no element is missing
    
    observedXor = 0
    for elem in A:
        observedXor ^= elem
    
    if correctXor ^ observedXor == 0: #if values are equal, their XOR is 0
        return 1
    return 0
