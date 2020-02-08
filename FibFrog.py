def FibFrog(A):
    # A represents spaces on a river. A[k] = 1 if there is a leaf at index k
    # a frog is located at one bank of river (A[-1]) and wants to jump to other bank
    # frog can only jump a distance F, where F is any Fibonacci number
    # find minimum number of jumps for frog to cross river (or -1 if there is no way to cross)

    # we simplify algorithm by recognizing that it must always be possible to step on opposite bank
    A.append(1)
 
    fib_set = get_fib_seq_up_to_n(len(A))
     
    # reachable[k] = least number of jumps to index k, or -1 if index k is unreachable
    reachable = [-1] * (len(A))
     
    # find reachable leaves
    for jump in fib_set:
        if A[jump-1] == 1:
            reachable[jump-1] = 1
     
    # iterate all positions until you reach opposite bank
    for idx in range(len(A)):
        # ignore non-leaves and already found paths
        if A[idx] == 0 or reachable[idx] > 0:
            continue
 
        # get optimal jump count to reach this leaf
        min_idx = -1
        min_value = 100000
        for jump in fib_set:
            previous_idx = idx - jump
            if previous_idx < 0:
                break
            if reachable[previous_idx] > 0 and min_value > reachable[previous_idx]:
                min_value = reachable[previous_idx]
                min_idx = previous_idx
        if min_idx != -1:
            reachable[idx] = min_value +1
 
    return reachable[len(A)-1]

def get_fib_seq_up_to_n(N):
    # max. size of A is given as 100000, and there are 26 Fibonacci numbers smaller than 100000
    fib = [0] * (27)
    fib[1] = 1
    for i in range(2, 27):
        fib[i] = fib[i - 1] + fib[i - 2]
        if fib[i] > N:
            return fib[2:i]
