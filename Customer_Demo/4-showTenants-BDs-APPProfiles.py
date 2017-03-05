__author__ = 'soumukhe'
#!/usr/bin/env python

from cobra.mit.access import MoDirectory
from cobra.mit.session import LoginSession
import cobra.mit.access
import cobra.mit.session
import cobra.mit.request
import cobra.model.pol
import cobra.model.fv
import cobra.model.vz
import re
import requests
requests.packages.urllib3.disable_warnings()

# To Get Rid of https certificate insuecure warning


#  Login to APIC
def login(apicUrl, user, password):
    try:
        loginSession = LoginSession(apicUrl,user,password)
        moDir = MoDirectory(loginSession)
        moDir.login()
        # print moDir
    except:
        print "the username and/or password you entered is incorrect"
    return moDir



login_apic = login('https://10.29.198.168', 'apic#fallback\\admin', 'Br3adb@n')

Tenants =login_apic.lookupByClass("fvTenant")

#  Login done

for i in Tenants:
    # print i.dn
    print "Tenant Name:", i.name


# print dir(i)

BDs =login_apic.lookupByClass("fvBD")
for i in BDs:
    print "BD Name=", i.name

APPPro =login_apic.lookupByClass("fvAp")
for i in APPPro:
    print "AppProfile Name:",  i.name

VRFs =login_apic.lookupByClass("fvCtx")
for i in VRFs:
    print "VRF Name:", i.name

BDR = login_apic.lookupByClass("fvRsBd")
for i in BDR:
    # print dir(i)
    print "BD Relationship:", i.tnFvBDName