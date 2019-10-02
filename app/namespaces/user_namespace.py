from flask_restplus import Namespace, Resource


api_user = Namespace('user', description='User operations')


@api_user.route("/")
class User(Resource):

    def get(self):
        """
        Returns a list of users
        """

        return {"status": "user here"}

    def post(self):
        """
        Adds a new user to the list
        """


@api_user.route("<int:id>")
class UserId(Resource):
    def get(self, id):
        """
        Displays user's details
        """
    def put(self, id):
        """
        Edits a selected user
        """
