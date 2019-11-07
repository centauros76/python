import sys, os
import matplotlib.pylab as plt
sys.path.append(os.pardir)
import common.common as cm


def function_2(x):
    return x[0] ** 2 + x[1] ** 2


init_x = cm.np.array([-3.0, 4.0])
lr = 0.1
step_num = 50

x, x_history = cm.gradient_descent(function_2, init_x, lr=lr, step_num=step_num)

plt.plot( [-5, 5], [0,0], '--b')
plt.plot( [0,0], [-5, 5], '--b')
plt.plot(x_history[:,0], x_history[:,1], 'o')

plt.xlim(-3.5, 3.5)
plt.ylim(-4.5, 4.5)
plt.xlabel("X0")
plt.ylabel("X1")
plt.show()