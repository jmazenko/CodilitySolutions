def Nesting(S):
    # determine if a given string of parentheses is properly nested
    stack = []
    for char in S:
        if char == '(':
            stack.append(char)
        else:
            if len(stack) == 0 or stack[len(stack)-1] != '(':
                return 0
            stack.pop(len(stack)-1)
    if len(stack) > 0:
        return 0
    return 1
