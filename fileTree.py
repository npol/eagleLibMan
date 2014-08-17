# -*- coding: utf-8 -*-
"""
Created on Fri Jul 11 22:20:38 2014

@author: npol
"""

import wx
from wx.lib.pubsub import Publisher as pub
import glob
import os
import lbrLib

class filePanel(wx.Panel):
    def __init__(s, parent):
        wx.Panel.__init__(s, parent, style=wx.RAISED_BORDER)
        s.files = fileTree(s)
        """
        fileSizer = wx.BoxSizer(wx.VERTICAL)
        fileSizer.Add(s.files, proportion=1,flag=wx.EXPAND)
        """
        fileSizer = wx.GridSizer(rows=0,cols=1)
        fileSizer.Add(s.files,flag=wx.EXPAND)
        s.SetSizerAndFit(fileSizer)
        s.Layout()


class fileTree(wx.TreeCtrl):
    def __init__(s, parent):
        global filePaths
        wx.TreeCtrl.__init__(s, parent, size=(200,-1), style=wx.TR_DEFAULT_STYLE|wx.TR_HIDE_ROOT)
        
        s.Bind(wx.EVT_TREE_ITEM_ACTIVATED, s.onLibChanged)
        
        pub.subscribe(s.updateTree, 'newFilePaths')
        print lbrLib.filePaths
        s.root = s.AddRoot('Root')#Hidden
        s.updateTree('')

    #Find .lbr files in given directory
    def searchDir(s, directory, fileExt):
        path = os.path.join(directory, fileExt)
        return glob.glob(path)
    #External request to update tree with current filepaths
    def updateTree(s, message):
        print 'Recieved request to update tree'
        print lbrLib.filePaths
        s.DeleteChildren(s.root)
        for dir in lbrLib.filePaths:
            dirNode = s.AppendItem(s.root, dir)
            files = s.searchDir(dir, '*.lbr')
            for lib in files:
                s.AppendItem(dirNode, os.path.split(lib)[1])
        return
    #User clicks on file or directory in tree
    def onLibChanged(s, event):
        global currLibFilename
        selItem = s.GetSelection()
        selName = s.GetItemText(selItem)
        #If not a lbr file, expand and select first child
        if(s.ItemHasChildren(selItem)):
            if(not s.IsExpanded(selItem)):
                s.Expand(selItem)
            s.UnselectAll()
            pub.sendMessage('libChanged','')
            return
        #If selected a lbr file, Send message to update all library-specific items
        if(selName[-4:] != '.lbr'):
            s.UnselectAll()
            pub.sendMessage('libChanged','')
            return
        currLibFilename = selName
        dirName = s.GetItemText(s.GetItemParent(selItem))
        pub.sendMessage('libChanged', os.path.join(dirName,currLibFilename))
        return
        
