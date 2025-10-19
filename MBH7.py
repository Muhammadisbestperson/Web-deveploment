import random
playing=True
number = str(random.randint(100,1000))
print('I will generate a number from 100 to 1000, and you have to guess the number one digit at a time.')
print("The game ends afer you have 1 hero/win!")
while playing:
    guess=input('Give me your best guess!\n')
    if number == guess:
        print('You won the game on having 1 hero')
        print("The number was",number)
        break
    else:
        ("Your guess isn't quite right,try again.\n")