from pydantic import BaseModel

class GeographyConfig(BaseModel):
    serviceKey:str
    latitude:str
    longitude:str
    locdate:str
    dnYn:str
    