"""
Author:  Ivanloe L. Manuel
Date written: 11/12/2025
Assignment:   Module 03 Practice Exercise - Debugging
Short Desc:   A program that analyzes text readability using the Flesch formula.
    It counts sentences, words, and syllables, with corrected logic so consecutive vowels are treated as one syllable.
"""

# Take the inputs
fileName = input("Enter the file name: ")
inputFile = open(fileName, 'r')
text = inputFile.read()

# Count the sentences
sentences = text.count('.') + text.count('?') + \
            text.count(':') + text.count(';') + \
            text.count('!')

# Count the words
words = len(text.split())

# Count the syllables
syllables = 0
vowels = "aeiouAEIOU"

for word in text.split():
    prev_char_vowel = False
    for ch in word:
        if ch in vowels:
            if not prev_char_vowel:   # only count the first in a sequence
                syllables += 1
            prev_char_vowel = True
        else:
            prev_char_vowel = False

    # Adjustments for common endings
    for ending in ['es', 'ed', 'e']:
        if word.endswith(ending):
            syllables -= 1
    if word.endswith('le'):
        syllables += 1

# Compute the Flesch Index and Grade Level
index = 206.835 - 1.015 * (words / sentences) - \
        84.6 * (syllables / words)
level = int(round(0.39 * (words / sentences) + 11.8 * \
                  (syllables / words) - 15.59))

# Output the results
print("The Flesch Index is", index)
print("The Grade Level Equivalent is", level)
print(sentences, "sentences")
print(words, "words")
print(syllables, "syllables")