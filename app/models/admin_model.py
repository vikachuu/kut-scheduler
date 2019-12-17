import datetime

from app.main import db


class Admin(db.Model):
    __tablename__ = "admin"

    admin_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100)) 
    username = db.Column(db.String(100), unique=True, nullable=False)
    photo_url = db.Column(db.String(100))
    is_superadmin = db.Column(db.Boolean())

    def __init__(self, admin_id, first_name, last_name, username, photo_url, is_superadmin=False):
        self.admin_id = admin_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.photo_url = photo_url
        self.is_superadmin = is_superadmin
