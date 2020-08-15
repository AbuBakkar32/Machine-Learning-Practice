import time
sum = 0

for i in range(6):
    if i > 0:
        time.sleep(1.0)
        print('(', end='')
    for j in range(i):
        time.sleep(1.0)
        print('{}'.format(j + 1), end='')
        if (j + 1) < i:
            time.sleep(1.0)
            print('+', end='')
        if (j + 1) == i:
            time.sleep(1.0)
            print(')+', end='')

    sum += i

if i == 5:
    time.sleep(1.0)
    print(".....+(", end='')
    for k in range(5):
        time.sleep(1.0)
        print("{}+".format(k + 1), end='')
        if k == 4:
            time.sleep(1.0)
            print(".....+n)", end='')

print('\n The Sum Is: ', sum)
