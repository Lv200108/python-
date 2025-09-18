# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 14:35:44 2021

@author: lenovo
"""

import matplotlib.pyplot as plt


labels = ['Class 1', 'Class 2', 'Class 3']
sizes = [30.521, 40.3, 50.536]
explode = [0.3, 0, 0] 
colors = ['r', 'g', 'b']

plt.pie(sizes, explode = explode, labels = labels, colors = colors, 
        autopct ='%4.1f%%', shadow = True, startangle = 60)
plt.show()
