def blockSizeIsValid(A, max_block_cnt, max_block_size):
    block_sum = 0
    block_count = 0
 
    for element in A:
        if block_sum + element > max_block_size:
            block_sum = element
            block_count += 1
        else:
            block_sum += element
        if block_count >= max_block_count:
            return False
 
    return True
 
def MinMaxDivision(A, K):
    # divide array A into K blocks of size 0 or more, then find smallest possible large sum of one block
    lower_bound = max(A)
    upper_bound = sum(A)
 
    if K == 1:
        return upper_bound #if only one block is allowed
    if K >= len(A):
        return lower_bound # if each block has one element
 
    while lower_bound <= upper_bound:
        candidate_mid = (lower_bound + upper_bound) // 2
        if blockSizeIsValid(A, K, candidate_mid):
            upper_bound = candidate_mid - 1
        else:
            lower_bound = candidate_mid + 1
 
    return lower_bound
