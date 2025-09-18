# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 11:15:39 2021

@author: wangh
"""

import numpy as np
import matplotlib.pyplot as plt

font = {'family':'SimHei',
     'style':'italic',
    'weight':'normal',
      'color':'blue',
      'size':18
}

x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
y = np.sin(x)

plt.plot(x, y, label = 'y = sin(x)')  
plt.title('正弦曲线',  fontdict = font)  

