# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 10:46:50 2021

@author: lenovo
"""

from scipy import stats
import matplotlib.pyplot as plt

#正态分布
x = stats.norm.rvs(loc = 0, scale = 1.0, size = 10000)
plt.hist(x, bins = 100)
plt.show()

#均匀分布
x = stats.uniform.rvs(loc = 0, scale = 1.0, size = 10000)
plt.hist(x, bins = 100)
plt.show()