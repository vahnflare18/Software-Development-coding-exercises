"""
Author:  Ivanloe L. Manuel
Date written: 11/26/2025
Assignment:   Module 05 Practice Exercise 6-6
Short Desc:   This program defines a custom function called myRange() that replicates the behavior of Python’s
 built‑in range() function but returns a list instead of a range object.
"""
def myRange(start, stop=None, step=None):
    # Handle case where only stop is provided
    if stop is None:
        stop = start
        start = 0

    # Default step
    if step is None:
        step = 1

    # Validate step
    if step == 0:
        raise ValueError("step argument must not be zero")

    result = []

    # Counting up
    if step > 0:
        while start < stop:
            result.append(start)
            start += step
    # Counting down
    else:
        while start > stop:
            result.append(start)
            start += step

    return result
print(myRange(10))          # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(myRange(1, 10))       # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(myRange(1, 10, 2))    # [1, 3, 5, 7, 9]