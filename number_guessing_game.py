import random

number = random.randint(1, 100)

while True:
    try:
        user_number = int(input("Guess the number between 1 and 100: "))
        if number < user_number:
            print("Lower")
        elif number > user_number:
            print("Higher")
        else:
            print("Congratulations! You guessed the number.")
            break
    except ValueError:
        print("Invalid input")
