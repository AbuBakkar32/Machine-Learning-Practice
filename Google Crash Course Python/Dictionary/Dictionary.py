# The email_list function receives a dictionary, which contains domain names as keys, and a list of users as values.
# Fill in the blanks to generate a list that contains complete email addresses (e.g. diana.prince@gmail.com).

''''def email_list(domains):
	emails = []
	for keys, users in domains.items():
	  for user in users:
	    emails.append(user+'@'+keys)
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))
'''

# The groups_per_user function receives a dictionary, which contains group names with the list of users.
# Users can belong to multiple groups. Fill in the blanks to return a dictionary with the users as keys and a list of their groups as values.
from copy import deepcopy

'''def groups_per_user(group_dictionary):
    user_groups = {}
    for group, users in group_dictionary.items():
        for user in users:
            if user not in user_groups:
                user_groups[user] = []
            user_groups[user].append(group)
    return user_groups


print(groups_per_user({"local": ["admin", "userA"],
                       "public": ["admin", "userB"],
                       "administrator": ["admin"]}))'''

# The add_prices function returns the total price of all of the groceries in the dictionary. Fill in the blanks to complete this function.

"""
def add_prices(basket):
	# Initialize the variable that will be used for the calculation
	total = 0
	# Iterate through the dictionary items
	for value in basket.values():
		# Add each price to the total calculation
		# Hint: how do you access the values of
		# dictionary items?
		total += value
	# Limit the return value to 2 decimal places
	return round(total, 2)  

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, 
	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44

"""

# The format_address function separates out parts of the address string into new strings: house_number and street_name, and returns: "house number X on street named Y".
# The format of the input string is: numeric house number, followed by the street name which may contain numbers, but never by themselves, and could be several words long.
# For example, "123 Main Street", "1001 1st Ave", or "55 North Center Drive". Fill in the gaps to complete this function.

"""
def format_address(address_string):
    house_number = ''
    street_name = ''
    parts = address_string.split()
    for part in parts:
        if part.isdigit():
            house_number = part
        else:
            street_name += part
            street_name += ' '
    return "house number {} on street named {}".format(house_number, street_name)

print(format_address("123 Main Street"))
print(format_address("1001 1st Ave"))
print(format_address("55 North Center Drive"))
"""

# The highlight_word function changes the given word in a sentence to its upper-case version.
# For example, highlight_word("Have a nice day", "nice") returns "Have a NICE day". Can you write this function in just one line?

'''
def highlight_word(sentence, word):
    return (sentence.replace(word, word.upper()))


print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))
'''

# Use a dictionary to count the frequency of letters in the input string. Only letters should be counted, not blank spaces, numbers, or punctuation. Upper case should be considered the same as lower case.
# For example, count_letters("This is a sentence.") should return {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}.

'''
def count_letters(text):
    result = {}
    for letter in text:
        if letter.isidentifier():
            letter = letter.lower()
            if letter in result:
                result[letter] += 1
            else:
                result[letter] = 1
                
    return result


print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}
'''

# Taylor and Rory are hosting a party. They sent out invitations, and each one collected responses into dictionaries, with names of their friends and how many guests each friend is bringing.
# Each dictionary is a partial list, but Rory's list has more current information about the number of guests.
# Fill in the blanks to combine both dictionaries into one, with each friend listed only once, and the number of guests from Rory's dictionary taking precedence, if a name is included in both dictionaries.
# Then print the resulting dictionary.
'''
def combine_guests(guests1, guests2):
    # guests = guests1.copy()
    # guests.update(guests2)
    # return guests
    
    combined_dic = guests1
    for key2 in guests2:
        if key2 in guests1:
            pass
        else:
            combined_dic[key2] = guests2[key2]
  
  return combined_dic
    
    
    # backup = guests1.copy()
    # guests1.update(guests2)
    # for guest in guests1:
    #     if guest in backup:
    #         guests1[guest] = backup[guest]
    # return guests1


Rorys_guests = {"Adam": 2, "Brenda": 3, "David": 1, "Jose": 3, "Charlotte": 2, "Terry": 1, "Robert": 4}
Taylors_guests = {"David": 4, "Nancy": 1, "Robert": 2, "Adam": 1, "Samantha": 3, "Chris": 5}

print(combine_guests(Rorys_guests, Taylors_guests))
'''

# Use a list comprehension to create a list of squared numbers (n*n).
# The function receives the variables start and end, and returns a list of squares of consecutive numbers between start and end inclusively.
# For example, squares(2, 3) should return [4, 9].
'''
def squares(start, end):
    # list = []
    # for i in range(start, end+1):
    #     b = i * i
    #     list.append(b)
    # return list

    # Or using list comprehension
    return [a * a for a in range(start, end + 1)]


print(squares(2, 3))  # Should be [4, 9]
print(squares(1, 5))  # Should be [1, 4, 9, 16, 25]
print(squares(0, 10))  # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''


# A professor with two assistants, Jamie and Drew, wants an attendance list of the students, in the order that they arrived in the classroom.
# Drew was the first one to note which students arrived, and then Jamie took over.
# After the class, they each entered their lists into the computer and emailed them to the professor, who needs to combine them into one, in the order of each student's arrival.
# Jamie emailed a follow-up, saying that her list is in reverse order. Complete the steps to combine them into one list as follows: the contents of Drew's list, followed by Jamie's list in reverse order, to get an accurate list of the students as they arrived.

def combine_lists(list1, list2):
    new_list = list2
    for i in reversed(range(len(list1))):
        new_list.append(list1[i])
    return new_list


Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]
print(combine_lists(Jamies_list, Drews_list))
