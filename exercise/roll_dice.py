import random


def roll_dice(number_dice):
    return [random.randint(1, 6) for _ in range(number_dice)]


roll_count = 0

while True:
    choice = input("Do you want to roll the dice? (y/n): ").lower()
    if choice == 'y':
        number_of_dice = int(input("How many dice do you want to roll? "))
        dice = roll_dice(number_of_dice)
        print(f"Dice: {dice}")
        roll_count += 1
        print(f"You have rolled the dice {roll_count} times.")
    elif choice == 'reset':
        roll_count = 0
        print("Roll count has been reset.")
    elif choice == 'n':
        print(f"Thank you for playing the game. You rolled the dice {roll_count} times.")
        break
    else:
        print("Invalid input.")
