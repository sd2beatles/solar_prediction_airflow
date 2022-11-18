from flask import Flask
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from resources.geography import blp as GeoBluePrint
from resources.weather import blp as WeatherPrint
from data_collector.help_funciton import get_value
from db import db



def create_app(db_url=None):
    user,passwd=get_value('../dev.ini','mysql','user'),get_value('../dev.ini','mysql','password')
    app=Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"]=True
    app.config["API_TITLE"]="Stores REST API"
    app.config["API_VERSION"]="v1"
    app.config["OPENAPI_VERSION"]="3.0.3"
    app.config["OPENAPI_URL_PREFIX"]="/"
    app.config["OPENAPI_SWAGGER_UI_PATH"]="/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"]="https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    #app.config["SQLALCHEMY_DATABASE_URI"]=db_url or os.getenv("DATABASE_URL","sqlite:///data.db")
    app.config["SQLALCHEMY_DATABASE_URI"]="mysql+pymysql://{0}:{1}@127.0.0.1:3306/solardb"\
        .format(user,passwd)
    app.config["SQLALCHEMY_TRACK_MODIFICATION"]=False
    db.init_app(app)
    api=Api(app)
    
    @app.before_first_request
    def create_tables():
        db.create_all()
    
    api.register_blueprint(GeoBluePrint)
    api.register_blueprint(WeatherPrint)
    return app
        