# REFERENCE FUNCTION
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
"""
*6. Circular Prime*
*Intro:* The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

*Problem:* How many circular primes are there below one million?
"""

print("\nNumber 6")
def circular(x):
    if prime(x):
        cir = []
        length = len(str(x))
        if length == 1:
            cir.append(x) 
        else:
            num = x
            count = 0
            while count < length - 1:
                rem = num%10
                num = str(rem) + str(num)
                num = num[0:length]
                num = int(num)
                cir.append(num)
                count = count + 1
        
        for i in cir:
            if prime(i) == False:
                return False
            return True
    return False
circular_prime = 0
for i in range(1, 1000000):
    if circular(i):
        circular_prime = circular_prime + 1
print("Number of circular primes below a million: ", circular_prime)
