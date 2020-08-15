from string import punctuation
import time
from datetime import datetime

vowels = 'aeiou'
text = 'Hello every one my name is abu bakkar siddik. i am from bangladesh. i am studing as a software engineer under daffodil international university. my dreame so long and may Allah full fill my dreams'
text = text.casefold()
count = {}.fromkeys(vowels, 0)
cons = {}

for char in text:
    if char in count:
        count[char] += 1
    else:
        cons[char] = cons.get(char, 0)+1
print(count)
print(cons)

# simple code for remove punctuation character
data = {}
for i, j in cons.items():
    if i in punctuation:
        continue
    if i == ' ':
        continue
    else:
        data[i] = j

print('\n<<<<<<<<<<This the clear item count after processing data>>>>>>>>>>')
print(data)


