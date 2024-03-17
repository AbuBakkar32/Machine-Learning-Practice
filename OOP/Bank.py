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


def is_prime(num):
    """
    This function checks if a number is prime.

    Args:
        num: The number to check.

    Returns:
        True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


# Example usage
number = 11
if is_prime(number):
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")
