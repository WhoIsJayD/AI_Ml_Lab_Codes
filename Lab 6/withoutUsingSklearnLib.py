import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv("Iris.csv", header='infer').values

x = data[:, 0:-1]
y = data[:, -1]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, stratify=y)
nClasses = np.unique(y_train).shape[0]
distance = np.zeros(shape=x_train.shape[0])
pred = np.zeros(shape=x_test.shape[0])
classVotes = np.zeros(shape=nClasses)

k = int(input("Enter the nearest neighbor number(k) : "))
for i in range(x_test.shape[0]):
    distance = np.sqrt(np.sum((x_train - x_test[i]) ** 2, axis=1))
    kMinIndex = np.argpartition(distance, k)[0:k]
    invDist = 1 / (distance + 10e-20)
    Denom = sum(invDist[kMinIndex])
    for j in range(k):
        classVotes[int(y_train[kMinIndex[j]])] += invDist[kMinIndex[j]]
    classVotes /= Denom
    pred[i] = np.argmax(classVotes)

print(f"""
1. Pred : {pred}\n
2. Class Votes : {classVotes}\n
3. nClasses :{nClasses}\n
5. Distance : {distance}\n
6. Classification : C{classVotes.tolist().index(max(classVotes.tolist()))}
""")
