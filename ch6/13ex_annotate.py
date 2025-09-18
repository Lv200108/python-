# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 09:38:40 2021

@author: wangh
"""
#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.annotate.html#matplotlib.pyplot.annotate

import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
plt.plot(t, s, lw=2)

plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5), 
             arrowprops=dict(arrowstyle = '->', color='r', linewidth = 1))

plt.ylim(-2, 2)
plt.show()