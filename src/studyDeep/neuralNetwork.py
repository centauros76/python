import numpy as np
import scipy.special
import matplotlib.pyplot
import time
import datetime
import imageio


class neuralNetwork:

    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        self.innodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes

        # self.win = (np.random.rand(self.hnodes, self.innodes) - 0.5)
        # self.who = (np.random.rand(self.onodes, self.hnodes) - 0.5)

        # more sensitive weight
        self.win = np.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.innodes))
        self.who = np.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))

        self.lr = learningrate

        self.activation_function = lambda x: scipy.special.expit(x)

        pass

    def train(self, inputs_list, targets_list):

        inputs = np.array(inputs_list, ndmin=2).T
        targets = np.array(targets_list, ndmin=2).T

        hidden_inputs = np.dot(self.win, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)

        final_inputs = np.dot(self.who, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)

        output_errors = targets - final_outputs
        hidden_errors = np.dot(self.who.T, output_errors)

        self.who += self.lr * np.dot((output_errors * final_outputs * (1.0 - final_outputs)), np.transpose(hidden_outputs))
        self.win += self.lr * np.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), np.transpose(inputs))

        pass

    def query(self, inputs_list):
        inputs = np.array(inputs_list, ndmin=2).T

        hidden_inputs = np.dot(self.win, inputs)

        hidden_outputs = self.activation_function(hidden_inputs)

        final_inputs = np.dot(self.who, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)

        return final_outputs

    def draw(self, test_input_all_values):
        image_array = np.asfarray(test_input_all_values[1:]).reshape(28, 28)
        matplotlib.pyplot.imshow(image_array, cmap='Greys', interpolation='None')
        matplotlib.pyplot.show()


# init
start = time.time()
in_nodes = 784
hidden_nodes = 100
out_nodes = 10

lr = 0.2

n = neuralNetwork(in_nodes, hidden_nodes, out_nodes, lr)

#train_data_file = open('/Users/rene.kwak/Private/studyData/mnist_train_100.csv', 'r')
train_data_file = open('/Users/rene.kwak/Private/studyData/mnist_train.csv', 'r')
train_data_list = train_data_file.readlines()
train_data_file.close()


# train
epochs = 2
for e in range(epochs):
    for recode in train_data_list:
        all_values = recode.split(',')
        inputs = (np.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
        targets = np.zeros(out_nodes) + 0.01
        targets[int(all_values[0])] = 0.99
        n.train(inputs, targets)
        pass
    pass

sec = time.time() - start
train_time = str(datetime.timedelta(seconds=sec)).split('.')
train_time = train_time[0]
print("train time :: {}".format(train_time))

# test
test_data_file = open('/Users/rene.kwak/Private/studyData/mnist_test.csv', 'r')
test_data_list = test_data_file.readlines()
test_data_file.close()

scorecard = []
for i in range(0, len(test_data_list)):
#for i in range(0, 1):
    test_all_values = test_data_list[i].split(',')
    #n.draw(test_all_values)
    final_output = n.query((np.asfarray(test_all_values[1:]) / 255.0 * 0.99) + 0.01)
    test_label = int(test_all_values[0])
    neuralNetwork_answer = int(final_output.argmax())

    if test_label == neuralNetwork_answer:
        scorecard.append(1)
    else:
        #print("test data label :: {}".format(test_label))
        #print("neuralNetwork answer :: {}".format(neuralNetwork_answer))
        scorecard.append(0)

scorecard_array = np.asarray(scorecard)
print("incorrect count :: {}".format(scorecard_array.size - scorecard_array.sum()))
print("correct ratio :: {}".format(scorecard_array.sum()/scorecard_array.size * 100))
sec = time.time() - start
process_time = str(datetime.timedelta(seconds=sec)).split('.')
process_time = process_time[0]
print(process_time)


# get Test data
img_array = imageio.imread('/Users/rene.kwak/Private/0_28by28.png', as_gray=True)


img_data = 255.0 - img_array.reshape(784)

image_array = np.asfarray(img_data).reshape(28, 28)
matplotlib.pyplot.imshow(image_array, cmap='Greys', interpolation='None')
matplotlib.pyplot.show()


img_data = (img_data / 255.0 * 0.99) + 0.01

final_output = n.query((np.asfarray(img_data)))
print(final_output)
neuralNetwork_answer = int(final_output.argmax())
print("neuralNetwork answer :: {}".format(neuralNetwork_answer))

process_time = str(datetime.timedelta(seconds=sec)).split('.')
process_time = process_time[0]
print(process_time)
