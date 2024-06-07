# Constants
VOWELS = 'aeiou'
TEXT = (
    'Hello every one my name is abu bakkar siddik. i am from bangladesh. '
    'I am studying as a software engineer under daffodil international university. '
    'My dream is so long and may Allah fulfill my dreams'
).casefold()

# Initialize counts
counts = {char: 0 for char in VOWELS}
consonants = {}

# Count vowels and consonants
for char in TEXT:
    if char in VOWELS:
        counts[char] += 1
    elif char.isalpha():  # Count only alphabetic characters as consonants
        consonants[char] = consonants.get(char, 0) + 1

# Output the results
print(f'The Vowels are: {counts}')
print(f'The consonants are: {consonants}')
