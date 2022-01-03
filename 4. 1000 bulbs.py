"""
*4. 1000 Bulbs*
*Intro:* There are 1000 light bulbs and 1000 persons. All light bulbs are initially off. Person 1 goes flipping light bulb 1, 2, 3, 4, … person 2 then flips 2, 4, 6, 8, … person 3 then 3, 6, 9, … etc until all 1000 persons have done this. 

*Problem:*
*a.* What is the status of light bulb 25, 93, 576, 132, 605, 26, 45, 37, 36 after all persons have flipped their respective light bulbs? 
*b.* Is there a general solution to predict the status of a light bulb? 
*c.* How many light bulbs are on after all 1000 persons have gone by?
"""

print("\nNumber 4")
import math
"""
def isperfect(x):
    if math.pow(int(math.sqrt(x)), 2) == x:
        return True
    else:
        return False
count = 0
for i in range( 1, 1000):
    if isperfect(i):
        count = count + 1
"""

print("There are ", int(math.sqrt(1000)), "light bulbs on")
