from ..exts import db
from datetime import datetime

class Staff(db.Model):
    __tablename__ = 'staff'

    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    name = db.Column(db.String(128),nullable=False)
    gender = db.Column(db.String(16),nullable=False)
    birthyear = db.Column(db.Integer,nullable=False)
    workyear = db.Column(db.Integer,nullable=False)
    daylike = db.Column(db.String(128),nullable=True)
    timelike = db.Column(db.String(128),nullable=True)

class Schedule(db.Model):
    __tablename__ = 'schedule'

    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    d1_morning = db.Column(db.String(128),nullable=True)
    d1_afternoon = db.Column(db.String(128),nullable=True)
    d1_evening = db.Column(db.String(128),nullable=True)
    d2_morning = db.Column(db.String(128),nullable=True)
    d2_afternoon = db.Column(db.String(128),nullable=True)
    d2_evening = db.Column(db.String(128),nullable=True)
    d3_morning = db.Column(db.String(128),nullable=True)
    d3_afternoon = db.Column(db.String(128),nullable=True)
    d3_evening = db.Column(db.String(128),nullable=True)
    d4_morning = db.Column(db.String(128),nullable=True)
    d4_afternoon = db.Column(db.String(128),nullable=True)
    d4_evening = db.Column(db.String(128),nullable=True)
    d5_morning = db.Column(db.String(128),nullable=True)
    d5_afternoon = db.Column(db.String(128),nullable=True)
    d5_evening = db.Column(db.String(128),nullable=True)
    d6_morning = db.Column(db.String(128),nullable=True)
    d6_afternoon = db.Column(db.String(128),nullable=True)
    d6_evening = db.Column(db.String(128),nullable=True)
    d7_morning = db.Column(db.String(128),nullable=True)
    d7_afternoon = db.Column(db.String(128),nullable=True)
    d7_evening = db.Column(db.String(128),nullable=True)
    week = db.Column(db.Integer,nullable=False)

