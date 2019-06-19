import argparse
import lxml
import requests

class Spider:
    def parseArgs(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-u', '--url', help='base url')
        parser.add_argument('-s', '--start', help='start endpoint')
        parser.add_argument('-e', '--end', help='end endpoint')
        args = parser.parse_args()
        self.baseUrl = args.url
        self.startPoint = args.start
        self.endPoint = args.end
    def __init__(self):
        self.parseArgs()

if __name__ == '__main__':
    spider = Spider()
    if spider.endPoint :
        print(spider.endPoint)


