def remove_duplicates(arr):
    arr1=set()
    result=[]
    for arr2 in arr:
        if arr2 not in arr1:
            arr1.add(arr2)
            result.append(arr2)
    return result