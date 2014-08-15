import wx
from wx.lib.pubsub import Publisher as pub

class libGUI(wx.Panel):
    def __init__(s, parent):
        wx.Panel.__init__(s, parent, style=wx.RAISED_BORDER)
        s.parent = parent
        s.devSetTree = wx.TreeCtrl(s, size=(200,-1),style=wx.TR_DEFAULT_STYLE)
        s.pkgTree = wx.TreeCtrl(s, size=(200,-1),style=wx.TR_DEFAULT_STYLE)
        s.symTree = wx.TreeCtrl(s, size=(200,-1),style=wx.TR_DEFAULT_STYLE)
        
        s.devSetTreeRoot = s.devSetTree.AddRoot('DeviceSets')
        s.pkgTreeRoot = s.pkgTree.AddRoot('Packages')
        s.symTreeRoot = s.symTree.AddRoot('Symbols')
        
        libSizer = wx.GridSizer(rows=0,cols=1,vgap=5,hgap=5)
        libSizer.Add(s.devSetTree,flag=wx.EXPAND)
        libSizer.Add(s.pkgTree,flag=wx.EXPAND)
        libSizer.Add(s.symTree,flag=wx.EXPAND)
        
        s.SetSizer(libSizer)
        libSizer.Fit(s)
        
        s.devSetTree.Bind(wx.EVT_TREE_ITEM_ACTIVATED, s.onDevClick)
        s.pkgTree.Bind(wx.EVT_TREE_ITEM_ACTIVATED, s.onPkgClick)
        s.symTree.Bind(wx.EVT_TREE_ITEM_ACTIVATED, s.onSymClick)
        
        pub.subscribe(s.onLibChanged, 'libChanged')
        
        s.clearDevsetTree()
        s.clearPkgTree()
        s.clearSymTree()
        
        s.symTree.Disable()
        s.pkgTree.Disable()
        s.devSetTree.Disable()
        return
    def popPkgTree(s):
        s.clearPkgTree()
        a = s.pkgTree.AppendItem(s.pkgTreeRoot, 'pkg1')
        s.pkgTree.SetItemData(a, wx.TreeItemData(0))
        b = s.pkgTree.AppendItem(s.pkgTreeRoot, 'pkg2')
        s.pkgTree.SetItemData(b, wx.TreeItemData(1))
        c = s.pkgTree.AppendItem(s.pkgTreeRoot, 'pkg3')
        s.pkgTree.SetItemData(c, wx.TreeItemData(2))
        s.pkgTree.Expand(s.pkgTreeRoot)
        s.pkgTree.UnselectAll()
        return
    def popSymTree(s):
        s.clearSymTree()
        a = s.symTree.AppendItem(s.symTreeRoot, 'sym1')
        s.symTree.SetItemData(a, wx.TreeItemData(0))
        b = s.symTree.AppendItem(s.symTreeRoot, 'sym2')
        s.symTree.SetItemData(b, wx.TreeItemData(1))
        c = s.symTree.AppendItem(s.symTreeRoot, 'sym3')
        s.symTree.SetItemData(c, wx.TreeItemData(2))
        s.symTree.Expand(s.symTreeRoot)
        s.symTree.UnselectAll()
        return
    def popDevsetTree(s):
        s.clearDevsetTree()
        a = s.devSetTree.AppendItem(s.devSetTreeRoot, 'Devset1')
        s.symTree.SetItemData(a, wx.TreeItemData(0))
        b = s.devSetTree.AppendItem(s.devSetTreeRoot, 'Devset2')
        s.symTree.SetItemData(b, wx.TreeItemData(1))
        c = s.devSetTree.AppendItem(s.devSetTreeRoot, 'Devset3')
        s.symTree.SetItemData(c, wx.TreeItemData(2))
        s.devSetTree.Expand(s.devSetTreeRoot)
        s.devSetTree.UnselectAll()
        return
    def clearPkgTree(s):
        s.pkgTree.DeleteChildren(s.pkgTreeRoot)
        s.pkgTree.UnselectAll()
        return
    def clearSymTree(s):
        s.symTree.DeleteChildren(s.symTreeRoot)
        s.symTree.UnselectAll()
        return
    def clearDevsetTree(s):
        s.devSetTree.DeleteChildren(s.devSetTreeRoot)
        s.devSetTree.UnselectAll()
        return
    def onLibChanged(s, message):
        if(message.data == ''):#No library selected
            s.clearPkgTree()
            s.clearSymTree()
            s.clearDevsetTree()
            s.symTree.Disable()
            s.pkgTree.Disable()
            s.devSetTree.Disable()
        else:#Library selected, populate with elements
            s.symTree.Enable()
            s.pkgTree.Enable()
            s.devSetTree.Enable()
            s.popPkgTree()
            s.popSymTree()
            s.popDevsetTree()
        return
    def onSymClick(s, event):
        if(s.symTree.IsSelected(s.symTreeRoot)):
            count = s.symTree.GetChildrenCount(s.pkgTreeRoot)
            pub.sendMessage('editChanged',('syT',count))
            return
        selItem = s.symTree.GetSelection()
        selData = s.symTree.GetItemData(selItem)
        pub.sendMessage('editChanged',('sym',selData.GetData()))
        return
    def onPkgClick(s, event):
        if(s.pkgTree.IsSelected(s.pkgTreeRoot)):
            count = s.pkgTree.GetChildrenCount(s.pkgTreeRoot)
            pub.sendMessage('editChanged',('pkT',count))
            return
        selItem = s.pkgTree.GetSelection()
        selData = s.pkgTree.GetItemData(selItem)
        pub.sendMessage('editChanged',('pkg',selData.GetData()))
        return
    def onDevClick(s, event):
        if(s.devSetTree.IsSelected(s.devSetTreeRoot)):
            count = s.devSetTree.GetChildrenCount(s.devSetTreeRoot)
            pub.sendMessage('editChanged',('deT',count))
            return
        selItem = s.devSetTree.GetSelection()
        selData = s.devSetTree.GetItemData(selItem)
        pub.sendMessage('editChanged',('dev',selData.GetData()))
        return
    