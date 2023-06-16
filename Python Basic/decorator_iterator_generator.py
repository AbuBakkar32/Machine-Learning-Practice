"""
Iterators: In Python, an iterator is an object that implements the __iter__ method and the __next__ method,
allowing it to be used in a for loop or with the next function. The __iter__ method returns the iterator object
itself, and the __next__ method returns the next value in the iteration. When there are no more values to return,
the __next__ method raises a StopIteration exception.
"""

"""
Generators: A generator is a special type of iterator that uses 
the yield statement to return values one at a time, rather than returning all values at once. Generators are created 
using a generator function, which is a function that contains at least one yield statement. When the generator 
function is called, it returns a generator object that can be used in a for loop or with the next function. 
"""

"""
Decorators: In Python, a decorator is a special type of function that is used to modify the behavior of another 
function. A decorator is applied to a function using the @ symbol followed by the name of the decorator function. 
Decorators can be used to add or modify the behavior of a function, such as adding logging, timing, 
or authentication.
"""


# --------------------------------------------------- 1. Iterators ---------------------------------------------------
class example_range:
    def __init__(self, n):
        self.i = 4
        self.n = n


def __iter__(self):
    return self


def __next__(self):
    if self.i < self.n:
        i = self.i
        self.i += 1
        return i
    else:
        raise StopIteration()


n = example_range(10)
list(n)
for i in n:
    print(i, end=',')


# --------------------------------------------------- 2. Generators ---------------------------------------------------
def test_sequence():
    num = 0
    while num < 10:
        yield num
        num += 1


for i in test_sequence():
    print(i, end=",")


# Reverse a string
def reverse_str(test_str):
    length = len(test_str)
    for i in range(length - 1, -1, -1):
        yield test_str[i]


for char in reverse_str("Trojan"):
    print(char, end=" ")


# --------------------------------------------------- 3. Decorators ---------------------------------------------------
# def test_decorators(func):
#     def function_wrapper(x):
#         print("Before calling " + func.__name__)
#         res = func(x)
#         print(res)
#         print("After calling " + func.__name__)
#
#     return function_wrapper
#
#
# @test_decorators
# def sqr(n):
#     return n ** 2
#
#
# sqr(54)
#
#
# # multiple decorators
# def lowercase_decorator(function):
#     def wrapper():
#         func = function()
#         make_lowercase = func.lower()
#         return make_lowercase
#
#     return wrapper
#
#
# def split_string(function):
#     def wrapper():
#         func = function()
#         split_string = func.split()
#         return split_string
#
#     return wrapper
#
#
# @split_string
# @lowercase_decorator
# def test_func():
#     return 'MOTHER OF DRAGONS'
#
#
# test_func()
