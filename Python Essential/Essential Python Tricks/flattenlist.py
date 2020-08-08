# Flatten list of lists

a = [[1, 2], [3, 4]]

# Solutions:

print([x for _list in a for x in _list])

import itertools
print(list(itertools.chain(*a)))

print(list(itertools.chain.from_iterable(a)))

print(sum(a, []))

