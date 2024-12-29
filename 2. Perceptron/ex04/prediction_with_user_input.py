
""" Bu örnekte, kullanıcının girdiği değerlerle Perceptron modeli kullanarak tahmin yapılmaktadır."""

import numpy as np

class Perceptron:
    def __init__(self):
        self.W = None
        self.B = None

    def step_function(self, x):
        return (1 if x >= 0 else 0)

    def train(self, X, Y, alpha, epoch):
        n_samples, n_features = X.shape             # X.shape => (4,2)
        # n_samples: Veri kümesindeki toplam örnek sayısını ifade eder. (ör: Resim)
        # n_features: Her bir örnekteki özellik sayısnı ifade eder. (ör: pixel değerleri)
        self.W = np.random.rand(n_features)
        self.B = np.random.rand(1)   

        for _ in range(epoch):
            for i in range(n_samples):
                neuron_output = self.step_function(np.dot(X[i], self.W) + self.B)
                delta = alpha * (Y[i] - neuron_output) * X[i]
                self.W += delta
                self.B += alpha * (Y[i] - neuron_output)
        return (self.W, self.B)

    def predict(self, X):
        return (self.step_function(np.dot(X, self.W) + self.B)) 

inputlar = np.array([[0,1], [1,1], [1,0], [0,0]])
labels = np.array([1, 1, 1, 0])

perceptron1 = Perceptron()
w, b = perceptron1.train(inputlar, labels, alpha=0.1, epoch=50)

def step_function(x):
    return (1 if x >= 0 else 0)

input_user = input("OR operatörleri için sayilari virgül ile girin(ör: 0,1): ")
input_list = [int(i) for i in input_user.split(",")]        # Veriyi sayıya dönüştür ve liste yap

print(f"{input_list}: {step_function(np.dot(input_list, w) + b)}")
