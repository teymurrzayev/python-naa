def alternate(s: str) -> int:
    unique_chars = []
    for char in s:
        if char not in unique_chars:
            unique_chars.append(char)
    
    max_length = 0  

    for i in range(len(unique_chars)):
        for j in range(i+1, len(unique_chars)):
            char1, char2 = unique_chars[i], unique_chars[j]
            current_length = 0
            prev_char = None
            is_valid = True

            for char in s:
                if char == char1 or char == char2:
                    if char == prev_char:  
                        is_valid = False
                        break
                    prev_char = char
                    current_length += 1

            if is_valid and current_length > max_length:
                max_length = current_length

    return max_length if max_length >= 2 else 0
