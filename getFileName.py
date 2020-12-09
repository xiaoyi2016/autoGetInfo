#-*- coding：utf-8 -*-

#################################
# purpose: 把某个目录下的文件的名字
#  读取出来，存到excel表格中
# author: wan jie
# place: shanghai
#
#################################

import sys
import time
import os
import pandas as pd

TITLE_BASE_DT = '文件名字'
# 路径深度为2
PATH_DEPTH    = 3

def help():
        print('参数错误，请输入目录名称')

def saveFileName(outFile):
    dic = {
            TITLE_BASE_DT: ['1'],
           }

    df = pd.DataFrame(dic)
    df.to_csv(outFile,index=False,mode='a',header=0)

def getFileName(path,outlist,pathLevel):
    if pathLevel >= PATH_DEPTH:
        return
    pathLevel = pathLevel + 1
    filelist = os.listdir(path)
    for index in range(1, len(filelist)):
        (path, filename) = os.path.split(filelist[index])
        if 0 != len(filename):
            fname,ext = os.path.splitext(filename)
            if 0 != len(ext):
                if ext == '.exe':
                  outlist.extend(filename)
                  print(filename)


def process():
        if len(sys.argv) >= 2:
                inputPath = sys.argv[1]
                print(inputPath)
        else:
                help()

        currentTime = time.time()
        timeLocal = time.localtime(currentTime)
        dttime = time.strftime("%Y-%m-%d-%H-%M-%S", timeLocal)

        (path, filename) = os.path.split(inputPath)

        outFile = path + dttime + '.csv'

        filelist = os.listdir(path)
        filenames = []
        pathLevel = 0

        while pathLevel < PATH_DEPTH:
            for index in range(1,len(filelist)):
                subPath = inputPath + '\\' + filelist[index]
                getFileName(subPath,filenames)
                print(subPath)
                filelist = os.listdir(subPath)
            pathLevel = pathLevel + 1


        saveFileName(outFile)


if __name__ == '__main__':
        print('获取目录下的文件名')
        process()