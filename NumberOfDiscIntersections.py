def NumberOfDiscIntersections(A):
    # array A represents discs on a number line. If A[m] = n, there is a disc with midpoint m and radius n
    # compute number of pairs of intersecting discs
    events = [] # each entry of this array represents start and end points of one disc
    for i, a in enumerate(A):
        events += [(i-a, +1), (i+a, -1)] # we assume that +1 = start point, -1 = end point
    events.sort(key=lambda x: (x[0], -x[1])) # sort discs in ascending order by start point
    intersections, active_circles = 0, 0
    for _, circle_count_delta in events:
        intersections += active_circles * (circle_count_delta > 0) # only increase provided at least one circle is active
        active_circles += circle_count_delta # active_circles increases by one when a circle starts, decreases when a circle ends
        if intersections > 10E6:
            return -1
    return intersections

