from quizapp import db
from flask_login import UserMixin


class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(30),unique=True)
    email = db.Column(db.String(40),nullable=False,unique=True)
    password = db.Column(db.String(100))