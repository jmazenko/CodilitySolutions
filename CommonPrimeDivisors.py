def CommonPrimeDivisors(A, B):
    # A and B are arrays of positive integers
    # prime divisors of A[k] are divisors that are also prime numbers
    # find number of positions k at which A[k] and B[k] have same set of prime divisors
    count = 0
    for a,b in zip(A, B):
        x = gcd(a,b)
        
        while True:
            d = gcd(x, a)
            if d == 1:
                break
            a /= d

        while True:
            d = gcd(x, b)
            if d == 1:
                break
            b /= d
            
        if a == b == 1:
            count += 1

    return count

def gcd(x, y):
    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)
