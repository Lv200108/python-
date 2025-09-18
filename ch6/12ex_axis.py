# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 09:04:14 2021

@author: wangh
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-5,5.1,0.1) 
y =  x ** 3 
plt.plot(x,y,"-b")

plt.xlabel('x axis')
plt.ylabel('y axis')

plt.xlim([-6,6])
plt.ylim([-130,130])

plt.xticks(np.arange(-6, 6.1, 1.5))
plt.yticks(np.arange(-130, 130.1, 15))

plt.show()