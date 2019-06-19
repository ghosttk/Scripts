#-*- coding:utf-8 -*-
import os,sys
import requests
from lxml import etree

baseurl=sys.argv[1]
#baseurl='http://www.yiiframework.com/doc-2.0/'
clsName=sys.argv[2]
#clsName="list-group-item"
url=baseurl+'guide-index.html'
page=requests.get(url)
html=page.text
selector=etree.HTML(html)

content=selector.xpath('//a[@class="list-group-item"]/@href')
for c in content:
    if c[0]=='.':
        nav=c[2:]
        url=baseurl+nav
    elif c[0:4]=='http':
        nav=c.split('\/')[:-1]
        url=c
    else:
        nav=0
    if nav:        
        fname="./yii/"+nav
        if os.path.exists(fname):
            print('%s exists'%hfile)
            continue
        hfile=open('./yii/'+nav,'w')
        print('downloading %s\n'%hfile)
        page=requests.get(url)
        html=page.text
        hfile.write(html)
