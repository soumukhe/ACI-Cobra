__author__ = 'soumukhe'
#!/usr/bin/env python

import loginsjc
import re

md = loginsjc.logen()

# #*******************************   key of mac and values as a list of ip, encap, tn, appr, epg **************
items = md.lookupByClass("fvCEp")
# print type(items)
# print items

mydict = {}   # creates an empty dictionary.  Key will be MAC,  values will be list of ip, encap, tenant, appr, epg

for item in items :
    DN = str(item.dn)
    # print DN
    # **********  From the DN,  do regex search for Tenant,  APPProfile, EPG
    #
    tn = re.findall("uni/(.*?)/", DN)  # remember re.findall makes a list
    tn = tn[0]
    #
    appr = re.findall("ap-(.*?)/", DN)
    if re.search("ap-(.*?)/", DN) :   #   re.search replies none when nothing found
        appr = appr[0]
    else:
        appr = "n/a"
    #
    epg = re.findall("epg-(.*?)/", DN)
    if re.search("epg-(.*?)/", DN):
        epg = epg[0]
    else:
        epg = "n/a"
    # populate mydict with key of mac and values as a list of ip, encap, tn, appr, epg
    mydict[item.mac] = [item.ip, item.encap, tn, appr, epg]

# print mydict

# #*******************************   key of mac and values as topology **************
items = md.lookupByClass("fvRsCEpToPathEp")
# print type(items)
mydict1 = {}   # creates an empty dictionary.  Key will be MAC,  values will be topo

for item in items :
    DN = str(item.dn)
    # print DN
    # **********  From the DN,  do regex search for Tenant,  APPProfile, EPG
    #
    mac1 = re.findall("cep-(.*?)/", DN)    # remember re.findall makes a list
    topo =  re.findall("pod-1(.*)]", DN)  # remember re.findall makes a list
    # tn = tn[0]
    # print mac1,   topo
    #
    # populate mydict1 with key of mac and values as a list of topo info
    mydict1[mac1[0]] = [topo[0]]
# print mydict1


# #*************************************************************************************

template = "{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20} {6:<20}"
print template.format("MAC#", "IP", "Encap",  "Tenant", "APP-Profile", "EPG", "Topo")
print template.format("--------", "-----------", "-----------", "-----------", "-----------",  "--------------", "--------------" )



keylist = mydict.keys()
keylist.sort()

Kount = 0
for key in keylist:
    list1 = mydict[key]  #  make list1 with the values of the keys
    if mydict1.get(key):  # using get method in dictionary, if key does not exist, then it's false
        topology = mydict1[key][0]  #  since the value of topo is a list, get the 1st item of topo
    else:
        topology = "n/a"

    print template.format(key,  list1[0], list1[1], list1[2], list1[3], list1[4], topology)
    Kount +=1

print "\nTotal EndPoints :", Kount

# print json.dumps(mydict, indent=4)







