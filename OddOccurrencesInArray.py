def OddOccurrencesInArray(A):
    # given array in which every element except one occurs an even number of times, find value of unpaired element
    xorValues = 0
    for elem in A:
        xorValues ^= elem
    return xorValues
