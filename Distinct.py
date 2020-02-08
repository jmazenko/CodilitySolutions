def Distinct(A):
    # find number of distinct elements in A
    trimmed_list = set(())
    for elem in A:
        trimmed_list.add(elem)
    return len(trimmed_list)
