import sys, os
sys.path.append(os.pardir)
import common.common as cm

(train_img, train_label), (test_img, test_label) = cm.load_mnist(normalize=True, one_hot_label=True)

print(train_img.shape)
print(train_label.shape)

train_size = train_img.shape[0]
batch_size = 10
batch_mask = cm.np.random.choice(train_size, batch_size)
batch_img = train_img[batch_mask]
batch_label = train_label[batch_mask]