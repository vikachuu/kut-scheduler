from flask import Blueprint
from flask_restplus import Api


blueprint = Blueprint('api', __name__)
api = Api(blueprint, doc='/docs')

from app.namespaces.user_namespace import api_user

api.add_namespace(api_user)



# @web_app.route("/api/v1/health")
# @api.route("health")
# def health():
#     """
#     Checking application.
#     """
#     return {"status": "ok"}
