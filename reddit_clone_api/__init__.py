from flask import Flask
import click
from reddit_clone_api.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'


@app.cli.command()
def initdb():
    """Initialize the database."""
    click.echo('Init the db')  # todo


from reddit_clone_api import views, models
