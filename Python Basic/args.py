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


print(arg_printer(3, 4, param1=5, param2=6))

