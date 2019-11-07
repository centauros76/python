import common.common as cm


img, label = cm.get_data()
network = cm.init_network()

accuracy_cnt = 0
miss_cnt = 0
for i in range(len(img)):
    y = cm.predict(network, img[i])
    p = cm.np.argmax(y)

    if p == label[i]:
        accuracy_cnt += 1
    else:
        miss_cnt += 1

print("Accuracy :: " + str(float(accuracy_cnt) / len(img)))
print("Miss_cnt :: %d " % miss_cnt)
print("Miss :: " + str(float(miss_cnt) / len(img)))