def my_decorator(func):
    def wrapper(*args, **kwargs):
        # Add your additional functionality here
        print("Before function execution")
        result = func(*args, **kwargs)
        print("After function execution")
        return result

    return wrapper


@my_decorator
def my_function():
    print("Inside my_function")


# @my_decorator
# def function1():
#     print("Inside function1")
#
#
# @my_decorator
# def function2():
#     print("Inside function2")
