import requests 
from pprint import pprint
Response=requests.get("https://api.ipify.org/?format=json")
IPDict=Response.json()
#print(type(IPDict))
pprint(IPDict)
MyIp=IPDict['ip']
LocDict=requests.get("https://ipinfo.io/"+MyIp+"/geo").json()
pprint(LocDict['loc'])