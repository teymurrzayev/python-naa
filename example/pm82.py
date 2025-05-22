from collections import Counter

def pickingNumbers(a):
    freq = Counter(a)
    max_len = 0

    for num in freq:
        current = freq[num] + freq.get(num + 1, 0)
        max_len = max(max_len, current)

    return max_len
