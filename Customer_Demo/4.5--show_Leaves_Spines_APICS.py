#!/usr/bin/env python
import loginsjc
import re


md = loginsjc.logen()




items = md.lookupByClass("topSystem")

template = "{0:<30} {1:<25} {2:<25} {3:<25} {4:<20} "
print template.format("Node_Name", "Node_ID", "serial# ", "role", "OOB_Address")
print template.format("--------", "-----------", "-----------", "-----------", "-----------" )


for item in items:
    dn = str(item.dn)
    # print dn
    nodel = re.findall("topology/(.*)/sys", dn)
    print template.format(item.name, nodel[0], item.serial, item.role, item.oobMgmtAddr)


"""
for item in items:
    dn = str(item.dn)
    # print dn
    nodel = re.findall("pod-1/(.*)/sys", dn)

    print template.format( item.name, nodel[0], item.serial, item.role, item.oobMgmtAddr )

"""