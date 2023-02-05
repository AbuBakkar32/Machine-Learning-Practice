# convert number to word translation

def numToWord(num):
    """Convert number to word"""
    if num == 0:
        return "zero"
    elif num == 1:
        return "one"
    elif num == 2:
        return "two"
    elif num == 3:
        return "three"
    elif num == 4:
        return "four"
    elif num == 5:
        return "five"
    elif num == 6:
        return "six"
    elif num == 7:
        return "seven"
    elif num == 8:
        return "eight"
    elif num == 9:
        return "nine"
    elif num == 10:
        return "ten"
    elif num == 11:
        return "eleven"
    elif num == 12:
        return "twelve"
    elif num == 13:
        return "thirteen"
    elif num == 14:
        return "fourteen"
    elif num == 15:
        return "fifteen"
    elif num == 16:
        return "sixteen"
    elif num == 17:
        return "seventeen"
    elif num == 18:
        return "eighteen"
    elif num == 19:
        return "nineteen"
    elif num == 20:
        return "twenty"
    elif num == 30:
        return "thirty"
    elif num == 40:
        return "forty"
    elif num == 50:
        return "fifty"
    elif num == 60:
        return "sixty"
    elif num == 70:
        return "seventy"
    elif num == 80:
        return "eighty"
    elif num == 90:
        return "ninety"
    elif num < 100:
        return numToWord(num - num % 10) + "-" + numToWord(num % 10)
    elif num == 100:
        return "one hundred"
    elif num < 200:
        return "one hundred and " + numToWord(num % 100)
    elif num < 1000:
        return numToWord(num // 100) + " hundred and " + numToWord(num % 100)
    elif num == 1000:
        return "one thousand"
    elif num < 2000:
        return "one thousand " + numToWord(num % 1000)
    elif num < 1000000:
        return numToWord(num // 1000) + " thousand " + numToWord(num % 1000)
    elif num == 1000000:
        return "one million"
    elif num < 2000000:
        return "one million " + numToWord(num % 1000000)
    elif num < 1000000000:
        return numToWord(num // 1000000) + " million " + numToWord(num % 1000000)
    elif num == 1000000000:
        return "one billion"


print(numToWord(14450))
