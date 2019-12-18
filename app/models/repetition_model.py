import enum
from datetime import datetime

from app.main import db

class STATUS(enum.Enum):
    APPROVED = "approved"
    REVIEW = "review"
    DECLINED = "declined"


class Repetition(db.Model):
    __tablename__ = "repetition"

    repetition_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    room_number = db.Column(db.Integer, nullable=False)
    repetition_date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)
    number_of_people = db.Column(db.Integer, nullable=False)
    approved = db.Column(db.String(30), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id', onupdate="CASCADE",
                                                   ondelete="NO ACTION"), nullable=False)
    user =  db.relationship("User", back_populates="repetition")

    admin_id = db.Column(db.Integer, db.ForeignKey('admin.admin_id', onupdate="CASCADE",
                                                    ondelete="NO ACTION"), nullable=True)
    admin = db.relationship("Admin", back_populates="repetition")

    def __init__(self, room_number, repetition_date, start_time, end_time, 
                 number_of_people, approved, user_id, admin_id):
        self.room_number = room_number
        self.repetition_date = datetime.strptime(repetition_date, '%Y-%m-%d').date()
        self.start_time = datetime.strptime(start_time, '%H:%M').time()
        self.end_time = datetime.strptime(end_time, '%H:%M').time()
        self.number_of_people = number_of_people
        self.approved = STATUS[approved].value

        self.user_id = user_id
        self.admin_id = admin_id
