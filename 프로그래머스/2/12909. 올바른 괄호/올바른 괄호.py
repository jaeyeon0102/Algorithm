def solution(s):
    stack = []
    
    if s[0] == ')' or not s:
        return False
    
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
            
    return len(stack) == 0
