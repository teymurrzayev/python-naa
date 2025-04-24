def reverse_string(s):
    if 1>=len(s):
        return s
    return s[-1]+reverse_string[:-1]
print(reverse_string())