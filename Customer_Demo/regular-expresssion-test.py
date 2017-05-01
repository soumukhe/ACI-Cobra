__author__ = 'soumukhe'
#!/usr/bin/env python

import re

line = "uni/tn-SC-One/ap-DMZ_Web/epg-DMZ_App_1/cep-00:50:56:B9:02:23"

# re.findall makes a list
print "Tenant:", re.findall( "uni/(.*?)/", line) # Tenant: ['tn-SC-One']
print "APPPRofile: ", re.findall( "ap-(.*?)/", line) # APPPRofile:  ['DMZ_Web']
print "epg: ", re.findall( "epg-(.*?)/", line) # epg:  ['DMZ_App_1']

line1 = "topology/pod-1/paths-101/pathep-[eth1/2]"
print "Paths:" , re.findall( "pod-1/(.*?)]", line1) # Paths: ['paths-101/pathep-[eth1/2']

# re.search()            #  this either retruns None or something like: <_sre.SRE_Match object at 0x00000000029F9648>

"""
import re  #  import regular expression
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From: ', line)  :   #  could have aslo done:       if line.find("From:")  != -1 :    remember -1 means match was not found
     print line   #  all lines having From:  gets printed out

"""

line1 = "uni/tn-SM-Demo/ap-Filip/epg-filip1/to-[uni/tn-SM-Demo/ap-APP1/epg-WEB2]-subj-[uni/tn-SM-Demo/brc-Filip1/subj-filip1]-flt-564"

stppos = line1.find("/to")
print stppos
output = line1[0:stppos]   # this works.   Using slicing,  from beginning to stppos
print "Output: ", output
print "C-Tenant:", re.findall("tn-(.*?)/", output)  # re.findall makes a list
print "C-App Profile: ", re.findall("/ap-(.*?)/", output)
print "C-EPG: ", re.findall("/epg-(.+)", output)  #  .+ is repeat any character many times
print " Contract Name: ", re.findall("brc-(.*?)/", line1)