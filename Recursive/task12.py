def to_binary(n):
    if n==0:
        return "0"
    if n==1:
        return "1"
    return to_binary(n//2)+str(n%2)
print(to_binary())



