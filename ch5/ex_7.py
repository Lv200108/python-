# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 21:39:21 2021

@author: wangh
"""

import pandas as pd

df1 = pd.DataFrame({'学号':[201801,201802],
                    '姓名':['李明','王刚'],
                    '数学':[88,86]})

df2 = pd.DataFrame({'学号':[201803],
                    '姓名':['赵四'],
                    '数学':[80]})

print(df1, '\n\n', df2, '\n')
df = pd.concat([df1,df2])
print(df)