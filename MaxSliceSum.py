def MaxSliceSum(A):
    # find greatest possible sum of any array slice
    if max(A) <= 0:
        return max(A) # if no element is positive, we must choose highest non-positive element
    max_end = max_slice = 0
    for elem in A:
        max_end = max(0, max_end+elem)
        max_slice = max(max_slice, max_end)
    return max_slice
