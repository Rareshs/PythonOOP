from flask import Flask


def create_app():
    app = Flask(__name__)

    # Încarcă rutele
    from app.controllers.math_controllers import math_bp
    app.register_blueprint(math_bp, url_prefix="/api")

    return app
