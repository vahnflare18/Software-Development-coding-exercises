"""
Author: Ivanloe L. Manuel
Date written: 11/02/2025
Assignment: Module 02 Practice Exercise 3-9
Short Description: This program receives a series of numbers from the user, calculates their sum and average, and displays the results.
"""
theSum = 0
count = 0

while True:
    number_str = input("Enter a number or press Enter to quit: ")

    if number_str == "":
        break

    try:
        number = float(number_str)
        theSum += number
        count += 1
    except ValueError:
        print("Invalid input. Please enter a valid number or press Enter to quit.")

print("\nThe sum is", theSum)

if count > 0:
    average = theSum / count
    print("The average is", average)
else:
    print("No numbers were entered, so an average cannot be calculated.")