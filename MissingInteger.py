def MissingInteger(A):
    # find smallest positive integer not present in A
	seen = [False] * len(A)
	for elem in A:
		if 0 < elem <= len(A):
			seen[elem-1] = True

	for i in range(len(A)):
		if seen[i] == False:
			return i + 1
	return len(A)+1
