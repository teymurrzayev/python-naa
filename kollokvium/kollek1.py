def unique_char_strings_average(strings_list):
    n=len(strings_list)
    a=0
    b=0
    c=0
    for i in range(0,n):
        b=list(strings_list[i])
        b=len(strings_list[i])
        a+=b
        c=a/n
        c=int(c)
    return c
print(unique_char_strings_average(["salam", "shdgf"]))



