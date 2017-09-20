import requests
import json

def get_json(url):
    #create an app to get your api key here: https://www.bungie.net/en-us/Application
    api_key = "<replace this with your api key>"
    HEADERS = {"X-API-Key":api_key}
    
    res = requests.get(url, headers=HEADERS)
    
    error_stat = res.json()['ErrorStatus']
    if error_stat != "Success":
        print("Error status: " + error_stat + "\n")
        
    return res.json()

#gets your userid from a username search for convenience 
def get_userid(username):
    data = get_json("https://www.bungie.net/Platform/Destiny2/SearchDestinyPlayer/1/%s/" % username)
    
    return data["Response"][0]["membershipId"]
    
def get_character(userid):
    data = get_json("https://www.bungie.net/Platform/Destiny2/1/Profile/%s/?components=Characters" % userid)
    
    characters = []
    for characterid in data["Response"]["characters"]["data"]:
        character = {}
        
        classtype = data["Response"]["characters"]["data"][characterid]["classType"]
        if classtype == 0:
             character["classType"] = "Titan"
        elif classtype == 1:
            character["classType"] = "Hunter"
        elif classtype == 2:
            character["classType"] = "Warlock"
        else:
            character["classType"] = classtype
        
        character["basePower"] = data["Response"]["characters"]["data"][characterid]["stats"]["1885944937"]
        character["power"] = data["Response"]["characters"]["data"][characterid]["light"]
        character["dateLastPlayed"] = data["Response"]["characters"]["data"][characterid]["dateLastPlayed"]
        character["minutesPlayedTotal"] = data["Response"]["characters"]["data"][characterid]["minutesPlayedTotal"]
        characters.append(character)
        
    return characters
    
username = input("Destiny username: ")
userid = get_userid(username)
characters = get_character(userid)

for character in characters:
    print("Class: %s basePower: %s Power: %s" % (character["classType"],character["basePower"],character["power"]))
