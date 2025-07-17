import asyncio
from flask import render_template_string
from app import create_app
from app.db.database import init_db, database  
from flask import render_template

app = create_app()

loop = asyncio.get_event_loop()
loop.run_until_complete(database.connect())  
loop.run_until_complete(init_db())

@app.route("/")
def home():
    return render_template("home.html")