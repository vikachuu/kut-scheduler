import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.api import blueprint as api


web_app = Flask("KUT scheduler API")
web_app.config.from_object('config')

web_app.register_blueprint(api, url_prefix='/api/v1')

db = SQLAlchemy(web_app)

if __name__ == "__main__":
    web_app.run("0.0.0.0", 8080)
