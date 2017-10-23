import requests
from qgis.core import *
from qgis.gui import *

@qgsfunction(args=0, group='Custom', usesgeometry=True)
def GetWeather(value1, feature, parent):
	centroid = feature.geometry()
	longitude = centroid.asPoint().x()
	latitude = centroid.asPoint().y()
	
	
	urlr ="http://api.openweathermap.org/data/2.5/weather?lat=" + str(latitude) + "&lon=" +str(longitude)+ "&appid=d04dc77f790e6650d77c8497ecacc289"    
	t = requests.get(urlr)
	w = t.json()
	return str(w)
	

# -*- coding: utf-8 -*-
import requests
import json
from qgis.core import *
from qgis.gui import *

@qgsfunction(args=0, group='Custom', usesgeometry=True)
def GetWeather(value1, feature, parent, data):
	centroid = feature.geometry()
	longitude = centroid.asPoint().x()
	latitude = centroid.asPoint().y()
	headers = {'content-type': 'application/json'}
	payload = {'lat': latitude, 'lon': longitude, 'units':'metric','lang':'fr','mode':'json','appid':'d04dc77f790e6650d77c8497ecacc289'}
	url = "http://api.openweathermap.org/data/2.5/weather"
	t = requests.get(url, params=payload, headers=headers).json()
	w = json.dumps(t)
	g = json.loads(w)
	h = json.dumps(g['weather'])
	j = json.dumps(g['weather'][0]['main'])
	p = json.dumps(data)
	print (h)
	print (j)
	print (p)
	return p