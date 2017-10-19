import requests
import json
 
#1 = xbox
#2 = psn
membershipType = 1

HEADERS = {"X-API-Key":'put your api thingy here'}

def get_userids(username):
    api_url = "https://www.bungie.net/Platform/Destiny2/SearchDestinyPlayer/%s/%s/" % (membershipType,username)
    res = requests.get(api_url, headers=HEADERS)
    
    error_stat = res.json()['ErrorStatus']
    if error_stat != "Success":
        print("Error status: " + error_stat + "\n")
        return False
        
    return res.json()["Response"][0]["membershipId"]
    
userid = get_userids("spiffomatic64")
api_url = "https://www.bungie.net/Platform/Destiny2/%s/Profile/%s/?components=Characters,CharacterProgressions" % (membershipType,userid)

res = requests.get(api_url, headers=HEADERS)

print(res)

error_stat = res.json()['ErrorStatus']
if error_stat != "Success":
    print("Error status: " + error_stat + "\n")

print(json.dumps(res.json(), indent=4, sort_keys=True))
