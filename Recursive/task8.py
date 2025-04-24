def print_to_n(n):
    if n==1:
        print(n)
        return 
    print_to_n(n-1)
    print(n, end=' ')
