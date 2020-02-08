def ChocolatesByNumbers(N, M):
    # you have N chocolates arranged in a circle
    # you start eating at chocolate number 0, then advance M positions and eat chocolate at that position
    # after you eat one chocolate, you leave an empty wrapper
    # find number of chocolates you will eat before getting an empty wrapper
    X = gcd(N, M)
    return int(N/X)

def gcd(a, b): # this is Euclidean algorithm to find greatest common divisor of a and b
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
