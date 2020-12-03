# -*- coding: utf-8 -*-
#Tokenization
#Import libraries
#import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

text = "I believe this would help the reader understand how tokenization \
        works. as well as realize its importance."
        
sents = (sent_tokenize(text))
print(sents)
print(word_tokenize(text))

words = [word_tokenize(sent) for sent in sents]
print(words)
#perform tokenization
