def Brackets(S):
    # determine if a given string of parentheses, curly braces, and square braces is properly nested
    stack = []
    for char in S:
        if char in ('(', '{', '['):
            stack.append(char) #keep track of all currently unclosed characters
        elif char == ')':
            if len(stack) == 0 or stack[len(stack)-1] != '(':
                return 0
            stack.pop(len(stack)-1)
        elif char == '}':
            if len(stack) == 0 or stack[len(stack)-1] != '{':
                return 0
            stack.pop(len(stack)-1)
        elif char == ']':
            if len(stack) == 0 or stack[len(stack)-1] != '[':
                return 0
            stack.pop(len(stack)-1)
    if len(stack) > 0: #check for leftover characters
        return 0
    return 1
