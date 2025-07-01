def pickingNumbers(a: list[int]) -> int:
    frequency = {}
    for num in a:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    max_length = 0
    for num in frequency:
        current_length = frequency[num]
        if (num + 1) in frequency:
            current_length += frequency[num + 1]
        if current_length > max_length:
            max_length = current_length
    
    return max_length