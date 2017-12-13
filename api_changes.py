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
       
#should get this from the table in case of changes, but hardcoding for now
bucket_types = { 2422292810 : "Engram",
2465295065 : "Energy Weapons",
2689798304 : "Upgrade Point",
2689798305 : "Strange Coin",
2689798308 : "Glimmer",
2689798309 : "Legendary Shards",
2689798310 : "Silver",
2689798311 : "Bright Dust",
2973005342 : "Shaders",
3054419239 : "Emotes",
3161908920 : "Messages",
3284755031 : "Subclass",
3313201758 : "Modifications",
3448274439 : "Helmet",
3551918588 : "Gauntlets",
3621873013 : "Classification",
3796357825 : "3796357825",
3865314626 : "Materials",
4023194814 : "Ghost",
4274335291 : "Emblems",
4292445962 : "Clan Banners",
14239492 : "Chest Armor",
18606351 : "Shaders",
20886954 : "Leg Armor",
138197802 : "General",
215593132 : "Lost Items",
284967655 : "Ships",
375726501 : "Engrams",
444348033 : "444348033",
497170007 : "497170007",
953998645 : "Power Weapons",
1269569095 : "Auras",
1367666825 : "Special Orders",
1469714392 : "Consumables",
1498876634 : "Kinetic Weapons",
1585787867 : "Class Armor",
1626737477 : "1626737477",
1801258597 : "Bounty",
2025709351 : "Vehicle" }

def db_read(input_file):
    con = sqlite3.connect(input_file)
    cursor = con.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    stuff = {}
    
    for table in tables:
        #print(table[0])
        
        cursor.execute("SELECT * FROM %s;" % table[0])
        rows = cursor.fetchall()
        num = len(rows)
        
        for i in range(num):
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
                        
                itemTypeDisplayName = ""
                if "itemTypeDisplayName" in a:
                    if len(a["itemTypeDisplayName"])>0:
                        itemTypeDisplayName = a["itemTypeDisplayName"]
                        
                tooltipStyle = ""
                if "tooltipStyle" in a:
                    if len(a["tooltipStyle"])>0:
                        tooltipStyle = a["tooltipStyle"]
                        
                bucketTypeHash = ""
                tierTypeName = ""
                
                if "inventory" in a:
                    if "bucketTypeHash" in a["inventory"]:
                        if a["inventory"]["bucketTypeHash"]>0:
                            bucketTypeHash = bucket_types[a["inventory"]["bucketTypeHash"]]
                    if "tierTypeName" in a["inventory"]:
                        if len(a["inventory"]["tierTypeName"])>0:
                            tierTypeName = a["inventory"]["tierTypeName"]
                        
                stuff[a["hash"]] = [name, description, icon, itemTypeDisplayName, tooltipStyle, bucketTypeHash, tierTypeName, table]
            
    return stuff

old_items = db_read("world_sql_content_5b6870694dc15572dc92beb29a1693d2.content")
new_items = db_read("world_sql_content_4715157a8d3e073dccce96c62e065c67.content")

removed_items = {}
changed = {}

for item in old_items:
    if item in new_items:
        if old_items[item][0] != new_items[item][0] or old_items[item][1] != new_items[item][1]:
            changed[item] = []
            changed[item].append("%s - %s" % (old_items[item][0],new_items[item][0]))
            changed[item].append("%s - %s" % (old_items[item][1],new_items[item][1]))
            changed[item].append(new_items[item][2])
            changed[item].append("%s - %s" % (old_items[item][3],new_items[item][3]))
            changed[item].append("%s - %s" % (old_items[item][4],new_items[item][4]))
            changed[item].append("%s" % (new_items[item][7]))
        del new_items[item]
    else:
        removed_items[item] = old_items[item]
        
print('<html>')
print('<head>')
print('    <meta http-equiv="X-UA-Compatible" content="IE=edge">')
print('    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">')
print('    <meta name="viewport" content="width=device-width, initial-scale=1">')
print('    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->')
print('    <title>New CoO stuff</title>')
print('')
print('    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">')
print('    <link href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-table/1.11.1/bootstrap-table.css" rel="stylesheet">')
print('    <link href="https://drvic10k.github.io/bootstrap-sortable/Contents/bootstrap-sortable.css" rel="stylesheet">')
print('')
print('</head>')
print('')
print('<body bgcolor="lightgrey">')
print('<h1>New Stuff</h1>')
print('<table class="table table-bordered table-striped sortable">')
print('<thead>')
print(' <tr>')
print('     <th>Hash</th>')
print('     <th>Table</th>')
print('     <th>Name</th>')
print('     <th>Description</th>')
print('     <th>Type</th>')
print('     <th>ToolTipStyle</th>')
print('     <th>Icon</th>')
print(' </tr>')
print('</thead>')
print('<tbody> ')

