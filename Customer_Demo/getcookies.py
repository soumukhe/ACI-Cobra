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

def getcookies():

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
    # print cookies
    return cookies

getcookies()

