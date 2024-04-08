import os, sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_apscheduler import APScheduler
from datetime import datetime, timedelta


def start_tasks(app: Flask, db: SQLAlchemy) -> APScheduler:
    scheduler = APScheduler()
    scheduler.init_app(app)

    with app.app_context():
        engine = db.engine
        from ..db.langchain import Conversation
        sorted_tables = db.metadata.sorted_tables
        conversation_table = None
        for table in sorted_tables:
            if table.name == "conversation":
                conversation_table = table
        assert conversation_table is not None, "Could not find conversation table in sorted tables."

    @scheduler.task('interval', id='do_cleanup_job', seconds = 60, misfire_grace_time=1800)
    def cleanup_job():
        try:
            too_old = datetime.utcnow() - app.config['PERMANENT_SESSION_LIFETIME']
            with engine.begin() as conn:
                out = conn.execute(
                    conversation_table.delete().where(
                        conversation_table.c.timestamp <= too_old
                    )
                )
                print(f"Cleaned up {out.rowcount} rows.")
        except Exception as e:
            print("TASK ERROR: ", e)
        return

    scheduler.start()
    return scheduler
