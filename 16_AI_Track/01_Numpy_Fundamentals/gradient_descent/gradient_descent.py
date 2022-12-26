from abc import abstractmethod
import numpy as np

class LinearRegressionGD:
    def __init__(self, eta=0.1, epochs=100) -> None:
        self.eta = eta
        self.epochs = epochs
        self.theta = None

    @abstractmethod
    def fit(self):
        pass

    def predict(self, X):
        t0, t1 = float(self.theta[0]), float(self.theta[1])
        return t0 + t1 * X


class LBGD(LinearRegressionGD):
    def __init__(self, eta=0.1, epochs=1000) -> None:
        super().__init__(eta, epochs)

    def fit(self, X, y):
        theta = np.random.randn(2,1)
        X_train = np.c_[np.ones((100, 1)), X]
        y_train = y
        m = X_train.shape[0]
        for epoch in range(self.epochs):
            gradients = 2/m * X_train.T.dot(X_train.dot(theta) - y_train)
            theta = theta - self.eta * gradients
        self.theta = theta
        return self.theta

class LSGD(LinearRegressionGD):
    def __init__(self, eta=0.1, epochs=100, l_schedule=(5, 50)) -> None:
        super().__init__(eta, epochs)
        self.l_schedule = l_schedule

    def learning_schedule(self, s):
        s0, s1 = self.l_schedule
        return s0 / (s + s1)

    def fit(self, X, y):
        theta = np.random.randn(2,1)
        X_train = np.c_[np.ones((100, 1)), X]
        y_train = y
        m = X_train.shape[0]
        for epoch in range(self.epochs):
            for i in range(m):
                random_index = np.random.randint(m)
                xi = X_train[random_index: random_index+1]
                yi = y_train[random_index: random_index+1]
                gradients = 2*xi.T.dot(xi.dot(theta) - yi)
                eta = self.learning_schedule(self.eta*m + i)
                theta = theta - eta*gradients

        self.theta = theta
        return self.theta