from flask.cli import with_appcontext
import click
from app import db
from models import User
from db import bcrypt


@click.command("create-admin")
@with_appcontext
@click.option("--username", prompt=True, help="Admin username")
@click.option("--password", prompt=True, hide_input=True, confirmation_prompt=True)
def create_admin(username, password):
    """Create an admin user safely."""

    role = "admin"

    existing = User.query.filter_by(username=username).first()
    if existing:
        click.echo("User already exists.")
        return

    user = User(username=username, role=role)
    user.password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    db.session.add(user)
    db.session.commit()

    click.echo(f"Admin user '{username}' created successfully.")
