import pandas as pd

data1 = pd.read_csv("Data01.csv")
data2 = pd.read_csv("Data02.csv")

set1 = set(data1["PLAYER"])
set2 = set(data2["PLAYER"])

print(set1 - set2)

print(set1 & set2)

print(set1 | set2)

