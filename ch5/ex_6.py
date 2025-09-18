# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 21:08:54 2021

@author: wangh
"""

import pandas as pd

df1 = pd.DataFrame({'学号':[201801,201802,201803],
                    '姓名':['李明','王刚','赵四'],
                    '数学':[88,86,90]})

df2 = pd.DataFrame({'学号':[201801,201802,201803],
                    '姓名':['李明','王刚','赵四'],
                    '语文':[82,87,80]})

print(df1,'\n',df2,'\n')
df = pd.merge(df1, df2, on = ['学号','姓名'])
print('After merged:\n', df)