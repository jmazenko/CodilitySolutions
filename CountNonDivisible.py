def CountNonDivisible(A):
    # build and return array no_div, where no_div[k] = number of elements in A that are not divisors of element A[k]
    div = {}
    for elem in A:
        div[elem] = set([1, elem])

    A_max = max(A)
    idx = 2
    while idx * idx <= A_max:
        elem = idx
        while elem <= A_max:
            if elem in div and not idx in div[elem]:
                div[elem].add(idx)
                div[elem].add(elem // idx)
            elem += idx
        idx += 1

    count = {}
    for elem in A:
        if elem not in count:
            count[elem] = 1
        else:
            count[elem] += 1

    no_div = [0]*len(A)
    for idx, elem in enumerate(A):
        tmp = 0
        for value in div[elem]:
            tmp += count.get(value, 0)
        
        no_div[idx] = len(A) - tmp

    return no_div 
