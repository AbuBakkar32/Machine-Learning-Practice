List = [15, 6, 13, 22, 3, 52, 2]
print(f"Original list is: {List}")
n = len(List)

for i in range(n):
    for j in range(0, n - i - 1):
        if List[j] > List[j + 1]:
            List[j], List[j + 1] = List[j + 1], List[j]
print(f"The Sorted list is {List}")
