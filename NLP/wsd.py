# -*- coding: utf-8 -*-
#Word Sense Disambiguation
#Import Libraries
#nltk.download('wordnet')
from nltk.corpus import wordnet
for ss in wordnet.synsets('mouse'):
    print(ss, ss.definition())


from nltk.wsd import lesk
from nltk.tokenize import word_tokenize

context_1 = lesk(word_tokenize("Sing in a lower tone, along with the bass"), "bass")
print(context_1, context_1.definition())

context_2 = lesk(word_tokenize("The sea bass really very hard to catch"), "bass")
print(context_2, context_2.definition())

context_3 = lesk(word_tokenize("My mouse is not working, need to change it"), "mouse")
print(context_3, context_3.definition())

















#"Sing in a lower tone, along with the bass"
#"The sea bass really very hard to catch"
#"My mouse is not working, need to change it"


