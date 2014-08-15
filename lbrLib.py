import os.path
from wx.lib.pubsub import Publisher as pub

currLibFilename = ''
filePaths = []

def updatePaths():
    global filePaths
    global dirFile
    filePaths = []
    if(not os.path.isfile('directories.txt')):
        dirFile = open('directories.txt', 'w')
        dirFile.close()
    dirFile = open('directories.txt', 'r+')
    rawList = dirFile.readlines()
    for i in range(0,len(rawList)):
        rawList[i] = rawList[i].rstrip('\n')
    filePaths = rawList
    pub.sendMessage('updatePaths')
    return
