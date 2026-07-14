# Pandas Exercises - 4

import pandas as pd

# Reads CSV

df = pd.read_csv("nba.csv")

# Prints specified columns only

columns_to_display = ['Name', 'Team', 'Salary']

df2 = df[columns_to_display]

# Alternatively,

df2 = df[['Name', 'Team', 'Salary']]   # This is also possible - gives the same result

print(df2)

# Works successfully until here
