def repeatedString(s: str, n: int) -> int:
    a_in_s = s.count('a')
    full_repeats = n // len(s)
    remainder = n % len(s)

    total_a = full_repeats * a_in_s + s[:remainder].count('a')
    return total_a
