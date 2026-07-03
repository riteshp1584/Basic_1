# Pandas Exercises - 9

import pandas as pd

# Reads CSV

df = pd.read_csv("nba.csv")

# Get all rows, and some columns

data_1 = df.loc[:, ['Name', 'Age', 'College']]

# print(data_1)

# Make index as 'Name'

df2 = pd.read_csv('nba.csv', index_col='Name')

# Use slice operation, all names and some columns

data_2 = df2.loc[:, ['Team', 'Position', 'Weight']]

print(data_2)

# Works successfully until here
