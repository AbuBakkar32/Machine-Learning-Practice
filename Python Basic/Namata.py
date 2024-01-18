# import time
# 
# num = input("How many Namata you want?\n")
# num = (int(num) + 1)
# for i in range(int(num)):
#     if i == 0:
#         print('*************************')
#         continue
#     for j in range(11):
#         if j == 0:
#             continue
#         result = i * j
#         time.sleep(1)
#         print(f"{i}x{j}={result}")
#     print('*************************')


# Program to display the Fibonacci sequence up to n-th term

# nterms = int(input("How many terms? "))
# 
# # first two terms
# n1, n2 = 0, 1
# count = 0
# 
# # check if the number of terms is valid
# if nterms <= 0:
#     print("Please enter a positive integer")
# # if there is only one term, return n1
# elif nterms == 1:
#     print("Fibonacci sequence upto", nterms, ":")
#     print(n1)
# # generate fibonacci sequence
# else:
#     print("Fibonacci sequence:")
#     while count < nterms:
#         print(n1)
#         nth = n1 + n2
#         # update values
#         n1 = n2
#         n2 = nth
#         count += 1


nth = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0
print("Fibonacci sequence:")
while count < nth:
    print(n1)
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    count += 1
