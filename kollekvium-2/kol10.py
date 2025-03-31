def count_positive_numbers(lst):
    lst1=0
    for i in lst:
        if i > 0:
            lst1+=1
    return lst1

print(count_positive_numbers())