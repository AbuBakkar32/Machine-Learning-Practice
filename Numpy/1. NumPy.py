import numpy as np

a = np.zeros((3, 3, 3))

a

np.ones((2, 2, 4), dtype=int)

np.full((2, 2), "hellottwyyw", dtype='<U7')

np.random.rand(10)

data = np.random.randint(5, 10, (10, 10))

data[4:8]

data[4:8, 4:6]

data[4:6, 4:6]

data1 = np.random.randint(5, 15, size=(5, 3))

data2 = np.random.randint(5, 15, size=(5, 3))

np.hstack([data1, data2])

np.vstack([data1, data2])

np.concatenate([data1, data2], axis=1)

data1 = np.random.randint(5, 15, size=(5, 3, 2))

data2 = np.random.randint(5, 15, size=(5, 3, 2))

np.concatenate([data1, data2], axis=2)

a1, a2 = np.hsplit(data, [5])

a1

b1, b2, b3 = np.vsplit(data, [5, 7])

b1

b2

b3

data.shape

data.ndim

data.size

data.reshape(2, 50)

d = np.array([1, 2, 3, 4, 5, 6, 7, 9])

d.ndim

d.shape

d.size

d.reshape(8, 1)

data.reshape(-1, 20)

np.sum(data)

np.sum(data, axis=1)

data

np.sin(data)

data.T

data.mean(axis=1)

data.std(axis=1)

v = np.array([1, 2, 3, 4, 5])

s = 10

v + s

t = [10, 11]

a = np.array([[1], [2], [3], [4], [5]])

a.shape

a + v

a = np.random.randint(1, 5, size=(10, 2))

b = np.random.randint(1, 5, size=(5, 2))

a.reshape(1, 10, 2)

b.reshape(5, 1, 2) - a.reshape(1, 10, 2)

a = np.random.randint(1, 5, size=(10, 2))

b = np.random.randint(1, 5, size=(5, 3))

a.shape

b.shape

a.reshape(1, 10, 1, 2) - b.reshape(5, 1, 3, 1)
