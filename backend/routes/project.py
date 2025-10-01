from flask import Blueprint, request, jsonify
from db import db
from models import Project

project_bp = Blueprint("project", __name__)

# GET all projects
@project_bp.route("/", methods=["GET"])
def get_projects():
    projects = Project.query.all()
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
def add_project():
    data = request.json
    name = data.get("name")
    description = data.get("description", "")  # jika ada kolom description, tambahkan di model

    if not name:
        return jsonify({"error": "Project name cannot be empty"}), 400

    # buat instance Project
    new_project = Project(name=name, description=description)
    db.session.add(new_project)
    db.session.commit()

    return jsonify({"message": "Project added successfully"}, 201)

# UPDATE project
@project_bp.route("/<int:project_id>", methods=["PUT"])
def update_project(project_id):
    data = request.json
    name = data.get("name")
    description = data.get("description", "")

    project = Project.query.get(project_id)
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
def delete_project(project_id):
    project = Project.query.get(project_id)
    if not project:
        return jsonify({"error": "Project not found"}), 404

    db.session.delete(project)
    db.session.commit()

    return jsonify({"message": "Project deleted successfully"})
