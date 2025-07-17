# app/models/db_models.py

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
import pytz

db = SQLAlchemy()

RO_TZ = pytz.timezone("Europe/Bucharest")


class LogEntry(db.Model):
    __tablename__ = "log_entries"

    id = db.Column(db.Integer, primary_key=True)
    endpoint = db.Column(db.String(50), nullable=False)
    request_data = db.Column(db.Text, nullable=False)
    response_data = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    status_code = db.Column(db.Integer, nullable=False)
