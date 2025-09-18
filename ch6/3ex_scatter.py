# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 15:02:28 2021

@author: lenovo
"""

# -*- coding: utf-8 -*- 
import numpy as np
import matplotlib.pyplot as plt
 

x = np.random.normal(2,1.2,300) 
y = np.random.normal(2,1.2,300) 
 
color = '#1CCED1' #点的颜色
area = np.pi * 4 * 4  # 点面积 
plt.scatter(x, y, s = area, c = color, alpha = 0.8, label = 'Class A')
plt.savefig('scatter.png', dpi=300)
plt.show()
