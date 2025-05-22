def can_form_palindrome(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    odd_count = 0
    for count in freq.values():
        if count % 2 != 0:
            odd_count += 1

    if odd_count > 1:
        return "NO"
    else:
        return "YES"