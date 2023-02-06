def number_to_words(n):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
            "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if n < 20:
        return ones[n]
    if n < 100:
        return tens[n // 10] + (ones[n % 10] if (n % 10 != 0) else "")
    if n < 1000:
        return ones[n // 100] + "hundred" + (("and" + number_to_words(n % 100)) if (n % 100 != 0) else "")
    if n < 1000000:
        return number_to_words(n // 1000) + "thousand" + (number_to_words(n % 1000) if (n % 1000 != 0) else "")
    if n < 1000000000:
        return number_to_words(n // 1000000) + "million" + (number_to_words(n % 1000000) if (n % 1000000 != 0) else "")
    return number_to_words(n // 1000000000) + "billion" + (
        number_to_words(n % 1000000000) if (n % 1000000000 != 0) else "")
