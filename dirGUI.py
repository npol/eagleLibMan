import wx
from wx.lib.pubsub import Publisher as pub
import os
import lbrLib

class DirFrame(wx.Frame):
    def __init__(s):
        wx.Frame.__init__(s, None, title='Directory Settings')
        panel = wx.Panel(s)
        
        s.dirEntryL = wx.StaticText(panel, label='List directories with .lbr files, one directory per line')
        s.dirEntry = wx.TextCtrl(panel,style=wx.TE_MULTILINE,size=(300,100))
        s.dirOK = wx.Button(panel, label='OK')
        s.dirCancel = wx.Button(panel, label='Cancel')
        
        s.dirOK.Bind(wx.EVT_BUTTON, s.validate)
        s.dirCancel.Bind(wx.EVT_BUTTON, s.cancel)
        
        buttonSizer = wx.BoxSizer(wx.HORIZONTAL)
        buttonSizer.Add(s.dirOK)
        buttonSizer.Add(s.dirCancel)
        
        dirSizer = wx.GridBagSizer(hgap=5,vgap=5)
        dirSizer.Add(s.dirEntryL,pos=(0,0),flag=wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.EXPAND,border=5)
        dirSizer.Add(s.dirEntry,pos=(1,0),flag=wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.EXPAND,border=5)
        dirSizer.Add(buttonSizer,pos=(2,0),flag=wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,border=5)
        
        panel.SetSizer(dirSizer)
        dirSizer.Fit(panel)
        
        mainSizer = wx.BoxSizer(wx.HORIZONTAL)
        mainSizer.Add(panel)
        
        s.SetSizer(mainSizer)
        mainSizer.Fit(s)
        
        s.Show(True)
        
        #Show existing files
        for file in lbrLib.filePaths:
            s.dirEntry.WriteText(file + '\n')
    def validate(s, event):
        newFilePaths = []
        for lineNo in range(0,s.dirEntry.GetNumberOfLines()):
            file_str = (s.dirEntry.GetLineText(lineNo))
            if(file_str == ''):#Ignore for empty line
                continue
            if(os.path.exists(file_str)):#Check if path exists
                if(file_str not in newFilePaths):#Ignore duplicates
                    newFilePaths.append(file_str)
            else:
                dlg = wx.MessageDialog(s, "Bad filepath: %s" %(file_str),"Parsing Error",wx.OK|wx.ICON_ERROR)
                result = dlg.ShowModal()
                dlg.Destroy()
                return
        if(len(newFilePaths) == 0):
            print 'Found no filepaths'
            return
        lbrLib.filePaths = []
        for elem in newFilePaths:
            lbrLib.filePaths.append(elem)
        
        print 'A'
        print newFilePaths
        print lbrLib.filePaths

        #Write out to file
        lbrLib.dirFile.seek(0)
        lbrLib.dirFile.truncate()
        for file in newFilePaths:
            lbrLib.dirFile.write(file + '\n')
        
        #Inform fileTree to update
        pub.sendMessage('newFilePaths', 'Request: Update file Tree')
        s.closeWindow()
    def cancel(s, event):
        s.closeWindow()
    def closeWindow(s):
        s.Destroy()