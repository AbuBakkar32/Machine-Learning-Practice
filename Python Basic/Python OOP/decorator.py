# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         # Add your additional functionality here
#         print("Before function execution")
#         result = func(*args, **kwargs)
#         print("After function execution")
#         return result
#
#     return wrapper
#
#
# @my_decorator
# def my_function():
#     print("Inside my_function")


from datetime import datetime


def log_datetime(func):
    """Log the date and time of a function"""

    def wrapper():
        func()
        print(f'Function: {func.__name__}\nRun on: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
        print(f'{"-" * 30}')

    return wrapper


@log_datetime
def daily_backup():
    for i in range(10):
        print(i, end=' ')
    print("\n")
    print('Daily backup job has finished.')
    print("\n")


def main():
    daily_backup()


if __name__ == '__main__':
    main()
