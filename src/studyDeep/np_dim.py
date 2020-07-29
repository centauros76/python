import numpy as np

a = np.vstack([range(100)[i:i + 5] for i in range(45) if i % 5 == 0])
print("a :: {}".format(a))
# np array reverse
# print("a0 :: {}".format(np.flip(a, axis=0)))
# print("a1 :: {}".format(np.flip(a, axis=1)))
# print("a01 :: {}".format(np.flip(a)))
#
print("sum(a) :: {}".format(np.sum(a)))
print("average(a) :: {}".format(np.average(a)))
# print("a.min() :: {}".format(a.min()))
# print("a.max() :: {}".format(a.max()))
# print("a.argmin() :: {}".format(a.argmin()))
# print("a.argmax() :: {}".format(a.argmax()))
print("a.mean() :: {}".format(a.mean()))
print("np.median(a) :: {}".format(np.median(a)))
# print("np.all(a) :: {}".format(np.all(a)))
# print("np.any(a) :: {}".format(np.any(a)))

print("a.sum(axis=0) ::\n {}".format(a.sum(axis=0)))
print("a.mean(axis=0) ::\n {}".format(a.mean(axis=0)))
print("a.sum(axis=1) ::\n {}".format(a.sum(axis=1).reshape(9, 1)))
print("a.mean(axis=1) ::\n {}".format(a.mean(axis=1).reshape(9, 1)))
