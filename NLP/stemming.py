# -*- coding: utf-8 -*-
#Stemming
#Import Libraries
from nltk.tokenize import word_tokenize
from nltk.stem.lancaster import LancasterStemmer

l_s = LancasterStemmer()
new_text = "It is important to by very pythonly while you are pythoning\
             with python. All pythoners have pythoned poorly at least once."
             
stem_lan =  [l_s.stem(word) for word in word_tokenize(new_text)] 
print(stem_lan)       