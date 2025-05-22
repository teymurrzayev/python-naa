from collections import Counter

def migratoryBirds(arr):
    counts = Counter(arr)
    max_count = max(counts.values())

    return min([bird_id for bird_id, count in counts.items() if count == max_count])
