
""" 0-9 arası MNIST rakamları tahmin etme modeli. Kullanıcı istediği kadar gizli katman oluşturabilir. """

from keras._tf_keras.keras.datasets import mnist
from keras._tf_keras.keras.utils import to_categorical
import matplotlib.pyplot as plt
import numpy as np
import time

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.reshape(60000, 28*28) / 255.0         #  (28*28) 2D => (784) 1D
x_test = x_test.reshape(10000, 28*28)  / 255.0         

y_train = to_categorical(y_train, num_classes=10)
y_test = to_categorical(y_test, num_classes=10)

print(f"x_train shape: {x_train.shape}\ny_train shape: {y_train.shape}")
print(f"x_test shape: {x_test.shape}\ny_test shape: {y_test.shape}")


# Hyperparameters
learning_rate = 1e-2        # 0.01
epochs = 3000

def softmax(x):
    exps = np.exp(x - np.max(x)) 
    return exps / np.sum(exps, axis=1, keepdims=True)

def relu(x):
    return np.maximum(0, x)

def relu_derivative(x):
    return np.where(x > 0, 1, 0)

def cross_entropy_loss(Y, predictions):
    predictions = np.clip(predictions, 1e-9, 1 - 1e-9)
    return -np.mean(np.sum(Y * np.log(predictions), axis=1))

def calculate_accuracy(Y, predictions):
    actual = np.argmax(Y, axis=1)
    predicted_classes = np.argmax(predictions, axis=1)
    return np.mean(predicted_classes == actual)


class MLP:
    def __init__(self, input_unit, hidden_units, output_unit):
        self.layer = len(hidden_units)
        self.weights = []; self.biases = []

        self.weights.append(np.random.randn(input_unit, hidden_units[0]) * np.sqrt(2 / input_unit))
        self.biases.append(np.zeros(hidden_units[0]))

        for i in range(self.layer -1):
            self.weights.append(np.random.randn(hidden_units[i], hidden_units[i+1]) * np.sqrt(2 / hidden_units[i])) 
            self.biases.append(np.zeros(hidden_units[i+1]))

        self.weights.append(np.random.randn(hidden_units[len(hidden_units) -1], output_unit) * np.sqrt(2 / hidden_units[-1])) 
        self.biases.append(np.zeros(output_unit))

    def forward(self, X):
        self.hidden_output = []

        frst_output = relu(np.dot(X, self.weights[0]) + self.biases[0])   
        self.hidden_output.append(frst_output)

        for i in range(self.layer -1):
            output = relu(np.dot(self.hidden_output[i], self.weights[i+1]) + self.biases[i+1])   
            self.hidden_output.append(output)

        self.final_output = softmax(np.dot(self.hidden_output[-1], self.weights[-1]) + self.biases[-1])   
        return (self.final_output)

    def backward(self, inputs, Y):
        m = Y.shape[0]
        dW, dB = [], []
        error_list = []

        error_list.append(self.final_output - Y)                
        dW.append((1/m) * np.dot(self.hidden_output[-1].T, error_list[0]))  
        dB.append((1/m) * np.sum(error_list[0], axis=0))

        for i in range(self.layer, 0, -1):
            error_list.append(np.dot(error_list[-1], self.weights[i].T) * relu_derivative(self.hidden_output[i-1]))
            dW.append((1/m) * np.dot(inputs.T if i == 1 else self.hidden_output[i-2].T, error_list[-1]))
            dB.append((1/m) * np.sum(error_list[-1], axis=0))
        return (dW[::-1], dB[::-1])

    def update_parameters(self, dW, dB, learning_rate):
        for i in range(len(dW)):
            self.weights[i] -= learning_rate * dW[i]
            self.biases[i] -= learning_rate * dB[i]
        return (self.weights, self.biases)

    def train(self, X, Y, learning_rate, epoch):
        loss_list, accuracy_list = [], []

        for i in range(1, epoch +1):
            predictions = self.forward(X)
            dW, dB = self.backward(X, Y)
            W, B = self.update_parameters(dW, dB, learning_rate)

            loss = cross_entropy_loss(Y, predictions)
            loss_list.append(loss)
            acc = calculate_accuracy(Y, predictions)
            accuracy_list.append(acc)

            if i % 100 == 0:
                print(f"Epoch: {i} | Loss: {loss} | Accuracy: %{acc * 100:.2f}")  
        return (W, B, loss_list, accuracy_list)

model = MLP(
    input_unit=784,
    hidden_units=[64, 32, 64],
    output_unit=10
)

time_1 = time.time()
W, B, loss_list, accuracy_list = model.train(x_train, y_train, learning_rate, epochs)
time_2 = time.time()

print(f"Modelin Eğitim Süresi: {(time_2 - time_1) / 60:.2f} dk")

# İki alt grafik oluşturuyoruz
fig, axs = plt.subplots(2, 1, figsize=(8, 6))       # subplot => alt grafik
# İlk grafik - Accuracy
axs[0].plot(accuracy_list, label='Accuracy', color='b')
axs[0].set_xlabel('Epoch')
axs[0].set_ylabel('Accuracy')
axs[0].legend()
axs[0].grid(True)
# İkinci grafik - Loss
axs[1].plot(loss_list, label='Loss', color='r')
axs[1].set_xlabel('Epoch')
axs[1].set_ylabel('Loss')
axs[1].legend()
axs[1].grid(True)

plt.tight_layout()          # Alt grafikler arasında düzgün boşluk bırakır
plt.show()
