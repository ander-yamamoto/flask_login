from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))



class Node(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False) #INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT
    name = db.Column(db.String(100), unique=True, nullable=False) #TEXT NOT NULL UNIQUE,
    topic = db.Column(db.String(100), nullable=False) #TEXT NOT NULL,
    item_id = db.Column(db.String(100), nullable=False) #TEXT NOT NULL,
    ip = db.Column(db.String(16), nullable=False) #VARCHAR(16) NOT NULL,
    status = db.Column(db.Integer, nullable=False) #INTEGER NOT NULL,
    last_update = db.Column(db.DateTime, nullable=False) #timestamp NOT NULL

