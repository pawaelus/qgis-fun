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