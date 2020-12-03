# -*- coding: utf-8 -*-
#TD-IDF
#Import Libraries
from sklearn.feature_extraction.text import TfidfVectorizer

corpus = [
     'This is the first document from heaven',
     'but the second document is from mars',
     'And this is the third one from nowhere',
     'Is this the first document from nowhere?',
]

vector = TfidfVectorizer()
vector.fit(corpus)
print(vector.vocabulary_)
print(vector.idf_)