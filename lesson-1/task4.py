import random

the_number= random.randint(1, 4)
guess=None

print("Choose a number between 1 and 4")

while guess != the_number:
    guess=int(input())
    if guess > the_number:
        print("Player guess lower than the_number")
    elif guess < the_number:
        print("Player guess higher than the_number")
    else:
        print("Player guess the_number")
        break
print("Thank you")