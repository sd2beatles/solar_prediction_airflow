import sys
sys.path.append("..")
from db import db



class GeoModel(db.Model):
    
    locdate=db.Column(db.String(10),primary_key=True)
    location=db.Column(db.String(10),primary_key=True)
    altitudeMeridian=db.Column(db.String(20))
    altitude_09=db.Column(db.String(20))
    altitude_12=db.Column(db.String(20))
    altitude_15=db.Column(db.String(20))
    altitude_18=db.Column(db.String(20))
    azimuth_09=db.Column(db.String(20))
    azimuth_12=db.Column(db.String(20))
    azimuth_15=db.Column(db.String(20))
    azimuth_18=db.Column(db.String(20))
    