def next_greatest_letter(letters, target):
    for c in letters:
        if c > target:
            return c
    return letters[0]
