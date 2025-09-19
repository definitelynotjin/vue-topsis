from flask import Flask
from db import db, migrate
# import blueprint
from routes.project import project_bp
from routes.criteria import criteria_bp
from routes.alternative import alt_bp
from routes.score import score_bp
from routes.topsis import topsis_bp
from routes.export import export_bp

def create_app():
    app = Flask(__name__)

    # konfigurasi database MySQL
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/topsis_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # inisialisasi db & migrate
    db.init_app(app)
    migrate.init_app(app, db)

    # import models supaya Flask-Migrate bisa membaca
    from models import Alternative, Criteria, Score

    # daftarkan blueprint
    app.register_blueprint(project_bp, url_prefix="/project")
    app.register_blueprint(criteria_bp, url_prefix="/criteria")
    app.register_blueprint(alt_bp, url_prefix="/alternative")
    app.register_blueprint(score_bp, url_prefix="/score")
    app.register_blueprint(topsis_bp, url_prefix="/topsis")
    app.register_blueprint(export_bp, url_prefix="/export")

    @app.route("/")
    def home():
        return "Flask + MySQL TOPSIS API"

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
