import sys, os

sys.path.append(os.pardir)
import common.common as cm
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D


def function_1(x):
    return 0.01 * x ** 2 + 0.1 * x


def function_2(x):
    #return cm.np.sum(x ** 2)
    return x[0]**2 + x[1]**2

# x = cm.np.arange(0.0, 20.0, 0.1)
# y = function_1(x)
# plt.xlabel("x")
# plt.ylabel("f(x)")
# plt.plot(x, y)
# plt.show()

def function_tmp1(x):
    return x**2 + 4.0**2.0

def function_tmp2(x):
    return 3.0**2 + x*x

print(cm.numerical_diff(function_tmp1, 3.0))
print(cm.numerical_diff(function_tmp1, 4.0))

print(cm.numerical_gradient(function_2, cm.np.array([3.0, 4.0])))
print(cm.numerical_gradient(function_2, cm.np.array([0.0, 2.0])))
print(cm.numerical_gradient(function_2, cm.np.array([3.0, 0.0])))

