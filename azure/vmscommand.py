import subprocess as s
import json

def runaz(command):
    try:
        results = json.loads(s.check_output(command, shell=True,stderr=s.STDOUT))
        print("command: "+command)
        print("results: "+str(results))
        return results
    except Exception as e:
        print("Errors: "+str(e))
        return "errors"
    
    
cmmnd_list_vms_with_rg="az vm list --show-details --query \"[?storageProfile.imageReference.offer && (storageProfile.imageReference.offer=='CentOS' || storageProfile.imageReference.offer=='UbuntuServer' )].{Type:storageProfile.imageReference.offer, Name:name, Rg:resourceGroup, Ip:privateIps}\" --output json"

for i in runaz(cmmnd_list_vms_with_rg):
    if i['Type']=='UbuntuServer':
        runaz("az vm run-command invoke --resource-group "+i["Rg"]+" --name "+i["Name"]+" --scripts \" date \" --command-id RunShellScript")
    if i['Type']=='CentOS':
        runaz("az vm run-command invoke --resource-group "+i["Rg"]+" --name "+i["Name"]+" --scripts \" date \" --command-id RunShellScript")

