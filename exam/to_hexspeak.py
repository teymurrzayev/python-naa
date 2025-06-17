def to_hexspeak(num):
    hex_str = hex(int(num))[2:].upper().replace('0', 'O').replace('1', 'I')
    if any(c not in 'ABCDEFIO' for c in hex_str):
        return "ERROR"
    return hex_str
