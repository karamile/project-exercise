# Optional Enhancements
# • Allow the user to specify the minimum and maximum values for the number
# range before the game starts. This gives the player more control over the difficulty level.
# • Implement a feature that limits the number of guesses a player can make. If
# the player runs out of attempts, the game should end, and the correct number
# should be revealed.
# • Add a feature that keeps track of the fewest attempts it took to guess the
# number correctly. The program should display this "best score" at the end of
# each game.
# • Implement a high-score system that keeps track of the best scores across

import random


def guessing_game():
    print("Welcome to the Guessing Game!")

    min_value = int(input("Enter the minimum value for the number range: "))
    max_value = int(input("Enter the maximum value for the number range: "))

    number_to_guess = random.randint(min_value, max_value)
    max_attempts = int(input("Enter the maximum number of attempts: "))

    attempts = 0
    best_score = float('inf')

    while attempts < max_attempts:
        guess = int(input(f"Guess a number between {min_value} and {max_value}: "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            if attempts < best_score:
                best_score = attempts
            break
    else:
        print(f"Sorry, you've run out of attempts. The correct number was {number_to_guess}.")

    print(f"Your best score is {best_score} attempts.")
    print("Thank you for playing the game!")


guessing_game()
