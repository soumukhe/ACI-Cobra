__author__ = 'soumukhe'
#!/usr/bin/env python

import loginsjc
import re
import json


#  find encaps used for Static Bindings:  fvRsPathAtt

md = loginsjc.logen()

print md
# print dir(md)

items = md.lookupByClass("fvRInfoHolder")


TotContracts = 0
for item in items:
    # print item.dn
    line1 = str(item.dn)
    # print line1
    ContractName = re.findall("brc-(.*?)/", line1)  # this is a list
    if re.search("/subj-", line1):
        SubjectName = re.findall("/subj-(.*?)]", line1)  # this is a list
    if re.search("-subj-", line1):
        SubjectName = re.findall("-subj-\[(.*?)]", line1)  # this is a list
    stppos = line1.find("/to")
    consumer = line1[0:stppos]  # this works.   Using slicing,  from beginning to stppos
    print "******************"
    print "dn=", line1
    print "Contract Name: ", ContractName[0]
    print "Subject Name: ", SubjectName[0]
    print "Filter id: ", item.id
    print "Consumer: ", consumer
    print "Provider: ", item.toEpgDn

    TotContracts+=1

print "******************"
print "Total Contracts: ", TotContracts



