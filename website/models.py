from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(150),unique=True)
    username = db.Column(db.String(110),unique=True)
    password = db.Column(db.String(100))
    face_embedding = db.Column(db.String(500))
    date_created = db.Column(db.DateTime(timezone=True),default=func.now())
    hand_model = db.Column(db.String(100))
