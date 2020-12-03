# -*- coding: utf-8 -*-
#N-grams
from nltk.collocations import BigramCollocationFinder

word_list = ['I', 'believe', 'would', 'help', 'reader', 'understand', \
             'tokenization', 'works', 'well', 'realize', 'importance', 'text']

finde = BigramCollocationFinder.from_words(word_list)
print(finde.ngram_fd.items())
