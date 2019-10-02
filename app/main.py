from flask import Flask
from app.api import blueprint as api


web_app = Flask("KUT scheduler API")
web_app.register_blueprint(api, url_prefix='/api/v1')


if __name__ == "__main__":
    web_app.run("0.0.0.0", 8080)
