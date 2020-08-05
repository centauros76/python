import numpy as np
import matplotlib.pyplot

mnist_train_data_file = open('/Users/rene.kwak/Private/studyData/mnist_train_100.csv', 'r')
mnist_train_data_list = mnist_train_data_file.readlines()
mnist_train_data_file.close()

#for i in range(0, 10):
all_values = mnist_train_data_list[0].split(',')
image_array = np.asfarray(all_values[1:]).reshape((28, 28))
matplotlib.pyplot.imshow(image_array, cmap='Greys', interpolation='None')
matplotlib.pyplot.show()

scaled_input = (np.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
print(scaled_input)