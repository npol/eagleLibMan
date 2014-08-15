import wx
from wx.lib.pubsub import Publisher as pub

class editGUI(wx.Panel):
    def __init__(s, parent):
        wx.Panel.__init__(s, parent, style=wx.RAISED_BORDER)
        s.parent = parent
        boxSizer = wx.BoxSizer()
        s.text = wx.StaticText(s, label='No Library Selected')
        boxSizer.Add(s.text)
        s.SetSizer(boxSizer)
        boxSizer.Fit(s)
        pub.subscribe(s.onEditChanged, 'editChanged')
        return
    def onEditChanged(s, message):
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
    def confBlank(s):
        return
    def confDevset(s):
        return
    def confPkg(s):
        return
    def confSym(s):
        return
    