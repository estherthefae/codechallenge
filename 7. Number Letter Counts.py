#REFERENCE FUNCTIONS
def converter(x):
    numdict = {"1":["one"], "2":["two", "twenty"], "3":["three", "thirty"], "4":["four", "forty"], "5":["five", "fifty"], "6":["six", "sixty"], "7":["seven", "seventy"], "8":["eight", "eighty"], "9":["nine", "ninty"], "10": ["ten"], "11":["eleven"], "12":["twelve"], "13": ["thirteen"], "14":["fourteen"], "15": ["fifteen"], "16":["sixteen"], "17":["seventeen"], "18":["eighteen"], "19":["nineteen"]}
    x = x.lstrip("0")
    if x == "":
        return "0"
    if len(x) <= 2 and x in numdict:
        return ("and " + numdict[x][0])
    elif len(x) == 2 and x not in numdict:
        if x[-1] == "0":
            return ("and " + numdict[x[0]][1])
        else:
            return ("and " + numdict[x[0]][1] + " " + numdict[x[1]][0])

    elif len(x) == 3:
        if x[1:] in numdict or (x[1] == "0" and x[-1] != "0"):
            return (numdict[x[0]][0] + " hundred and " + numdict[x[1:].lstrip("0")][0])
        elif x[1:] not in numdict:
            if x[-1] == "0":
                if x[1] != "0":
                    return (numdict[x[0]][0] + " hundred and " + numdict[x[1]][1])
                else:
                    return (numdict[x[0]][0] + " hundred ")
            else:
                return (numdict[x[0]][0] + " hundred and " + numdict[x[1]][1] + " " + numdict[x[2]][0])
def seperator(num):
    x = num
    x = x.replace(",", "")
    x = x.strip(" - ")
    if len(x)%3 == 1:
        x = "00" + x
    elif len(x)%3 == 2:
        x = "0" + x
    if len(x) == 3:
        result = converter(x)
    elif len(x) > 3:
        xsplit = []
        for i in range(0, len(x), 3):
            xsplit.append(x[i: i + 3])
        if len(xsplit) == 2:
            result = converter(xsplit[0]) + " thousand, " + converter(xsplit[1]) 
        elif len(xsplit) == 3:
            result = (converter(xsplit[0]) + " million, " + converter(xsplit[1]) + " thousand, " + converter(xsplit[2]))  
        elif len(xsplit) == 4:
            result = (converter(xsplit[0]) + " billion, " + converter(xsplit[1]) + " million, " + converter(xsplit[2]) + " thousand, " + converter(xsplit[3]))
        elif len(xsplit) == 5:
            result = (converter(xsplit[0]) + " trillion," + converter(xsplit[1]) + " billion, " + converter(xsplit[2]) + " million, " + converter(xsplit[3]) + " thousand, " + converter(xsplit[4]))
        elif len(xsplit) == 6:
            result = (converter(xsplit[0]) + " quadrillion," + converter(xsplit[1]) + " trillion," + converter(xsplit[2]) + " billion, " + converter(xsplit[3]) + " million, " + converter(xsplit[4]) + " thousand, " + converter(xsplit[5]))
        elif len(xsplit) == 7:
            result = (converter(xsplit[0]) + " quintillion," +converter(xsplit[1]) + " quadrillion," + converter(xsplit[2]) + " trillion," + converter(xsplit[3]) + " billion, " + converter(xsplit[4]) + " million, " + converter(xsplit[5]) + " thousand, " + converter(xsplit[6]))
    return check(num, result)
def check (x, result):
    bug = ["0 quadrillion,", "0 million,", "0 billion,", "0 trillion,", " 0 thousand,"]
    for i in bug:
        if i in result:
            result = result.replace(i, "")
    result = result.replace("  ", " ")
    result = result.replace(", and", " and ")
    result = result.rstrip(", 0")
    if result[0:3] == "and" and result[4] in ["a", "n", "d"]:
        result = result[4] + result.lstrip("and ")
    else:
        result = result.lstrip("and ")
    if x[0] == "-":
        result = "minus " + result
    return result

"""
*7. Number Letter Counts*
*intro:* If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

*Problem:* If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

*Note:* Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

print("\nNumber 7")
count = 0
for i in range(1, 1001):
    i = str(i)
    solution = seperator(i)
    solution = (solution.replace(" ", "")).replace(",", "")
    count = count + len(solution)
print("Number Letter Count from 1 to 1000: ", count)

