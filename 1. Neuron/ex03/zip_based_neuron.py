
""" zip() ile nöron çıktısı hesplama. """

import numpy as np

def sigmoid(x):
    return (1 / (1 + np.exp(-x)))

inputs = [0, 1, 2, 3, 4, 5]
weights = [2.3, 0.2, -3.2, 4.6, 4.7]
bias = 3

noron_output = sigmoid(sum((x * w for x, w in zip(inputs, weights)), bias))
print(noron_output)
