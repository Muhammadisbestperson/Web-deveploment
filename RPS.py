import random
def get_user_choice():
    user_choice = input('Enter your choice (rock,paper, or scissors):').lower()
    while user_choice not in ['rock','paper','scissors']:
        print("Invalid choice. Please enter rock,paper,scissor")
        user_choice = input("Enter yout choice (rock,paper,or scissors)")
    return user_choice

def get_computer_choice():
    return random.choice(['rock','paper','scissors'])

def play_game():
     print("Welcome to Rock,Paper,Scissors!")
     user_choice = get_user_choice()
     computer_choice = get_computer_choice ()
     print(f"You chose{user_choice}.")
     print(f"computer chose {computer_choice}.")
     result = determine_winner(user_choice, computer_choice)
     print(result)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "it's a tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return " You win"
    else:
        return "Computer Wins!"
if __name__ == "__main__":
    play_game()
