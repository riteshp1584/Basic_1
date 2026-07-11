# Pandas Exercises - 7

import pandas as pd

# Reads CSV

df = pd.read_csv("nba.csv")

# Gives info for one single row

data_1 = df.iloc[5]

print(data_1)

# Gives info for multiple rows

# data_2 = df.iloc[[1, 2, 3, 4]]

# print(data_2)

# Gives info for multiple rows

data_3 = df.iloc[5:10]

print(data_3)

# Works successfully until here
