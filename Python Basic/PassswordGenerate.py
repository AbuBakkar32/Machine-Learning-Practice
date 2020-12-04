import string
import random

chars = string.ascii_uppercase + string.ascii_lowercase + string.digits


def randPass():
    chars = string.ascii_uppercase + string.digits + string.ascii_lowercase
    size = 5
    return ''.join(random.choice(chars) for _ in range(size, 20))


print(randPass())
