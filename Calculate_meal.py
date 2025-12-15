"""
Author:  Ivanloe L. Manuel
Date written: 10/29/2025
Assignment:   Module 01 Programming Assignment
Short Desc:   Calculates the total cost of a meal, including an 18% tip and a 7% sales tax, then show the total bill amount.
"""
def calculate_meal_total():
    
    try:
        # Get the charge for the food from the user.
        food_charge = float(input("Enter the charge for the food: $"))

        # Check for non-negative input.
        if food_charge < 0:
            print("Error: The food charge cannot be a negative number.")
            return

        # Define tax and tip rates.
        tip_rate = 0.18
        tax_rate = 0.07

        # Calculate the tip amount (18% of the food charge).
        tip_amount = food_charge * tip_rate

        # Calculate the sales tax amount (7% of the food charge).
        tax_amount = food_charge * tax_rate

        # Calculate the total bill by adding the food charge, tip, and tax.
        total_amount = food_charge + tip_amount + tax_amount

        # Display the results.
        print("\n--- Meal Summary ---")
        print(f"Food Charge: ${food_charge:.2f}")
        print(f"Tip (18%):   ${tip_amount:.2f}")
        print(f"Tax (7%):    ${tax_amount:.2f}")
        print("--------------------")
        print(f"Total Bill:  ${total_amount:.2f}")

    except ValueError:
        # Handle cases where the user enters non-numeric data.
        print("Invalid input. Please enter a valid number for the food charge.")
calculate_meal_total()