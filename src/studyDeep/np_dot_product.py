import numpy as np

# a = np.arange(6).reshape(2, 3)
# print("{} shape {}".format(a, np.shape(a)))
#
# b = np.arange(12).reshape(3, 4)
# print("{} shape {}".format(b, np.shape(b)))
#
# c = a.dot(b)
# print("a.dot(c) ::\n {} shape {}".format(c, np.shape(c)))
#
#
# d = np.arange(6).reshape(3, 2) - 3
# print(d)
#
# # print(np.sqrt(9))
# # print(np.square(3))
# #
# # print(np.log10(10))
#
# print(np.modf([2.4, 5.2, 6.1]))
# z = np.modf([2.4, 5.2, 6.1])[0]
# y = np.modf([2.4, 5.2, 6.1])[1]
#
# print(z, y)
#
# i = np.transpose(a)
# print(i)
#
# print(i == 2)


names = np.array(["Charles", "Kilho", "Hayoung", "Charles", "Hayoung", "Kilho", "Kilho"])
data = np.array([[ 0.57587275, -2.84040808,  0.70568712, -0.1836896 ],
                 [-0.59389702, -1.35370379,  2.28127544,  0.03784684],
                 [-0.28854954,  0.8904534 ,  0.18153112,  0.95281901],
                 [ 0.75912188, -1.88118767, -2.37445741, -0.5908499 ],
                 [ 1.7403012 ,  1.33138843,  1.20897442, -0.58004389],
                 [ 1.11585923,  1.02466538, -0.74409379, -1.55236176],
                 [-0.45921447,  2.53114818,  0.5029578 , -0.24088216]])
print(data[(names == 'Charles') | (names == 'Kilho')])

a = data[:, 3] < 0
print(a.reshape(7,1))