
""" Bu kod, MLP ile XOR problemini çözmek için ileri besleme ve geri yayılım kullanıyor. """

import numpy as np

def sigmoid(x):
    return (1 / (1 + np.exp(-x)))

def sigmoid_derivative(x):
    return x * (1 - x)

inputs = np.array([[1,1], [1,0], [0,1], [0,0]])         # XOR
labels = np.array([[0], [1], [1], [0]])               

np.random.seed(0)                       # aynı değerlerin sürekli olarak oluşturulması için 
i_W_h = np.random.rand(2,2)
i_B_h = np.random.rand(2)

h_W_o = np.random.rand(2,1)
h_B_o = np.random.rand(1)   

alpha = 0.1
epoch = 10000
for i in range(epoch):  

    # ileri besleme 
    hidden_output = sigmoid(np.dot(inputs, i_W_h) + i_B_h)
    final_output = sigmoid(np.dot(hidden_output, h_W_o) + h_B_o)

    # maliyet hesaplama 
    output_error = labels - final_output   

    # geri yayılım
    output_gradient  = output_error * sigmoid_derivative(final_output)
    hidden_gradient  = np.dot(output_gradient, h_W_o.T) * sigmoid_derivative(hidden_output)

    # W ve B güncellemeleri
    h_W_o += np.dot(hidden_output.T, output_gradient) * alpha          
    i_W_h += np.dot(inputs.T, hidden_gradient) * alpha  
    h_B_o += np.sum(output_gradient, axis=0) * alpha
    i_B_h += np.sum(hidden_gradient, axis=0) * alpha

# test
tests = np.array([[0,0], [0,1], [1,1], [1,0], [0,0], [1,1]])

hidden_output_test = sigmoid(np.dot(tests, i_W_h) + i_B_h)
final_output_test = sigmoid(np.dot(hidden_output_test, h_W_o) + h_B_o)   

def step_function(x):
    return (1 if x >= 0.5 else 0)

for i in range(len(tests)):
    print(f"{tests[i]}: {final_output_test[i]} -> {step_function(final_output_test[i])}")
