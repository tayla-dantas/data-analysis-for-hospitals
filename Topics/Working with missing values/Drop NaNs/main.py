#  write your code here 

import pandas as pd
df = pd.read_csv('./data/dataset/input.txt')
print("{0} {1}".format(len(df),len(df.dropna(axis=0))))

