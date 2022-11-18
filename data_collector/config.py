from pydantic import BaseModel
from datetime import datetime

class GeographyConfig(BaseModel):
    serviceKey:str
    latitude:str
    longitude:str
    locdate:str
    dnYn:str



class WeatherConfig(BaseModel):
    serviceKey:str
    location:str
    locdatetime:str
    temperature:float
    precipitation_form:float
    precipitation_prob:float
    humidity:float
    wind_speed:float
    wind_direction:float
    cloud:float
    
    