def MaxProductOfThree(A):
    # if A[P], A[Q], and A[R] are any three elements of A, find their greatest possible product
    A.sort()
    right_endpoint = A[len(A)-1] * A[len(A)-2] * A[len(A)-3]
    left_endpoint = A[0] * A[1] * A[len(A)-1]
    return max((left_endpoint, right_endpoint)) #max value will always be one of these two

