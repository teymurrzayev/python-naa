def remove_duplicates(arr):
    seen=set()
    result=[]
    for item in arr:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result