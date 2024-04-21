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

# ---------------------------------------------------------------------------------------------------
# A - Chess Move
# def rook_moves(pos):
#     row, col = pos[1], pos[0]
#     moves = []
#
#     for i in range(1, 9):
#         if i != int(row):
#             moves.append(col + str(i))
#         if col != chr(ord('a') + i - 1):
#             moves.append(chr(ord('a') + i - 1) + row)
#
#     return moves
#
#
# t = int(input())
# for _ in range(t):
#     pos = input().strip()
#     moves = rook_moves(pos)
#     for move in moves:
#         print(move)

# ---------------------------------------------------------------------------------------------------
# B - Guess The Array
# def solve():
#     t = int(input())
#     for _ in range(t):
#         n = int(input())
#         a = list(map(int, input().split()))
#         b = [0] * n
#         sum_a = sum(a)
#         b[0] = a[0]
#         for i in range(1, n):
#             if a[i] * b[i - 1] == 0:
#                 b[i] = a[i]
#             else:
#                 if abs(a[i] - a[i] // b[i - 1] * b[i - 1]) < abs(a[i] - 1):
#                     b[i] = a[i] // b[i - 1] * b[i - 1]
#                 else:
#                     b[i] = 1
#         print(' '.join(map(str, b)))
#
#
# def main():
#     solve()
#
#
# if __name__ == "__main__":
#     main()

# ---------------------------------------------------------------------------------------------------
# C - Break An Arm
# import math
#
# def calculate_AD(AB, CA, BC, ratio):
#     # Calculate the ratio of ADE to ABC
#     ratio = ratio / (ratio + 1)
#     # Calculate the length of AD
#     AD = AB * math.sqrt(ratio)
#     return AD
#
# # Read input
# test_cases = int(input())
#
# # Process each test case
# for case in range(1, test_cases + 1):
#     AB, CA, BC, ratio = map(float, input().strip().split())
#     AD = calculate_AD(AB, CA, BC, ratio)
#     print("Case {}: {:.10f}".format(case, AD))

# ---------------------------------------------------------------------------------------------------
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


# ---------------------------------------------------------------------------------------------------
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

# ---------------------------------------------------------------------------------------------------
# F - Mad Creatures!
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


# ---------------------------------------------------------------------------------------------------
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

# ---------------------------------------------------------------------------------------------------
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