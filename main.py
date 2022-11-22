import os
from data_collector.data_collector import *

if __name__=="__main__":
   
    path=os.path.join(os.getcwd(),"dev.ini")
    
    url=get_value(path,"public_rest_api","url",interpolation=True)
    service_key=get_value(path,'public_rest_api','service_key',interpolation=True)
    params ={'serviceKey' :service_key, 'locdate' :20190101,'latitude' : 12659, 'longitude' : 3734, 'dnYn' : 'N'}
    
    geography=Geogrphy(url,params)
    #weather=Weather(url,params)
    
    url="http://127.0.0.1:5000/geo/indvidual" 
    # url="http://127.0.0.1:5000/weather/dateby"
    # weather.insert_data(url)
    geography.insert_data(url)