# Forced Keyword Arguments
def f(*, a, b):
    print(a, b)


print(f(a=1, b=2))


# Using * and ** for Function Argument Unpacking
def f(a, b):
    print(a, b)


args = {'a': 1, 'b': 2}
print(*args)


def f(a, b, c):
    print(a, b, c)


l = [1, 2, 3]
print(*l)


# Decorating Your Functions
def print_argument(func):
    def wrapper(the_number):
        print("Argument for", func.__name__, "is", the_number)
        return func(the_number)

    return wrapper


@print_argument
def add_one(x):
    return x + 1


print(add_one(1))

# Anonymous Functions
add_one = lambda x: x + 1
add_one(3)
