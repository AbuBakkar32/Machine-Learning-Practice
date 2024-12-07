import nltk
from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize
from string import punctuation
from colorama import Fore

# Example sentence
example_sent = "This is a sample sentence, showing off the stop words filtration."

# Load English stopwords
stop_words = set(stopwords.words('english'))

# Tokenize and filter in one step
filtered_sentence = [
    word.upper() for word in wordpunct_tokenize(example_sent)
    if word.lower() not in stop_words and word not in punctuation
]

print(filtered_sentence)
