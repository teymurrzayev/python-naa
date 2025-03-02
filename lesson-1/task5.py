depozit=int(input())
amount=int(input())
operation=int(input())
if operation==1:
    if amount>depozit:
        print("You do not have enough money")
    else:
        depozit=depozit-amount
        print(depozit)
elif operation==2:
    depozit=depozit+amount
    print(depozit)
else:
    print("Invalid operation")





