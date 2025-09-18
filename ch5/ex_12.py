# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 10:51:21 2021

@author: lenovo
"""

#计算P值，若P<0.05（显著性水平a），拒绝原假设，否则不拒绝原假设

from scipy import stats
import matplotlib.pyplot as plt

#正态分布
x = stats.norm.rvs(loc = 0, scale = 1.0, size = 100000)
print(stats.kstest(x,'norm'))
print(stats.kstest(x,'uniform'))

print('\n')

x = stats.uniform.rvs(loc = 0, scale = 1.0, size = 100000)
print(stats.kstest(x,'norm'))
print(stats.kstest(x,'uniform'))