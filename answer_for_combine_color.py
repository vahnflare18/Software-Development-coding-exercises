"""
Author: Ivanloe L. Manuel
Date written: 11/02/2025
Assignment: Module 02 Programming Assignment
Short Description: This program prompts the user to enter two primary colors (red, blue, or yellow) and displays the results of that combination color.
"""
color1 = input("Enter the first primary color (red, blue, or yellow): ")
color2 = input("Enter the second primary color (red, blue, or yellow): ")

valid_colors = ["red", "blue", "yellow"]

if color1 not in valid_colors or color2 not in valid_colors:
    print ("Error: Invalid color entered. Please enter red, blue, or yellow.")
elif color1 == color2:
    print ("You entered the same color twice. Mixing requires two different primary colors.")
else:
    if ("red" in [color1, color2]) and ("blue" in [color1, color2]):
        print("Mixing red and blue gives you purple.")
    elif ("red" in [color1, color2]) and ("yellow" in [color1, color2]):
        print("Mixing red and yellow gives you orange.")
    elif ("blue" in [color1, color2]) and ("yellow" in [color1, color2]):
        print("Mixing blue and yellow gives you green.")