def MinAvgTwoSlice(A):
    # find smallest average of any slice with length 2 or higher
    min_idx = 0
    min_value = 10001
 
    for idx in range(len(A)-1): # large slices are constructed out of smaller ones, so we need only test all slices of length 2 or 3
        if (A[idx] + A[idx+1])/2.0 < min_value:
            min_idx = idx
            min_value = (A[idx] + A[idx+1])/2.0
        if idx < len(A)-2 and (A[idx] + A[idx+1] + A[idx+2])/3.0 < min_value:
            min_idx = idx
            min_value = (A[idx] + A[idx+1] + A[idx+2])/3.0
 
    return min_idx
