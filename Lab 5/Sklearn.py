import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv("BostonHousing.csv", header='infer').values

x = data[:, 0:-1]
y = data[:, -1]
n_rows = data.shape[0]
print("Total Rows:", n_rows)
test_split = float(input("Enter a value split in terms of % : "))
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_split / 100)
print("Shapes:", x_train.shape, y_train.shape, x_test.shape, y_test.shape)