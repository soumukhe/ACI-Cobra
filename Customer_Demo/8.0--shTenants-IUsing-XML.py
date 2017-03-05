__author__ = 'soumukhe'
#!/usr/bin/env python
import urllib
import requests
requests.packages.urllib3.disable_warnings()
import ssl, socket
import xml.etree.ElementTree as ET
import getcookies

cookies = getcookies.getcookies()
base_url = getcookies.base_url

#********************** Now do your json Query********************
# find Tenants:  https://{{apic}}/api/node/class/fvTenant.json

service_url = base_url + "node/class/fvTenant.xml"
# print service_url
get_response = requests.get(service_url,  cookies = cookies, verify = False)#  verify = False is needed because cert is self signed


print get_response.text  #  This is the XML

tree = ET.fromstring(get_response.text)    # Element Tree of XML

print tree

Tenants = tree.findall("./fvTenant")  #  go down one level deep and find fvTenant

for Tenant in Tenants:
    print Tenant.get("dn")  # if you look at the XML file,  "dn" is an attribute

