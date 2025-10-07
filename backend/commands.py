from flask.cli import with_appcontext
import click
from app import db
from models import User # sesuaikan path model kamu
from db import bcrypt

@click.command('create-admin')
@with_appcontext
def create_admin():
    """Create an admin user."""
    username = "admin"
    password = "1234"
    role = "admin"

    # cek kalau sudah ada
    if User.query.filter_by(username=username).first():
        click.echo("Admin user already exists.")
        return

    user = User(username=username, role=role)
    # user.set_password(password)  # pastikan kamu punya method hash password
    user.password_hash = bcrypt.generate_password_hash(password).decode("utf-8")
    db.session.add(user)
    db.session.commit()

    click.echo(f"Admin user created: {username}/{password}")
