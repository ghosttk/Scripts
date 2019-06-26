# -*- coding: utf-8 -*-  
import urllib
import sys
import xml.etree.ElementTree

def scrap(baseurl='http://xiaohua.zol.com.cn/detail5/', iStart=1, iEnd=1):
    url = baseurl+str(iStart)+'.html'
    f = urllib.urlopen(url)
    uf = f.read().decode('gbk')
    '''
    with open(str(iEnd)+'.txt', 'a', encoding='gbk') as of:
        of.write(uf)
    '''
    print(uf)

if __name__ == '__main__':
    scrap(sys.argv[1], sys.argv[2])
