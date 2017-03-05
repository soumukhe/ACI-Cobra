_author__ = 'soumukhe'
#!/usr/bin/env python
# Below Code is not using the Cobra SDK, but just pure json
import json
import urllib
import requests
requests.packages.urllib3.disable_warnings()
import ssl, socket




# base_url
base_url = "https://10.29.198.168/api/"

# Json Login Credentials
name_pwd = { "aaaUser" : { "attributes": {"name":"apic#fallback\\admin","pwd":"Br3adb@n"} } }
json_credentials = json.dumps(name_pwd, indent = 4)   #  make in pretty print json format


# *************Login to APIC************************
login_url = base_url + 'aaaLogin.json'
post_response = requests.post(login_url, data = json_credentials, verify = False) #  verify = False is needed because cert is self signed

# ***********Get Token from Login Response****************
auth = json.loads(post_response.text)  #  json dumps puts it in a dictionary of json items
# print json.dumps(auth, indent = 4)
login_attributes = auth['imdata'][0]['aaaLogin']['attributes']  #  drill down and get the attributes
auth_token = login_attributes['token']   # get the value of token from the key attributes

# Cookies
cookies = {}   # create empty dictionary
cookies['APIC-Cookie'] = auth_token  # APIC-Cookie is the required key for APIC

#********************** Now do your json Query********************
# find Tenants:  https://{{apic}}/api/node/class/fvTenant.json  ***  found from postman and visore

service_url = base_url + "node/class/fvTenant.json"
# print service_url
get_response = requests.get(service_url,  cookies = cookies, verify = False) #  verify = False is needed because cert is self signed

# print get_response.text    get_response looks like a dictionary, but it is actually unicode
# print type(get_response.text)

json_dict = json.loads(get_response.text)  #   json.loads creates a json array "dictionary" or list depending on initial { or [ in json data
# print type(json_dict)
nice_output = json.dumps(json_dict, indent = 4)  # json.dumps is pretty print json

print nice_output

print json_dict["imdata"][1]["fvTenant"]["attributes"]["dn"]  # show the Tenant 1 ( after 0), could have done 0 also

for Tenants in json_dict["imdata"]:
    print Tenants["fvTenant"]["attributes"]["dn"]  # drill down the structure to find the tenants