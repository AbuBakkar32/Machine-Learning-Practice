import string
import re
from collections import Counter

# Define the sentence
sentence = ("my name is Rakib. "
            "are your know me? hey Rakib your are so smart and sexy!. "
            "i love you Rakib."
            ).casefold()

# Remove punctuation and numbers
cleaned_sentence = re.sub(r'[^\w\s]', '', sentence)
cleaned_sentence = re.sub(r'\d+', '', cleaned_sentence)

# Split the sentence into words
words = cleaned_sentence.split()

# Count the occurrences of each word
word_count = Counter(words)

# Print the word count
for word, count in word_count.items():
    print(f"{word}: {count}")
