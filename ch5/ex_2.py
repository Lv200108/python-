# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 13:55:46 2021

@author: lenovo
"""
#https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://news.baidu.com'
data = requests.get(url)
soup = BeautifulSoup(data.content, 'html.parser', from_encoding = 'utf-8')

print('头条热点新闻')
firtHotnews = soup.select('strong')
for i in range(0,5):
   print(firtHotnews[i].get_text())
   
newsPD = pd.DataFrame(columns=['name','url'])   
for i in range(1,31):
   news = soup.find('a', mon = "ct=1&a=2&c=top&pn=" + str(i))   
   newsPD = newsPD.append([{'name':news.get_text(), 'url':news.get('href')},], ignore_index=True)
print('热点新闻')
print(newsPD)

writer = pd.ExcelWriter('news.xlsx')
newsPD.to_excel(writer, 'Sheet1')
writer.save()
writer.close() 




   

