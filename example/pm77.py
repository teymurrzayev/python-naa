def minimum_distances(a):
    last_seen = {}
    min_dist = float('inf')

    for i, val in enumerate(a):
        if val in last_seen:
            min_dist = min(min_dist, i - last_seen[val])
        last_seen[val] = i

    return min_dist if min_dist != float('inf') else -1
