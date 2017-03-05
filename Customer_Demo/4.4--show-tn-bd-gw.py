__author__ = 'soumukhe'
#!/usr/bin/env python

import loginsjc
import re
import json

md = loginsjc.logen()

# #*******************************   key of mac and values as a list of ip, encap, tn, appr, epg **************
items = md.lookupByClass("fvSubnet")

template = "{0:<30} {1:<30} {2:<30} "
print template.format("Tenant", "BD", "Gateway")
print template.format("--------", "-----------", "-----------" )



for item in items :
    DN = str(item.dn)
    # print DN
    # **********  From the DN,  do regex search for Tenant,  BD, Subnet
    #
    tn =  re.findall("uni/(.*)/BD", DN)
    if re.search("uni/(.*)/BD", DN) :   #   re.search replies none when nothing found
        tn = tn[0]
    else:
        tn = "n/a"
    bd =  re.findall("BD-(.*)/subnet", DN)
    if re.search("BD-(.*)/subnet", DN) :   #   re.search replies none when nothing found
        bd = bd[0]
    else:
        bd = "n/a"

    subnet = re.findall("subnet-\[(.*)]", DN)
    if re.search("subnet-\[(.*)]", DN) :   #   re.search replies none when nothing found
        subnet = subnet[0]
    else:
        subnet = "n/a"


    print template.format(tn, bd, subnet)



