import pandas as pd

names = ["A", "B", "C", "D","C"]
ages = [15,52,42,16,45]
group = ["G1", "G1", "G2", "G3", "G1"]

data = {"Names":names , "Ages" : ages, "groups" : group}

df = pd.DataFrame(data)

print(df.head())
