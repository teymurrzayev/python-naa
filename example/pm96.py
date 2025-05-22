def superReducedString(s: str) -> str:
    stack = []

    for char in s:
        if stack and stack[-1] == char:
            stack.pop()  # eyni hərfi sil
        else:
            stack.append(char)

    return ''.join(stack) if stack else "Empty String"
