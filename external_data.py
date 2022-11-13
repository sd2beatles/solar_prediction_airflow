from pydantic import BaseModel
from utilities.help_funciton import get_value 
from utilities.config import GeographyConfig
import requests
import xmltodict
import json
import urllib.parse
import os



class Base(object):
    def __init__(self,url,params):
        self.url=url
        self.params=GeographyConfig(**params)
    
    #rest_api provides two diffrent keys to authoerized users,
    #if you decide to use encoding key, set decoding as True.
    def get_data(self,method="xmltodict",decoding=False):
        if decoding==True:
            decode_key=urllib.parse.unquote(params['serviceKey'])
            params['serviceKey']=decode_key
                        
        response=requests.get(self.url,params=self.params)
        
        if method=="xmltodict":
            parsed_content=xmltodict.parse(response.content)
            result=json.loads(json.dumps(parsed_content))
        elif method=="utf-8":
            result=json.loads(response.content.decode("utf-8"))
        return result

            
        
        
class Geogrphy(Base):
    def __init__(self,url,params):
        super().__init__(url,params)

      
    def insert_data(self,dset_url):
        items=self.get_data()
        
        #only collect the relevant items 
        record=items['response']['body']['items']['item']
        return record
            
                    



if __name__=="__main__":
    
    path=os.path.join(os.getcwd(),"dev.ini")
    
    url=get_value(path,"public_rest_api","url",interpolation=True)
    service_key=get_value(path,'public_rest_api','service_key',interpolation=True)
    params ={'serviceKey' :service_key, 'locdate' :20150101,'latitude' : 12659, 'longitude' : 3734, 'dnYn' : 'N'}
    
    geography=Geogrphy(url,params)
    data=geography.insert_data('sdfd')
    print(data)

        
    
        
        

