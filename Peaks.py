def Peaks(A):
    # a peak is an array element that is greater than either of its neighbors
    # we want to divide array into blocks of equal size, each containing at least one peak. Find greatest possible block size
    peaks = []
 
    for i in range(1, len(A)-1): # find all peak positions
        if A[i-1] < A[i] > A[i+1]:
            peaks.append(i)
 
    if len(peaks) == 0:
        return 0
 
    for num_blocks in range(len(peaks), 0, -1): # if every block contains a single peak, number of blocks = number of peaks
        if len(A) % num_blocks == 0:
            block_size = len(A) // num_blocks
            found = [False] * num_blocks
            found_count = 0
            for peak in peaks:
                block_idx = peak//block_size
                if found[block_idx] == False:
                    found[block_idx] = True
                    found_count += 1
 
            if found_count == num_blocks:
                return num_blocks
 
    return 0
