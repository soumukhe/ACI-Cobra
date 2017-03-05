__author__ = 'soumukhe'
# list of packages that should be imported for this code to work; except for cobra.mit.request, others are imported from loginsjc.py

import cobra.mit.request


#  GET User Inputs for Tenants, VRF, etc

def getvalue(value):
    i = True
    y = "YES"
    value1 = value

    while (i ==True):
        if value == "Gateway":
            print "Enter BD Gateway Value in the form 10.1.1.1/24 below:"
        else:
            print "Enter", value1, "name below:"

        value = raw_input('----------> ')
        y = raw_input("if name is correct, enter \"YES\"  ")

        try:
            if ( y == "YES" ) and (len(value)  > 0)  :
                i = False
                print "**********************\n"
            else:
                x = 0/0    #  make the code in try: fail, so execution moves to except:
        except:
            print "**********************\n"
            continue   #  go back to the while statement
        return value


Tname = getvalue("Tenant")
VRFName = getvalue("vrf")
BDName = getvalue("BD")
Gty = getvalue("Gateway")

print "Creating Tenant with name: ",  Tname
print "VRFName = ", VRFName
print "BD = ", BDName
print "Gateway = ", Gty

# log into an APIC and create a directory object
import loginsjc
md = loginsjc.logen()

# the top level object on which operations will be made
topMo = cobra.model.pol.Uni('')


#  assign the names to variables, so we don't have to change object model names
Tenant = Tname
TenantVrf = VRFName
TBD = BDName
Subnet = Gty

# Define Object Models
Tenants = cobra.model.fv.Tenant(topMo, name=Tenant , descr='')
TVRF = cobra.model.fv.Ctx(Tenants, name=Tenant)
TBD = cobra.model.fv.BD(Tenants, mac='00:22:BD:F8:19:FF', name= TBD)
fvRsCtx = cobra.model.fv.RsCtx(TBD, tnFvCtxName=TVRF.name)
BDGateway = cobra.model.fv.Subnet(TBD, ip=Subnet)

###  Commit the Object Model
c = cobra.mit.request.ConfigRequest()
# to delete Tenant, uncomment line below
Tenants.delete()
c.addMo(Tenants)
md.commit(c)




