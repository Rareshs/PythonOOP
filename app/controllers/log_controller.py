from flask import Blueprint, render_template
from app.db.database import database
from app.utils.auth_decorator import login_required, admin_required

logs_bp = Blueprint("logs", __name__)

@logs_bp.route("/logs", methods=["GET"])
@login_required
@admin_required
async def get_logs():
    query = "SELECT * FROM log_entries ORDER BY timestamp DESC"
    rows = await database.fetch_all(query=query)
    return render_template("logs.html", logs=rows)
