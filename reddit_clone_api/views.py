from reddit_clone_api import app, db
from flask import render_template, flash, redirect, url_for, request
from reddit_clone_api.forms import LoginForm, RegistrationForm
from reddit_clone_api.models import User, Post, Subreddit, Comment
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse


@app.route('/')
@app.route('/index')
@login_required
def index():
    subreddits = Subreddit.query.all()[:10]
    return render_template('index.html', title='Home', subreddits=subreddits)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # if the user is already authenticated, redirect to index
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    # get the form data
    form = LoginForm()

    # check if the form is valid
    if form.validate_on_submit():
        # try to get the user from the database
        user = User.query.filter_by(username=form.username.data).first()
        # check if password match
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        # login user
        login_user(user, remember=form.remember_me.data)
        # redirect to 'next' if present, otherwise go to index
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)

    # by default render login page
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Subreddit': Subreddit, 'Comment': Comment}
