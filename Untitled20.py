
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
df = pd.DataFrame({'X':[7,2,0,3,4,2,5,0,3,4]})
# printing the given data
print(df)
print('_________________')
t = (df['X']!=0).cumsum() #performing cumulative sum if X != 0
x = t != t.shift() #shift column by one
df['Y'] = x.groupby((x != x.shift()).cumsum()).cumsum()
print(df)

