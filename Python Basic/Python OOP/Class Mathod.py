#
# # Create an Animal Class
# class Animal:
#     def __init__(self, **kwargs):
#         self._type = kwargs['type'] if 'type' in kwargs else 'Kitten'
#         self._name = kwargs['name'] if 'name' in kwargs else 'Fluffy'
#         self._sound = kwargs['sound'] if 'sound' in kwargs else 'Meow'
#
#     def type(self, t=None):
#         if t:
#             self._type = t
#         return self._type
#
#     def name(self, n=None):
#         if n:
#             self._name = n
#         return self._name
#
#     def sound(self, s=None):
#         if s:
#             self._sound = s
#         return self._sound
#
#     def __str__(self):
#         return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}"'
#
#
# def main():
#     a1 = Animal(type='Kitten', name='Fluffy', sound='Meow')
#     print(a1)
#
#
# if __name__ == '__main__':
#     main()

n, k = map(int, input().split())
m = list(map(int, input().split()))
b = list(map(int, input().split()))

c = [0] * (max(m + b) + 1)
d = [0] * (max(m + b) + 1)

a1 = 0
a2 = 0

for i in range(n):
    if m[i] > k:
        continue
    c[m[i]] += 1
    a1 += d[k - m[i]]

for i in range(n):
    if b[i] > k:
        continue
    d[b[i]] += 1
    a2 += c[k - b[i]]

if a1 > a2:
    print("Mahmoud".capitalize())
elif a1 == a2:
    print("Draw".capitalize())
else:
    print("Bashar".capitalize())

# 7 3
# 1 1 2 3 4 1 2
# 2 2 2 1 1 1 2
