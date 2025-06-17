def diet_plan_performance(calories: list[int], k: int, lower: int, upper: int) -> int:
    score = 0
    window_sum = sum(calories[:k])
    if window_sum < lower:
        score -= 1
    elif window_sum > upper:
        score += 1
    
    for i in range(1, len(calories) - k + 1):
        window_sum = window_sum - calories[i - 1] + calories[i + k - 1]
        if window_sum < lower:
            score -= 1
        elif window_sum > upper:
            score += 1
    
    return score