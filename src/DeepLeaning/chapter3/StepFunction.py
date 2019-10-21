import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    return np.array(x > 0, dtype=np.int)

def test(x):
    return x ** 128


x = np.arange(-5.0, 5.0, 0.01)
y = test(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()
