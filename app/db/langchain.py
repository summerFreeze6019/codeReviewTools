from flask import g, session, current_app, Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app: Flask = current_app
db: SQLAlchemy = app.config['SESSION_SQLALCHEMY']

class Conversation(db.Model):
    __tablename__ = "conversation"
    id = db.Column(db.Integer, primary_key = True)
    uid = db.Column(db.String, unique=True)
    messages = db.Column(db.String)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    last_modified = db.Column(db.DateTime) 
