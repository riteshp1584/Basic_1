# Pandas Exercises - 10

import pandas as pd

# Reads CSV

df = pd.read_csv("nba.csv", index_col='Name')

# All rows, some columns

data_1 = df.iloc[:, [1, 5]]

print(data_1)

# Works successfully until here
