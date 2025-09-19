from flask import Blueprint, request, jsonify
from db import db
from models import Alternative

alt_bp = Blueprint("alternatives", __name__)

# GET alternatives by project_id
@alt_bp.route("/<int:project_id>", methods=["GET"])
def get_alternatives(project_id):
    alternatives = Alternative.query.filter_by(project_id=project_id).all()
    result = []
    for alt in alternatives:
        result.append({
            "id": alt.id,
            "name": alt.name,
            "nip": getattr(alt, "nip", None),
            "project_id": alt.project_id
        })
    return jsonify(result)


# POST add new alternative
@alt_bp.route("/", methods=["POST"])
def add_alternative():
    data = request.json
    project_id = data.get("project_id")
    name = data.get("name")
    nip = data.get("nip", "")

    if not project_id or not name:
        return jsonify({"error": "Project and Alternative name cannot be empty"}), 400

    # buat instance Alternative
    new_alt = Alternative(project_id=project_id, name=name, nip=nip)
    db.session.add(new_alt)
    db.session.commit()

    return jsonify({"message": "Alternative added succesfully"}, 201)
