# -*- coding: utf-8 -*-

import pandas as pd
corpus = [
     'This is the first document from heaven',
     'but the second document is from mars',
     'And this is the third one from nowhere',
     'Is this the first document from nowhere?',
]

df = pd.DataFrame({'text':corpus})
df

from sklearn.feature_extraction.text import CountVectorizer
count_v = CountVectorizer()
X = count_v.fit_transform(df.text).toarray()
print(X)
print(count_v.vocabulary_)

count_v = CountVectorizer(stop_words=['this','is'])
X = count_v.fit_transform(df.text).toarray()
print(X)
print(count_v.vocabulary_)