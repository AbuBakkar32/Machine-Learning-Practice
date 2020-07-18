# total = 0
# count = 0
# list = []
# while True:
#     value = input("Enter a Number: ")
#     if value == 'done':
#         break
#     values = float(value)
#     list.append(values)
# average = sum(list) / len(list)


# line = 'From stephan.marquard@uct.ac.a Sat Jan  5 09:14:16 2008'
# word = line.split()
# email = word[1]
# a = email.split('@')
# print(a)
# print(a[1])


bigc = None
bigw = None
counts = dict()
line = input('Enter a New line of text:')
words = line.split()

for name in words:
    counts[name] = counts.get(name, 0) + 1
print('Words:', counts)

for key, values in counts.items():
    if bigc is None or values > bigc:
        bigc = values
        bigw = key
print(bigw, '=', bigc)


