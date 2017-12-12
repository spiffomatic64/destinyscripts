#! python3

import requests
import json
import urllib
import zipfile
import sqlite3
import glob
import os
import platform
import time
import datetime
from jsondiff import diff
            
# Use the manifest script to download the DB, then this script to parse/download images
# Yea I could automate it together, but im lazy

def get_items_description(input):
    con = sqlite3.connect(input)
    cursor = con.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    cursor.execute("SELECT * FROM %s;" % "DestinyInventoryItemDefinition")
    rows = cursor.fetchall()
    num = len(rows)
    
    items = {}
    
    for i in range(num):
        value = ""
        a = json.loads(rows[i][1])
        if "displayProperties" in a and "hash" in a:
            name = ""
            if "name" in a["displayProperties"]:
                if len(a["displayProperties"]["name"])>0:
                    name = a["displayProperties"]["name"]
            
            description = ""
            if "description" in a["displayProperties"]:
                if len(a["displayProperties"]["description"])>0:
                    description = a["displayProperties"]["description"]
                    
            icon = ""
            if "icon" in a["displayProperties"]:
                if len(a["displayProperties"]["icon"])>0:
                    icon = a["displayProperties"]["icon"]
            
            if icon != "":
                items[a["hash"]] = [name, description, icon]
            #print("%s - %s" % (a["hash"], value))

    return items
                


stuff = get_items_description("../world_sql_content_5b6870694dc15572dc92beb29a1693d2.content")

for thing in stuff:
    bungie_url = "https://bungie.net%s" % stuff[thing][2]
    filename = "%s.%s" % (stuff[thing][0],stuff[thing][2][-3:])
    filename = filename.replace(" ","_")
    filename = filename.replace("/","-")
    filename = filename.replace("\"","'")
    
    print("Filename: %s Icon: %s" % (filename,bungie_url))
    
    urllib.request.urlretrieve(bungie_url,filename)
