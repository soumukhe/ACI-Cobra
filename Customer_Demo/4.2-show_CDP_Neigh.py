#!/usr/bin/env python

import loginsjc
import re


md = loginsjc.logen()




items = md.lookupByClass("cdpAdjEp")

template = "{0:<40} {1:<25} {2:<25} {3:<20} "
print template.format("Neighbor", "Local_Leaf_Switch", "Local_Leaf_Port", "Neighbor_Port")
print template.format("--------", "-----------", "-----------", "-----------" )

for item in items:
    dn = str(item.dn)
    # print dn
    portl = re.findall("if-\[(.*)\]/adj", dn)
    if re.search("pod-1", dn):
        node = re.findall("pod-1/(.*)/sys", dn)
    if re.search("pod-2", dn):
        node = re.findall("pod-2/(.*)/sys", dn)

    print template.format(item.sysName, node[0] , portl[0], item.portId)
