# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 13:06:40 2017

@author: smandape
This python script is for geocoding of addresses using a local copy of Data Science Toolkit (DSTK). 
addresses are provided in text format, one address on each line. 

"""

import re
import requests
import time


time_in = time.time()
with open("test_addresses_full_list_clean.txt", 'r') as infile, open("final_lat_lng_output.txt", "a") as f:
    for line in infile:
        line = line.rstrip('\n')
        line1 = re.sub('\s+','+', line.rstrip())
        r = requests.get('http://localhost:8080/maps/api/geocode/json?sensor=false&address=' + line1)
        lat = r.json()["results"][0]["geometry"]["location"]["lat"]
        lng = r.json()["results"][0]["geometry"]["location"]["lng"]
        #print ("Address: %s\tLat: %s\tLng: %s\n" % (line, lat, lng) )
        f.write("%s\t%s\t%s\n" % (line, lat, lng))
        
time_out = time.time()
total_time = time_out - time_in
print ("Time in mins = %f" % (total_time/60))