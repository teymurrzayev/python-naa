def find_smallest_number(lst):
    if not lst:
        return None
    else:
        return min(lst)

print(find_smallest_number())