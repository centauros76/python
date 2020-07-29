import numpy as np

# x = np.array([10, 20, 30, 40, 50])
# y = np.array([0, 1, 2, 3, 4])
#
# print(x + y)
# print(x - y)
#
# z = np.array([[5, 6], [7, 8]]) + np.array([[10, 20], [30, 40]]) - np.array([[1, 2], [3, 4]])
# print(z)

# a = np.array([[1, 5, 3, 2],
#              [5, 4, 9, 8]])
# b = np.array([4, 2, 2, 4])
# c = np.array([1, 2, 3, 4])
# d = np.zeros(6)
# print(a == b)
# print(a >= b)
# print(np.all(a == b))
# print(np.all(a == c))
# print(np.any(a == b))
# print(np.any(a < -1))
# print(c.any())
# z = np.where(a > 3, a, 0)
# print(z)
# max = np.argmax(a

# a = np.arange(5).reshape(5, 1)
# b = np.arange(5)
# print(a + b)

x = np.vstack([range(9)[i:i + 4] for i in range(6)])
print('='*10,'x')
print(x)
print('='*10,'y')
y = np.arange(6)[:, np.newaxis]
print(y)
print('='*10, 'z')
z = np.arange(4)
print(z)
print('*'*10, 'x + y')
print(x + y)
print('*'*10, 'x + z')
print(x + z)



