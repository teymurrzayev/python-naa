def check_segment_length(s: str) -> bool:
    max_ones = 0
    max_zeros = 0
    current_ones = 0
    current_zeros = 0
    
    for char in s:
        if char == '1':
            current_ones += 1
            current_zeros = 0
            if current_ones > max_ones:
                max_ones = current_ones
        else: 
            current_zeros += 1
            current_ones = 0
            if current_zeros > max_zeros:
                max_zeros = current_zeros
    
    return max_ones > max_zeros