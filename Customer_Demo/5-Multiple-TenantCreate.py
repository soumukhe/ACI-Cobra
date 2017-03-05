from cobra.mit.access import MoDirectory
from cobra.mit.session import LoginSession
import requests
requests.packages.urllib3.disable_warnings()

import loginsjc
import re
import json

# Import the config request
from cobra.mit.request import ConfigRequest
configReq = ConfigRequest()


#  login

md = loginsjc.logen()


# Import the object classes from the model
from cobra.model.fv import Tenant
from cobra.model.fv import Ctx
from cobra.model.fv import BD
from cobra.model.fv import Subnet
from cobra.model.fv import RsCtx
from cobra.model.fv import Ap
from cobra.model.fv import AEPg
from cobra.model.fv import RsBd


# Get the top level policy universe directory
uniMo = md.lookupByDn('uni')

'''
# create the objects
fvTenantMo = Tenant(uniMo, 'SM-ExampleCorp')
fvCtxMo = Ctx(fvTenantMo, "SM-MyVRF")
fvBDMo = BD(fvTenantMo, name='SM-MyVRF-BD')
fvRsCtxMo = RsCtx(fvBDMo, tnFvCtxName='SM-MyVRF')
fvSubnetMo = Subnet(fvBDMo, ip='121.121.121.1/24')


# Add the tenant object to the config request and commit
# below line is if you wanted to delete the Tenant
# fvTenantMo.delete()
configReq.addMo(fvTenantMo)
md.commit(configReq)


'''




for i in range (20):
    md = loginsjc.logen()
    configReq = ConfigRequest()
    uniMo = md.lookupByDn('uni')
    tenant = "SM-ExampleCorp" + str(i)
    vrf = "SM-MyVRF" + str(i)
    bd = "SM-MyVRF-BD" + str(i)
    subnet = "121.121." + str(i) + ".1/24"
    appprofile = "SM-MYAPP" + str(i)
    epg = "SM-MYEPG" + str(i)

    # print tenant, vrf, bd, subnet
    # create the objects
    fvTenantMo = Tenant(uniMo, tenant)
    fvCtxMo = Ctx(fvTenantMo, vrf)
    fvBDMo = BD(fvTenantMo, name= bd)
    fvRsCtxMo = RsCtx(fvBDMo, tnFvCtxName= vrf)
    fvSubnetMo = Subnet(fvBDMo, ip=subnet )
    fvAPPMo = Ap(fvTenantMo, name= appprofile)
    fvAEPgMo = AEPg(fvAPPMo, name= epg)
    fvRsBdMo = RsBd(fvAEPgMo, tnFvBDName= bd)
    # commit the config:
    #  if you want to delete the tenants, take comment out the next line
    fvTenantMo.delete()
    print "Tenant: ", tenant
    configReq.addMo(fvTenantMo)
    md.commit(configReq)




