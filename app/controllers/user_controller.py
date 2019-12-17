from app.models.user_model import User
from app.main import db


class UserController:
    
    @staticmethod
    def create_user(post_data):
        # check if user already exists
        user = User.query.filter_by(user_id=post_data.get('id')).first()
        if not user:
            user = User(
                user_id=post_data.get('id'),
                first_name=post_data.get('first_name'),
                last_name=post_data.get('last_name'),
                username=post_data.get('username'),
                photo_url=post_data.get('photo_url')
            )

            # insert the user
            db.session.add(user)
            db.session.commit()

            return {"data": {
                        "user": {
                            "user_id": user.user_id,
                            "first_name": user.first_name,
                            "last_name": user.last_name,
                            "username": user.username,
                            "photo_url": user.photo_url
                        },
                    "status": 201,
                    "error": None
                    }}
        else:
            return {"data": {
                        "user": {
                            "user_id": user.user_id,
                            "first_name": user.first_name,
                            "last_name": user.last_name,
                            "username": user.username,
                            "photo_url": user.photo_url
                        },
                    "status": 200,
                    "error": f"User {user.username} already exists."
                    }}

    @staticmethod
    def get_all_users():
        users = User.query.all()
        users_list = []
        for user in users:
            users_list.append({"user_id": user.user_id,
                                "first_name": user.first_name,
                                "last_name": user.last_name,
                                "username": user.username,
                                "photo_url": user.photo_url})
        return {"data": {
                        "users": users_list,
                    "status": 200,
                    "error": None
                    }}

    @staticmethod
    def get_user_by_id(user_id):
        user = User.query.filter_by(user_id=user_id).first()
        return {"data": {
                        "user": {
                            "user_id": user.user_id,
                            "first_name": user.first_name,
                            "last_name": user.last_name,
                            "username": user.username,
                            "photo_url": user.photo_url
                        },
                    "status": 200,
                    "error": None
                    }}
