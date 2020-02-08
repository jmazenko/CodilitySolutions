def MinPerimeterRectangle(N):
    # if a rectangle has area N, find its smallest possible perimeter
    horiz = vert = 0
    min_perim = (2*N) + 2 # value if N is prime
    i = 1
    while pow(i, 2) <= N: # if A * B = N, A and B are both accounted for, so we need only test up to a certain factor
        if N % i == 0:
            horiz = i
            vert = N//i
            if ((2*horiz) + (2*vert)) < min_perim:
                min_perim = ((2*horiz) + (2*vert))
        i += 1
    return min_perim
