def compare_swaps_bubble_insertion_sort(arr):
    bubble, insertion = 0, 0

    a = arr[:]
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                bubble += 1

    a = arr[:]
    for i in range(1, len(a)):
        j = i
        while j > 0 and a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
            insertion += 1
            j -= 1
    return "insertion" if insertion < bubble else "bubble"