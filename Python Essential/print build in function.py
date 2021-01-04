# How to print all Built-In functions in Python?
import re

list = []
for j in dir(__builtins__):
    if not re.match(r'^[A-Z_]', j):
        list.append(j)
    for a, b, c in zip(list[::3], list[1::3], list[2::3]):
        print('{:<20}{:<20}{:<}'.format(a, b, c))
