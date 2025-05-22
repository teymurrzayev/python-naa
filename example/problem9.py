def caesarCipher(s, k):
    result = ""
    k = k % 26  

    for ch in s:
        if ch.islower():
            result += chr((ord(ch) - ord('a') + k) % 26 + ord('a'))
        elif ch.isupper():
            result += chr((ord(ch) - ord('A') + k) % 26 + ord('A'))
        else:
            result += ch  

    return result