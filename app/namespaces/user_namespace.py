import os
import hashlib
import hmac

from flask import request
from flask_restplus import Namespace, Resource

api_user = Namespace('user', description='User operations')


@api_user.route("/")
class User(Resource):

    def get(self):
        """
        Return a list of users
        """
        from app.controllers.user_controller import UserController
        return UserController.get_all_users()

    def post(self):
        """
        Add a new user
        """
        from app.controllers.user_controller import UserController
        post_data = request.get_json()
        return UserController.create_user(post_data)


@api_user.route("/login")
class UserLogin(Resource):

    def _concat_params_to_string(self, params):
        params_for_hash = {key: params[key] for key in params.keys() if key != "hash"}
        
        data_check_string = ['{}={}'.format(k, v) for k, v in params_for_hash.items()]
        data_check_string = '\n'.join(sorted(data_check_string))
        return data_check_string

    def post(self):
        """
        Login user through telegram
        """
        post_data = request.get_json()

        user_data = {
            "id": post_data.get("id", None),
            "first_name": post_data.get("first_name", None),
            "last_name": post_data.get("last_name", None),
            "username": post_data.get("username", None),
            "photo_url": post_data.get("photo_url", None),
            "auth_date": post_data.get("auth_date", None),
            "hash": post_data.get("hash", None)
        }

        data_check_string = self._concat_params_to_string(user_data)
        data_check_string_bytes = data_check_string.encode("utf-8")

        secret_key = os.environ.get("ACCESS_TOKEN", None)
        secret_key_bytes = hashlib.sha256(secret_key.encode("utf-8")).digest()

        hmac_string = hmac.new(secret_key_bytes, data_check_string_bytes, hashlib.sha256).hexdigest()

        # if everything is ok with telegram then
        from app.controllers.user_controller import UserController
        return UserController.create_user(post_data)

        # TODO: check
        # if hmac_string == user_data["hash"]:
        #     return {"status": "loged in successfully"}, 201
        # else:
        #     return {"fail": hmac_string,
        #             "hash": user_data["hash"]}, 400


@api_user.route("/<int:id>")
class UserId(Resource):
    def get(self, id):
        """
        Returns user by user_id
        """
        from app.controllers.user_controller import UserController
        return UserController.get_user_by_id(id)

    def put(self, id):
        """
        Edits a selected user
        """
