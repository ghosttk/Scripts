# -*- coding: utf-8 -*-  
import urllib.request
import sys
from html.parser import HTMLParser

class MyParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.in_div = False
    def _attr(self, attrlist, attrname):
        for attr in attrlist:
            if attr[0] == attrname:
                return attr[1]
        return None
    def handle_starttag(self, tag, attrs):
        if tag == 'div' and self._attr(attrs, 'class') == 'article-text':
            self.in_div = True
    def handle_data(self, data):
        if self.in_div == True :
            print("Encountered data  :")
            with open('test.txt', 'w', encoding='utf-8') as wf:
                wf.write(str(data))
            #self.in_div = False 

def scrap(baseurl='http://xiaohua.zol.com.cn/detail5/', iStart=59391, iEnd=59392):
    url = baseurl+str(iStart)+'.html'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}  
    req = urllib.request.Request(url, headers=headers)
    f = urllib.request.urlopen(req)
    uf = f.read().decode('gbk')
    parser = MyParser()
    #parser.feed(str(uf))
    parser.feed(uf)

if __name__ == '__main__':
    if len(sys.argv) == 3:
        scrap(sys.argv[1] or None, sys.argv[2] or None)
    else:
        scrap()
