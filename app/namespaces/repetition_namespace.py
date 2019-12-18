from flask import request
from flask_restplus import Namespace, Resource

api_repetition = Namespace('repetition', description='Repetition operations')


@api_repetition.route("/")
class Repetition(Resource):

    def get(self):
        """
        Return a list of repetitions
        """
        from app.controllers.repetition_controller import RepetitionController
        return RepetitionController.get_all_repetitions()

    def post(self):
        """
        Add a new repetition
        """
        from app.controllers.repetition_controller import RepetitionController
        post_data = request.get_json()
        return RepetitionController.create_repetition(post_data)


@api_repetition.route("/<int:id>")
class RepetitionId(Resource):
    # def get(self, id):
    #     """
    #     Returns repetition by repetition_id
    #     """
    #     return None

    def put(self, id):
        """
        Edits a selected repetition
        """
        from app.controllers.repetition_controller import RepetitionController
        post_data = request.get_json()
        return RepetitionController.update_repetition_by_id(id, post_data)
