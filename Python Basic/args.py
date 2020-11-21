def addition(a, b, *args, option=True):
    result = 0
    if option:
        for i in args:
            result += i
        return a + b + result
    else:
        return result


# print(addition(9, 10, 5, 6, 10, 10, 100))

# Kwargs Example

def arg_printer(a, b, option=True, **kwargs):
    print(a, b)
    print(option)
    print(kwargs)


# print(arg_printer(3, 4, param1=5, param2=6))

def arg_printer(a, b, *args, option=True, **kwargs):
    print(a, b)
    print(args)
    print(option)
    print(kwargs)


# lst = [1, 4, 5]
# print(arg_printer(lst))
# print(arg_printer(*lst))

# lst = [1, 4, 5]
# tpl = ('a', 'b', 4)
# arg_printer(*lst, *tpl, 5, 6)

dct = {'param1':5, 'param2':8}
arg_printer(5, 6, **dct)
# print(arg_printer(1, 4, 6, 5, param1=5, param2=6))


