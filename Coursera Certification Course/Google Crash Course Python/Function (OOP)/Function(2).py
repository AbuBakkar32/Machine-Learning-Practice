# Fill in the blanks to make the factorial function return the factorial of n.
# Then, print the first 10 factorials (from 0 to 9) with the corresponding number.
# Remember that the factorial of a number is defined as the product of an integer and all integers before it.
# For example, the factorial of five (5!) is equal to 1*2*3*4*5=120. Also recall that the factorial of zero (0!) is equal to 1.

'''def factorial(n):
    result = 1
    for x in range(1, n):
        result = x * result
    return result

for n in range(0, 10):
    print(n, factorial(n + 1))'''

# Write a script that prints the multiples of 7 between 0 and 100.
# Print one multiple per line and avoid printing any numbers that aren't multiples of 7.
# Remember that 0 is also a multiple of 7.
'''for i in range(0, 100):
    if i % 7 == 0:
        print(i)'''

# Complete the function digits(n) that returns how many digits the number has. For example: 25 has 2 digits and 144 has 3 digits.
# Tip: you can figure out the digits of a number by dividing it by 10 once per digit until there are no digits left.
'''
def digits(n):
	count = 0
	if n == 0:
	  	count += 1
	while (n>0):
		count += 1
		n = n // 10
	return count
	
print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1
'''

# The even_numbers function returns a space-separated string of all positive numbers that are divisible by 2, up to and including the maximum that's passed into the function.
# For example, even_numbers(6) returns “2 4 6”. Fill in the blank to make this work.
'''
def even_numbers(maximum):
	return_string = ""
	for x in range(2,maximum+1):
		if x%2==0:
			return_string += str(x) + " "
	return return_string.strip()

print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10)) # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed
'''

# The counter function counts down from start to stop when start is bigger than stop, and counts up from start to stop otherwise.
# Fill in the blanks to make this work correctly.

'''def counter(start, stop):
    x = start
    if x >= stop:
        return_string = "Counting down: "
        while x >= stop:
            return_string += str(x)
            if x > stop:
                return_string += ","
            x -= 1
    else:
        return_string = "Counting up: "
        while x <= stop:
            return_string += str(x)
            if x < stop:
                return_string += ","
            x += 1
    return return_string


print(counter(1, 10))  # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1))  # Should be "Counting down: 2,1"
print(counter(5, 5))  # Should be "Counting up: 5"
'''

'''def count_users(group):
    count = 0
    for member in get_members(group):
        if is_group(member):
            count += count_users(member)
        else:
            count+=1
    return count

print(count_users("sales")) # Should be 3
print(count_users("engineering")) # Should be 8
print(count_users("everyone")) # Should be 18'''

'''def sum_positive_numbers(n):
  if n < 1:
    return 0
  else:
    return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15'''

# The replace_ending function replaces the old string in a sentence with the new string, but only if the sentence ends with the old string.
# If there is more than one occurrence of the old string in the sentence, only the one at the end is replaced, not all of them.
# For example, replace_ending("abcabc", "abc", "xyz") should return abcxyz, not xyzxyz or xyzabc.
# The string comparison is case-sensitive, so replace_ending("abcabc", "ABC", "xyz") should return abcabc (no changes made).

'''def replace_ending(sentence, old, new):
    if sentence.endswith(old):
        i = sentence.rfind(old)
        new_sentence = sentence[:i] + new
        return new_sentence

    return sentence


print(replace_ending("It's raining cats and cats", "cats", "dogs"))
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts"))
print(replace_ending("The weather is nice in May", "may", "april"))
print(replace_ending("The weather is nice in May", "May", "April"))'''

# The is_palindrome function checks if a string is a palindrome.
# A palindrome is a string that can be equally read from left to right or right to left, omitting blank spaces, and ignoring capitalization.
# Examples of palindromes are words like kayak and radar, and phrases like "Never Odd or Even".
# Fill in the blanks in this function to return True if the passed string is a palindrome, False if not.
'''def is_palindrome(input_string):
    new_string = ""
    reverse_string = ""
    for letter in input_string:
        if letter != ' ':
            new_string += letter
            reverse_string = letter + reverse_string
    if new_string.lower() == reverse_string.lower():
        return True
    return False


print(is_palindrome("Never Odd or Even"))
print(is_palindrome("abc"))
print(is_palindrome("kayak"))'''

text = [('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")]

for a, b, c in text:
    print("{} is {} years old and works as {}".format(a, b, c))
