# -*- coding: utf-8 -*-  
import urllib.request
import re
import sys
import xml.etree.ElementTree as ET

def scrap(baseurl='http://xiaohua.zol.com.cn/detail5/', iStart=1, iEnd=1):
    url = baseurl+str(iStart)+'.html'
    f = urllib.request.urlopen(url)
    uf = f.read().decode('gbk')
    with open('test.txt', 'w', encoding='utf-8') as opf:
        opf.write(str(uf))
    '''
    uf = re.sub(u"[\x00-\x08\x0b-\x0c\x0e-\x1f]+",u"", uf)

    root = ET.parse('test.txt')
    article = root.find('//div[@class="article-text"]')
    print(article)
    with open(str(iEnd)+'.txt', 'a', encoding='gbk') as of:
        of.write(uf)
        '''
    print(str(uf))

if __name__ == '__main__':
    scrap(sys.argv[1], sys.argv[2])
