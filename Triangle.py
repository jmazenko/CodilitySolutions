def Triangle(A):
    # determine if there are any three elements in A that could represent side lengths of a triangle
    A.sort()
    for i in range(2, len(A)):
        if A[i-1] + A[i-2] > A[i]:
            if A[i] + A[i-1] > A[i-2]:
                if A[i] + A[i-2] > A[i-1]:
                    return 1
    return 0
