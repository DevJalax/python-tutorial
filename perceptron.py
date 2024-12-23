import numpy as np

class Perceptron:
    def __init__(self, learning_rate=0.01, max_iterations=1000):
        self.learning_rate = learning_rate
        self.max_iterations = max_iterations

    def fit(self, X, y):
        self.weights = np.zeros(X.shape[1])
        self.bias = 0

        for _ in range(self.max_iterations):
            for x_i, y_i in zip(X, y):
                if y_i * (np.dot(x_i, self.weights) + self.bias) <= 0:
                    self.weights += self.learning_rate * y_i * x_i
                    self.bias += self.learning_rate * y_i

    def predict(self, X):
        return np.sign(np.dot(X, self.weights) + self.bias)

# Example usage:
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
y = np.array([1, 1, -1, -1])

perceptron = Perceptron()
perceptron.fit(X, y)
print(perceptron.predict(np.array([[1, 2], [5, 6]])))
