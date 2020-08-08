"""transpose 2d array [[a,b], [c,d], [e,f]] -> [[a,c,e], [b,d,f]]"""

original = [['a', 'b'], ['c', 'd'], ['e', 'f']]
transposed = zip(*original)
print(list(transposed))
