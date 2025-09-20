from db import db

# Tabel Project
class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)

# Tabel Criteria
class Criteria(db.Model):
    __tablename__ = 'criteria'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    weight = db.Column(db.Float, nullable=False)
    type = db.Column(db.Enum('benefit', 'cost'), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)

    project = db.relationship('Project', backref=db.backref('criteria', lazy=True))

# Tabel Alternative
class Alternative(db.Model):
    __tablename__ = 'alternatives'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    id_alt = db.Column(db.String(50), nullable=True)  # Menambahkan kolom nip
    # rank = db.Column(db.Integer, nullable=True)  # Menambahkan kolom rank

    project = db.relationship('Project', backref=db.backref('alternatives', lazy=True))

# Tabel Score
class Score(db.Model):
    __tablename__ = 'scores'
    id = db.Column(db.Integer, primary_key=True)
    alternative_id = db.Column(db.Integer, db.ForeignKey('alternatives.id'), nullable=False)
    criteria_id = db.Column(db.Integer, db.ForeignKey('criteria.id'), nullable=False)
    value = db.Column(db.Float, nullable=False)

    alternative = db.relationship('Alternative', backref=db.backref('scores', lazy=True))
    criteria = db.relationship('Criteria', backref=db.backref('scores', lazy=True))

# Get Ranking Result
class TopsisResult(db.Model):
    __tablename__ = "topsis_results"
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, nullable=False)
    alternative_id = db.Column(db.Integer, nullable=False)
    score = db.Column(db.Float, nullable=False)
    rank = db.Column(db.Integer, nullable=False)
