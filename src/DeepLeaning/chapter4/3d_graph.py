import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.axes3d as p3
import numpy as np

x = np.arange(-3, 4, 0.1)
y = x.reshape(x.shape[0], 1)
z = x**2 + y**2

x, y = np.meshgrid(x, y)

fig = plt.figure(figsize=(12, 6))
#ax = plt.axes(projection='3d')
#ax.contour3D(x, y, z, 20, cmap=plt.cm.rainbow)

ax = p3.Axes3D(fig)
ax.plot_wireframe(x, y, z)

plt.show()

