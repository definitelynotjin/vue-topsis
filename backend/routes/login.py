from flask import Blueprint, request, jsonify
from db import db
from models import User
from db import bcrypt
from flask_jwt_extended import create_access_token

login_bp = Blueprint("login", __name__)

#login user
@login_bp.route("/auth", methods=["POST"])
def login_user():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()

    if not user or not bcrypt.check_password_hash(user.password_hash, password):
        return jsonify({"error": "Invalid username or password"}), 401

    # Simpan role ke dalam token
    access_token = create_access_token(identity=str(user.id), additional_claims={"role": user.role})
    return jsonify({
        "access_token": access_token,
        "user": {
            "id": user.id,
            "username": user.username,
            "role": user.role
            }
        },200)