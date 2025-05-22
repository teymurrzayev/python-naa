def alternate(s):
    max_len = 0
    unique_letters = list(set(s))  

    for i in range(len(unique_letters)):
        for j in range(i + 1, len(unique_letters)):
            a = unique_letters[i]
            b = unique_letters[j]
            filtered = [ch for ch in s if ch == a or ch == b]

            
            if is_alternating(filtered):
                max_len = max(max_len, len(filtered))

    return max_len

def is_alternating(arr):
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            return False
    return True
print(alternate()) 