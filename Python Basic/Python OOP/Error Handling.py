def main():
    try:
        x = 10/0
    except ZeroDivisionError:
        print("Number not divisor by zero")
    except :
        print('Unknown Error Occure')
    else:
        print(x)


if __name__ == '__main__':
    main()