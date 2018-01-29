from flask import Flask
from flask_restplus import Resource, Api
from reddit_clone_api import api, login
from flask_login import current_user, login_required
from werkzeug.exceptions import Unauthorized


@api.route('/currentuser')
class HelloWorld(Resource):

    @login_required
    def get(self):
        return {
            'username': str(current_user.username),
            'emails': str(current_user.email),
            'subreddits': str(current_user.subreddits)
        }
