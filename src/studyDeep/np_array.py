import numpy as np

# list = [1, 2, 3, 4]
# arr = np.array(list)
# print(arr.shape)
# print(arr.dtype)
#
# a = np.zeros(10)
# print(a)
#
# b = np.zeros((2, 4))
# print(b)
#
# c = np.ones(5)
# print(c)
#
# d = np.ones((3,5))
# print(d)
#
# e = np.arange(6, 20)
# print(e)
#
# f = np.full((3, 4), 10, dtype=np.int64)
# print(f)
#
# g = np.empty((2, 3), dtype=np.int64)
# print(g)
#
# h = np.zeros_like(list)
# print(h)
#
# i = np.zeros_like(f)
# print(i)
#
# j = np.ones_like(f)
# print(j)
#
# k = np.identity(3, dtype=np.int64)
# print(k)
#
# l = np.identity(4, dtype=np.int64)
# print(l)
#
# m = np.eye(3, 4, 0, dtype=np.int64)
# print("="*10)
# print(m)
#
# n = np.eye(3, 4, 1, dtype=np.int64)
# print("="*10)
# print(n)
# o = np.eye(3, 4, -1, dtype=np.int64)
# print("="*10)
# print(o)
# for i in range(-5, 6):
#     p = np.eye(3, 4, i, dtype=np.int64)
#     print("="*4, i)
#     print(p)

# arr = np.array([[1, 2, 3], [4, 5, 6]])
# arr2 = np.array([[7, 8, 9], [10, 11, 12]])
# arr3 = np.array([20, 21, 22])
#
# a = arr + arr2
# print(a)
#
# b = arr - arr2
# print(b)
#
# c = arr * arr2
# print(c)
#
# d = arr / arr2
# print(d)
#
# e = arr + arr3
# print(e)

# a = np.arange(10)
# i = 0
# while i < 10:
#     print("a[{}] = {}".format(i, a[i]))
#     i += 1
#
# b = a[3:8]
# print(b)


b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
c = b[2, ]
print(c)

e = []
for d in b:
    e.append(d[1])
print(e)
