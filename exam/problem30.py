def findPoisonedDuration(timeSeries, duration):
    if not timeSeries:
        return 0

    total = 0
    for i in range(len(timeSeries) - 1):
        diff = timeSeries[i + 1] - timeSeries[i]
        total += min(diff, duration)

    total += duration  
    return total