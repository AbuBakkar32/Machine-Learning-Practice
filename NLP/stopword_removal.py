# -*- coding: utf-8 -*-
#Import libraries
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from string import punctuation

text = "I believe this would help the reader understand how tokenization \
        works. as well as realize its importance (text) ."
        
print(punctuation)

custom_list = set(stopwords.words('english')+list(punctuation))

word_list = [word for word in word_tokenize(text) if word not in custom_list]
print(word_list)