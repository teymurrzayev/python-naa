def rotate_function(arr):
    k=int(input())
    n=len(arr)
    if n>k and k>0:
        arr=arr[:-k]+arr[-k:]
        print(arr)
    else:
        print("Your code is wrong")
       



