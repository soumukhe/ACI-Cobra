#!/usr/bin/env python
import argparse
#import ConfigParser
import getpass
import requests
import json


import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

#Future Config File Support
'''
conf_parser = argparse.ArgumentParser(
    # Turn off help, so we print all options in response to -h
        add_help=False
        )
conf_parser.add_argument("-c", "--conf_file",
                         help="Specify config file", metavar="FILE")
args, remaining_argv = conf_parser.parse_known_args()

conf = {
    "format" : "xml",
    "name" : "auto-export",
    "remotePort": "22",
    "apicuser": "admin",
    }

if args.conf_file:
    config = ConfigParser.SafeConfigParser()
    config.read([args.conf_file])
    conf = dict(config.items("Export"))

# Don't surpress add_help here so it will handle -h
parser = argparse.ArgumentParser(
    # Inherit options from config_parser
    parents=[conf_parser],
    # print script description with -h/--help
    description=__doc__,
    # Don't mess with format of description
    formatter_class=argparse.RawDescriptionHelpFormatter,
    )
parser.set_defaults(**conf)'''


parser = argparse.ArgumentParser(description="Small Utility to Create a Remote Location and Export Job")

parser.add_argument("-e", "--remote", type=str, required=True, help="Remote IP: ex. 127.0.0.1")
parser.add_argument("-p", "--path", type=str, required=True, help="Remote Path: ex. /Users/username/Downloads/")
parser.add_argument("-u", "--user", type=str, required=True, help="Remote Username")
parser.add_argument("-U", "--apicuser", type=str, required=True, help="APIC Admin username")
parser.add_argument("-a", "--apic", type=str, required=True, help="APIC URI: ex. https://10.0.0.1")
parser.add_argument("-f", "--format", type=str, default="xml", help="JSON or XML format")
parser.add_argument("-d", "--delete", nargs='?', default=False, const = True, type=bool, help="Delete Export Job")
#add support to trigger export
#parser.add_argument("-t", "--trigger", )

#Future Config File Support
#args = parser.parse_args(remaining_argv)

args = parser.parse_args()


#Base URL
base_url = args.apic + "/api/"

#Assemble Login URL
login_url = base_url + "aaaLogin.xml" 
#+ args.format

#Login Body Post
login_body = "<aaaUser name='" + args.apicuser + "' pwd='" + getpass.getpass(prompt='APIC Password:') + "' />"

#Post the Login
apic = requests.Session()
login_post = apic.post(login_url, data=json.dumps(login_body), verify=False)

if args.delete == True:
    print "Deleting Configurations"

#Collect the Cookie
#auth_cookie = login.cookies['APIC-Cookie']

#Assemble URL and Body for Export Location
remote_url = base_url + "/node/mo/uni/fabric.json"
remote_body = json.loads('{"fileRemotePath":{"attributes":{"remotePort":"22","name":"AG1B57", "host":"","protocol":"scp","remotePath":"","userName":"","userPasswd":"","status":"created"},"children":[]}}')

#Set Values based on User Inputs
remote_body['fileRemotePath']['attributes']['host'] = args.remote
remote_body['fileRemotePath']['attributes']['remotePath'] = args.path
remote_body['fileRemotePath']['attributes']['userName'] = args.user

if args.delete:
    print "Deleting Export Location"
    remote_body['fileRemotePath']['attributes']['status'] = 'deleted'
else:
    print "Creating Export Location"
    remote_body['fileRemotePath']['attributes']['userPasswd'] = getpass.getpass(prompt='Remote Location Password:')



#Post the Remote Location
remote_post = apic.post(remote_url, data=json.dumps(remote_body), verify=False)
if json.loads(remote_post.text)['totalCount'] == "0":
    print "Success"
else:
    raise IOError("Error: " + remote_post.text)



#Assemble URL and Body for Export Job
export_url = base_url + "/node/mo/uni/fabric.json"

export_body = json.loads('{"configExportP":{"attributes":{"name":"AG1B57","format":"xml","adminSt":"triggered","status":"created"},"children":[{"configRsRemotePath":{"attributes":{"tnFileRemotePathName":"AG1B57","status":"created,modified"},"children":[]}}]}}')
export_body['configExportP']['attributes']['format'] = args.format.lower()

if args.delete:
    print "Deleting Export"
    export_body = json.loads('{"configExportP":{"attributes":{"dn":"uni/fabric/configexp-AG1B57","status":"deleted"},"children":[]}}')

else:
    print "Creating Export Location"
    



#Post the Export
export_post = apic.post(export_url, data=json.dumps(export_body), verify=False)
if json.loads(export_post.text)['totalCount'] == "0":
    print "Success"
else:
    raise IOError("Error: " + export_post.text)
