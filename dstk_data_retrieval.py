# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 15:35:56 2017

@author: smandape
"""

import requests
#r = requests.get('http://www.datasciencetoolkit.org/maps/api/geocode/json?sensor=false&address=1600+Amphitheatre+Parkway+Mountain+View+CA')
r = requests.get('http://www.datasciencetoolkit.org/maps/api/geocode/json?sensor=false&address=895+Flag+Lake+Rd+Pottsville+AR')
lat = r.json()["results"][0]["geometry"]["location"]["lat"]
lng = r.json()["results"][0]["geometry"]["location"]["lng"]

print ("Lat: %s\nLng: %s\n" % (lat, lng) )




#json_encoded = json.dumps(r.json())
#print (json_encoded)
# 895+Flag+Lake+Rd+Pottsville+AR+72858+USA  