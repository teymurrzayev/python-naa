def second_largest(arr):
    if len(arr) < 2:
        return None    
    temp1=arr[0] 
    temp2=arr[1]
    if temp1 < temp2:
        temp1=temp2
        temp2=temp1
    for n in arr[2:]:
        if n > temp1:
            temp1=n
            temp2=temp1
        elif n > temp2:
            temp2 = n
    return temp2
        


