from flask import Flask
import click
from reddit_clone_api.config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.cli.command()
def initdb():
    """Initialize the database."""
    click.echo('Init the db')  # todo


from reddit_clone_api import views
