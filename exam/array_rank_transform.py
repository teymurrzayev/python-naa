def array_rank_transform(arr: list[int]) -> list[int]:
    sorted_unique = sorted(set(arr))
    rank_dict = {num: i+1 for i, num in enumerate(sorted_unique)}
    
    return [rank_dict[num] for num in arr]