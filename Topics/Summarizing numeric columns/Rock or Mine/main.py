#  write your code here 
import pandas as pd
df_rock = pd.read_csv('./data/dataset/input.txt')


r = df_rock.loc[df_rock.labels == 'R', :]
m = df_rock.loc[df_rock.labels == 'M', :]

print("M = " + str(round(m.null_deg.median(), 3)) + " R = " + str(round(r.null_deg.median(), 3)))
