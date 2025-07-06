def quick_sort_partition(arr: list[int], pivot_index: int) -> int:
    if not arr or pivot_index >= len(arr):
        return -1 
    
    pivot = arr[pivot_index]
    arr[pivot_index], arr[-1] = arr[-1], arr[pivot_index]
    
    i = 0
    for j in range(len(arr) - 1):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[-1] = arr[-1], arr[i]
    return i