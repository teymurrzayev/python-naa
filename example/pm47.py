from collections import Counter

def happyLadybugs(b):
    if '_' not in b:
        for i in range(len(b)):
            if (i > 0 and b[i] == b[i - 1]) or (i < len(b) - 1 and b[i] == b[i + 1]):
                continue
            return "NO"
        return "YES"
    else:
        counts = Counter(b)
        for k in counts:
            if k != '_' and counts[k] == 1:
                return "NO"
        return "YES"
