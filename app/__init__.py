from flask import Flask
from .db.database import init_db


def create_app():
    app = Flask(__name__)

    # Inițializează baza de date
    init_db(app)

    # Încarcă rutele
    from app.controllers.math_controllers import math_bp
    app.register_blueprint(math_bp, url_prefix="/api")

    return app
