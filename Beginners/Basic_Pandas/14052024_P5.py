# Pandas Exercises - 5

import pandas as pd

# Reads CSV

df = pd.read_csv("nba.csv", index_col='Name')

# Important to first make the desired column as Index (as shown above in read_csv method)

data_1 = df.loc[['Avery Bradley', 'Evan Turner']]

print(data_1)

# Works successfully until here
