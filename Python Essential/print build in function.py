"""
Author: Abu Bakkar Siddikk
Date: 2024-06-03
Description: Build in function and Namata 1 to 10
"""

# How to print all Built-In functions in Python?
import re
import time

list = []
count = 0
for j in dir(__builtins__):
    if not re.match(r'^[A-Z_]', j):
        list.append(j)
        count += 1

for a, b, c in zip(list[::3], list[1::3], list[2::3]):
    print('{:<20}{:<20}{:<}'.format(a, b, c))

name = "Abubakkar"
print(name[1::3])
print(name[2::3])
print(name[::3])
print(name[2::-1])


# 1 to 10 Namata

def print_namata_table(number: int):
    """
    Prints the multiplication table of the given number.
    """
    print(f'\n{"* " * 10}Namata of {number}{" *" * 10}')
    for j in range(1, 11):
        print(f'\t{number} x {j} = {number * j}')
    print(end='\t')


def print_all_namata_tables():
    """
    Prints the multiplication tables from 1 to 10.
    """
    for i in range(1, 11):
        print_namata_table(i)


if __name__ == "__main__":
    print_all_namata_tables()

print("hello world")
