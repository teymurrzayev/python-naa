def power_of_string(s: str) -> int:
    if not s:
        return 0
    
    max_power = 1
    current_power = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            current_power += 1
            max_power = max(max_power, current_power)
        else:
            current_power = 1
    
    return max_power