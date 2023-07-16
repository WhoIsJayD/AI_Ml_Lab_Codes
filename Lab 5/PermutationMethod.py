import math
import numpy as np
import pandas as pd
data = pd.read_csv("BostonHousing.csv", header='infer').values

x = data[:, 0:-1]
y = data[:, -1]
n_rows = data.shape[0]
print("Total Rows:", n_rows)

test_split = float(input("Enter a number between 0 and 1 to specify the test split:"))
n_rows_train = math.floor((1 - test_split) * n_rows)
all_indices = np.random.permutation(n_rows)
x_train = x[all_indices[0:n_rows_train], :]
y_train = y[all_indices[0:n_rows_train]]
x_test = x[all_indices[n_rows_train:], :]
y_test = y[all_indices[n_rows_train:]]

print("Shapes:", x_train.shape, y_train.shape, x_test.shape, y_test.shape)
