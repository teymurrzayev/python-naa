def increasing_func(arr):
    arr1=[]
    n=len(arr)
    for i in range(0,n):
        for j in range(1,n):
            if arr[i]>arr[j]:
                arr1.append(arr)
            if arr[i]==arr[j]:
                arr.remove(i)
                arr1.append(arr)
            else:
                print(arr)
    return arr1
print(increasing_func([]))
