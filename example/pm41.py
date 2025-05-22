def find_shortest_subarray_with_degree(nums):
    from collections import defaultdict

    count = defaultdict(int)
    first_index = {}
    last_index = {}
    degree = 0

    for i, num in enumerate(nums):
        count[num] += 1
        if num not in first_index:
            first_index[num] = i
        last_index[num] = i
        degree = max(degree, count[num])

    min_len = float('inf')
    for num in count:
        if count[num] == degree:
            length = last_index[num] - first_index[num] + 1
            min_len = min(min_len, length)

    return min_len
