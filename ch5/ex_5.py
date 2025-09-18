# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 20:52:40 2021

@author: wangh
"""

import pandas as pd

df = pd.DataFrame({'学号':[201801,201802,201803,201804],
                   '班级':['A','B','A','C'],
                   '成绩':[88,86,90,82]
        })

grp = df.groupby('班级')

print(dir(grp))

for name,group in grp:
    print(name)
    print(group)
