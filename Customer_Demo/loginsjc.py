__author__ = 'soumukhe'
#!/usr/bin/env python
import urllib
import json
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

#  Login to APIC
# log into an APIC and create a directory object



def logen():
    ls = cobra.mit.session.LoginSession('https://<ip>', 'apic#fallback\\<user_name>', '<password>')
    md = cobra.mit.access.MoDirectory(ls)
    md.login()
    return md

"""
# LSC Login
def logen():
    ls = cobra.mit.session.LoginSession('https://10.92.97.203', 'admin', 'cisc0123')
    md = cobra.mit.access.MoDirectory(ls)
    md.login()
    return md

"""
