# Swaping values
a, b = 5, 10
print(a, b)
a, b = b, a
print(a, b)

# One string of all items within a list
p = ["Python", "is", "a", "popular", "language"]
print(" ".join(p))

# Most common element in the list
list1 = [0, 1, 2, 3, 3, 2, 3, 1, 4, 5, 4]
print(max(set(list1), key=list1.count))

# Test if two strings are anagrams
from collections import Counter


def anagram(string_1, string_2):
    return Counter(string_1) == Counter(string_2)


anagram('pqrs', 'rqsp')
anagram('pqrs', 'rqqs')

# Reverse a string with slicing
str = "PQRST"
reverse_str = str[::-1]
print(reverse_str)


# Reverse a list using slicing approach
def Reverse(lst):
    lst1 = lst[::-1]
    return lst1


lst = [5, 6, 7, 8, 9, 10]
print(Reverse(lst))

# Transpose a matrix
mat = [(5, 6, 7), (8, 9, 10), (11, 12, 13), (14, 15, 16)]
for row in mat:
    print(row)
print("\n")
t_mat = zip(*mat)
for row in t_mat:
    print(row)

# Chained comparison
a = 3
print(1 < a < 10)
print(5 < a < 15)
print(a < 7 < a * 7 < 49)
print(8 > a <= 6)
print(3 == a > 2)

# Dictionary ‘get’
dict = {"P": 1, "Q": 2}
print(dict["P"])
print(dict["R"])

dict = {"P": 1, "Q": 2}
print(dict.get("P"))
print(dict.get("R"))
print(dict.get("R", "Unavailable! "))


# Sort dictionary by value
def dict():
    keyval = {}

    # Initializing the value
    keyval[3] = 48
    keyval[2] = 6
    keyval[5] = 10
    keyval[1] = 22
    keyval[6] = 15
    keyval[4] = 245
    print("Task 3:-\nKeys and Values sorted",
          "in alphabetical order by the value")
    # Remember this would arrange in aphabetical sequence
    # Convert it to float to mathematical purposes
    print(sorted(keyval.elements(), key=
    lambda k_val: (k_val[1], k_val[0])))


def main():
    dict()


if __name__ == "__main__":
    main()

# List comprehension
list1 = [2, 4, 6, 8]
list2 = [3 * p for p in list1]
print(list2)

# Time consumed to implement a part of the program
import time

initial_Time = time.time()
# Program to test follows
x, y = 5, 6
z = x + y
# Program to test ending
ending_Time = time.time()
Time_lapsed_in_Micro_sec = (ending_Time - initial_Time) * (10 ** 6)
print(" Time lapsed in micro_seconds: {0} ms").format(Time_lapsed_in_Micro_sec)

# Merge dictionaries
dic1 = {'men': 6, 'boy': 5}
dic2 = {'boy': 3, 'girl': 5}
merged_dic = {**dic1, **dic2}
print(merged_dic)

# Digitize
number = 2468
# with map
digit_list = list(map(int, str(number)))
print(digit_list)
[2, 4, 6, 8]
# with list comprehension
digit_list = [int(a) for a in str(number)]
print(digit_list)
[2, 4, 6, 8]
# Even simpler approach
digit_list = list(str(number))
print(digit_list)


# Test for uniqueness

def uniq(list):
    if len(list) == len(set(list)):
        print("total items are unique")
    else:
        print("List includes duplicate item")


uniq([0, 2, 4, 6])
# total items are unique
uniq([1, 3, 3, 5])
# List includes duplicate item

# Using enumeration
sample_list = [4, 5, 6]
for j, item in enumerate(sample_list):
    print(j, ': ', item)

# Evaluate the factorial of any number in a single line
import functools

fact = (lambda i: functools.reduce(int.__mul__, range(1, i + 1), 1)(4))
print(fact)


# Return several functions’ elements
def a():
    return 5, 6, 7, 8


# Calling the above function.
w, x, y, z = a()
print(w, x, y, z)


# Incorporate a true Python switch-case statement
def aswitch(a):
    return aswitch._system_dic.get(a, None)


aswitch._system_dic = {'mangoes': 4, 'apples': 6, 'oranges': 8}
print(aswitch('default'))
print(aswitch('oranges'))


# With splat operator unpacking function arguments
def test(a, b, c):
    print(p, q, r)


test_Dic = {'a': 4, 'b': 5, 'c': 6}
test_List = [10, 11, 12]
test(*test_Dic)
test(**test_Dic)
test(*test_List)
