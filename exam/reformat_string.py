def reformat_string(s: str) -> str:
    letters = []
    digits = []
    
    for char in s:
        if char.isalpha():
            letters.append(char)
        else:
            digits.append(char)
    
    if abs(len(letters) - len(digits)) > 1:
        return ""
    
    result = []
    if len(letters) > len(digits):
        first, second = letters, digits
    else:
        first, second = digits, letters
    
    for i in range(len(first)):
        result.append(first[i])
        if i < len(second):
            result.append(second[i])
    
    return ''.join(result)