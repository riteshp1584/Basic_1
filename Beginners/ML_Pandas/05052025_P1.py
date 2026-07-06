# To learn Pandas specifically for ML Projects

import pandas as pd

dataframe = pd.DataFrame({"Score" : ["Low",
                                     "Low",
                                     "Medium",
                                     "Medium",
                                     "High",
                                     "Barely More Than Medium"]})

scale_mapper = {"Low" : 1,
                "Medium" : 2,
                "Barely More Than Medium" : 3,
                "High" : 4}

dataframe2 = dataframe["Score"].replace(scale_mapper)

print(dataframe)

print(dataframe2)
