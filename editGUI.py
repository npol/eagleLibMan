import wx
from wx.lib.pubsub import Publisher as pub

class editGUI(wx.Panel):
    def __init__(s, parent):
        wx.Panel.__init__(s, parent, style=wx.RAISED_BORDER)
        s.confBlank()
        pub.subscribe(s.onEditChanged, 'editChanged')
        return
    def onEditChanged(s, message):
        if(True):
            print message.data
            if(message.data[0] == ''):#Clicked on directory, deselect all libraries
                s.confBlank()#Sets text to 'No Library Selected'
            elif(message.data[0] == 'lbr'):#Clicked on library in filetree, show libeditor
                s.confLib(message.data[1])
            return
        if(message.data[0] == 'syT'):
            s.text.SetLabel('%d symbols' %(message.data[1]))
        elif(message.data[0] == 'pkT'):
            s.text.SetLabel('%d packages' %(message.data[1]))
        elif(message.data[0] == 'deT'):
            s.text.SetLabel('%d devicesets' %(message.data[1]))
        elif(message.data[0] == 'sym'):
            s.text.SetLabel('Symbol %d' %(message.data[1]))
        elif(message.data[0] == 'pkg'):
            s.text.SetLabel('Package %d' %(message.data[1]))
        elif(message.data[0] == 'dev'):
            s.text.SetLabel('Deviceset %d' %(message.data[1]))
        elif(message.data[0] == 'lbr'):
            s.text.SetLabel('Library')
        elif(message.data[0] == ''):
            s.text.SetLabel('No Library Selected')
        else:
            print 'error'
            print message.data
        return
    def clearPanel(s):
        for child in s.GetChildren():
            child.Destroy()
        return
    def confBlank(s):
        s.clearPanel()
        s.text = wx.StaticText(s, label='No Library Selected')
        sizer=wx.GridSizer(1,1)
        sizer.Add(s.text,flag=wx.ALIGN_CENTER)
        s.SetSizer(sizer)
        sizer.Fit(s)
        s.Layout()
        return
    def confLib(s, fileName):
        s.clearPanel()
        s.libL = wx.StaticText(s, label='Library: %s' %(fileName))
        s.verL = wx.StaticText(s, label='Created in Eagle Version')
        s.ver = wx.TextCtrl(s)
        s.vecFontL = wx.StaticText(s, label='Always Vector Font')
        s.vecFont = wx.wx.TextCtrl(s)
        s.verTextL = wx.StaticText(s, label='Vertical Text')
        s.verText = wx.TextCtrl(s)
        #TODO: Add widgets for grid
        #TODO: Add layer settings
        mainSizer = wx.GridBagSizer(hgap=5,vgap=5)
        mainSizer.Add(s.libL,pos=(0,0),flag=wx.ALL,span=(1,2))
        mainSizer.Add(s.verL,pos=(1,0),flag=wx.ALL)
        mainSizer.Add(s.ver,pos=(1,1),flag=wx.ALL)
        mainSizer.Add(s.vecFontL,pos=(2,0),flag=wx.ALL)
        mainSizer.Add(s.vecFont,pos=(2,1),flag=wx.ALL)
        mainSizer.Add(s.verTextL,pos=(3,0),flag=wx.ALL)
        mainSizer.Add(s.verText,pos=(3,1),flag=wx.ALL)
        s.SetSizer(mainSizer)
        mainSizer.Fit(s)
        s.Layout()
        return
    def confDevset(s):
        return
    def confPkg(s):
        return
    def confSym(s):
        return
    