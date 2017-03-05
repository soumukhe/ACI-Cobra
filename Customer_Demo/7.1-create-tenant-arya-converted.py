import cobra

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


#  login

md = loginsjc.logen()






# the top level object on which operations will be made
topMo = md.lookupByDn('uni')

# build the request using cobra syntax
fvTenant = Tenant(topMo, ownerKey='', name='SM-TotalRealJunk', descr='', ownerTag='')
fvBD = cobra.model.fv.BD(fvTenant, ownerKey='', vmac='not-applicable', unkMcastAct='flood', name='SMSHU2-BD', descr='', unkMacUcastAct='proxy', arpFlood='no', limitIpLearnToSubnets='no', llAddr='::', mcastAllow='no', mac='00:22:BD:F8:19:FF', epMoveDetectMode='', unicastRoute='yes', ownerTag='', multiDstPktAct='bd-flood', type='regular', ipLearning='yes')
fvRsBDToNdP = cobra.model.fv.RsBDToNdP(fvBD, tnNdIfPolName='')
fvRsCtx = cobra.model.fv.RsCtx(fvBD, tnFvCtxName='SHSHU2-VRF')
fvRsIgmpsn = cobra.model.fv.RsIgmpsn(fvBD, tnIgmpSnoopPolName='')
fvSubnet = cobra.model.fv.Subnet(fvBD, name='', descr='', ctrl='', ip='121.121.121.1/24', preferred='yes', virtual='no')
fvRsBdToEpRet = cobra.model.fv.RsBdToEpRet(fvBD, resolveAct='resolve', tnFvEpRetPolName='')
fvBD2 = cobra.model.fv.BD(fvTenant, ownerKey='', vmac='not-applicable', unkMcastAct='flood', name='SMSSHCBD', descr='', unkMacUcastAct='proxy', arpFlood='no', limitIpLearnToSubnets='no', llAddr='::', mcastAllow='no', mac='00:22:BD:F8:19:FF', epMoveDetectMode='', unicastRoute='yes', ownerTag='', multiDstPktAct='bd-flood', type='regular', ipLearning='yes')
fvRsBDToNdP2 = cobra.model.fv.RsBDToNdP(fvBD2, tnNdIfPolName='')
fvRsCtx2 = cobra.model.fv.RsCtx(fvBD2, tnFvCtxName='SM-SHaredSVC-VRF')
fvRsIgmpsn2 = cobra.model.fv.RsIgmpsn(fvBD2, tnIgmpSnoopPolName='')
fvSubnet2 = cobra.model.fv.Subnet(fvBD2, name='', descr='', ctrl='', ip='151.99.1.1/24', preferred='yes', virtual='no')
fvRsBdToEpRet2 = cobra.model.fv.RsBdToEpRet(fvBD2, resolveAct='resolve', tnFvEpRetPolName='')
fvCtx = cobra.model.fv.Ctx(fvTenant, ownerKey='', name='SHSHU2-VRF', descr='', knwMcastAct='permit', pcEnfDir='ingress', ownerTag='', pcEnfPref='enforced')
fvRsBgpCtxPol = cobra.model.fv.RsBgpCtxPol(fvCtx, tnBgpCtxPolName='')
fvRsCtxToExtRouteTagPol = cobra.model.fv.RsCtxToExtRouteTagPol(fvCtx, tnL3extRouteTagPolName='')
fvRsOspfCtxPol = cobra.model.fv.RsOspfCtxPol(fvCtx, tnOspfCtxPolName='')
vzAny = cobra.model.vz.Any(fvCtx, matchT='AtleastOne', name='', descr='')
fvRsCtxToEpRet = cobra.model.fv.RsCtxToEpRet(fvCtx, tnFvEpRetPolName='')
fvCtx2 = cobra.model.fv.Ctx(fvTenant, ownerKey='', name='SM-SHaredSVC-VRF', descr='', knwMcastAct='permit', pcEnfDir='ingress', ownerTag='', pcEnfPref='enforced')
fvRsBgpCtxPol2 = cobra.model.fv.RsBgpCtxPol(fvCtx2, tnBgpCtxPolName='')
fvRsCtxToExtRouteTagPol2 = cobra.model.fv.RsCtxToExtRouteTagPol(fvCtx2, tnL3extRouteTagPolName='')
fvRsOspfCtxPol2 = cobra.model.fv.RsOspfCtxPol(fvCtx2, tnOspfCtxPolName='')
vzAny2 = cobra.model.vz.Any(fvCtx2, matchT='AtleastOne', name='', descr='')
fvRsCtxToEpRet2 = cobra.model.fv.RsCtxToEpRet(fvCtx2, tnFvEpRetPolName='')
# vnsSvcCont = cobra.model.vns.SvcCont(fvTenant)
fvAp = cobra.model.fv.Ap(fvTenant, ownerKey='', prio='unspecified', name='SMSHCAPP1', descr='', ownerTag='')
fvAEPg = cobra.model.fv.AEPg(fvAp, isAttrBasedEPg='no', matchT='AtleastOne', name='SMSHCEPG1', prio='unspecified', descr='', pcEnfPref='unenforced')
fvRsConsIf = cobra.model.fv.RsConsIf(fvAEPg, tnVzCPIfName='exp-SM-SHSVC-SHL3-Conc', prio='unspecified')
fvRsConsIf2 = cobra.model.fv.RsConsIf(fvAEPg, tnVzCPIfName='EXP-SMSHP-Contract', prio='unspecified')
fvRsDomAtt = cobra.model.fv.RsDomAtt(fvAEPg, tDn='uni/vmmp-VMware/dom-UCSB-DVS_VSphere6.0', primaryEncap='unknown', classPref='encap', delimiter='', instrImedcy='lazy', encap='unknown', resImedcy='lazy')
fvRsBd = cobra.model.fv.RsBd(fvAEPg, tnFvBDName='SMSSHCBD')
fvRsCustQosPol = cobra.model.fv.RsCustQosPol(fvAEPg, tnQosCustomPolName='')
fvAp2 = cobra.model.fv.Ap(fvTenant, ownerKey='', prio='unspecified', name='SMSHU2APP', descr='', ownerTag='')
fvAEPg2 = cobra.model.fv.AEPg(fvAp2, isAttrBasedEPg='no', matchT='AtleastOne', name='SMSHU2', prio='unspecified', descr='', pcEnfPref='unenforced')
fvRsConsIf3 = cobra.model.fv.RsConsIf(fvAEPg2, tnVzCPIfName='exp-SMSHUSER2Contract', prio='unspecified')
fvRsDomAtt2 = cobra.model.fv.RsDomAtt(fvAEPg2, tDn='uni/vmmp-VMware/dom-UCSB-DVS_VSphere6.0', primaryEncap='unknown', classPref='encap', delimiter='', instrImedcy='lazy', encap='unknown', resImedcy='lazy')
fvRsBd2 = cobra.model.fv.RsBd(fvAEPg2, tnFvBDName='SMSHU2-BD')
fvRsCustQosPol2 = cobra.model.fv.RsCustQosPol(fvAEPg2, tnQosCustomPolName='')
fvRsTenantMonPol = cobra.model.fv.RsTenantMonPol(fvTenant, tnMonEPGPolName='')
vzCPIf = cobra.model.vz.CPIf(fvTenant, ownerKey='', name='exp-SM-SHSVC-SHL3-Conc', descr='', ownerTag='')
vzRsIf = cobra.model.vz.RsIf(vzCPIf, tDn='uni/tn-SM-SharedSVC-Provider/brc-SM-SHSVC-SHL3-Conc', prio='unspecified')
vzCPIf2 = cobra.model.vz.CPIf(fvTenant, ownerKey='', name='exp-SMSHUSER2Contract', descr='', ownerTag='')
vzRsIf2 = cobra.model.vz.RsIf(vzCPIf2, tDn='uni/tn-SM-SharedSVC-Provider/brc-SM-SHUER2Contract', prio='unspecified')
vzCPIf3 = cobra.model.vz.CPIf(fvTenant, ownerKey='', name='EXP-for-SHU2', descr='', ownerTag='')
vzRsIf3 = cobra.model.vz.RsIf(vzCPIf3, tDn='uni/tn-SM-SharedSVC-Provider/brc-allowAllSHU2', prio='unspecified')
vzCPIf4 = cobra.model.vz.CPIf(fvTenant, ownerKey='', name='EXP-SMSHP-Contract', descr='', ownerTag='')
vzRsIf4 = cobra.model.vz.RsIf(vzCPIf4, tDn='uni/tn-SM-SharedSVC-Provider/brc-SM-SHPContract', prio='unspecified')


# commit the generated code to APIC

fvTenant.delete()
c = cobra.mit.request.ConfigRequest()
c.addMo(fvTenant)
md.commit(c)
