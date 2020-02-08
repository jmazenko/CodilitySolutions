def CountDiv(A, B, K):
    # return number of integers divisible by K in range [A..B]
    min_value =  ((A + K - 1) // K) * K # smallest possible divisor in range
 
    if min_value > B:
      return 0
 
    return ((B - min_value) // K) + 1
