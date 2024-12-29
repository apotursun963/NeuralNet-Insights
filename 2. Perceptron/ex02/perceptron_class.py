
""" Perceptron Class """

import numpy as np

class Perceptron:
    def __init__(self):
        pass

    def step_function(self, x):
        return (1 if x >= 0 else 0)

    def train(self, X, Y, alpha, epoch):
        global W, B
        W = np.random.rand(X.shape[1])
        B = np.random.rand(1)
        for _ in range(epoch):
            for i in range(X.shape[0]):
                neuron_output = self.step_function(np.dot(X[i], W) + B)
                output_error = Y[i] - neuron_output
                W += alpha * output_error * X[i]
                B += alpha * output_error
        return (W, B)

    def predict(self, X_array):
        return np.array([self.step_function(np.dot(x, W) + B) for x in X_array])    # vektör döndürüyor

inputlar = np.array([[0,1], [1,1], [1,0], [0,0]])
labels = np.array([1, 1, 1, 0])

perceptron1 = Perceptron()
perceptron1.train(inputlar, labels, alpha=0.1, epoch=10)

# test
tests = np.array([[0,0], [0,1], [1,1], [1,0], [0,0], [1,1]])
y_output = perceptron1.predict(tests)
for i in range(len(y_output)):
    print(f"{tests[i]}: {y_output[i]}")
