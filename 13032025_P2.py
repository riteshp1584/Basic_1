# Pandas Exercises (for ML Concepts)

import pandas as pd

url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/titanic.csv'

df = pd.read_csv(url)

df_1 = df[df['Sex'] == 'male'].head(10)   # first ten males

print(df_1)

df_2 = df[(df['Sex'] == 'male') & (df['Age'] > 60)]

print(df_2)

df_3 = df.sort_values(by=['Age']).head(10)
pd.set_option('display.max_columns', None)

print(df_3)
