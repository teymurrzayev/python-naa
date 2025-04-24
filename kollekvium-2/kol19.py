def count_vowels(s):
    vowel="aeouiAEOUI"
    sum=0
    for letter in s:
        if letter in vowel:
            sum+=1
    return sum
print(count_vowels())
