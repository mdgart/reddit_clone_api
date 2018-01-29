from flask import Flask, Blueprint
import click
from reddit_clone_api.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_restplus import Api

app = Flask(__name__)
blueprint = Blueprint('api', __name__, url_prefix='/api')
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = 'login'

api = Api(blueprint, doc='/swagger/')

app.register_blueprint(blueprint)


@app.cli.command()
def initdb():
    """Initialize the database."""
    click.echo('Init the db')  # todo


from reddit_clone_api import views, models, rest_api
