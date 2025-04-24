def remove_duplicates(lst):
    list1 = []
    for num in lst:
        if num not in list1:  
            list1.append(num)
    return list1

print(remove_duplicates())