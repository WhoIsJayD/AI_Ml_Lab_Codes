import random
import numpy as np
import pandas as pd
df = pd.read_csv("BostonHousing.csv", header="infer").values.tolist()
df2 = []
value_split = int(input("Enter the split value in terms of % :"))
indexes=[]
for i in range(int(len(df) * (value_split / 100))):
    rand_value = random.choice(df)
    indexes.append(df.index(rand_value))
    df.remove(rand_value)
    df2.append(rand_value)
df = np.array(df)
df2 = np.array(df2)
print(df)
print("Shape : ", df.shape)
print("----" * 20)
print(df2)
print("Shape :", df2.shape)
print("----" * 20)
print(indexes)
