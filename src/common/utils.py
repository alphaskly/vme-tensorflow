import re
import os

def listFiles(path, allFile):
    dirs = os.listdir(path)
    for fileName in dirs:
        filePath = os.path.join(path, fileName)
        if os.path.isdir(filePath):
            listFiles(filePath, allFile)
        else:
            allFile.append(filePath)

def execCmd(cmd):
    m = os.popen('ipconfig','r')
    for line in m:
        print (re.findall(r'', line.rstrip()))
    m.close()

f = open('E:\workspace_c++\CodeWriter.cpp', 'r')
for line in f:
    print (re.split(R'\s\s+', line))
f.close()