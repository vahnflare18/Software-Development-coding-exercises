"""
Author:  Ivanloe L. Manuel
Date written: 12/05/2025
Assignment:   Module 6 Assignment - Python and Integrated Development Environments (IDEs)
Short Desc:   This program number‑guessing game where the computer picks a random number between 1 and 100,
and the player keeps guessing until correct, with feedback for too high/too low and error handling for invalid input.
"""
import random

low = 1
high = 100
# Computer picks a random number between 1 and 100
number = random.randint(low, high)
attempts = 0

while True:
    try:
        # Collect user input
        guess = int(input("Enter your guess (1-100): "))
        attempts += 1

        # Conditional checks
        if guess > number:
            print("Too high, try again.")
        elif guess < number:
            print("Too low, try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

    except ValueError:
        # Handle invalid inputs like letters or symbols
        print("Invalid input! Please enter a number.")