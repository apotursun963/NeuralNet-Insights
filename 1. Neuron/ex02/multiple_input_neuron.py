
""" Çok girişli bir nöron örneği. """

import numpy as np

def sigmoid(x):
    return (1 / (1 + np.exp(-x)))

İnputs = [67, 23, 89]        # input vektörü (3 tane girdimiz var)
Weights = [4, 2, 5]          # weight vektörü (3 tane ağırlığımız var)
Bias = 3

Weighted_sum = (İnputs[0] * Weights[0] + İnputs[1] * Weights[1] + İnputs[2] * Weights[2]) + Bias
neuron_output = sigmoid(Weighted_sum)
print(neuron_output)
