# Pandas Exercises - 3

import pandas as pd

# Reads CSV

df = pd.read_csv("nba.csv")

# Prints only specific column 'Name' in this case

print(df['Name'])

print(df)
