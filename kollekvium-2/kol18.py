def find_longest_word(words):
    longword=""
    for word in words:
        if len(word) > len(longword):
            longword=word
    return longword
print(find_longest_word())