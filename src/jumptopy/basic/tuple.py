t2 = (1,)

## tuple value is permanent
## t2[0] = 2 --> TypeError: 'tuple' object does not support item assignment
## del t2[0] --> TypeError: 'tuple' object doesn't support item deletion

t1 = (1, 2, "a", "b")
print("t1[0] is {}, t1[3] is {} ".format(t1[0], t1[3]))
print("t1[1:] is {}".format(t1[1:]))

t2 = (3, 4)
print("t1 + t2 is {}".format(t1 + t2))
print("t2 * 3 is {}".format(t2*3))
print("len(t2) is {}".format(len(t2)))
