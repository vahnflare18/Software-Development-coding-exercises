"""
Author: Ivanloe L. Manuel
Date written: 11/18/2025
Short Desc: This program reads a text file, extracts all unique words,
sorts them alphabetically, and prints them. It demonstrates Python file handling,
list operations, string processing, and the use of loops with membership checks to avoid duplicates.
"""
def main():
    inName = input("Enter the input file name: ")
    #Variables
    uniqueWords = []
    try:
        # Open file handling
        with open(inName, 'r') as inputFile:
            for line in inputFile:
                words = line.split()
                for word in words:
                    if word not in uniqueWords:
                        uniqueWords.append(word)
        # Sort words alphabetically
        uniqueWords.sort()
        # Print each word
        for word in uniqueWords:
            print(word)
    except FileNotFoundError:
        print("Error: File not found.")
if __name__ == "__main__":

    main()
