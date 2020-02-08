def solution(A):
    # if some element appears at more than half of array indices, find its first occurrence
	if len(A) > 0:
		N = len(A)
		B = A.copy()
		B.sort() # we cannot sort A in-place because returned index must be relative to original array
		candidate = B[N//2]
		count = 0
		for i in range(N):
			if B[i] == candidate:
				count += 1
		if count > N//2:
			return A.index(candidate)
	return -1
