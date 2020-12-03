import string
import random

chars = string.ascii_uppercase + string.ascii_lowercase + string.digits


# li = []
# for i in range(15):
#     password = random.choice(chars)
#     li.append(password)
# print(''.join(li))

def randPass():
    chars = string.ascii_uppercase + string.digits + string.ascii_lowercase
    size = 5
    return ''.join(random.choice(chars) for _ in range(size, 20))


print(randPass())
