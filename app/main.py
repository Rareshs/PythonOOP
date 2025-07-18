import asyncio
from flask import render_template, request, jsonify,session, redirect, url_for
from app import create_app
from app.db.database import init_db, database, log_request

app = create_app()

loop = asyncio.get_event_loop()
loop.run_until_complete(database.connect())
loop.run_until_complete(init_db())


@app.route("/")
def home():
    if "user" not in session:
        return redirect(url_for("auth.login"))
    return render_template("home.html")


# ---- 404 handler la nivel de app ----
@app.errorhandler(404)
async def handle_404(error):
    endpoint = request.path
    request_data = request.args.to_dict()
    # logăm 404-ul
    await log_request(endpoint, request_data, {"error": "Not Found"}, 404)
    return jsonify({"error": "Not Found"}), 404
