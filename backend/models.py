from db import db

# Tabel Project
class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"), nullable=False)  # opsional: untuk mengaitkan proyek dengan pengguna tertentu

    criteria = db.relationship('Criteria', backref='project', lazy=True, cascade="all, delete-orphan")
    alternatives = db.relationship('Alternative', backref='project', lazy=True, cascade="all, delete-orphan")


# Tabel Criteria
class Criteria(db.Model):
    __tablename__ = 'criteria'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    weight = db.Column(db.Float, nullable=False)
    type = db.Column(db.Enum('benefit', 'cost'), nullable=False)

    project_id = db.Column(
        db.Integer,
        db.ForeignKey('projects.id', ondelete="CASCADE"),  # <--- tambahkan CASCADE
        nullable=False
    )

        # relasi ke Score
    scores = db.relationship(
        'Score',
        backref='criteria',
        cascade="all, delete-orphan",
        passive_deletes=True
    )

# Tabel Alternative
class Alternative(db.Model):
    __tablename__ = 'alternatives'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    id_alt = db.Column(db.String(50), nullable=True)

    project_id = db.Column(
        db.Integer,
        db.ForeignKey('projects.id', ondelete="CASCADE"),  # <--- tambahkan CASCADE
        nullable=False
    )

    # relasi ke Score
    scores = db.relationship(
        'Score',
        backref='alternative',
        cascade="all, delete-orphan",   # <--- penting!
        passive_deletes=True
    )

# Tabel Score
class Score(db.Model):
    __tablename__ = 'scores'
    id = db.Column(db.Integer, primary_key=True)
    alternative_id = db.Column(
        db.Integer,
        db.ForeignKey('alternatives.id', ondelete="CASCADE"),  # <--- tambahkan CASCADE
        nullable=False
    )
    criteria_id = db.Column(
        db.Integer,
        db.ForeignKey('criteria.id', ondelete="CASCADE"),      # opsional: biar kalau Criteria dihapus, Scores ikut terhapus
        nullable=False
    )
    value = db.Column(db.Float, nullable=False)

    # relasi balik
    # criteria = db.relationship('Criteria', backref=db.backref('scores', lazy=True))


# Get Ranking Result
class TopsisResult(db.Model):
    __tablename__ = "topsis_results"
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, nullable=False)
    alternative_id = db.Column(db.Integer, nullable=False)
    score = db.Column(db.Float, nullable=False)
    rank = db.Column(db.Integer, nullable=False)

# Table User (opsional, untuk autentikasi)
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='user')  # roles: admin, user

    projects = db.relationship('Project', backref='user', cascade="all, delete-orphan", lazy=True)




