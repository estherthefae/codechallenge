"""
*5. Numbers Conversion*
*intro:* If you converted numbers to words, then:

-1050 _will be:_ minus one thousand and fifty

2659917 _will be:_ two million, six hundred and fifty nine thousand, nine hundred and seventeen

*Problem:* Write a Program that will convert any integer to words - the commas and all - with a range from minus 1 quintillion to plus  1 quintillion.
"""

print("\nNumber 5")
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
    
again = "yes"
while again == "yes":
    number = input("Enter the number in figures: ")
    print(number + " in words: " + seperator(number))
    again = input("Do you want to try again: " ).lower()
