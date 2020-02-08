import math

def FrogJump(X, Y, D):
    # a frog is at position X and wants to reach position Y. Every jump propels frog a distance D. Find minimum number of jumps
    return math.ceil((Y-X)/D)
