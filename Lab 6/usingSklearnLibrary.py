import pandas as pd
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

data = pd.read_csv("Iris.csv", header='infer').values

x = data[:, 0:-1]
y = data[:, -1]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, stratify=y)
k = int(input("Enter the nearest neighbor number(k) : "))
model = KNeighborsClassifier(n_neighbors=k, weights="distance")
model.fit(x_train, y_train)
pred = model.predict(x_test)
accuracy = accuracy_score(y_test, pred)
print("Accuracy : ", accuracy)
print(classification_report(y_test, pred))
