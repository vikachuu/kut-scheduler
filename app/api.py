from flask import Blueprint
from flask_restplus import Api


blueprint = Blueprint('api', __name__)
api = Api(blueprint, doc='/docs')

from app.namespaces.health_namespace import api_health
from app.namespaces.user_namespace import api_user
from app.namespaces.login_namespace import api_login

api.add_namespace(api_health)
api.add_namespace(api_user)
api.add_namespace(api_login)
