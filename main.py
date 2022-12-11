import os
from data_collector.data_collector import *
import argparse

'''
    Input the final destination url. Just remember that the address must
    be linked to our code in the section of backend. 
    
    In the case of weather class, the codes are as follows; 
    
    url="http://127.0.0.1:5000/weather/dateby"
    weather=Weather(url,params)
    weather.insert_data(url)
    
'''



if __name__=="__main__":
    
    #insert your path
    path="/mnt/d/solar_prediction/new/dev.ini"
    
    #obtain required information for retrieving public data
    url=get_value(path,"public_rest_api","url",interpolation=True)
    service_key=get_value(path,'public_rest_api','service_key',interpolation=True)
    
    #input the required information for your parameters
    params ={'serviceKey' :service_key, 'locdate' :20190101,'latitude' : 12659, 'longitude' : 3734, 'dnYn' : 'N'}
    
    #instaniate the Geography class
    geography=Geogrphy(url,params)
   

    dest_url="http://127.0.0.1:5000/geo/indvidual" 
        
    #run the class function to send the retrieve data to the MySQL database
    geography.insert_data(dest_url)