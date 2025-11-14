import random 
import time
number=random.randint(0,200)
def intro():
    print("May I ask for your name? It is very important!")
    global name
    name=input()
    print(name +",we are going to play a game.where you have to guess a number between 0 and 200")
    if(number%2==0):
        x='even'
    else:
        x='odd'
        print('\nThis is an {} number',format(x))
        time.sleep(.5)
        print('Go ahead and guess!')
def pick():
    guessesTaken=0
    while guessesTaken <6:
        time.sleep(.25)
        enter=input("Guess:")
        try:
            guess=int(enter)
            if guess<=200 and guess>=0:
                guessesTaken=guessesTaken+1
                if guessesTaken<6:
                    if guess<number:
                        print("The guess of the number you have entered is too low")
                    if guess>number:
                        print("The guess of the number that you have entered is too high")
                    if guess!=number:
                        time.sleep(.5)
                        print("Try Again")
                    if guess==number:
                        break
                if guess>200 or guess<0:
                    print("That number is not in the range! Silly Goose!")
                    time.sleep(.25)
                    print("Please enter a number between 0 and 200")
        except:
            print("I don't think that "+enter+"is a number. Sorry :( ") 
            if guess == number:
                guessesTaken=str(guessesTaken)
                print("Excellent,{}! You guessed the number in {} guesses!".format(name,guessesTaken))
            if guess != number:
                print("Nope. The number was "+str(number))
playagain="yes"
while playagain=="yes" or playagain=='y'or playagain=="Yes":
    intro()
    pick()
    print("Do you want to play again? YOUR ANSWER HAS A LOT OF VALUE FOR US")
    playagain=input()