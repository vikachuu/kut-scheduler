from app.models.admin_model import Admin
from app.main import db

class AdminController:

    @staticmethod
    def create_admin(post_data):
        admin = Admin.query.filter_by(admin_id=post_data.get('id')).first()
        if not admin:
            admin = Admin(
                admin_id=post_data.get('id'),
                first_name=post_data.get('first_name'),
                last_name=post_data.get('last_name'),
                username=post_data.get('username'),
                photo_url=post_data.get('photo_url'),
                is_superadmin=post_data.get('is_superadmin')
            )

            db.session.add(admin)
            db.session.commit()

            return {"data": {
                            "admin": {
                                "admin_id": admin.admin_id,
                                "first_name": admin.first_name,
                                "last_name": admin.last_name,
                                "username": admin.username,
                                "photo_url": admin.photo_url,
                                "is_superadmin": admin.is_superadmin
                            },
                        "status": 201,
                        "error": None
                        }}
        else:
            return {"data": {
                        "admin": {
                            "admin_id": admin.admin_id,
                            "first_name": admin.first_name,
                            "last_name": admin.last_name,
                            "username": admin.username,
                            "photo_url": admin.photo_url,
                            "is_superadmin": admin.is_superadmin
                        },
                    "status": 200,
                    "error": f"Admin {admin.username} already exists."
                    }}

    @staticmethod
    def login_admin(post_data):
        admin = Admin.query.filter_by(admin_id=post_data.get('id')).first()
        if not admin:
            return {"data": {
                        "admin": None,
                    "status": 401,
                    "error": f"You are unauthorized as admin."
                    }}
        else:
            return {"data": {
                            "admin": {
                                "admin_id": admin.admin_id,
                                "first_name": admin.first_name,
                                "last_name": admin.last_name,
                                "username": admin.username,
                                "photo_url": admin.photo_url,
                                "is_superadmin": admin.is_superadmin
                            },
                        "status": 200,
                        "error": None
                        }}

    @staticmethod
    def get_all_admins():
        admins = Admin.query.all()
        admins_list = []
        for admin in admins:
            admins_list.append({"admin_id": admin.admin_id,
                                "first_name": admin.first_name,
                                "last_name": admin.last_name,
                                "username": admin.username,
                                "photo_url": admin.photo_url,
                                "is_superadmin": admin.is_superadmin})
        return {"data": {
                        "admins": admins_list,
                    "status": 200,
                    "error": None
                    }}

    @staticmethod
    def get_admin_by_id(admin_id):
        admin = Admin.query.filter_by(admin_id=admin_id).first()
        return {"data": {
                        "admin": {
                            "admin_id": admin.admin_id,
                            "first_name": admin.first_name,
                            "last_name": admin.last_name,
                            "username": admin.username,
                            "photo_url": admin.photo_url,
                            "is_superadmin": admin.is_superadmin
                        },
                    "status": 200,
                    "error": None
                    }}
