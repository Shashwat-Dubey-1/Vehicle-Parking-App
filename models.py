from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id       = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    role     = db.Column(db.String(10), nullable=False)  # 'admin' or 'user'

class ParkingLot(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    name     = db.Column(db.String(120), nullable=False)
    address  = db.Column(db.String(200))
    pincode  = db.Column(db.String(10))
    price    = db.Column(db.Float, nullable=False)
    max_spots= db.Column(db.Integer, nullable=False)

class ParkingSpot(db.Model):
    id      = db.Column(db.Integer, primary_key=True)
    lot_id  = db.Column(db.Integer, db.ForeignKey('parking_lot.id'), nullable=False)
    status  = db.Column(db.String(1), default='A')  # 'A' = available, 'O' = occupied

class Reservation(db.Model):
    id         = db.Column(db.Integer, primary_key=True)
    spot_id    = db.Column(db.Integer, db.ForeignKey('parking_spot.id'), nullable=False)
    user_id    = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    in_time    = db.Column(db.DateTime, default=datetime.utcnow)
    out_time   = db.Column(db.DateTime)
    cost       = db.Column(db.Float)
