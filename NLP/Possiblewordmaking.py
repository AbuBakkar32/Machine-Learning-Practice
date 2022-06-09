import itertools
# from PyDictionary import PyDictionary
from pydictionary import Dictionary

# inp_word = "eaplp"
# syn_words = []
# dict = Dictionary(inp_word)
#
# print(dict.print_antonyms())

s = 'alepp'
data = []
t = list(itertools.permutations(s, len(s)))
for i in range(0, len(t)):
    data.append(''.join(t[i]).strip())

s = set(data)
for i in s:
    print(i)