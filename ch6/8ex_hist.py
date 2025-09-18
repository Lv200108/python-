# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 08:20:33 2021

@author: wangh
"""


from matplotlib import pyplot as plt 
import numpy as np  
 
a = np.array([1,2,3,4,5,12,13,14,15,19]) 
plt.hist(a, bins =  [0,3,12,15,20]) 
plt.title("histogram") 
plt.show()
