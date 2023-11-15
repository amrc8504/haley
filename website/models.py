from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(15))
    user_name = db.Column(db.String(20))

class Quiz(db.Model):
    answer1 = db.Column(db.String(50), primary_key=True)
    answer2 = db.Column(db.String(50))
    answer3 = db.Column(db.String(50))
    answer4 = db.Column(db.String(50))
    answer5 = db.Column(db.String(50))
    answer6 = db.Column(db.String(50))
    answer7 = db.Column(db.String(50))