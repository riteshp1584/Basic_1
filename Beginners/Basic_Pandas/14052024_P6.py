# Pandas Exercises - 6

import pandas as pd

# Reads CSV

df = pd.read_csv("nba.csv", index_col='Team')

# Important to first make the desired column as Index (as shown above in read_csv method)

data_1 = df.loc[['Boston Celtics', 'Utah Jazz']]

print(data_1)

# Works successfully until here
