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
from jsondiff import diff
            

def db_read(input_file):
    con = sqlite3.connect(input_file)
    cursor = con.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    for table in tables:
        print(table[0])
        
        cursor.execute("SELECT * FROM %s;" % table[0])
        rows = cursor.fetchall()
        num = len(rows)
        
        for i in range(num):
            a = json.loads(rows[i][1])
            
            if "displayProperties" in a:
                if "description" in a["displayProperties"]:
                    description = a["displayProperties"]["description"]
                if "name" in a["displayProperties"]:
                    name = a["displayProperties"]["name"]
                    if description == "Keep it secret.  Keep it safe." or name == "Classified":
                        print(a["displayProperties"]["description"])
                    
db_read("world_sql_content_4715157a8d3e073dccce96c62e065c67.content")
