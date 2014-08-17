import wx
from wx.lib.pubsub import Publisher as pub

unitList = ['mic','mm','mil','inch']

class editGUI(wx.Panel):
    def __init__(s, parent):
        wx.Panel.__init__(s, parent)
        s.confBlank()
        pub.subscribe(s.onEditChanged, 'editChanged')
        return
    def onEditChanged(s, message):
        if(message.data[0] == 'syT'):
            s.confBlank()#TODO: replace with GUI initator
            s.text.SetLabel('%d symbols' %(message.data[1]))
        elif(message.data[0] == 'pkT'):
            s.confBlank()#TODO: replace with GUI initiator
            s.text.SetLabel('%d packages' %(message.data[1]))
        elif(message.data[0] == 'deT'):
            s.confBlank()#TODO: replace with GUI initiator
            s.text.SetLabel('%d devicesets' %(message.data[1]))
        elif(message.data[0] == 'sym'):
            s.confBlank()#TODO: replace with GUI initiator
            s.text.SetLabel('Symbol %d' %(message.data[1]))
        elif(message.data[0] == 'pkg'):
            s.confBlank()#TODO: replace with GUI initiator
            s.text.SetLabel('Package %d' %(message.data[1]))
        elif(message.data[0] == 'dev'):
            s.confBlank()#TODO: replace with GUI initiator
            s.text.SetLabel('Deviceset %d' %(message.data[1]))
        elif(message.data[0] == 'lbr'):#Clicked on library in file tree, open libeditor
            s.confLib(message.data[1])
        elif(message.data[0] == ''):#Clicked on directory in file tree, deselect
            s.confBlank()#Sets text to 'No Library Selected'
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
        
        mainSizer = wx.GridBagSizer(hgap=5,vgap=5)
        
        #Library Settings
        s.libBox = wx.StaticBox(s, label='Library Settings')
        s.libL = wx.StaticText(s, label='Library: %s' %(fileName))
        s.verL = wx.StaticText(s, label='Created in Eagle Version')
        s.ver = wx.TextCtrl(s)
        s.vecFontL = wx.StaticText(s, label='Always Vector Font')
        s.vecFont = wx.wx.TextCtrl(s)
        s.verTextL = wx.StaticText(s, label='Vertical Text')
        s.verText = wx.TextCtrl(s)
        
        s.libBoxSizer = wx.StaticBoxSizer(s.libBox)
        s.libSizer = wx.GridBagSizer(hgap=5,vgap=5)
        s.libSizer.Add(s.libL,pos=(0,0),flag=wx.ALL,span=(1,2))
        s.libSizer.Add(s.verL,pos=(1,0),flag=wx.ALL)
        s.libSizer.Add(s.ver,pos=(1,1),flag=wx.ALL)
        s.libSizer.Add(s.vecFontL,pos=(2,0),flag=wx.ALL)
        s.libSizer.Add(s.vecFont,pos=(2,1),flag=wx.ALL)
        s.libSizer.Add(s.verTextL,pos=(3,0),flag=wx.ALL)
        s.libSizer.Add(s.verText,pos=(3,1),flag=wx.ALL)
        s.libBoxSizer.Add(s.libSizer)
        
        mainSizer.Add(s.libBoxSizer,pos=(0,0),flag=wx.ALL)
        
        #Grid Settings
        global unitList
        s.gridBox = wx.StaticBox(s, label='Grid Settings')
        s.gridDistL = wx.StaticText(s, label='distance')
        s.gridDist = wx.TextCtrl(s)
        s.gridDistUnitL = wx.StaticText(s, label='Distance Unit')
        s.gridDistUnit = wx.ComboBox(s, choices=unitList,name='Distance Unit')
        s.gridUnitL = wx.StaticText(s, label='Unit')
        s.gridUnit = wx.ComboBox(s, choices=unitList,name='Unit')
        s.gridAltDistL = wx.StaticText(s, label='Alt Distance')
        s.gridAltDist = wx.TextCtrl(s)
        s.gridAltUnitDistL = wx.StaticText(s, label='Alt Distance Unit')
        s.gridAltUnitDist = wx.ComboBox(s, choices=unitList,name='Alt Distance Unit')
        s.gridAltUnitL = wx.StaticText(s, label='Alt Unit')
        s.gridAltUnit = wx.ComboBox(s, choices=unitList,name='Alt Unit')
        s.gridStyleL = wx.StaticText(s, label='Style')
        s.gridStyle = wx.ComboBox(s, choices=['dots','lines'],name='Style')
        s.gridDispL = wx.StaticText(s, label='Display')
        s.gridDisp = wx.ComboBox(s, choices=['on','off'],name='Display')
        
        s.gridSizer = wx.GridBagSizer(hgap=5,vgap=5)
        s.gridSizer.Add(s.gridDistL,pos=(0,0),flag=wx.ALL)
        s.gridSizer.Add(s.gridDist,pos=(0,1),flag=wx.ALL)
        s.gridSizer.Add(s.gridDistUnitL,pos=(1,0),flag=wx.ALL)
        s.gridSizer.Add(s.gridDistUnit,pos=(1,1),flag=wx.ALL)
        s.gridSizer.Add(s.gridUnitL,pos=(2,0),flag=wx.ALL)
        s.gridSizer.Add(s.gridUnit,pos=(2,1),flag=wx.ALL)
        s.gridSizer.Add(s.gridAltDistL,pos=(3,0),flag=wx.ALL)
        s.gridSizer.Add(s.gridAltDist,pos=(3,1),flag=wx.ALL)
        s.gridSizer.Add(s.gridAltUnitDistL,pos=(4,0),flag=wx.ALL)
        s.gridSizer.Add(s.gridAltUnitDist,pos=(4,1),flag=wx.ALL)
        s.gridSizer.Add(s.gridAltUnitL,pos=(5,0),flag=wx.ALL)
        s.gridSizer.Add(s.gridAltUnit,pos=(5,1),flag=wx.ALL)
        s.gridSizer.Add(s.gridStyleL,pos=(6,0),flag=wx.ALL)
        s.gridSizer.Add(s.gridStyle,pos=(6,1),flag=wx.ALL)
        s.gridSizer.Add(s.gridDispL,pos=(7,0),flag=wx.ALL)
        s.gridSizer.Add(s.gridDisp,pos=(7,1),flag=wx.ALL)
        
        s.gridBoxSizer = wx.StaticBoxSizer(s.gridBox)
        s.gridBoxSizer.Add(s.gridSizer)
        
        mainSizer.Add(s.gridBoxSizer,pos=(0,1),flag=wx.ALL)
        
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
    