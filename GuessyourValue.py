import random

lowest_number=190
highest_number=1200
answer= random.randint(lowest_number,highest_number)
guesses=0
is_running=True

print("Number Guessing game for Ages 10+")
print(f"select a number between {lowest_number} and {highest_number}")
while is_running:

    guess=input("enter your guess:")

    if guess.isdigit():
        guess=int(guess)
        guesses += 1
    if guess < lowest_number or guess > highest_number:
        print("That number is out of range")
        print(f"Please select a number between {lowest_number} and {highest_number}")
    elif guess <  answer:
        print("too low! Try again")
    elif guess > answer:
        print("too high! Try again")
    else:
        print(f"Correct! The answer was {answer}")
        print(f"number of guesses:{guesses}")
        is_running=False
else:
    print("Your Answer is invalid or is not a number")
    print(f"Please select a number between {lowest_number} and {highest_number}")   