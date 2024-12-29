
""" Üç Katmanlı Multi-layer Perceptron """

import numpy as nmp

def sigmoid(x):
    return (1 / (1 + nmp.exp(-x)))

def sigmoid_turevi(x):
    return x * (1 - x)          

class NeuralNetwork:
    def __init__(self, input_size=2, hidden_size=2, output_size=1):
        self.input_weight_to_hidden = nmp.random.rand(input_size, hidden_size)      
        self.hidden_weight_to_output = nmp.random.rand(hidden_size, output_size)
        self.hidden_biases = nmp.random.rand(hidden_size)
        self.output_biases = nmp.random.rand(output_size)

    def forward(self, inputs):
        self.hidden_output = sigmoid(nmp.dot(inputs, self.input_weight_to_hidden) + self.hidden_biases)
        self.final_ouput = sigmoid(nmp.dot(self.hidden_output, self.hidden_weight_to_output) + self.output_biases)
        return (self.final_ouput)

    def calculate_error(self, target):
        output_error = target - self.final_ouput
        output_gradient = output_error * sigmoid_turevi(self.final_ouput)       # gradyan(eğim) değerleri hesaplanıyor
        hidden_error = nmp.dot(output_gradient, self.hidden_weight_to_output.T)
        hidden_gradient= hidden_error * sigmoid_turevi(self.hidden_output)
        return (hidden_gradient, output_gradient)

    def backward(self, inputs, targets, learning_rate):
        self.forward(inputs)
        hidden_gradient, output_gradient = self.calculate_error(targets)         # Ağırlık/Bias güncelleme miktarları
        self.hidden_weight_to_output += nmp.dot(self.hidden_output.T, output_gradient) * learning_rate
        self.input_weight_to_hidden += nmp.dot(inputs.T, hidden_gradient) * learning_rate 
        self.output_biases += output_gradient.sum(axis=0) * learning_rate
        self.hidden_biases += hidden_gradient.sum(axis=0) * learning_rate

    def train_model(self, inputs, targets, epochs=3000, learning_rate=0.1):
        for _ in range(epochs):
            self.forward(inputs)
            self.backward(inputs, targets, learning_rate)

# AND operatörü
inputlar = nmp.array([[1, 1], [0, 0], [1, 1], [0, 1]])
etiket_verileri = nmp.array([[1], [0], [1], [0]])

Model1 = NeuralNetwork()
Model1.train_model(inputlar, etiket_verileri)

test_input = nmp.array([[1,1], [1,1], [0,0], [0,1]])
for girdi in test_input:
    output = Model1.forward(girdi)
    print(f"{girdi} = {1}") if output >= 0.5 else print(f"{girdi} = {0}")
