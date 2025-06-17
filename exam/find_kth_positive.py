def find_kth_positive(arr: list[int], k: int) -> int:
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] - mid - 1 < k:
            left = mid + 1
        else:
            right = mid
    return left + k