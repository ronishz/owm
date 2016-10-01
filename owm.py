#key=386d48296ba54ccd7de07205a3fd843b
import requests
#524901
from pprint import pprint
q1=raw_input("Enter name of city")
r=requests.get("http://api.openweathermap.org/data/2.5/forecast/city?q="+q1+"&APPID=386d48296ba54ccd7de07205a3fd843b")
pprint(r.json())
