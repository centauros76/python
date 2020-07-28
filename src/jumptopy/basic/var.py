a = [1, 2, 3]
b = a

print("id(a) is {}, id(b) is {}, a = b is same ? {}".format(id(a), id(b), (a is b)))

c = a[:]
print("id(a) is {}, id(b) is {}, a = c[:] is same ? {}".format(id(a), id(c), (a is c)))

from copy import copy
d = copy(a)
print("id(a) is {}, id(d) is {}, d = copy(a) is same ? {}".format(id(a), id(d), (a is d)))

z, y = ('python', 'java')
print(z, y)

(za, zb) = 'hello', 'python'
print(za, zb)

za, zb = zb, za
print(za, zb)

