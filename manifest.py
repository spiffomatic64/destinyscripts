#! python3

import requests
import json
import urllib
import zipfile
import sqlite3
from jsondiff import diff
 
def get_manifest():
    # Uncomment this line to print JSON output to a file:
    #f = open('output.txt', 'w')
    membershipType = 1

    HEADERS = {"X-API-Key":'xxxxxxxxxxxxxxx'}
        
    xur_url = "https://bungie.net/Platform/Destiny2/Manifest"
    res = requests.get(xur_url, headers=HEADERS)

    error_stat = res.json()['ErrorStatus']
    if error_stat != "Success":
        print("Error status: " + error_stat + "\n")

    print(json.dumps(res.json(), indent=4, sort_keys=True))
    content_url = "http://bungie.net%s" % res.json()["Response"]["mobileWorldContentPaths"]["en"]
    print("Downloading url: %s" % content_url)
    
    urllib.request.urlretrieve(content_url,"world.content")
    
def extract_zip():
    zip_ref = zipfile.ZipFile("world.content", 'r')
    zip_ref.extractall(".")
    zip_ref.close()
    
def download_extract():
    get_manifest()
    extract_zip()
    

def db_read():
    con = sqlite3.connect('world_sql_content_6bc14cc5650f6485f655e5028b3cda26.content')
    con2 = sqlite3.connect('world_sql_content_91380328719f1363349daf43951cfbe3.content')
    cursor = con.cursor()
    cursor2 = con2.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    for table in tables:
        print(table[0])
        
        cursor.execute("SELECT * FROM %s;" % table[0])
        rows = cursor.fetchall()
        num = len(rows)
        
        cursor2.execute("SELECT * FROM %s;" % table[0])
        rows2 = cursor2.fetchall()
        
        for i in range(num):
            stuff = diff(json.loads(rows[i][1]),json.loads(rows2[i][1]))
            
            if len(stuff)>0:
                
                thing = str(stuff)
                real = 0
                for entry in stuff:
                    if str(stuff[entry]).find("destiny2_content")==-1:
                        real = 1
                
                if real==1:
                    print("Diff: %s" % stuff)
                    print("\tOld: %s" % rows2[i][1])
                    print("\tNew: %s" % rows[i][1])
                    print()
                
#get_manifest()
#download_extract()
db_read()
