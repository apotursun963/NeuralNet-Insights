
""" Bir nöron Class'ı """

import numpy as np

def sigmoid(x):
    return (1 / (1 + np.exp(-x)))

class Neuron:
    Neuron_Sayisi = 0
    def __init__(self, inputs, weights, biases):
        self.inputs = inputs
        self.weights = weights
        self.biases = biases
        Neuron.Neuron_Sayisi += 1

    @classmethod
    def noron_sayisi(cls): 
        return (f"Nöron Sayisi: {cls.Neuron_Sayisi}")
    
    @property
    def neuron_output(self): 
        return (sigmoid((np.dot(self.inputs, self.weights)) + self.biases))

İnputs = np.random.rand(3,5)
Weights = np.random.rand(5,3)
Bias = np.random.rand(3, 1)

neuron1 = Neuron(İnputs, Weights, Bias)          
neuron2 = Neuron(İnputs, Weights, Bias)     

print(neuron2.neuron_output)
print(Neuron.noron_sayisi())
