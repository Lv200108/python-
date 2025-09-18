# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 19:19:47 2021

@author: wangh
"""

import pandas as pd

df = pd.read_excel('repeated.xlsx')
print('导入的excel表为：')
print(df,'\n')

print('判断整行是否重复：')
flag1 = df.duplicated()
print(flag1,'\n')

print('判断一行的子集是否重复：')
flag2 = df.duplicated(subset = (['No', 'Name']))
print(flag2,'\n')

print('去掉重复行：')
df1 = df;
df1.drop_duplicates(subset = None, keep = 'first', inplace = True)
print(df1, '\n')

print('去掉重复行的子集：')
df2 = df;
df3 = df2.drop_duplicates(subset = ['No'], keep = 'first', inplace = False)
print(df3, '\n')

print(df2)