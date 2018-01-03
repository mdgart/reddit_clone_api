from reddit_clone_api import app


@app.route('/')
def index():
    return 'Hello Potatoes!'
