def CountFactors(N):
    # find number of factors of N
    i = 1
    factors = 0
    while pow(i, 2) < N:
        if N % i == 0:
            factors += 2 # to save time, we only loop up to square root of N
        i += 1
    if pow(i, 2) == N:
        factors += 1
    return factors
