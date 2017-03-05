__author__ = 'soumukhe'
#!/usr/bin/env python

import loginsjc
import re
import json


#  find encaps used for Static Bindings:  fvRsPathAtt

md = loginsjc.logen()

print md
print dir(md)


items = md.lookupByClass("fvTenant")
print items
for item in items:
   print item.name

#======================================================================================
"""
items = md.lookupByClass("fvTenant")
for item in items:
    print item.dn
"""


"""
items = md.lookupByClass("healthInst")

# print items

for item in items :
    # print item

    if int(item.cur) > 50 :
        print item.cur, item.dn

"""

"""
# show lldp neighbors
items = md.lookupByClass("lldpAdjEp")

template = "{0:<40} {1:<25} {2:<25} {3:<20} "
print template.format("Neighbor", "Local_Leaf_Switch", "Local_Leaf_Port", "Neighbor_Port")
print template.format("--------", "-----------", "-----------", "-----------" )

for item in items:
    dn = str(item.dn)
    # print dn
    portl = re.findall("if-\[(.*)\]/adj", dn)
    nodel = re.findall("pod-1/(.*)/sys", dn)

    print template.format(item.sysName, nodel[0] , portl[0], item.portDesc)


"""

"""
# show cdp neighbors
items = md.lookupByClass("cdpAdjEp")

template = "{0:<40} {1:<25} {2:<25} {3:<20} "
print template.format("Neighbor", "Local_Leaf_Switch", "Local_Leaf_Port", "Neighbor_Port")
print template.format("--------", "-----------", "-----------", "-----------" )

for item in items:
    dn = str(item.dn)
    # print dn
    portl = re.findall("if-\[(.*)\]/adj", dn)
    nodel = re.findall("pod-1/(.*)/sys", dn)

    print template.format(item.sysName, nodel[0] , portl[0], item.portId)
"""
