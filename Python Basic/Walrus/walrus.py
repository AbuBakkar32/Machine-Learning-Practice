large_squere = [
    x ** 2
    for x in range(15)
    if x ** 2 > 20
]
print('A', large_squere)

large_squere1 = [
    squere
    for x in range(15)
    if (squere := x ** 2) > 20
]
print('B', large_squere1)

if 15 ** 2 > 20:
    x = 15 ** 2
    print('C', x)

if (squere := 15 ** 2) > 20:
    x = squere
    print('D', x)
