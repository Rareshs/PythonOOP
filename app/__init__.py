import os
from flask import Flask
from dotenv import load_dotenv 


def create_app():
    load_dotenv()
    

    base_dir = os.path.abspath(os.path.dirname(__file__))
    templates_path = os.path.join(base_dir, "templates")

    app = Flask(__name__, template_folder=templates_path)

    # Setare secret_key din variabilă de mediu
    app.secret_key = os.environ.get("SECRET_KEY")

    from app.controllers.math_controllers import math_bp
    from app.controllers.log_controller import logs_bp
    from app.controllers.auth_controller import auth_bp

    app.register_blueprint(math_bp, url_prefix="/api")
    app.register_blueprint(logs_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")

    return app
