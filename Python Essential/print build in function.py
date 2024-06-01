# How to print all Built-In functions in Python?
import re
import time

# list = []
# for j in dir(__builtins__):
#     if not re.match(r'^[A-Z_]', j):
#         list.append(j)
#     for a, b, c in zip(list[::3], list[1::3], list[2::3]):
#         print('{:<20}{:<20}{:<}'.format(a, b, c))


# name = "Abubakkar"
# print(name[1::3])
# print(name[2::3])
# print(name[::3])
# print(name[2::-1])

# 1 to 10 Namata

for i in range(1, 11):
    print(f'\n{"* " * 10}Namata of {i}{" *" * 10}')
    for j in range(1, 11):
        print(end='\t')
        print(f'{i} x {j} = {i * j}')
    print(end='\t')
