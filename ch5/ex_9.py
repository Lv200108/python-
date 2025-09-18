# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 19:19:47 2021

@author: wangh
"""

import pandas as pd

df = pd.read_excel('string2.xlsx')
print('导入的excel表为：')
print(df,'\n')

#
df1 = df;
df1['Name'] = df1['Name'].map(str.strip)
print(df1,'\n')
