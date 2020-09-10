import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from string import punctuation

example_sent = "This is a sample sentence, showing off the stop words filtration."

stop_words = set(stopwords.words('english'))
print(stop_words)
word_tokens = word_tokenize(example_sent)
print(word_tokens)

# filtered_sentence = [w for w in word_tokens if not w in stop_words]

filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

print(filtered_sentence)

filter = []
for a in filtered_sentence:
    if a not in punctuation:
        filter.append(a)
print(filter)

