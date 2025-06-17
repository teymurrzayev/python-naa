def calculate_typing_time(keyboard: str, word: str) -> int:
    char_positions = {char: idx for idx, char in enumerate(keyboard)}
    
    total_time = 0
    current_pos = 0 
    
    for char in word:
        target_pos = char_positions[char]
        total_time += abs(target_pos - current_pos)
        current_pos = target_pos
    
    return total_time