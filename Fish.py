def Fish(A, B):
    # there are N fish in a river. A[k] = size of fish k, while B[k] = direction (0 = upstream, 1 = downstream)
    # when two fish moving in opposite directions meet, larger fish eats smaller fish. Calculate how many fish will stay alive
    survivors = 0
    fish_stack = [] # maintain stack of all fish swimming downstream
    
    for i in range(len(A)):
        if B[i] == 0:
            while len(fish_stack) > 0: # large fish swimming upstream eats small fish off of stack until none remain, or large fish is eaten itself
                if fish_stack[-1] > A[i]: # A[-1] represents last element of array
                    break
                fish_stack.pop()
            else:
                survivors += 1 # if no downstream fish are ahead of this upstream fish, it survives
        else:
            fish_stack.append(A[i])
    survivors += len(fish_stack)
    return survivors
