# app/main.py

import asyncio
from flask import render_template_string
from app import create_app
from app.db.database import init_db

app = create_app()

# Inițializează baza de date la pornirea aplicației
asyncio.get_event_loop().run_until_complete(init_db())


@app.route("/")
def home():

    return render_template_string("""
    <html>
    <head>
        <title>Python Math Microservice</title>
        <style>
            body { font-family: Arial, sans-serif; background: #f9f9f9; padding: 30px; }
            h1 { color: #333; }
            a { display: block; margin: 10px 0; color: #007BFF; text-decoration: none; }
        </style>
    </head>
    <body>
        <h1>🎯 Python Math Microservice</h1>
        <p>Welcome! Try the following endpoints:</p>
        <a href="/api/pow?a=2&b=3">/api/pow?a=2&b=3</a>
        <a href="/api/fibonacci?n=6">/api/fibonacci?n=6</a>
        <a href="/api/factorial?n=5">/api/factorial?n=5</a>
    </body>
    </html>
    """)
