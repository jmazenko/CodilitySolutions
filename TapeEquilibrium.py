def TapeEquilibrium(A):
    # tape is split into two portions and sum of each portion is calculated. Find smallest possible difference between sums
    first_sum = A[0]
    second_sum = sum(A[1:])
    min_diff = abs(first_sum - second_sum)
    for i in range(1, len(A)-1):
        first_sum += A[i]
        second_sum -= A[i] #keeping track of sums this way is much more efficient than fully recalculating them at every step
        if abs(first_sum - second_sum) < min_diff:
            min_diff = abs(first_sum - second_sum)
    return min_diff
