import random
from termcolor import colored


def guess(x):
    randmon_number = random.randint(1, x)
    guess = 0
    count = 0
    set_count = 3

    while guess != randmon_number:
        if count == set_count:
            print(colored("\nSorry!!! You have Attampt so Many Times", "red"))
            break

        elif count != set_count:
            count += 1
            guess = int(input(f"Please guess a number between 1 to {x}: "))

            if guess < randmon_number:
                print("Sorry!! guess again. its too Low")
            elif guess > randmon_number:
                print("Sorry!! guess again. its too High")
            elif guess == randmon_number:
                print(colored(f"Yahoooo!! Congrates!!! You have correctly guess {randmon_number} number", "green"))


guess(10)
