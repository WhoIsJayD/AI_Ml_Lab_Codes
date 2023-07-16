<<<<<<< HEAD
import numpy as np
from matplotlib import pyplot as plt

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
Y = np.array([0, 1, 1, 0])

plt.scatter(x=X[:, 0], y=X[:, 1], c=Y)
plt.show()

n_samples = X.shape[0]
n_features = X.shape[1]

w = np.random.uniform(0, 1, size=n_features)
b = np.random.uniform(0, 1, 1)

n_epoch = int(input("Enter number of epochs : "))
lr = 0.01

for e in range(n_epoch):
    for s in range(n_samples):
        net = np.dot(X[s, :], w)+b
        if net >= 0:
            a = 1
        else:
            a = 0
        error = Y[s]-a
        w = w+lr*error*X[s, :]
        b = b+lr*error

m = -w[0]/w[1]
c = -b/w[1]

def plot_decision_boundary(X):
    for x in np.linspace(np.min(X[:, 0]), np.max(X[:, 0])):
        y = m*x+c
        plt.plot(x, y, linestyle='-', color='k', marker='.')
        plt.scatter(X[:,0],X[:,1],c=Y)
        plt.show()


plot_decision_boundary(X)
=======
import numpy as np
from matplotlib import pyplot as plt

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
Y = np.array([0, 1, 1, 0])

plt.scatter(x=X[:, 0], y=X[:, 1], c=Y)
plt.show()

n_samples = X.shape[0]
n_features = X.shape[1]

w = np.random.uniform(0, 1, size=n_features)
b = np.random.uniform(0, 1, 1)

n_epoch = int(input("Enter number of epochs : "))
lr = 0.01

for e in range(n_epoch):
    for s in range(n_samples):
        net = np.dot(X[s, :], w)+b
        if net >= 0:
            a = 1
        else:
            a = 0
        error = Y[s]-a
        w = w+lr*error*X[s, :]
        b = b+lr*error

m = -w[0]/w[1]
c = -b/w[1]

def plot_decision_boundary(X):
    for x in np.linspace(np.min(X[:, 0]), np.max(X[:, 0])):
        y = m*x+c
        plt.plot(x, y, linestyle='-', color='k', marker='.')
        plt.scatter(X[:,0],X[:,1],c=Y)
        plt.show()


plot_decision_boundary(X)
>>>>>>> 3514783facb8b753c5c5fea915ca1d2a17a618fc
