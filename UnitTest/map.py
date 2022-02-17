# Map Function working with calculate the Celcius to Fahrenheit
# temps = [("berlin", 35), ("germany", 50), ("england", 41), ("Dhaka", 26), ("France", 10)]
# c_to_f = lambda data: (data[0], round((9 / 5) * data[1] + 32, 2));
# result = map(c_to_f, temps)
# a = dict(result)
# print(json.dumps(a, indent=4))
#
# # List Comprehension is a concise way to create a list.
# # It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses.
# # The expression is evaluated once for each item in the list that will be returned.
# A = [1, 2, 3, 4]
# B = [5, 6, 7, 8]
# com = [(i, j) for i in A for j in B]
#
# import time
#
#
# def count_item(number):
#     print("Counting", end="", flush=True)
#     num = 0
#     for i in number:
#         num += 1
#         time.sleep(1)
#         print(".", end=" ", flush=True)
#     print(f"\nTotal Number of Items: {num}")
#     return num

# family = {
#     "member1": {
#         "Name": "Ajay",
#         "Age": 59,
#         "Occupation": {
#             "Occupation": "Software Engineer",
#             "score": [1, 2, 4],
#         },
#         "Relation": "Dad"
#     }
# }
#
# print(family)  # Accessing parent dictionary
#
# print("\n\n", family["member1"])  # Accessing child dictionary
#
# print("\n\n", family["member1"]["Occupation"]["score"][2])  # Accessing child dictionary key
