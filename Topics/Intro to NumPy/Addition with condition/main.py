import numpy as np

def custom_sum(arg1, arg2):

    if(isinstance(arg1, list) and isinstance(arg2, list)):
        return 'Both arguments are lists, not arrays'
    elif(isinstance(arg1, list) or isinstance(arg2, list)):
        return 'One argument is a list'
    else:
        arg1 = np.array(arg1)
        arg2 = np.array(arg2)
        return arg1 + arg2