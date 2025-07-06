def sort_by_frequency(nums: list[int]) -> list[int]:
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
   
    nums.sort(key=lambda x: (freq[x], -x))
    
    return nums