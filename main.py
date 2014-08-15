# -*- coding: utf-8 -*-
"""
Created on Fri Jul 11 19:16:56 2014

@author: npol
"""

import wx
import sys
import fileTree
from dirGUI import *
from lbrReader import *
from libGUI import *
from editGUI import *
import lbrLib
from wx.lib.pubsub import Publisher as pub

#Custom Menu ID's
ID_DIRECTORIES = wx.NewId()

class mainFrame(wx.Frame):
    def __init__(s, parent, title):
        wx.Frame.__init__(s, None, wx.ID_ANY, title=title)
        s.CreateStatusBar()
        
        filemenu = wx.Menu()
        filemenu.Append(wx.ID_ABOUT, '&About', 'Information about this program')
        filemenu.Append(wx.ID_EXIT, '&Exit', 'Terminate the program')
        
        settingsmenu = wx.Menu()
        settingsmenu.Append(ID_DIRECTORIES, '&Directories', 'Set Library Path Locations')
        
        s.menubar = wx.MenuBar()
        s.menubar.Append(filemenu, 'File')
        s.menubar.Append(settingsmenu, 'Settings')
        s.SetMenuBar(s.menubar)
        
        wx.EVT_MENU(s, ID_DIRECTORIES, s.startDirFrame)
        wx.EVT_MENU(s, wx.ID_EXIT, s.closeAll)
        
        pub.subscribe(s.onLibChanged, 'libChanged')
        
        s.filePanel = fileTree.filePanel(s)
        s.libPanel = libGUI(s)
        s.editPanel = editGUI(s)
        
        mainSizer = wx.BoxSizer(wx.HORIZONTAL)
        mainSizer.Add(s.filePanel,0,flag=wx.EXPAND)
        mainSizer.Add(s.libPanel,0,flag=wx.EXPAND)
        mainSizer.Add(s.editPanel,1,flag=wx.EXPAND)
        s.SetSizer(mainSizer)
        mainSizer.Fit(s)
        s.Layout()
        s.SetSize((1000,500))
        s.SetMinSize((600,400))
        
        s.Show(True)
    def startDirFrame(s, event):
        dirFrame = DirFrame()
        dirFrame.Show(True)
    def closeAll(s, event):
        lbrLib.dirFile.close()
        s.Destroy()
        sys.exit(0)
    def onLibChanged(s, message):
        global currLibFilename
        currLibFilename = message.data
        if(message.data == ''):#Clicked on directory
            s.menubar.EnableTop(2,False)
            pub.sendMessage('editChanged',('',0))
        else:
            s.menubar.EnableTop(2,True)
            pub.sendMessage('editChanged',('lbr',0))
        return
lbrLib.updatePaths()
app = wx.App(False)
frame = mainFrame(None, 'Eagle Library Manager')
app.MainLoop()
