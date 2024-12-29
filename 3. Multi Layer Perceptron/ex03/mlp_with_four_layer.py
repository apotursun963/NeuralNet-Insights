
""" Dört Katmanlı Multi-layer Perceptron """

import numpy as np

def sigmoid(x):
    return (1 / (1 + np.exp(-x)))

def sigmoid_derivative(x):
    return x * (1 - x)

def mse_loss(y_true, y_pred):
    return ((y_true - y_pred) ** 2).mean()

def accuracy(y_true, y_pred):
    predictions = y_pred > 0.5
    return np.mean(predictions == y_true)

class MLP:
    n_parameters = [0]*3
    def __init__(self, x_size, h1_size, h2_size ,o_size):
        np.random.seed(0)       
        self.i_W_h1 = np.random.rand(x_size, h1_size)
        self.h1_W_h2 = np.random.rand(h1_size, h2_size)
        self.h2_W_o = np.random.rand(h2_size, o_size)
        self.i_B_h1 = np.random.rand(h1_size)
        self.h1_B_h2 = np.random.rand(h2_size)
        self.h2_B_o = np.random.rand(o_size)

        # Calculate the Parameters
        n_W = (x_size * h1_size) + (h1_size * h2_size) + (h2_size * o_size)
        n_B = h1_size + h2_size + o_size
        MLP.n_parameters = [n_W, n_B, (n_W + n_B)]

    def Parameter(self):
        return (f"n_Weight: {self.n_parameters[0]} | n_Bias: {self.n_parameters[1]} | Sum Parameters: {self.n_parameters[2]}")
    
    def forward(self, X):
        self.hidden1_output = sigmoid(np.dot(X, self.i_W_h1) + self.i_B_h1)
        self.hidden2_output = sigmoid(np.dot(self.hidden1_output, self.h1_W_h2) + self.h1_B_h2)
        self.final_output = sigmoid(np.dot(self.hidden2_output, self.h2_W_o) + self.h2_B_o)
        return (self.final_output)

    def cost(self, final_output, Y):
        return (Y - final_output)

    def backward(self, output_error, alpha):
        self.output_gradient = output_error * sigmoid_derivative(self.final_output)
        self.hidden2_gradient = np.dot(self.output_gradient, self.h2_W_o.T) * sigmoid_derivative(self.hidden2_output)
        self.hidden1_gradient = np.dot(self.hidden2_gradient, self.h1_W_h2.T) * sigmoid_derivative(self.hidden1_output)
        
        self.h2_W_o += np.dot(self.hidden2_output.T, self.output_gradient) * alpha          
        self.h1_W_h2 += np.dot(self.hidden1_output.T, self.hidden2_gradient) * alpha  
        self.i_W_h1 += np.dot(inputs.T, self.hidden1_gradient) * alpha  
        self.h2_B_o += np.sum(self.output_gradient, axis=0) * alpha
        self.h1_B_h2 += np.sum(self.hidden2_gradient, axis=0) * alpha
        self.i_B_h1 += np.sum(self.hidden1_gradient, axis=0) * alpha

    def train(self, X, Y, alpha, epoch):
        for i in range(1, epoch +1):
            model_prediction = self.forward(X)
            model_output_error = self.cost(model_prediction, Y)
            self.backward(model_output_error, alpha)
            if i % 250 == 0:                                        
                loss = mse_loss(Y, self.forward(inputs))
                acc = accuracy(Y, self.forward(inputs))
                print(f"Epoch: {i} | Loss: {loss} | Accuracy: %{acc * 100:.2f}")

    def predict(self, X):
        predict = self.forward(X).reshape(-1)         # tek boyutlu vektör hale getirildi
        return ([1 if value >= 0.5 else 0 for value in predict])  # değerleri 0 1 arasına getirme  

# XOR operatörü
inputs = np.array([[1,1], [1,0], [0,1], [0,0]])         # XOR
labels = np.array([[0], [1], [1], [0]])

mlp1 = MLP(x_size=2, h1_size=16, h2_size=8, o_size=1)
mlp1.train(inputs, labels, 1, 5000)

# test
tests = np.array([[1,0], [0,0], [0,1], [1,1]])
prediction = mlp1.predict(tests)
for test, predict in zip(tests, prediction):
    print(f"{test}: {predict}")

print(f"Parametreler: {mlp1.Parameter()}")
