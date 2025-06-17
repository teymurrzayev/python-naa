def caesarCipher(s: str, k: int) -> str:
    result = []
    k = k % 26  
    
    for char in s:
        if char.isupper():         
            shifted = ord(char) + k
            if shifted > ord('Z'):
                shifted -= 26
            result.append(chr(shifted))
        elif char.islower():
            shifted = ord(char) + k
            if shifted > ord('z'):
                shifted -= 26
            result.append(chr(shifted))
        else:
            result.append(char)
    
    return ''.join(result)