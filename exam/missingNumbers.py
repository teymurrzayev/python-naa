def missingNumbers(arr: list[int], brr: list[int]) -> list[int]:
    from collections import defaultdict

    freq_arr = defaultdict(int)
    freq_brr = defaultdict(int)
    
    for num in arr:
        freq_arr[num] += 1
    
    for num in brr:
        freq_brr[num] += 1
    
    missing = []
    for num in freq_brr:
        if freq_arr[num] != freq_brr[num]:
            missing.append(num)

    return sorted(missing)