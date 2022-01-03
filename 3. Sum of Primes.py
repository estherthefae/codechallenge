"""
3. Sum of Primes*
*Intro:* The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

*Problem:* Write a program to find the sum of all the primes below one million.
"""

print("\nNumber 3")
def prime(x):
    if x == 1:
        return False
    top = [2, 3, 5, 7]
    result = []
    if x in top:
        return True
    else:
        for i in top:
            if x%i == 0 and x not in top:
                return False
        return True
summation = 0
for i in range(1, 1000000, 2):
    if prime(i) is True:
        summation = summation + i
print("Sum of prime numbers between 1 and 1 million: ", summation)
