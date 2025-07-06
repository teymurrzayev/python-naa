def sum_of_unique_elements(nums: list[int]) -> int:
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    
    return sum(num for num, cnt in count.items() if cnt == 1)