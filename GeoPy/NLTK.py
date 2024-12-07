import nltk
from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize
from string import punctuation
from colorama import Fore

# Example sentence
count = 0
example_sent = "This is a sample sentence, showing off the stop words filtration."

# Load English stopwords
stop_words = set(stopwords.words('english'))
for word in stop_words:
    count +=1
    print(word, end=", ")
print(f"\nTotal Stop Words Found {count}")


# Tokenize and filter in one step
filtered_sentence = [
    word for word in wordpunct_tokenize(example_sent)
    if word.lower() not in stop_words and word not in punctuation
]

print(filtered_sentence)


