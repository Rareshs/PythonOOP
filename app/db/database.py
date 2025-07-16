import json
from flask import Flask
from app.models.db_models import db, LogEntry


def init_db(app: Flask):
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///logs.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()


def log_request(endpoint: str, request_data: dict, response_data: dict):
    entry = LogEntry(
        endpoint=endpoint,
        request_data=json.dumps(request_data),
        response_data=json.dumps(response_data),
    )
    db.session.add(entry)
    db.session.commit()
