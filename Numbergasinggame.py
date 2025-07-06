import random
num=random.randint(1,1000)
user=int(input("Hello Sir,welcome to the guessing game part 2 Please write your name )")) 
print("welcome {}, have good luck in this game ")
num_guesses=0
while(num_guesses<1000):
    user=int(input("Welcome to another number guessing Game (Part 2). Enter your guess from(1-1000)"))
   
    num_guesses+=1

    if user<num:
        print("Your guess is too low, please guess a higher number.")
    if user>num:
        print("Your guess is too high, please guess a lower number.")  
    if user==num:
        break


if num==user:
       print("You guessed the number in",num_guesses,"tries")
else:
    print("You couldn't guess the number. The number is ",num)                                                                                                                                                                                                                  