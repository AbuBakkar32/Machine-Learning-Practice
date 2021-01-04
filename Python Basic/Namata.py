import time

num = input("How many Namata you want?\n")
num = (int(num) + 1)
for i in range(int(num)):
    if i == 0:
        print('*************************')
        continue
    for j in range(11):
        if j == 0:
            continue
        result = i * j
        time.sleep(1)
        print(f"{i}x{j}={result}")
    print('*************************')



