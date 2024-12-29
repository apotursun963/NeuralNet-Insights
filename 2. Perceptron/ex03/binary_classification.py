
"""
Bu kod, ikili sınıflandırma problemi üzerinde çalışarak metin verilerini 
sayısal verilere dönüştürüp bir perceptron modeli ile bu verileri sınıflandırmayı amaçlar.
"""

import numpy as np
from sklearn.preprocessing import LabelEncoder

class Perceptron:
    def __init__(self, input_size):
        self.weights = np.random.rand(input_size)
        self.bias = np.random.rand(1)
    
    def train(self, X, Y, learning_rate=0.1, epoch=50):
        for _ in range(epoch):
            for i in range(X.shape[0]):         # x.shape[0] => satır sayısı(n_samples)
                neuron_output = self.step_function(np.dot(X[i], self.weights) + self.bias)
                output_error = Y[i] - neuron_output
                self.weights += learning_rate * X[i] * output_error
                self.bias += learning_rate * np.sum(output_error)
        return (self.weights, self.bias)

    def step_function(self, x):
        return (1 if x >= 0 else 0)

    def predict(self, X):
        return (self.step_function(np.dot(X, self.weights) + self.bias))

# input & target
inputlar = np.array(["Spam", "Spam Değil"])    
targetlar = np.array([1, 0])

label_encoder = LabelEncoder()               # Label Encoder: Kategorik verileri sayısal değerlere dönüştürür (ör. ["kırmızı", "yeşil", "mavi"] → [0, 1, 2]).
encoded_inputs = label_encoder.fit_transform(inputlar)

perceptron1 = Perceptron(input_size=1)
perceptron1.train(encoded_inputs, targetlar)    

# Test
test = np.array(["Spam", "Spam Değil", "Spam", "Spam Değil"])  
test_data = label_encoder.transform(test)           # metin veriler sayısal verilere dönüştürülüyor  
print(test_data)                    # [0 1 0 1] => "spam": 0 | "spam Değil": 1 olarak dönüştürüldü

for i in range(len(test)):
    print(f"{test[i]} : {perceptron1.predict(test_data[i])}")
