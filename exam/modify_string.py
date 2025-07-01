def modify_string(s: str) -> str:
    s = list(s)
    for i in range(len(s)):
        if s[i] == '?':
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if (i == 0 or c != s[i-1]) and (i == len(s)-1 or c != s[i+1]):
                    s[i] = c
                    break
    return ''.join(s)