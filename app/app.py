import os, glob
from .tasks import start_tasks
from .db import create_all
from .api import init_api
from flask import Flask
from flask_cors import CORS
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_apscheduler import APScheduler

def init_configuration(app: Flask) -> None:
    app.config.from_pyfile(
        'config.py',
        silent=False 
    )


def create_app() -> Flask:
    db: SQLAlchemy = SQLAlchemy() 
    app: Flask = Flask('gerty-rest', instance_relative_config=True)
    init_configuration(app)
    CORS(app, supports_credentials = True) 

    #os.makedirs(app.config['SESSION_FILE_DIR'], exist_ok=True)
    #if os.path.exists(app.config['SESSION_FILE_DIR']) and not app.config['SESSION_RESTART_PERSIST']:
    #    for file in glob.glob(os.path.join(app.config['SESSION_FILE_DIR'], '*')):
    #        os.remove(file)
    db.init_app(app)
    app.config['SESSION_SQLALCHEMY'] = db
    Session(app)
    create_all(app, db)
    
    scheduler = start_tasks(app, db)

    init_api(app, db)

    return app


