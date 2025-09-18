# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 08:26:10 2021

@author: wangh
"""


import numpy as np 
from matplotlib import pyplot as plt 
 
x = np.arange(-5,5.1,0.5) 
y =  x ** 2 
plt.plot(x,y,'bo-.') 
plt.show()
