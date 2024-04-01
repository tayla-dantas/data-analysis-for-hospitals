#  write your code here 

import pandas as pd

df = pd.read_csv('./data/dataset/input.txt', index_col='Name')
print(df.head(10))