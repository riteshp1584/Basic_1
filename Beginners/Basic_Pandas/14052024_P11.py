# Pandas Exercises - 10

import pandas as pd

df = pd.DataFrame({'A':[12, 4, 5, 44, 50],
                  'B':[5, 2, 54, 3, 2],
                  'C':[20, 16, 7, 3, 8],
                  'D':[14, 3, 17, 2, 6]})

print(df)

# Gets average along the horizontal axis

df2 = df.mean(axis=0)

print(df2)

# Gets average along the vertical axis

df3 = df.mean(axis=1)

print(df3)
