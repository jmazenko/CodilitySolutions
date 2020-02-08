def Ladder(A, B):
    # a ladder has A[k] rungs. You initially step on rung 1 or rung 2, and ascend either 1 or 2 rungs with every subsequent step
    # after your last step, you must be standing on rung number A[k], not non-existent rung above it
    # number of ways of climbing can be large, so we take number of ways modulo 2^P for some integer P
    # build and return array results, where results[k] = (number of ways of climbing a ladder with A[k] rungs) modulo (2^B[i])
    L = max(A)
    P_max = max(B)
  
    fib = [0] * (L+2)
    fib[1] = 1
    for i in range(2, L + 2):
        fib[i] = (fib[i-1] + fib[i-2]) & ((1 << P_max) - 1)
  
    results = [0] * len(A)
  
    for idx in range(len(A)):
        results[idx] = fib[A[idx]+1] & ((1 << B[idx]) - 1)
  
    return results
