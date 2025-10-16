from flask import Blueprint, request, jsonify
from db import db
from sqlalchemy.exc import IntegrityError
from models import User
from db import bcrypt
from utils.decorator import admin_required
from flask_jwt_extended import get_jwt_identity
user_bp = Blueprint("user", __name__)

#Register new ser
@user_bp.route("/register", methods=["POST"])
@admin_required
def register_user():
    data = request.json
    username = data.get("username")
    password = str(data.get("password"))  # jaga-jaga biar selalu string
    role = data.get("role", "user")  # default role is 'user'
    # return jsonify(data)

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already exists"}), 400

    # ✅ pakai instance, bukan class
    hashed_pw = bcrypt.generate_password_hash(password).decode("utf-8")
    new_user = User(username=username, password_hash=hashed_pw, role=role)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User registered successfully"}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Database error occurred"}), 500
    
#get all users (admin only)
@user_bp.route("/", methods=["GET"])
@admin_required
def get_all_users():
    current_user_id = get_jwt_identity()
    users = User.query.all()
    result = []
    for u in users:
        result.append({
            "id": u.id,
            "username": u.username,
            "role": u.role
        })
    return jsonify(result)

#Get specific user information ( for profile view )
@user_bp.route("/<int:user_id>", methods=["GET"])
def get_current_user(user_id):
    specific_user = User.query.filter_by(id=user_id).first()

    if not specific_user:
        return jsonify({"Error: User Not Found"}), 404

    result = {
        "username" : specific_user.username,
        "role": specific_user.role
    }
    return jsonify(result)


#update user (admin only)
@user_bp.route("/<int:user_id>", methods=["PUT"])
@admin_required
def update_user(user_id):
    data = request.json
    username = data.get("username")
    password = data.get("password")
    role = data.get("role")

    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    if username:
        if User.query.filter(User.username == username, User.id != user_id).first():
            return jsonify({"error": "Username already exists"}), 400
        user.username = username
    if password:
        user.password_hash = bcrypt.generate_password_hash(password).decode("utf-8")
    if role:
        user.role = role

    try:
        db.session.commit()
        return jsonify({"message": "User updated successfully"}), 200
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Database error occurred"}), 500

#delete user (admin only)
@user_bp.route("/<int:user_id>", methods=["DELETE"])
@admin_required
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully"}), 200   

