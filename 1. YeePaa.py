"""
*1. YeePaa*
*Intro:* If we list out all the natural numbers from 1 to 15, the multiples of 3 will be 3, 6, 9, 12, 15  are while the multiples of 5 will be 5, 10 and 15.

*Problem:* Write a simple Program to take an input "X" and list vertically on the screen all natural numbers from 1 to X. In front of each number, if it's a multiple of 3, put *"Yee"*; if it's a multiple of 5, put *"Paa"* and if it's both a multiple 3 & 5, out *"Yee-Paa"*. Input validation - X can only be a positive integer greater than or equal to 10.
"""

print("\nNumber 1")
x = int(input("Enter amount of numbers: "))
if x < 10:
    x = int(input("Wrong input\nEnter number: "))
print("Numbers within range")
for i in range(1, x+1):
    if (i%3 == 0 and i%5 == 0):
        print(i, "Yee-Paa")
    elif (i%3 == 0 and i%5 != 0):
        print(i, "Yee")
    elif (i%3 != 0 and i%5 == 0):
        print(i, "Paa")
    else:
        print(i)
