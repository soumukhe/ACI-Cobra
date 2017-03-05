__author__ = 'soumukhe'
#!/usr/bin/env python

import loginsjc
import re
import json


#  find encaps used for Static Bindings:  fvRsPathAtt

md = loginsjc.logen()

print md
# print dir(md)

items = md.lookupByClass("fvnsVlanInstP")



for item in items:
    print item.name