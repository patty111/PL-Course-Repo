import pandas as pd

data1 = pd.read_csv("Data01.csv") # NBA history top 10 scorer
data2 = pd.read_csv("Data02.csv") # lebron's top 10

set1 = set(data1["PLAYER"])
set2 = set(data2["PLAYER"])


# top 10 scorer not in lebron's top 10
print(set1 - set2)

# in both lebron's top 10 and History top 10 scorer
print(set1 & set2)

# in either lebron's top 10 or History top 10 scorer
print(set1 | set2)

