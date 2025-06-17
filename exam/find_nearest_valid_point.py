def find_nearest_valid_point(x: int, y: int, points: list[list[int]]) -> int:
    min_distance = float('inf')
    result_index = -1

    for i, (px, py) in enumerate(points):
        if px == x or py == y: 
            distance = abs(x - px) + abs(y - py)
            if distance < min_distance:
                min_distance = distance
                result_index = i

    return result_index
