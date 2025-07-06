def minimum_distances(a: list[int]) -> int:
    last_occurrence = {}
    min_distance = float('inf')
    
    for index, num in enumerate(a):
        if num in last_occurrence:
            distance = index - last_occurrence[num]
            if distance < min_distance:
                min_distance = distance
        last_occurrence[num] = index
    
    return min_distance if min_distance != float('inf') else -1