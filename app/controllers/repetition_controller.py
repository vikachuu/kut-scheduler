import requests

from app.models.repetition_model import Repetition, STATUS
from app.main import db

from sqlalchemy import or_


class RepetitionController:

    @staticmethod
    def send_telegram_notification(text):
        chat_id = "218723630"
        response = requests.post(f"https://api.telegram.org/bot991724672:AAGoleDB0JnglGo8pLyKRJMi1GkrBiM0oE4/sendMessage?chat_id={chat_id}&text={text}")
        return response

    @staticmethod
    def create_repetition(post_data):
        # check if repetition already exists
        repetition = Repetition.query.filter(Repetition.room_number==post_data.get('room_number'), 
                                            Repetition.repetition_date==post_data.get('repetition_date'),
                                            Repetition.start_time==post_data.get('start_time'),
                                            or_(Repetition.approved=="approved", Repetition.approved=="review")).first()
        if not repetition:
            repetition = Repetition(
                room_number=post_data.get('room_number'),
                repetition_date=post_data.get('repetition_date'),
                start_time=post_data.get('start_time'),
                end_time=post_data.get('end_time'),
                number_of_people=post_data.get('number_of_people'),
                approved="REVIEW",
                user_id=post_data.get('user_id'),
                admin_id=post_data.get('admin_id')
            )

            # insert the repetition
            db.session.add(repetition)
            db.session.commit()

            response = RepetitionController.send_telegram_notification("New repetition was booked. Come and have a look.")

            return {"data": {
                        "repetition": {
                            "repetition_id": repetition.repetition_id,
                            "room_number": repetition.room_number,
                            "repetition_date": repetition.repetition_date.strftime("%Y-%m-%d"),
                            "start_time": repetition.start_time.strftime("%H:%M"),
                            "end_time": repetition.end_time.strftime("%H:%M"),
                            "number_of_people": repetition.number_of_people,
                            "approved": repetition.approved,
                            "user_id": repetition.user_id,
                            "admin_id": repetition.admin_id,
                        },
                    "status": 201,
                    "error": None
                    }}
        else:
            return {"data": None,
                    "status": 400,
                    "error": f"Repetition in room {repetition.room_number} on {repetition.repetition_date} at {repetition.start_time} already exists."
                    }

    @staticmethod
    def get_all_repetitions():
        repetitions = Repetition.query.all()
        repetitions_list = []
        for repetition in repetitions:
            repetitions_list.append({
                "repetition_id": repetition.repetition_id,
                "room_number": repetition.room_number,
                "repetition_date": repetition.repetition_date.strftime("%Y-%m-%d"),
                "start_time": repetition.start_time.strftime("%H:%M"),
                "end_time": repetition.end_time.strftime("%H:%M"),
                "number_of_people": repetition.number_of_people,
                "approved": repetition.approved,
                "user_id": repetition.user_id,
                "admin_id": repetition.admin_id
                })
        return {"data": {
                        "repetitions": repetitions_list,
                    "status": 200,
                    "error": None
                    }}

    @staticmethod
    def update_repetition_by_id(repetition_id, post_data):
        repetition = Repetition.query.filter_by(repetition_id=repetition_id).first()
        if repetition is None:
            return {"data": None,
                    "status": 400,
                    "error": f"Repetition does not exist."
                    }
        else:
            repetition.approved = STATUS[post_data.get("approved")].value if post_data.get("approved") else repetition.approved
            repetition.admin_id = post_data.get("admin_id") if post_data.get("admin_id") else repetition.admin_id

            db.session.commit()

            return {"data": {
                        "repetition": {
                            "repetition_id": repetition.repetition_id,
                            "room_number": repetition.room_number,
                            "repetition_date": repetition.repetition_date.strftime("%Y-%m-%d"),
                            "start_time": repetition.start_time.strftime("%H:%M"),
                            "end_time": repetition.end_time.strftime("%H:%M"),
                            "number_of_people": repetition.number_of_people,
                            "approved": repetition.approved,
                            "user_id": repetition.user_id,
                            "admin_id": repetition.admin_id,
                        },
                    "status": 200,
                    "error": None
                    }}
