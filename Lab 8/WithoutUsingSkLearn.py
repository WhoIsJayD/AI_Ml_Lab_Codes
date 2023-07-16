import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from tabulate import tabulate


def makeTable(k, n):
    data = pd.read_csv("Iris.csv", header='infer').values

    x = data[:, 1:-1]
    y = data[:, -1]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
    centroids = np.zeros(shape=(k, x_train.shape[1]))
    per = np.random.permutation(x_train.shape[0])
    for i in range(k):
        centroids[i, :] = x_train[per[i], :]
    for it in range(n):
        dist = np.zeros(shape=(k, x_train.shape[0]))
        for i in range(k):
            dist[i, :] = np.sqrt(np.sum((x_train - centroids[i, :]) ** 2, axis=1))
        membership = np.argmin(dist, axis=0)
        for i in range(k):
            centroids[i, :] = np.mean(x_train[membership == i, :], axis=0)
    dist = np.zeros(shape=(k, x_test.shape[0]))
    for i in range(k):
        dist[i] = np.sqrt(np.sum((x_test - centroids[i]) ** 2, axis=1))
    membership = np.argmin(dist, axis=0)
    return [centroids.tolist(), f"Y_Test=      {y_test.astype(int).tolist()}\nMembership=  {membership.tolist()}\n."]


k = int(input("Enter the nearest neighbor number(k) : "))
n = int(input("Enter the number of iterations :"))
display = {}
for i in range(1, k + 1):
    ans = makeTable(i, n)
    display[i] = ans
tabulated_data = tabulate(pd.DataFrame(display).T, tablefmt="pretty", headers=["Centroids", "Comparison"])
print(tabulated_data)