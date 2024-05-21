num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            print(i, "times", num // i, "is", num)
            break
    else:
        print(num, "is a prime number")

else:
    print(f"{num} Is Not a Prime Number")


# make a function for fibinacci series
def fibonacci(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)

    for i in range(2, n):
        c = a + b
        a = b
        b = c
        print(c)


# make a function for factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# make a function for armstrong number
def armstrong(n):
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if n == sum:
        print(f"{n} is an Armstrong number")
    else:
        print(f"{n} is not an Armstrong number")


# make a function for check palindrome
def palindrome(s):
    if s == s[::-1]:
        print(f"{s} is a palindrome")
    else:
        print(f"{s} is not a palindrome")


name = 'Hannah'
print(palindrome(name.lower()))
