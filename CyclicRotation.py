def CyclicRotation(A, K):
    # rotate array A to the right K times
    for i in range(K):
        A.insert(0, A[len(A)-1]) # push last element of A onto front of list
        A.pop(len(A)-1) # remove last element
    return A
