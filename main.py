import random

def roll_dice():
    dice_result = random.randint(1, 6)
    return dice_result

def main():
    print("Welcome to the Dice Roller!")
    roll_again = True

    while roll_again:
        input("Press Enter to roll the dice...")
        result = roll_dice()
        print(f"You rolled a {result}!")

        choice = input("Do you want to roll again? (y/n): ")
        if choice.lower() != "y":
            roll_again = False

    print("Thank you for using the Dice Roller!")

if __name__ == "__main__":
    main()
