def product_list(arr):
    if not arr:
        return 1
    if 0 in arr:
        return 0
    return arr[0]*product_list(arr[1:])
print(product_list())