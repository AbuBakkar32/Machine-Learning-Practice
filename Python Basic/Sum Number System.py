sum = 0
for i in range(6):
    if i > 0:
        print('(', end='')
    for j in range(i):
        print('{}'.format(j + 1), end='')
        if (j + 1) < i:
            print('+', end='')
        if (j+1) == i:
            print(')+', end='')

    sum += i
if i == 5:
    print(".....+(", end='')
    for k in range(5):
        print("{}+".format(k + 1), end='')
        if k == 4:
            print(".....+n)", end='')

print('\n The Sum Is: ', sum)
