from nltk.tokenize import word_tokenize
from collections import Counter
from nltk.corpus import stopwords
from gensim.corpora.dictionary import Dictionary
import nltk
#
# counter = Counter(word_tokenize("""The cat is in the box. The cat likes the box.
#                         The box is over the cat."""))
#
# print(counter)


# text = """The cat is in the box. The cat likes the box.                   The box is over the cat."""
# tokens = [w for w in word_tokenize(text.lower()) if w.isalpha()]
# no_stops = [t for t in tokens if t not in stopwords.words('english')]
# print(Counter(no_stops).most_common(2))

# my_documents = ['The movie was about a spaceship and aliens.','I really liked the movie!','Awesome action scenes, but boring characters.','The movie was awful! I hate alien films.','Space is cool! I liked the movie.','More space films, please!',]
# tokenized_docs = [word_tokenize(doc.lower()) for doc in my_documents]
# dictionary = Dictionary(tokenized_docs)
# corpus = [dictionary.doc2bow(doc) for doc in tokenized_docs]
# print(corpus)
# #print(dictionary.token2id)


sentence = '''In New York, I like to ride the Metro to               visit MOMA and some restaurants rated               well by Ruth Reichl.'''
tokenized_sent = nltk.word_tokenize(sentence)
tagged_sent = nltk.pos_tag(tokenized_sent)
print(tagged_sent[:3])