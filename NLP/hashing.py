# -*- coding: utf-8 -*-
#Hashing
#Import Libraries
from sklearn.feature_extraction.text import HashingVectorizer
import pandas as pd
corpus = [
     'This is the first document from heaven',
     'but the second document is from mars',
     'And this is the third one from nowhere',
     'Is this the first document from nowhere?',
]

df = pd.DataFrame({'text':corpus})

hash_v = HashingVectorizer(n_features=12, norm=None,alternate_sign=False)
hash_v.fit_transform(df.text).toarray()