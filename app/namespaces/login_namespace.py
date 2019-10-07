import os
import hashlib
import hmac

from flask import request
from flask_restplus import Namespace, Resource


api_login = Namespace("login", description="User login oauth2")


@api_login.route("/")
class Login(Resource):

    def _concat_params_to_string(self, params):
        params_for_hash = {key: params[key] for key in params.keys() if key != "hash"}
        key_value_list = []
        for key in sorted(params_for_hash.keys()):
            key_value_list.append(key+"="+params_for_hash[key])
        data_check_string = "\n".join(key_value_list)
        return data_check_string

    # def get(self):
    #     return {"test": "login"}

    def get(self):
        """
        Adds new user
        """
        user_data = {
            "id": request.args.get("id", None),
            "first_name": request.args.get("first_name", None),
            "last_name": request.args.get("last_name", None),
            "username": request.args.get("username", None),
            "photo_url": request.args.get("photo_url", None),
            "auth_date": request.args.get("auth_date", None),
            "hash": request.args.get("hash", None)
        }

        data_check_string = self._concat_params_to_string(user_data)
        data_check_string_bytes = bytes(data_check_string, "utf-8")

        secret_key = os.environ.get("ACCESS_TOKEN", None)
        secret_key_bytes = hashlib.sha256(secret_key.encode("utf-8")).digest()

        hmac_string = hmac.new(secret_key_bytes, data_check_string_bytes, hashlib.sha256).hexdigest()
        if hmac_string == user_data["hash"]:
            return {"status": "loged in successfully"}, 200



            