
""" dot() ile daha hızlı nöron çıktısı hesaplama """

import numpy as np

def sigmoid(x):
    return (1 / (1 + np.exp(-x)))

inputs = [1, 2, 3, 4]
weights = [2.3, 0.2, -3.2, 4.3]
bias = 5

neuron_output = sigmoid(np.dot(inputs, weights) + bias)
print(neuron_output)

