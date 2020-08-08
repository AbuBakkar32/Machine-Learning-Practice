
class Foo(object):
    def __init__(self, value):
        self.bar = value

    def __eq__(self, other):
        return self.bar == getattr(other, 'bar')
    
    def __hash__(self):
        return int(self.bar)
    
    def __repr__(self):
        return '{}'.format(self.bar)

item1 = Foo(15)
item2 = Foo(15)
item3 = Foo(5)

lst = [item1, item2, item3]


print(set(lst))

# original
unique_lst = list({getattr(obj, 'bar'): obj for obj in lst}.values())
print(unique_lst)  # [item2, item3]
