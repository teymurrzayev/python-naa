def closestNumbers(arr):
    arr.sort()
    result = []

    for i in range(len(arr) - 1):
        result.append(arr[i])
        result.append(arr[i + 1])

    return result