import xml.etree.ElementTree as ET
"""
tree = ET.parse("test.lbr")
print tree.findtext("head/title")
print tree.getroot()

tree.write("test2.lbr")

#Get Version
root = tree.getroot()
root_at = root.attrib
if('version' in root_at):
    print 'version: %s\n' %(root.attrib['version'])
else:
    print 'version not found\n'

#Get settings
settings = root[0][0]
assert(settings.tag == 'settings')
#No attributes
#Children:
#alwaysvectorfont: no
#verticaltext: up

#Get Grid info
grid = root[0][1]
assert(grid.tag == 'grid')
#Attributes:
#distance, style, multiple, altdistance, altunit, unit, altunitdist, display, unitdist
#No Children


#Get Layer info
layers = root[0][2]
assert(layers.tag == 'layers')
#No attributes
#Children are all layers


#Get Library
lib = root[0][3]
assert(lib.tag == 'library')
#No attributes
#Children:
#Packages, Symbols, Devicesets

#Get Packages
packages = root[0][3][0]
assert(packages.tag == 'packages')

#Get symbols
symbols = root[0][3][1]
assert(symbols.tag == 'symbols')

#Get devicesets
devicesets = root[0][3][2]
assert(devicesets.tag == 'devicesets')
"""

"""
s.root: Handle to library tree
s.eagleVersion: Eagle Version code
s.settings: {'alwaysvectorfont': 'no', 'verticaltext': 'up'}
s.grid: {distance, style, multiple, altdistance, altunit, unit, altunitdist, display, unitdist}

"""

class libReader:
    def __init__(s, filename):
        s.tree = ET.parse(filename)
        
        #Check for valid header
        if(s.tree.getroot() != 'eagle'):
            print 'Header Error'
            return
        s.root = s.tree.getroot()
        
        #Get version
        s.eagleVersion = s.root.attrib['version']
        
        #Get settings
        s.settingsNode = s.root[0][0]
        if(s.settings.tag != 'settings'):
            print 'Format error: settings'
            return
        s.settings = {}
        for i in range(0,len(s.settingsNode)):
            s.settings.update(s.settingsNode[i].attrib)
        
        #Get Grid info
        s.gridNode = s.root[0][1]
        if(s.gridNode.tag != 'grid'):
            print 'Format error: grid'
            return
        s.grid = {}
        #distance attribute
        s.grid['distance'] = s.gridNode.distance
        #style attribute
        s.grid['style'] = s.gridNode.style
        #multiple attribute
        s.grid['multiple'] = s.gridNode.multiple
        #altdistance attribute
        s.grid['altdistance'] = s.gridNode.altdistance
        #altunit attrbute
        s.grid['altunit'] = s.gridNode.altunit
        #unit attribute
        s.grid['unit'] = s.gridNode.unit
        #altunitdist attribute
        s.grid['altunitdist'] = s.gridNode.altunitdist
        #display attribute
        s.grid['display'] = s.gridNode.display
        #unitdist attribute
        s.grid['unitdist'] = s.gridNode.unitdist
        
        #Get layer info
        s.layerNode = s.root[0][2]
        if(s.layerNode.tag != 'layers'):
            print 'Format error: layers'
            return
        
        #Get library
        s.libNode = s.root[0][3]
        if(s.libNode.tag != 'library'):
            print 'Format error: library'
            return
        s.pkgNode = s.libNode[0]
        if(s.pkgNode.tag != 'packages'):
            print 'Format error: packages'
            return
        s.symNode = s.libNode[1]
        if(s.symNode.tag != 'symbols'):
            print 'Format error: symbols'
            return
        s.devsetNode = s.libNode[2]
        if(s.devsetNode.tag != 'devicesets'):
            print 'Format error: devicesets'
            return
        return
    def writeLib(s, filename, tree):
        tree.write(filename)
        
        





