def balancedSums(arr: list[int]) -> str:
    total_sum = sum(arr)
    left_sum = 0
    
    for num in arr:
        right_sum = total_sum - num - left_sum
        if left_sum == right_sum:
            return "YES"
        left_sum += num
    
    return "NO"

