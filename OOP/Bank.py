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


# t = int(input())
#
# for _ in range(t):
#     pos = input()
#
#     for j in range(8):
#         if pos[0] != chr(ord('a') + j):
#             print(chr(ord('a') + j) + pos[1])
#         if pos[1] != chr(ord('1') + j):
#             print(pos[0] + chr(ord('1') + j))

# G - Black Ops?
# import sys
#
# def find_max_value(n, m, v, queries):
#     max_value = 0.0
#     for a, b, e in queries:
#         if e == 0.0:
#             continue
#         max_value = max(max_value, (v[a - 1] + v[b - 1]) / e)
#     return max_value
#
# for line in sys.stdin:
#     try:
#         n, m = map(int, line.strip().split())
#         v = list(map(float, sys.stdin.readline().strip().split()))
#         queries = []
#         for _ in range(m):
#             a, b, e = map(float, sys.stdin.readline().strip().split())
#             queries.append((int(a), int(b), e))
#         max_value = find_max_value(n, m, v, queries)
#         print("%.10f" % max_value)
#     except (ValueError, IndexError):
#         print("Invalid input format")
#         continue
#     except EOFError:
#         break
#
# sys.exit(0)

# H - The Guilty One
# def count_cows(stalls, distance):
#     count = 1
#     last_position = stalls[0]
#     for stall in stalls:
#         if stall - last_position >= distance:
#             count += 1
#             last_position = stall
#     return count
#
#
# def largest_minimum_distance(stalls, cows):
#     stalls.sort()
#     left, right = 0, stalls[-1] - stalls[0]
#
#     while left <= right:
#         mid = (left + right) // 2
#         if count_cows(stalls, mid) >= cows:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return right
#
#
# t = int(input())
# for _ in range(t):
#     n, c = map(int, input().split())
#     stall_locations = [int(input()) for _ in range(n)]
#     result = largest_minimum_distance(stall_locations, c)
#     print(result)


# E - Treat Treat Treat
# def serve_ice_cream(n, x, queue):
#     ice_cream_left = x
#     distressed_kids = 0
#
#     for operation, d in queue:
#         if operation == '+':
#             ice_cream_left += d
#         else:
#             if ice_cream_left >= d:
#                 ice_cream_left -= d
#             else:
#                 distressed_kids += 1
#
#     return ice_cream_left, distressed_kids
#
#
# # Read input
# n, x = map(int, input().split())
# queue = [input().split() for _ in range(n)]
#
# # Convert ice cream packs to integers
# for i in range(n):
#     queue[i][1] = int(queue[i][1])
#
# ice_cream_left, distressed_kids = serve_ice_cream(n, x, queue)
# print(ice_cream_left, distressed_kids)

# D - Determination
# def is_teacher_suspicious(n, tasks):
#     task_set = set()
#     for i in range(n - 1):
#         if tasks[i] == tasks[i + 1]:
#             return "NO"
#         task_set.add(tasks[i])
#     return "YES" if tasks[-1] not in task_set else "NO"
#
#
# t = int(input())
#
# for _ in range(t):
#     n = int(input())
#     tasks = input().strip()
#     print(is_teacher_suspicious(n, tasks))


# C - Break An Arm
import math


def find_ad(ab, ac, bc, area_ratio):
    """
    Finds the length of AD given the side lengths of triangle ABC,
    DE parallel to BC, and the area ratio between triangles ADE and BDEC.
    """

    # Calculate the altitude of triangle ABC from A to BC
    s = (ab + ac + bc) / 2  # Semi-perimeter
    area_abc = math.sqrt(s * (s - ab) * (s - ac) * (s - bc))  # Heron's formula
    altitude = 2 * area_abc / bc

    # Calculate the height of triangle ADE from A to DE
    height_ade = altitude * area_ratio / (1 + area_ratio)

    # Calculate AD using the formula for right triangles (ADE)
    return math.sqrt(ac ** 2 - height_ade ** 2)


# Read the number of test cases
t = int(input())

for case_num in range(1, t + 1):
    # Read the side lengths and area ratio
    ab, ac, bc, area_ratio = map(float, input().split())

    # Calculate AD
    ad = find_ad(ab, ac, bc, area_ratio)

    # Print the result
    print(f"Case {case_num}: {ad:.6f}")  # Output with 6 decimal places
