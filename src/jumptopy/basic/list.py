a = [1, 2, 3, 4, 5]
b = a[:2]
c = a[2:]
print("a is {}, b is {}, c is {}".format(a, b, c))
print("b * 2 is {}".format(b * 2))
print("len(b) is {}".format(len(b)))
print("b * a[1] is {}".format(b*a[1]))
print("hi + str(a[1]) is {}".format('hi'+str(a[1])))

del b[:2]
print("after del b[:2] b is {}".format(b))

a.append(4)
print("after a.append(4) a is {}".format(a))
a.sort()
print("a.sort is {}".format(a))
a.reverse()
print("a.reverse is {}".format(a))

print("a.index(3) is {}".format(a.index(3)))

print("a.count(4) is {}".format(a.count(4)))
print("a is {}".format(a))
print("a.pop(4) is {}".format(a.pop(4)))
print("a is {}".format(a))
a.remove(4)
print("a.remove(4) is {}".format(a))
a.extend([7,8])
print("a.extend[7,8] is {}".format(a))