def beautifulDays(i, j, k):
    count = 0
    for day in range(i, j + 1):
        rev = int(str(day)[::-1])  
        if abs(day - rev) % k == 0:
            count += 1
    return count
