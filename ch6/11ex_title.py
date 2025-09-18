# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 07:54:44 2021

@author: wangh
"""
#https://blog.csdn.net/TeFuirnever/article/details/88945563

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-5,5.1,0.1) 
y =  x ** 3 
plt.plot(x,y,"-b")
plt.title(r"$y=x^{3}$", rotation = 0, fontstyle = 'italic', fontweight = 'light') 
plt.show()