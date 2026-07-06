# Usage of Dataframe features

# Example 2

import pandas as pd

# Read the Excel File

df = pd.read_excel("E:\DRIVE (Just Like Another Drive)\Contain\RD_1.xlsx")

# Outputs DataFrame

print(df)

# Removes rows containing all NaNs

df2 = df.dropna(how='all')

print(df2)

# Works successfully until here
