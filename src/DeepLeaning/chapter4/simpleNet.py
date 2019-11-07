import sys, os

sys.path.append(os.pardir)
from common.function import softmax, cross_entropy_error, numerical_gradient
import numpy as np


class simpleNet:
    def __init__(self):
        self.W = np.random.randn(2, 3)

    def predict(self, x):
        return np.dot(x, self.W)

    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy_error(y, t)

        return loss


net = simpleNet()

x = np.array([0.6, 0.9])
t = np.array([0, 0, 1])


def f(W):
    return net.loss(x, t)


dW = numerical_gradient(f, net.W)
print(dW)


