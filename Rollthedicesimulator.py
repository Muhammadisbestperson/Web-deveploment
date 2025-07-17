import random

def roll_dice(num_sides=6):
    """
    Simulates rolling a single die.

    Args:
        num_sides (int): The number of sides on the die. Defaults to 6.

    Returns:
        int: The result of the dice roll.
    """
    if num_sides < 1:
        print("Error: A die must have at least one side.")
        return None
    return random.randint(1, num_sides)

def main():
    print("Welcome to the Dice Rolling Simulator!")
    while True:
        try:
            user_input = input("Press Enter to roll the dice (or 'q' to quit): ").strip().lower()
            if user_input == 'q':
                print("Goodbye!")
                break
            elif user_input == '':
                result = roll_dice()
                if result is not None:
                    print(f"You rolled a: {result}")
            else:
                print("Invalid input. Please press Enter or 'q'.")
        except ValueError:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()