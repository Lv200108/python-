# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 09:20:17 2021

@author: lenovo
"""
import requests
import requests_html
from requests_html import HTMLSession
import json

#参数说明：
#className：爬取图片的检索词
#numberOfPage: 下载图片的页数，每页48张图片，共下载48 * numberOfPage张图片
#imagePath: 下载图片保存的位置 
def sogouImage(className, numberOfPage, imagePath):
    numberOfImage = 1;
    for i in range(0,numberOfPage):
        images = requests.get('https://pic.sogou.com/napi/pc/searchList?mode=1&start=' + str(i) + '&xml_len=48&query=' + className)
        jdData = json.loads(images.text)
       
        seesion = HTMLSession()
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}  
        data = jdData['data']['items']
        for image in data:
            picUrl = image['picUrl']
            imageData = seesion.get(picUrl, headers = headers).content
            with open(imagePath + str(numberOfImage) + '.jpg', 'wb') as f:
                f.write(imageData)
            print('下载第', numberOfImage, '张图片.')
            numberOfImage = numberOfImage + 1
   
    print('下载完成!')
 
sogouImage('狗',10,'D:/image/')