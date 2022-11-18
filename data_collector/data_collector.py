import os  
from pydantic import BaseModel
from .config import GeographyConfig,WeatherConfig
from configparser import ConfigParser
import requests
import xmltodict
import json
import urllib.parse




def get_value(path,key,value,interpolation=True):
    # if you want to avoid interpolation,set interpolation as False
    parser=ConfigParser() if interpolation else ConfigParser(interpolation=None)
    
    parser.read(path)
    return parser.get(key,value)



class Base(object):
    def __init__(self,url):
        self.url=url
       
    #rest_api provides two diffrent keys to authoerized users,
    #if you decide to use encoding key, set decoding as True.
    def get_data(self,params,method="xmltodict",decoding=False):
        if decoding==True:
            decode_key=urllib.parse.unquote(params['serviceKey'])
            params['serviceKey']=decode_key
                        
        response=requests.get(self.url,params=params)
        
        if method=="xmltodict":
            parsed_content=xmltodict.parse(response.content)
            result=json.loads(json.dumps(parsed_content))
        elif method=="utf-8":
            result=json.loads(response.content.decode("utf-8"))
        return result
    



class Weather(Base):
    def __init__(self, url, params):
        super().__init__(url)
        #self.params=WeatherConfig(**params)
        self.params=params
        self.fields=["location",
                    "locdatetime",
                     "temperature",
                     "precipitation_form",
                     "precipitation_prob",
                     "humidity",
                     "wind_speed",
                     "wind_direction",
                     "cloud"]
        
    def insert_data(self,dest_url):
        try:
            #items=self.get_data(self.params)
            record={"location":"Seoul",
                    "locdatetime":"fmt:234 mt:234 dt:2 234T07:00:00",
                    "temperature":23.23,
                    "precipitation_form":11,
                    "precipitation_prob":0.3,
                    "humidity":23.3,
                    "wind_speed":11.2,
                    "wind_direction":23.1,
                    "cloud":11}
            
            #only collect the relevant items
            #record=items['response']['body']['items']['item']
            data={key:value for key,value in record.items() if key in self.fields}
            result=requests.put(dest_url,json=data)
            
            print(result.status_code)
        except:
            pass
    
    
            
        
        
class Geogrphy(Base):
    def __init__(self,url,params):
        super().__init__(url)
        
        self.params=GeographyConfig(**params)
        self.fields=['location',
                'locdate',
                'altitudeMeridian',
                'altitude_09',
                'altitude_12',
                'altitude_15',
                'altitude_18',
                'azimuth_09',
                'azimuth_12',
                'azimuth_15',
                'azimuth_18']

    #dest_url refers to the end url where we want to send our geo information
    def insert_data(self,dest_url):
        
        items=self.get_data(self.params)
        
        #only collect the relevant items 
        record=items['response']['body']['items']['item']
        data={key:value for key,value in record.items() if key in self.fields}
        
        #post the information
        data=requests.put(dest_url,json=data)
      
        
 
     
        


        
    
        
        

