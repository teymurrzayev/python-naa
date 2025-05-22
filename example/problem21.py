def compare_swaps_bubble_insertion_sort(arr):
    def bubble_swaps(a):
        a = a.copy()
        swaps = 0
        n = len(a)
        for i in range(n):
            for j in range(0, n - i - 1):
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
                    swaps += 1
        return swaps

    def insertion_swaps(a):
        a = a.copy()
        swaps = 0
        for i in range(1, len(a)):
            key = a[i]
            j = i - 1
            while j >= 0 and a[j] > key:
                a[j + 1] = a[j]
                swaps += 1
                j -= 1
            a[j + 1] = key
        return swaps

    bubble = bubble_swaps(arr)
    insertion = insertion_swaps(arr)

    return "bubble" if bubble < insertion else "insertion"
