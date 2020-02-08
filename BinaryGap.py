def BinaryGap(N):
    # given number N, find length of longest contiguous subsequence of 0's in binary representation of N
    binary_string = str(bin(N))[2:]
    has_gap = False
    max_gap = 0
    gap_counter = 0
    for digit in binary_string:
    	if digit == '1':
            if max_gap < gap_counter:
                max_gap = gap_counter
            has_gap = True
            gap_counter = 0
        elif has_gap:
            gap_counter += 1
    return max_gap

    # alternate one-line solution; exclusive to Python
    # return len(max(bin(N)[2:].strip('0').strip('1').split('1')))
