import os
import hashlib
import hmac

from flask import request
from flask_restplus import Namespace, Resource

api_admin = Namespace('admin', description='Admin operations')


@api_admin.route("/")
class Admin(Resource):

    def post(self):
        """
        Add a new admin
        """
        from app.controllers.admin_controller import AdminController
        post_data = request.get_json()
        return AdminController.create_admin(post_data)

    def get(self):
        """
        Get list of all admins
        """
        from app.controllers.admin_controller import AdminController
        return AdminController.get_all_admins()


@api_admin.route("/login")
class AdminLogin(Resource):

    def _concat_params_to_string(self, params):
        params_for_hash = {key: params[key] for key in params.keys() if key != "hash"}
        
        data_check_string = ['{}={}'.format(k, v) for k, v in params_for_hash.items()]
        data_check_string = '\n'.join(sorted(data_check_string))
        return data_check_string

    def post(self):
        """
        Login admin through telegram
        """
        post_data = request.get_json()

        admin_data = {
            "id": post_data.get("id", None),
            "first_name": post_data.get("first_name", None),
            "last_name": post_data.get("last_name", None),
            "username": post_data.get("username", None),
            "photo_url": post_data.get("photo_url", None),
            "auth_date": post_data.get("auth_date", None),
            "hash": post_data.get("hash", None)
        }

        data_check_string = self._concat_params_to_string(admin_data)
        data_check_string_bytes = data_check_string.encode("utf-8")

        secret_key = os.environ.get("ACCESS_TOKEN", None)
        secret_key_bytes = hashlib.sha256(secret_key.encode("utf-8")).digest()

        hmac_string = hmac.new(secret_key_bytes, data_check_string_bytes, hashlib.sha256).hexdigest()

        # TODO: check
        # if hmac_string == user_data["hash"]:
        #     return {"status": "loged in successfully"}, 201
        # else:
        #     return {"fail": hmac_string,
        #             "hash": user_data["hash"]}, 400 

        # if everything is ok with telegram then
        from app.controllers.admin_controller import AdminController
        return AdminController.login_admin(admin_data)


@api_admin.route("/<int:id>")
class AdminId(Resource):
    def get(self, id):
        """
        Returns admin by admin_id
        """
        from app.controllers.admin_controller import AdminController
        return AdminController.get_admin_by_id(id)
