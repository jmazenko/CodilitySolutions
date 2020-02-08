def MaxDoubleSliceSum(A):
    # suppose 0 < X < Y < Z < len(A). A double slice divides A into three parts that contain all array elements in range X-Z, except X, Y, and Z themselves
    # according to problem constraints, neither first nor last element can appear in any double slice. Find largest sum of any double slice
    ending_here = [0] * len(A)
    starting_here = [0] * len(A)
     
    for i in range(1, len(A)):
        ending_here[i] = max(0, ending_here[i-1] + A[i])
     
    for j in reversed(range(len(A)-1)):
        starting_here[j] = max(0, starting_here[j+1] + A[j])
     
    max_double_slice = 0
     
    for k in range(1, len(A)-1):
        max_double_slice = max(max_double_slice, starting_here[k+1] + ending_here[k-1])
         
    return max_double_slice
