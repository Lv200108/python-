# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 17:53:41 2021

@author: wangh
"""

import pandas as pd

df = pd.read_excel('null.xlsx')
print('导入的excel表为：\n', df, '\n')


print('判断每个元素是否为空值：\n', df.isnull(), '\n')
print('判断每一列是否含有空值：\n', df.isnull().any(), '\n')

df1 = df.dropna()
print('将有空值的行去掉：\n', df1, '\n')

#df3 = df
#df3['Col3'] = df['Col3'].fillna(0)
#print('将Col3中的空缺值填充为0：\n', df3)

df3 = df
df3 = df.fillna(0)
print('将Col3中的空缺值填充为0：\n', df3)
