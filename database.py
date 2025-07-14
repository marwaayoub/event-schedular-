

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(100))
    description = db.Column(db.Text)
    status = db.Column(db.String(20), nullable=False, default='upcoming')