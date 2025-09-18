# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 21:05:58 2021

@author: wangh
"""

import matplotlib.pyplot as plt
import numpy as np

numberOfPoints = 16

theta = np.linspace(0.0, 2*np.pi, numberOfPoints)
r = 30 * np.random.rand(numberOfPoints)
plt.polar(theta, r, linewidth = 1, c = 'g', marker = "o", mfc = "b", ms = 12)
plt.show()