def find_final_array(arr: list[int]) -> list[int]:
    changed = True
    while changed:
        changed = False
        new_arr = arr.copy()
        for i in range(1, len(arr) - 1):
            left = arr[i - 1]
            right = arr[i + 1]
            current = arr[i]
            if current < left and current < right:
                new_arr[i] += 1
                changed = True
            elif current > left and current > right:
                new_arr[i] -= 1
                changed = True
        arr = new_arr
    return arr