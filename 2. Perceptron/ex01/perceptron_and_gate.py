
""" 
Bu örnek, temel bir Perceptron yapısını ve AND mantık operatörünü uygulamaktadır.
alpha: Öğrenme oranı | delta: Ağırlık güncelleme miktarı.
"""

import numpy as np

def step_func(x):
    return (1 if x >= 3 else 0)

inputs = np.array([[1,0], [0,1], [0,0], [1,1]])     # AND
labels = np.array([0, 0, 0, 1])                    

alpha = 1
weights = np.array([1, 1])
for epoch in range(1):
    for i in range(len(inputs)):
        neuron_output = step_func(np.dot(inputs[i], weights))
        delta = alpha * (labels[i] - neuron_output) * inputs[i] 
        weights += delta
        print(f"input: {inputs[i]} | delta: {delta} | weights: {weights}")

# test
tests = np.array([[0,1], [1,1], [1,0], [0,0]])
for i in range(len(tests)):
    test_output = step_func(np.dot(tests[i], weights))      # Öğrenilmiş Weights değeri kullanılıyor
    print(f"{tests[i]}: {test_output}")
