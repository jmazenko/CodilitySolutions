def CountSemiprimes(N, P, Q):
    # a semiprime number is a product of two distinct primes, or the square of one prime
    # P and Q are arrays of positive integers in which no element is larger than N
    # build and return array semi_p_count, where semi_p_count[k] = number of semiprimes in range (P[k]..Q[k]), inclusive
    prime_table = [False]*2+[True]*(N-1)
    prime = []
    semi_prime = [0]*(N+1)
    result = []

    idx = 2
    while idx**2 <= N:
        i = 2
        while idx * i <= N:
            prime_table[idx*i] = False
            i += 1
        idx += 1
    
    for idx in range(len(prime_table)):
        if prime_table[idx]:
            prime.append(idx)

    for idx in range(len(prime)):
        for i in range(idx, len(prime)):
            tmp = prime[idx] * prime[i]
            if tmp <= N:
                semi_prime[tmp] = 1
            else:
                break

    for idx in range(1, N+1):
        semi_prime[idx] += semi_prime[idx-1]

    for idx in range(len(P)):
        result.append(semi_prime[Q[idx]] - semi_prime[P[idx] - 1])

    return result
