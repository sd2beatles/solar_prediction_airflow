from marshmallow import Schema,fields
from pkg_resources import require



class GeoSchema(Schema):
    locdate=fields.Str(required=True)
    location=fields.Str(required=True)
    altitudeMeridian=fields.Str()
    altitude_09=fields.Str()
    altitude_12=fields.Str()
    altitude_15=fields.Str()
    altitude_18=fields.Str()
    azimuth_09=fields.Str()
    azimuth_12=fields.Str()
    azimuth_15=fields.Str()
    azimuth_18=fields.Str()
 
 
class GeoParamSchema(Schema):
    locdate=fields.Str()
    location=fields.Str()
    
    
class GeoSearchAll(Schema):
    location=fields.Str()