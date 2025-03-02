a=float(input())
b=float(input())
operation=int(input())
if 1<= operation <=4:
    if operation == 1:
        print((a+b))
    if operation == 2:
        if a>b:
            print(a-b)
        else:
         print(b-a)
    if operation == 3:
        print(a*b)
    if operation == 4:
        if b == 0:
            print("no division by zero")
        else:
            print(a/b)
else:
    print("operation number is not defined")