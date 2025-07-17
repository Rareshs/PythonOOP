from flask import Flask
import os

def create_app():
    # Specificăm manual unde se află template-urile
    base_dir = os.path.abspath(os.path.dirname(__file__))
    templates_path = os.path.join(base_dir, "templates")

    app = Flask(__name__, template_folder=templates_path)

    from app.controllers.math_controllers import math_bp
    from app.controllers.log_controller import logs_bp
    app.register_blueprint(math_bp, url_prefix="/api")
    app.register_blueprint(logs_bp)

    return app
