import os
from flask import Flask
from flask_cors import CORS
from db import db, migrate, bcrypt
from flask_jwt_extended import JWTManager
import commands

# import blueprint
from routes.project import project_bp
from routes.criteria import criteria_bp
from routes.alternative import alt_bp
from routes.score import score_bp
from routes.topsis import topsis_bp
from routes.export import export_bp
from routes.imports import import_bp
from routes.user import user_bp
from routes.login import login_bp


def create_app():
    app = Flask(__name__)

    cors_origins = os.getenv("CORS_ORIGINS", "http://localhost:3000")
    cors_origins = [origin.strip() for origin in cors_origins.split(",")]

    # -------------------------
    # CORS
    # -------------------------
    _ = CORS(
        app,
        resources={
            r"/*": {
                "origins": cors_origins,
                "supports_credentials": True,
                "allow_headers": ["Content-Type", "Authorization"],
                "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            }
        },
    )

    # -------------------------
    # ENV-BASED CONFIGURATION
    # -------------------------

    DB_USER = os.getenv("DB_USER", "flaskuser")
    DB_PASS = os.getenv("DB_PASS", "flask123")
    DB_HOST = os.getenv("DB_HOST", "host.docker.internal")
    DB_NAME = os.getenv("DB_NAME", "topsis_db")

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
    )

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # JWT
    app.config["JWT_SECRET_KEY"] = os.getenv(
        "JWT_SECRET_KEY", "ganti_dengan_key_rahasia"
    )

    # -------------------------
    # Initialize Extensions
    # -------------------------
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    JWTManager(app)

    # Import CLI Commands
    app.cli.add_command(commands.create_admin)

    # -------------------------
    # Blueprint registration
    # -------------------------
    app.register_blueprint(project_bp, url_prefix="/project")
    app.register_blueprint(criteria_bp, url_prefix="/criteria")
    app.register_blueprint(alt_bp, url_prefix="/alternative")
    app.register_blueprint(score_bp, url_prefix="/score")
    app.register_blueprint(topsis_bp, url_prefix="/topsis")
    app.register_blueprint(export_bp, url_prefix="/export")
    app.register_blueprint(import_bp, url_prefix="/import")
    app.register_blueprint(user_bp, url_prefix="/user")
    app.register_blueprint(login_bp, url_prefix="/login")

    @app.route("/")
    def home():
        return "Flask + MySQL TOPSIS API"

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
