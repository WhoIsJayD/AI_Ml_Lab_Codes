import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor

data = pd.read_csv("BostonHousing.csv", header='infer').values

x = data[:, 0:-1]
y = data[:, -1]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
k = int(input("Enter the nearest neighbor number(k) : "))

model = KNeighborsRegressor(n_neighbors=k, weights='distance')
model.fit(x_train, y_train)
pred = model.predict(x_test)
mae = mean_absolute_error(y_test, pred)
mse = mean_squared_error(y_test, pred)
print("Using Sklearn: ")
print("MAE: ", mae)
print("MSE: ", mse)
