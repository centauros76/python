import common as cm
import numpy as np
'''
x, _ = cm.get_data()
network = cm.init_network()
W1, W2, W3 = network['W1'], network['W2'], network['W3']

print(x.shape)
print(x[0].shape)
print(W1.shape)
print(W2.shape)
print(W3.shape)
'''

img, label = cm.get_data()
network = cm.init_network()

batch_size = 100
accuracy_cnt = 0

for i in range(0, len(img), batch_size):
    img_batch = img[i:i+batch_size]
    y_batch = cm.predict(network, img_batch)
    p = np.argmax(y_batch, axis=1)
    accuracy_cnt += np.sum(p == label[i:i+batch_size])

print("Accuracy :: " + str(float(accuracy_cnt) / len(img)))