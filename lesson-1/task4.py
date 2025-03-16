def random_number():
    guess=None
    print("Choose a number between 1 and 4")
    
    while guess != random_number:
        guess=int(input())
        if guess > random_number:
            print("Player guess lower than the_number")
        elif guess < random_number:
            print("Player guess higher than the_number")
        else:
            print("Congratulations")
            break

    print("Thank you")