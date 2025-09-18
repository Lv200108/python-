# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 17:32:35 2021

@author: lenovo
"""

import numpy as np

x = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(x)

#All number
print('Max:', np.max(x))
print('Min:', np.min(x))
print('Mean:', np.mean(x))
print('Variance:', np.var(x))
print('Sum:', np.sum(x))
print('Product:', np.prod(x))
print('Median:', np.median(x))
print('Percentile:', np.percentile(x,45),'\n')


#Each column
print('Max:', np.max(x, axis = 0))
print('Min:', np.min(x, axis = 0))
print('Mean:', np.mean(x, axis = 0))
print('Variance:', np.var(x, axis = 0))
print('Sum:', np.sum(x, axis = 0))
print('Product:', np.prod(x, axis = 0))
print('Median:', np.median(x, axis = 0))
print('Percentile:', np.percentile(x,45, axis = 0),'\n')

#Each row
print('Max:', np.max(x, axis = 1))
print('Min:', np.min(x, axis = 1))
print('Mean:', np.mean(x, axis = 1))
print('Variance:', np.var(x, axis = 1))
print('Sum:', np.sum(x, axis = 1))
print('Product:', np.prod(x, axis = 1))
print('Median:', np.median(x, axis = 1))
print('Percentile:', np.percentile(x,45, axis = 1),'\n')