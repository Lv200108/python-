# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 13:55:46 2021

@author: lenovo
"""
#https://requests.readthedocs.io/en/master/

import requests

url = 'https://www.baidu.com'
data = requests.get(url)


print(data.status_code)
print(data.encoding)
print(data.content.decode('utf-8'))
