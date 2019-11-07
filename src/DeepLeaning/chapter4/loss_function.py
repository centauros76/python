import sys, os
sys.path.append(os.pardir)
import common.common as cm

t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
y1 = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
y2 = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]

mse1 = cm.mean_squared_error(cm.np.array(y1), cm.np.array(t))
mse2 = cm.mean_squared_error(cm.np.array(y2), cm.np.array(t))

cee1 = cm.cross_entropy_error(cm.np.array(y1), cm.np.array(t))
cee2 = cm.cross_entropy_error(cm.np.array(y2), cm.np.array(t))


print("mse1 : %f" % mse1)
print("mse2 : %f" % mse2)
print("cee1 : %f" % cee1)
print("cee2 : %f" % cee2)