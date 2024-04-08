from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_all(app: Flask, db: SQLAlchemy):
    with app.app_context():
        from . import langchain 
        db.create_all()
    return
