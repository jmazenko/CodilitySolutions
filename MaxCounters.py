def MaxCounters(N, A):
    # you have N counters, each initialized to 0. If A[k] = N + 1, all counters are set to largest value of any counter
    # if A[k] <= N, counter number k is increased by one. Return an array representing outputs
    outputs = [0] * N
    max_val = 0
    for elem in A:
        if elem == N+1:
            outputs.clear()
            outputs.extend([max_val] * N)
        else:
            outputs[elem-1] += 1
            if outputs[elem-1] > max_val:
                max_val = outputs[elem-1]
    return outputs
