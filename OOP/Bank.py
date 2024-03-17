# class BankAccount:
#     bank_name = 'ABC bank, XYZ Street, New Delhi'
#
#     def __init__(self, name, balance=0, bank=bank_name):
#         self.name = name
#         self.balance = balance
#         self.bank = bank
#
#     def display(self):
#         print(self.name, self.balance, self.bank)
#
#     def withdraw(self, amount):
#         self.balance -= amount
#
#     def deposit(self, amount):
#         self.balance += amount
#
#
# a1 = BankAccount('Mike', 200, 'PQR Bank Delhi')
# a2 = BankAccount('Tom')
#
# a1.display()
# a2.display()


def IsPrimeNumber(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return print(f'{num} is not a prime number')
    return print(f'{num} is a prime number')


IsPrimeNumber(2)
