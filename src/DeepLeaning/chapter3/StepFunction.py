import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    return np.array(x > 0, dtype=np.int)

def test(x):
    return (x) ** 256


x = np.arange(-10.0, 10.0, 0.01)
y = test(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.xlim(-10, 10)
plt.show()
