# -*- coding: utf-8 -*-  
import os
import zipfile
import os.path
strdir = './'

def getFileCate(fname):
    idx = fname.find('_')
    if idx<0:
        return False
    catIndex = fname[:idx]
    zipFileName = catIndex + ".zip"
    if os.path.exists(zipFileName):
        zipDest = zipfile.ZipFile(zipFileName, 'a')
    else:
        zipDest = zipfile.ZipFile(zipFileName, 'w')
    zipDest.write(fname) 
    print(idx)
# 获取指定路径下的所有文件，文件夹
for parent, dirnames, filenames in os.walk(strdir,  followlinks=True):
    print(parent)
    for filename in filenames:
      	getFileCate(filename)
        file_path = os.path.join(parent, filename)
        print(file_path)
    print('\n')

