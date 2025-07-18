from flask import Blueprint
from app.db.database import database
from app.utils.auth_decorator import admin_required
from flask import render_template
logs_bp = Blueprint("logs", __name__)


@logs_bp.route("/logs", methods=["GET"])
@admin_required
async def get_logs():
    query = "SELECT * FROM log_entries ORDER BY timestamp DESC"
    rows = await database.fetch_all(query=query)
    return render_template("logs.html", logs=rows)
