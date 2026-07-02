# Pandas Exercises - 8

import pandas as pd

# Reads CSV

df = pd.read_csv("nba.csv", index_col='Name')

# Lists all columns available in the df

data_1 = df.columns

print (data_1)

# Lists all columns available in the df using for loop

for col in df:
    print(col)

df2 = df[['Age', 'College', 'Salary']]

# Took index_col as 'Name' to list names in .loc method

df3 = df2.loc[['Avery Bradley', 'R.J. Hunter']]

print(df3)

# Works successfully until here
