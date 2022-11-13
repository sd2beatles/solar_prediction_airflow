from flask import Flask
from flask_smorest import Api
from flask_jwt_extended import JWTManager
import secrets
from db import db
import os
import models 
from resources.geography import blp as GeoBluePrint


def create_app(db_url=None):

    app=Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"]=True
    app.config["API_TITLE"]="Stores REST API"
    app.config["API_VERSION"]="v1"
    app.config["OPENAPI_VERSION"]="3.0.3"
    app.config["OPENAPI_URL_PREFIX"]="/"
    app.config["OPENAPI_SWAGGER_UI_PATH"]="/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"]="https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"]=db_url or os.getenv("DATABASE_URL","sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATION"]=False
    db.init_app(app)
    api=Api(app)
    
    @app.before_first_request
    def create_tables():
        db.create_all()
    
    api.register_blueprint(GeoBluePrint)
    return app
        