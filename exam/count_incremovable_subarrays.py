def count_incremovable_subarrays(nums: list[int]) -> int:
    count = 0
    n = len(nums)
    
    for i in range(n):
        for j in range(i, n):
            remaining = nums[:i] + nums[j+1:]
            is_increasing = True
            for k in range(len(remaining) - 1):
                if remaining[k] >= remaining[k+1]:
                    is_increasing = False
                    break
            if is_increasing or not remaining:
                count += 1
                
    return count