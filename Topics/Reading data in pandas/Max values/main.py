#  write your code here 

#  write your code here
import pandas as pd

df = pd.read_csv('./data/dataset/input.txt')
print(df.describe().loc['max', 'Age'])
