
""" Hazır model kullanarak perceptron oluşturma """

from sklearn.linear_model import Perceptron
import numpy as nmp

inputlar = nmp.array([[1, 0], [1, 1], [0, 1], [0, 0]])
etiket_verileri = nmp.array([1, 1, 1, 0])

perceptron = Perceptron(max_iter=10)
perceptron.fit(inputlar, etiket_verileri)

# test
x_test = nmp.array([[0, 1], [1, 0], [0, 0], [0, 1]])
for girdi in x_test:
    result = perceptron.predict([girdi])
    print(f"Giriş: {girdi}, Tahmin: {result[0]}")
