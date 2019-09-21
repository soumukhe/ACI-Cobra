__author__ = 'soumukhe'
#!/usr/bin/env python

# Kindly make sure that you have the modules threading and websocket client installed also.  "pip install threading"    "pip install websocket-client"
# Please use python 3

import requests
requests.packages.urllib3.disable_warnings()
import json
import ssl
import websocket
import threading
import schedule
import time
import sys

# Ensure using python3
if sys.version_info[0] < 3:
    raise Exception("Must be using Python 3")

#Please put in IP for APIC and Credentials here:
APIC = "APIC IP"
user = "Username"
password = "Password"




URL = "https://" + APIC + "/api/aaaLogin.json"
BODY = {"aaaUser": {"attributes": {"name": user, "pwd": password}}}

# websocket_url = "wss://" + APIC + "/socket{}".format(token)


def getCookie():
    global cookie
    global token
    login_response = requests.post(URL, json=BODY, verify=False)
    response_body = login_response.content
    # convert response_body to a dict
    response_body_dictionary = json.loads(response_body)
    #print(response_body_dictionary)
    #collect token for authentication
    token = response_body_dictionary["imdata"][0]["aaaLogin"]["attributes"]["token"]
    #print (token)
    cookie = {"APIC-cookie": token}
    #print (cookie)
    return cookie




def WSocket():
    # This module starts the initial connect to the APIC Web Socket
    global ws
    websocket_url = "wss://" + APIC + "/socket{}".format(token)
    ws = websocket.create_connection(websocket_url, sslopt={"cert_reqs": ssl.CERT_NONE})
    print( "WebSocket Subscription Status Code: ", ws.status)
    #print (type(ws))
    #return ws


def Subscribe():
    # This module subscribes to interested objects in ACI
    global tenant_subscription_id
    global bd_subscription_id
    global epg_subscription_id
    global app_profile_subscription_id
    global vrf_subscription_id
    global aaalogin_subscription_id
    global aaalogout_subscription_id




    # subscribe to fvTenant
    tenant_url = "https://" + APIC + "/api/class/fvTenant.json?subscription=yes&refresh-timeout=60?query-target=subtree"
    #print (tenant_url)
    tenant_subscription = requests.get(tenant_url, verify=False, cookies=cookie)
    json_dict = json.loads(tenant_subscription.text)
    nice_output = json.dumps(json_dict, indent=4)
    # print (nice_output)
    tenant_subscription_id = json_dict["subscriptionId"]
    print ("Tenant-Subscription ID: ", tenant_subscription_id)
    # return tenant_subscription_id

    # subscribe to fvBD
    bd_url = "https://" + APIC + "/api/class/fvBD.json?subscription=yes&refresh-timeout=3600?query-target=subtree"
    bd_subscription = requests.get(bd_url, verify=False, cookies=cookie)
    json_dict = json.loads(bd_subscription.text)
    nice_output = json.dumps(json_dict, indent=4)
    # print (nice_output)
    bd_subscription_id = json_dict["subscriptionId"]
    print("BD-Subscription ID: ", bd_subscription_id)

    # subscribe to fvAEPg
    epg_url = "https://" + APIC + "/api/class/fvAEPg.json?subscription=yes&refresh-timeout=60?query-target=subtree"
    epg_subscription = requests.get(epg_url, verify=False, cookies=cookie)
    json_dict = json.loads(epg_subscription.text)
    nice_output = json.dumps(json_dict, indent=4)
    # print (nice_output)
    epg_subscription_id = json_dict["subscriptionId"]
    print("epg-Subscription ID: ", epg_subscription_id)

    # subscribe to fvAp
    APP_Profile_url = "https://" + APIC + "/api/class/fvAp.json?subscription=yes&refresh-timeout=60?query-target=subtree"
    APP_Profile_subscription = requests.get(APP_Profile_url, verify=False, cookies=cookie)
    json_dict = json.loads(APP_Profile_subscription.text)
    nice_output = json.dumps(json_dict, indent=4)
    # print (nice_output)
    app_profile_subscription_id = json_dict["subscriptionId"]
    print("APP_Profile-Subscription ID: ", app_profile_subscription_id)

    # subscribe to fvCtx
    APP_Profile_url = "https://" + APIC + "/api/class/fvCtx.json?subscription=yes&refresh-timeout=60?query-target=subtree"
    APP_Profile_subscription = requests.get(APP_Profile_url, verify=False, cookies=cookie)
    json_dict = json.loads(APP_Profile_subscription.text)
    nice_output = json.dumps(json_dict, indent=4)
    # print (nice_output)
    vrf_subscription_id = json_dict["subscriptionId"]
    print("VRF Subscription ID: ", vrf_subscription_id)

    # subscribe to aaaActiveUserSession - created
    AAALogin_url = "https://"  + APIC + "/api/class/aaaActiveUserSession.json?subscription=yes&refresh-timeout=60?query-target=self&query-target-filter=and(wcard(aaaActiveUserSession.status,\"created\"))"
    AAALogin_subscription = requests.get(AAALogin_url, verify=False, cookies=cookie)
    json_dict = json.loads(AAALogin_subscription.text)
    nice_output = json.dumps(json_dict, indent=4)
    #print (nice_output)
    aaalogin_subscription_id = json_dict["subscriptionId"]
    print("AAALogin-Subscription ID: ", aaalogin_subscription_id)
    #
    # subscribe to aaaActiveUserSession - deleted
    AAALogout_url = "https://" + APIC + "/api/class/aaaActiveUserSession.json?subscription=yes&refresh-timeout=60?query-target=self&query-target-filter=and(wcard(aaaActiveUserSession.status,\"deleted\"))"
    AAALogout_subscription = requests.get(AAALogout_url, verify=False, cookies=cookie)
    json_dict = json.loads(AAALogout_subscription.text)
    nice_output = json.dumps(json_dict, indent=4)
    #print (nice_output)
    aaalogout_subscription_id = json_dict["subscriptionId"]
    print("AAALogout-Subscription ID: ", aaalogout_subscription_id)
    print ("\n" * 2 )

