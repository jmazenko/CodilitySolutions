def FrogRiverOne(X, A):
    # a frog is trying to jump across a river that is X spaces wide. A[k] = position where a leaf falls and stays at k seconds
    # find earliest time at which all spaces are covered by leaves, allowing frog to cross river
    spots_covered = set(()) # constructs an empty set
    for i, e in enumerate(A):
        spots_covered.add(e) # only works when array element is not already part of set
        if len(spots_covered) == X:
            return i
    return -1
