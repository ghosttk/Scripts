#-*- coding:utf-8 -*-
import argparse
import requests
from lxml import etree

class Spider:
    def parseArgs(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-u', '--url', help='base url')
        parser.add_argument('-s', '--start', help='start endpoint')
        parser.add_argument('-e', '--end', help='end endpoint')
        parser.add_argument('-i', '--id', help='book id')
        args = parser.parse_args()
        self.baseUrl = args.url or 'http://www.sixqing.com'
        self.startPoint = args.start 
        self.endPoint = args.end
        self.bookId = args.id or '40399'
    def scrapById(self):
        self.bookUrl = self.baseUrl + '/' + self.bookId + '/'
        page=requests.get(self.bookUrl)
        html=page.text
        selector=etree.HTML(html)
        content=selector.xpath('//a[@class="a1"]/@href')
        if content:
            self.startUrl = self.baseUrl + content[0]
            return self.startUrl
    def nextChapter(self, url):
        page=requests.get(url)
        html=page.text
        selector=etree.HTML(html)
        content = selector.xpath('//div[@id="chaptercontent"]/p/text()')
        if content:
            if url != self.bookUrl:
                f = open(self.bookId + '.txt', 'a', encoding='utf-8')
                chapterId = url.split('/')[-1]
                f.write(chapterId + '\n')
            for c in content:
                f = open(self.bookId + '.txt', 'a', encoding='utf-8')
                f.write(c)
                f.close()
        nextUrl =selector.xpath('//a[@class="a4"]/@href')
        if nextUrl and nextUrl !=self.bookUrl:
            nextUrl = self.baseUrl + nextUrl[0] 
            self.nextChapter(nextUrl)
        return 
    def __init__(self):
        self.parseArgs()

if __name__ == '__main__':
    spider = Spider()
    if spider.bookId:
        url = spider.scrapById()
        spider.nextChapter(url)
