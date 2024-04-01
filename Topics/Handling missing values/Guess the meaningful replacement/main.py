#  write your code here 

import pandas as pd
df = pd.read_csv('./data/dataset/input.txt')

df['totsp'] = df.apply(lambda row: row['livingsp'] + row['nonlivingsp'], axis=1)

print(int(df.loc[:, 'totsp'].sum()))