for item in new_items:
    print(" <tr>")
    print("  <td>")
    print("   %s" % item)
    print("  </td>")
    
    print("  <td>")
    print("   %s" % new_items[item][7])
    print("  </td>")
    
    print("  <td>")
    print("   %s" % new_items[item][0])
    print("  </td>")
    
    print("  <td>")
    print("   %s" % new_items[item][1])
    print("  </td>")
    
    print("  <td>")
    print("   %s" % new_items[item][3])
    print("  </td>")
    
    print("  <td>")
    print("   %s" % new_items[item][4])
    print("  </td>")
    
    print("  <td>")
    if new_items[item][2] != "":
        print("   <img src=\"https://bungie.net%s\">" % new_items[item][2])
    print("  </td>")
    
    print(" </tr>")
    
print('     </tbody>')
print('</table>')

print('<h1>Changed Stuff</h1>')
print('<table class="table table-bordered table-striped sortable">')
print('<thead>')
print(' <tr>')
print('     <th>Hash</th>')
print('     <th>Table</th>')
print('     <th>Name</th>')
print('     <th>Description</th>')
print('     <th>Type</th>')
print('     <th>ToolTipStyle</th>')
print('     <th>Icon</th>')
print(' </tr>')
print('</thead>')
print('<tbody> ')

for item in changed:
    print(" <tr>")
    print("  <td>")
    print("   %s" % item)
    print("  </td>")
    
    print("  <td>")
    print("   %s" % changed[item][5])
    print("  </td>")
    
    print("  <td>")
    print("   %s" % changed[item][0])
    print("  </td>")
    
    print("  <td>")
    print("   %s" % changed[item][1])
    print("  </td>")
    
    print("  <td>")
    print("   %s" % changed[item][3])
    print("  </td>")
    
    print("  <td>")
    print("   %s" % changed[item][4])
    print("  </td>")
    
    print("  <td>")
    if changed[item][2] !="":
        print("   <img src=\"https://bungie.net%s\">" % changed[item][2])
    print("  </td>")
    
    print(" </tr>")
    
print('     </tbody>')
print('</table>')

print('<h1>Removed Stuff</h1>')
print('<table class="table table-bordered table-striped sortable">')
print('<thead>')
print(' <tr>')
print('     <th>Hash</th>')
print('     <th>Table</th>')
print('     <th>Name</th>')
print('     <th>Description</th>')
print('     <th>Type</th>')
print('     <th>ToolTipStyle</th>')
print('     <th>Icon</th>')
print(' </tr>')
print('</thead>')
print('<tbody> ')

for item in removed_items:
    print(" <tr>")
    print("  <td>")
    print("   %s" % item)
    print("  </td>")
    
    print("  <td>")
    print("   %s" % removed_items[item][7])
    print("  </td>")
    
    print("  <td>")
    print("   %s" % removed_items[item][0])
    print("  </td>")
    
    print("  <td>")
    print("   %s" % removed_items[item][1])
    print("  </td>")
    
    print("  <td>")
    print("   %s" % removed_items[item][3])
    print("  </td>")
    
    print("  <td>")
    print("   %s" % removed_items[item][4])
    print("  </td>")
    
    print("  <td>")
    if removed_items[item][2] !="":
        print("   <img src=\"https://bungie.net%s\">" % removed_items[item][2])
    print("  </td>")
    
    print(" </tr>")
    
print('     </tbody>')
print('</table>')

print('')
print('<!-- jQuery (necessary for Bootstrap\'s JavaScript plugins) -->')
print('    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>')
print('    <!-- Include all compiled plugins (below), or include individual files as needed -->')
print('    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>')
print('    <script src="https://drvic10k.github.io/bootstrap-sortable/Scripts/bootstrap-sortable.js"></script>')
print('')
print('')
print('')
print('</body>')
print('</html>')
