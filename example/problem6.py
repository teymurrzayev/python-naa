def balancedSums(arr):
    total = sum(arr)
    left_sum = 0

    for i in arr:
        if left_sum == (total - left_sum - i):
            return "YES"
        left_sum += i

    return "NO"