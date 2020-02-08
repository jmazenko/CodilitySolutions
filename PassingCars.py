def PassingCars(A):
    # A[k] = 0 means car k is going east; A[k] = 1 means car k is going west. Two cars pass if first is traveling east, second is traveling west
    # find number of pairs of passing cars
    pre_sums = [0] * len(A)
    pre_sums[0] = A[0]
    for i in range(1, len(A)):
        pre_sums[i] += A[i] + pre_sums[i-1] # pre_sums[t] = number of cars observed going west at time t
    passing_pairs = 0
    for j in range(len(A)):
        if A[j] == 0:
            passing_pairs += pre_sums[len(A)-1] - pre_sums[j]
        if passing_pairs > 1000000000:
            return -1
    return passing_pairs
