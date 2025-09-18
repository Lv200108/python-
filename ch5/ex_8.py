# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 19:19:47 2021

@author: wangh
"""

import pandas as pd

df = pd.read_excel('string1.xlsx')
print('导入的excel表为：')
print(df,'\n')

#小写
df1 = df;
df1['Name'] = df1['Name'].map(str.lower)
print(df1,'\n')

#大写
df2 = df;
df2['Name'] = df2['Name'].map(str.upper)
print(df2,'\n')

#首字母大写
df2 = df;
df2['Name'] = df2['Name'].map(str.title)
print(df2)