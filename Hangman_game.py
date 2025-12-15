"""
Author:  Ivanloe L. Manuel
Date written: 12/08/2025
Assignment:   Module 7: Assignment - Python Development - Hangman Game
Short Desc:   This program is a simple Hangman word-guessing game. The computer randomly selects a word from a list .
The player has 6 attempts to guess the word by entering one letter at a time.
"""
import random

def hangman():
    # Word list
    words = ['python', 'java', 'kotlin', 'javascript']
    word = random.choice(words)  # Computer selects a random word

    attempts = 6
    guessed_letters = set()
    hidden_word = ["-"] * len(word)  # Display hidden word with dashes

    print("Welcome to Hangman!")

    # Game loop
    while attempts > 0 and "-" in hidden_word:
        print("\nWord: " + "".join(hidden_word))
        print(f"Attempts left: {attempts}")
        print("Guessed letters:", " ".join(sorted(guessed_letters)))

        guess = input("Guess a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
            for i, letter in enumerate(word):
                if letter == guess:
                    hidden_word[i] = guess
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            attempts -= 1

    # End of game
    if "-" not in hidden_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
    else:
        print("\n💀 Game over! The word was:", word)

# Run the game
if __name__ == "__main__":
    hangman()