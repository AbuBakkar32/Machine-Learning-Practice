import random
from string import punctuation


def suffle(string):
    lists = list(string)
    random.shuffle(lists)
    return ' '.join(lists)


upperpas1 = chr(random.randint(65, 90))
upperpas2 = chr(random.randint(65, 90))
upperpas3 = random.randint(65, 90)
upperpas4 = chr(random.randint(65, 90))
upperpas5 = chr(random.randint(65, 90))

password = (upperpas1 + upperpas2 + str(upperpas3) + upperpas4 + upperpas5)
password = suffle(password)
print(password)
