import pandas as pd

names = ["A", "B", "C", "D","E"]
ages = [15,52,42,16,45]

data = {"Names":names , "Ages" : ages}

df = pd.DataFrame(data)

print(df.head())

#24.11