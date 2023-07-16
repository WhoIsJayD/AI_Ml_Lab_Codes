import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from tabulate import tabulate


def MAE(pred, y_test):
    return np.mean(abs(pred - y_test))


def MSE(pred, y_test):
    return np.mean((pred - y_test) ** 2)


def RMSE(mse):
    return np.sqrt(mse)


def MAPE(pred, y_test):
    return np.mean(abs(pred - y_test) / y_test)


def KNNRegressor(k):
    data = pd.read_csv("BostonHousing.csv", header='infer').values

    x = data[:, 0:-1]
    y = data[:, -1]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
    nClasses = np.unique(y_train).shape[0]
    distance = np.zeros(shape=x_train.shape[0])
    pred = np.zeros(shape=x_test.shape[0])

    # k = int(input("Enter the nearest neighbor number(k) : "))
    for i in range(x_test.shape[0]):
        distance = np.sqrt(np.sum((x_train - x_test[i]) ** 2, axis=1))
        kMinIndex = np.argpartition(distance, k)[0:k]
        invDist = 1 / (distance + 10e-20)
        Denom = sum(invDist[kMinIndex])
        pred[i] = np.dot(invDist[kMinIndex] / Denom, y_train[kMinIndex])
    return [MAE(pred, y_test), MSE(pred, y_test), RMSE(MSE(pred, y_test)), MAPE(pred, y_test)]


display = {}
n = int(input("Enter the number of 'k' till which you have to compare: "))
for i in range(1, n+1):
    ans = KNNRegressor(i)
    display[i] = ans

print(tabulate(pd.DataFrame(display).T, tablefmt="pretty", headers=["MAE", "MSE", "RMSE", "MAPE"]))
