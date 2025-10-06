from flask import Blueprint, request, jsonify
from db import db
from models import Project
from flask_jwt_extended import get_jwt_identity
from utils.decorator import user_required

project_bp = Blueprint("project", __name__)

# GET all projects
@project_bp.route("/", methods=["GET"])
@user_required
def get_projects():
    user_id = get_jwt_identity()  # dapatkan user_id dari token JWT
    projects = Project.query.filter_by(user_id = user_id).all()
    result = []
    for p in projects:
        result.append({
            "id": p.id,
            "name": p.name,
            "description": p.description
            # jika ada kolom tambahan seperti description, bisa ditambahkan di sini
        })
    return jsonify(result)


# POST add new project
@project_bp.route("/", methods=["POST"])
@user_required
def add_project():
    user_id = get_jwt_identity()  # dapatkan user_id dari token JWT
    data = request.json
    name = data.get("name")
    description = data.get("description", "")  # jika ada kolom description, tambahkan di model


    if not name:
        return jsonify({"error": "Project name cannot be empty"}), 400

    # buat instance Project
    new_project = Project(name=name, description=description, user_id=user_id)  # ganti 1 dengan user_id yang sesuai jika perlu
    db.session.add(new_project)
    db.session.commit()

    return jsonify({"message": "Project added successfully"}, 201)

# UPDATE project
@project_bp.route("/<int:project_id>", methods=["PUT"])
def update_project(project_id):
    data = request.json
    name = data.get("name")
    description = data.get("description", "")

    project = Project.query.filter_by(id=project_id, user_id=get_jwt_identity).first()
    if not project:
        return jsonify({"error": "Project not found"}), 404

    if not name:
        return jsonify({"error": "Project name cannot be empty"}), 400

    project.name = name
    project.description = description
    db.session.commit()

    return jsonify({"message": "Project updated successfully"})

# DELETE project
@project_bp.route("/<int:project_id>", methods=["DELETE"])
@user_required
def delete_project(project_id):
    user_id = get_jwt_identity()
    project = Project.query.filter_by(id=project_id, user_id=user_id).first()
    if not project:
        return jsonify({"error": "Project not found"}), 404

    db.session.delete(project)
    db.session.commit()

    return jsonify({"message": "Project deleted successfully"})
