import pandas as pd

csv = pd.read_csv("train.csv")
csv["Cabin"].fillna(csv["Cabin"].mode()[0], inplace=True)
csv["Age"].fillna(csv["Age"].mean().round().astype(int), inplace=True)
csv["Embarked"].fillna(csv["Embarked"].mode()[0], inplace=True)
csv.to_csv('train_complete.csv', index=False)
print(csv)
