import sys
sys.path.append("..")

from flask import request,make_response
from flask.views import MethodView
from flask_smorest import Blueprint,abort
from sqlalchemy.exc import SQLAlchemyError
from schema import GeoSchema,GeoParamSchema,GeoSearchAll
from models.geography import GeoModel
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError,IntegrityError
from db import db


blp=Blueprint("geography",__name__,description="Operation on Geo Information")

#
#{'altitudeMeridian': '29˚ 24´', 'altitude_09': '11˚ 04´', 'altitude_12': '28˚ 50´', 'altitude_15': '20˚ 31´', 'altitude_18': '-07˚ 14´', 'azimuth_09': '130˚ 49´', 'azimuth_12': '170˚ 43´', 'azimuth_15': '215˚ 26´', 'azimuth_18': '246˚ 27´', 'latitude': '3733', 'latitudeNum': '37.5500000', 'location': '서울', 'locdate': '20150101', 'longitude': '12658', 'longitudeNum': '126.9666660'}
@blp.route("/geo/indvidual")
class GeoList(MethodView):
    @blp.arguments(GeoParamSchema)
    @blp.response(200,GeoSchema)
    def get(self,record):
        data=GeoModel.query.filter_by(location=record['location'],locdate=record['locdate']).first()
        return data
    
    @blp.arguments(GeoSchema)
    @blp.response(200,GeoSchema)
    def put(self,record):
        match=GeoModel(**record)
        try:
            db.session.add(match)
            db.session.commit()
            
        except IntegrityError:
            abort(400,message="The current infomration has alread exists")
            
        return record
            
    @blp.arguments(GeoParamSchema)
    def delete(self,record):
        data=GeoModel.query.filter_by(location=record['location'],locdate=record['locdate']).first()
        if data:
            db.session.delete(data)
            db.session.commit()
            return make_response({"message":"The selected item deleted!"},200)
        else:
            return make_response({"message":"The item not found!"},404)
        
@blp.route("/geo")
class GeoList(MethodView):
    @blp.arguments(GeoSearchAll)
    @blp.response(200,GeoSchema(many=True))
    def get(self,record):
        data=GeoModel.query.filter_by(location=record['location']).all()
        return data
    
        
        