def printws():
    while True:
        print(ws.recv())




def refresh():
    # This module refreshes the subscription.  Default Timeout for refresh is 60 seconds as also hardcoded in the subscription module "refresh-timeout=60"
    while True:
        time.sleep(30)
        # refresh subscription  -- fvTenant
        tenant_refresh_url = "https://" + APIC + "/api/subscriptionRefresh.json?id={}".format(tenant_subscription_id)
        tenant_refresh_response = requests.get(tenant_refresh_url, verify=False, cookies=cookie)
        #print(tenant_refresh_response.content)
        #
        # refresh subscription  -- fvBD
        tenant_refresh_url = "https://" + APIC + "/api/subscriptionRefresh.json?id={}".format(bd_subscription_id)
        tenant_refresh_response = requests.get(tenant_refresh_url, verify=False, cookies=cookie)
        #print(tenant_refresh_response.content)
        #
        # refresh subscription  -- fvAEPg
        tenant_refresh_url = "https://" + APIC + "/api/subscriptionRefresh.json?id={}".format(epg_subscription_id)
        tenant_refresh_response = requests.get(tenant_refresh_url, verify=False, cookies=cookie)
        #print(tenant_refresh_response.content)
        #
        # refresh subscription  -- fvAp
        tenant_refresh_url = "https://" + APIC + "/api/subscriptionRefresh.json?id={}".format(app_profile_subscription_id)
        tenant_refresh_response = requests.get(tenant_refresh_url, verify=False, cookies=cookie)
        #print(tenant_refresh_response.content)
        #
        # refresh subscription  -- fvCtx
        tenant_refresh_url = "https://" + APIC + "/api/subscriptionRefresh.json?id={}".format(vrf_subscription_id)
        tenant_refresh_response = requests.get(tenant_refresh_url, verify=False, cookies=cookie)
        # print(tenant_refresh_response.content)
        #
        # refresh subscription  -- aaaActiveUserSession - Status Created
        tenant_refresh_url = "https://" + APIC + "/api/subscriptionRefresh.json?id={}".format(aaalogin_subscription_id)
        tenant_refresh_response = requests.get(tenant_refresh_url, verify=False, cookies=cookie)
        #print(tenant_refresh_response.content)
        #
        # refresh subscription  -- aaaActiveUserSession - Status Deleted
        tenant_refresh_url = "https://" + APIC + "/api/subscriptionRefresh.json?id={}".format(aaalogout_subscription_id)
        tenant_refresh_response = requests.get(tenant_refresh_url, verify=False, cookies=cookie)
        # print(tenant_refresh_response.content)

def startThreading():
    th = threading.Thread(target=printws)
    th1 = threading.Thread(target=refresh)
    th.start()
    th1.start()



if __name__ == "__main__":

    cookie = getCookie()
    #print (cookie)
    token =  (cookie["APIC-cookie"])
    #print (token)
    print("\n" * 2)
    print ("*" * 10, "WebSocket Subscription Status & Messages", "*" * 10)
    WSocket()
    Subscribe()
    startThreading()


