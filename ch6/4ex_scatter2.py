# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 17:40:03 2021

@author: wangh
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 08:26:10 2021

@author: wangh
"""


import numpy as np 
from matplotlib import pyplot as plt 
import matplotlib as mpl
 
x = np.random.rand(88)
y = np.random.rand(88)
plt.scatter(x, y, s = 100 * x ** 2 + 300 * y ** 2, c = np.random.rand(88), 
            cmap = mpl.cm.RdYlBu, marker = "o")
plt.show()
