import json

# Map Function working with calculate the Celcius to Fahrenheit
temps = [("berlin", 35), ("germany", 50), ("england", 41), ("Dhaka", 26), ("France", 10)]
c_to_f = lambda data: (data[0], round((9 / 5) * data[1] + 32, 2));
result = map(c_to_f, temps)

a = dict(result)
print(json.dumps(a, indent=6))

# List Comprehension
A = [1, 2, 3, 4]
B = [5, 6, 7, 8]
com = [(i, j) for i in A for j in B]
for i, j in com:
    print()
