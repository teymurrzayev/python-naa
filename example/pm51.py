from collections import Counter

def isValidStringSameOccurence(s):
    freq = Counter(s)
    count_freq = Counter(freq.values())

    if len(count_freq) == 1:
        return "YES"

    if len(count_freq) == 2:
        keys = list(count_freq.keys())
        val1, val2 = keys[0], keys[1]
        if (count_freq[val1] == 1 and (val1 - 1 == val2 or val1 == 1)) or \
           (count_freq[val2] == 1 and (val2 - 1 == val1 or val2 == 1)):
            return "YES"

    return "NO"
