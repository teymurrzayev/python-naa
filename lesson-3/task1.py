def flatten_arr(arr):
    flattened_arr=[]
    for arr1 in arr:
        if isinstance(arr1,list):
            flattened_arr.append(arr1)
            for arr2 in arr:
                if isinstance(arr2,list):
                    flattened_arr.append(arr2)
                    for arr3 in arr:
                        if isinstance(arr3,list):
                            flattened_arr.append(arr3)
                        else:
                            arr3=list(arr3)
                            flattened_arr.append(arr3)
                else:
                    arr2=list(arr2)
                    flattened_arr.append(arr2)
        else:
            arr1=list(arr1)
            flattened_arr.append(arr1)
    return flattened_arr
print(flatten_arr)