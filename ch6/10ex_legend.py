# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 08:29:04 2021

@author: wangh
"""
#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-2,2.1,0.1) 
y1 = x ** 2
y2 = x **3 
plt.plot(x,y1,"-b",label = r"$y=x^{2}$")
plt.plot(x,y2,"-r",label = r"$y=x^{3}$")
plt.legend(loc = 'lower left', bbox_to_anchor=(0.3, 0.6), 
           fontsize = "large", title = "power functions")
plt.show()