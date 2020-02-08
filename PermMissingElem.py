def PermMissingElem(A):
    # given a permutation missing one element, find missing value
    correctXor = 0
    for i in range(1, len(A)+2):
        correctXor ^= i #XOR if no element was missing
    
    observedXor = 0
    for elem in A:
        observedXor ^= elem
    
    return correctXor ^ observedXor
