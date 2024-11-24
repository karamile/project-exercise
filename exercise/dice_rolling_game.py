#loop
#ask: roll the dice and get the sum of the numbers on the dice. If the sum is 7 or 11, you win. If the sum is 2, 3, or 12, you lose. If the sum is anything else, you keep rolling the dice until you get the sum from the first roll again, in which case you win, or you get a 7, in which case you lose.
#if user enter y, then roll the dice again, if user enter n, then stop the game
#generate two random numbers between.
#print them.
#if user enters n.
# print thank you for playing the game.
# terminate the game.
#else
#print invalid input.
######################
import random

while True:
  choice = input("Do you want to roll the dice? (y/n): ").lower()
  if choice == 'y':
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    print(f"Die 1: {die1}, Die 2: {die2}")
  elif choice == 'n':
    print("Thank you for playing the game.")
    break
  else:
    print("Invalid input.")
#
#Optional Enhancements
#• Modify the program so the user can specify how many dice they want to roll.
#• Add a feature that keeps track of how many times the user has rolled the dice
#during the session. This will require a counter that increments each time the
#dice are rolled.
#
#Optional Enhancements • Modify the program so the user can specify how many dice they want to roll. • Add a feature that keeps track of how many times the user has rolled the dice during the session. This will require a counter that increments each time the dice are rolled.