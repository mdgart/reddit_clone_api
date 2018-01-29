from reddit_clone_api import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from reddit_clone_api import login

user_subreddit = db.Table('user_subreddit', db.Model.metadata,
                          db.Column('user_id', db.Integer,
                                    db.ForeignKey('user.id')),
                          db.Column('subreddit_id', db.Integer,
                                    db.ForeignKey('subreddit.id'))
                          )


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    subreddits = db.relationship('Subreddit',
                                 secondary=user_subreddit,
                                 back_populates="members")
    owned_subreddit = db.relationship(
        'Subreddit', backref='owner', lazy='dynamic')
    comments = db.relationship('Comment', backref='user', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Subreddit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True, nullable=False)
    title = db.Column(db.String(256), index=True, nullable=False)
    description = db.Column(db.Text())
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    posts = db.relationship('Post', backref='subreddit', lazy='dynamic')
    members = db.relationship('User',
                              secondary=user_subreddit,
                              back_populates='subreddits')

    def __repr__(self):
        return '<Subreddit {}>'.format(self.name)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    body = db.Column(db.Text())
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    subreddit_id = db.Column(db.Integer, db.ForeignKey('subreddit.id'))
    comments = db.relationship('Comment', backref='post', lazy='dynamic')

    def __repr__(self):
        return '<Post {}>'.format(self.title)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text(), nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    def __repr__(self):
        return '<Comment {}>'.format(self.body)


'''
from reddit_clone_api import db
from reddit_clone_api.models import User, Post, Subreddit, Comment
u = User(username='mauro', email='mauro.degiorgi@gmail.com')
'''
