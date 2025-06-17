def repeated_string(s, n):
    return s.count('a') * (n // len(s)) + s[:n % len(s)].count('a')
