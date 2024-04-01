#  write your code here 

import pandas as pd
df = pd.read_csv('./data/dataset/input.txt')
df.dropna(axis=1, thresh=7, inplace=True)
mode = df['price'].mode()[0] # calculate the mode
df['price'].fillna(mode, inplace=True) # replace NaNs with that mode
print(df.head())