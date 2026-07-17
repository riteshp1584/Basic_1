# Pandas Exercises (for ML Concepts)

import pandas as pd
import numpy as np

url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/titanic.csv'

df = pd.read_csv(url)

df2 = df.groupby('Sex').value_counts()

print(df2)
