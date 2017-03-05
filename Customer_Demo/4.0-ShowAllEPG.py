#!/usr/bin/env python

import loginsjc
import re


md = loginsjc.logen()




items = md.lookupByClass("fvAEPg")

print  "this is items: ", items

for item in items:
    print " these are my EPGs: ", item.name