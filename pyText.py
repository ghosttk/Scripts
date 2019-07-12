
import sys 
import re

def parseText():
    with open(sys.argv[1], 'r') as f:
        for line, value in enumerate(f):
            match = re.match('\d', value)
            if match != None:
                print('\t'+value)
                with open('result.txt', 'a') as result:
                    result.write(value)

if __name__ == '__main__':
    parseText()
