#  write your code here

import pandas as pd
df = pd.read_csv('./data/dataset/input.txt')
#df.fillna(0, inplace=True)
mode = df['location'].mode()[0] # calculate the mode
df['location'].fillna(mode, inplace=True) # replace NaNs with that mode
print(df.head())