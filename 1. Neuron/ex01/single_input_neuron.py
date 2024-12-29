
""" Tek girişli bir nöron örneği. """

import numpy as np

def step(x):
    return (1 if x > 0 else 0)

input_value = 50
weight = 2.5
bias = 3

Weighted_sum = (input_value * weight) + bias
neuron_output = step(Weighted_sum)
print(neuron_output)
