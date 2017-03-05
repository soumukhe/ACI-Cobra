__author__ = 'soumukhe'
#!/usr/bin/env python

import loginsjc
import re
import json


#  find encaps used for Static Bindings:  fvRsPathAtt

md = loginsjc.logen()

list = []
items = md.lookupByClass("fvRsPathAtt")




for item in items:
     if item.encap != "unknown" :
        # print item.encap
        vlan = re.findall("vlan-(\S*)",item.encap)
        list.append(int(vlan[0]))


vlansUnique = []
for vlanid in list:
    if vlanid  not in vlansUnique:
        vlansUnique.append(vlanid)

vlansUnique.sort()
print  "Vlans aready used for StaticBindings: ", vlansUnique


# md = loginsjc.logen("https://10.29.198.168")

md = loginsjc.logen()
# md = loginsjc.logen("https://10.29.198.168")

list1 = []
items = md.lookupByClass("l3extRsPathL3OutAtt")


for item in items:
     if item.encap != "unknown" :
        # print item.encap
        vlan = re.findall("vlan-(\S*)",item.encap)
        list1.append(int(vlan[0]))


vlansUnique = []
for vlanid in list1:
    if vlanid  not in vlansUnique:
        vlansUnique.append(vlanid)

vlansUnique.sort()
print  "Vlans aready used for L3Outs: ", vlansUnique





