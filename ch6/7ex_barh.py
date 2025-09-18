# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 15:25:07 2021

@author: lenovo
"""

import matplotlib.pyplot as plt

country = ['USA', 'China', 'Japan', 'Germany', 'UK'] 
GDP = [209328, 147228, 50487, 38030, 27110]
plt.barh(country, GDP)
