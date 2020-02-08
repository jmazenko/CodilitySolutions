def EquiLeader(A):
    # write your code in Python 3.6
    candidate = ''
    candidate_count = 0
 
    for value in A:
        if candidate == '':
            candidate = value
            candidate_count = 1
        else:
            if value != candidate:
                candidate_count -= 1
                if candidate_count == 0:
                    candidate = ''
            else:
                candidate_count += 1
 
    if candidate_count == 0:
        return 0
 
    count = 0
    last_idx = 0
 
    for i, e in enumerate(A):
        if e == candidate:
            count += 1
            last_idx = i
 
    if count < len(A)//2:
        return 0
 
    equi_count = 0
    left_count = 0
    for i, e in enumerate(A):
        if e == candidate:
            left_count +=1
        if left_count > (i + 1)//2 and \
            count - left_count > (len(A) - i - 1) //2:
            equi_count += 1
 
    return equi_count
