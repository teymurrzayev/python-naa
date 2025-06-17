def dist_plan_performance(calories, k, lower, upper):
    total = 0
    for i in range(len(calories)-k+1):
        s = sum(calories[i:i+k])
        if s < lower:
            total -= 1
        elif s > upper:
            total += 1
    return total
