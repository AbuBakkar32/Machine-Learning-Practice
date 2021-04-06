text = input("Enter a String: ")
lenght = len(text)
print(*text, sep='|')
print('=' * (lenght * 2 - 1))
print(*range(lenght))


