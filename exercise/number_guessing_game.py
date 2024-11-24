# /#
# Write a program to have the computer randomly select a number between 1 and 100,
# and then prompt the player to guess the number. The program should give
# hints if the guess is too high or too low.
# /
import random

number = random.randint(1, 100)
while True:
    try:
        guess = int(input("Guess the number between 1 to 100: "))
        if guess == number:
            print(f"Congratulations! You guessed the number in  tries.")
            break
        elif guess < number:
            print("Too low.")
        else:
            print("Too high.")
    except ValueError:
        print("Invalid input. Please enter a number.")
